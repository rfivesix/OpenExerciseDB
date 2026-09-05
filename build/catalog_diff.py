#!/usr/bin/env python3
"""Compares two catalog databases and detects breaking or dangerous changes.

Adopted from an earlier pipeline and extended to the schema in SCHEMA.md 8. The
logic for v1 columns is unchanged — it has fulfilled its purpose and its tests
continue to run. Added features include:

* new columns of `exercises` (classification, license provenance),
* relational tables `exercise_muscles`, `exercise_equipment`, `exercise_tags`
  each summarized into a comparable, sorted value per exercise,
* **Invariant 21**: an active exercise must not disappear without an alias or
  `merged_into` pointing to a successor. This makes deduplication safe;
  without this check, the `exercise_aliases` table is only a promise.
* **Invariant 22**: the count of active exercises never drops by more than 5%.
* **License regression**: a translation that loses its license attribution is
  an attribution violation, not a cosmetic issue (SCHEMA.md 3b).
* **schema_version** must not run backwards (SCHEMA.md 9).

Usage:

    python3 build/catalog_diff.py --old old.db --new new.db \
        --json-out artifacts/diff_report.json --fail-on-breaking
"""
import argparse
import json
import os
import sqlite3
import sys
from typing import Any, Dict, List, Tuple

REQUIRED_TABLES = ("exercises", "metadata")
REQUIRED_EXERCISE_COLUMNS = (
    "id",
    "name_de",
    "name_en",
    "description_de",
    "description_en",
    "category_name",
    "muscles_primary",
    "muscles_secondary",
)
OPTIONAL_EXERCISE_COLUMNS = (
    "image_path",
    "source",
    "created_by",
    "is_custom",
    # --- Schema v2. Compared as soon as column exists; a v1 database
    # on either side does not break comparison.
    "slug",
    "status",
    "merged_into",
    "modality",
    "mechanic",
    "force_vector",
    "movement_pattern",
    "laterality",
    "difficulty",
    "tracking_type",
    "supports_added_weight",
    "load_mode",
    "primary_equipment",
    "body_region",
    "upstream_source",
    "upstream_id",
    "upstream_license",
    "upstream_license_author",
)
MAIN_COMPARE_FIELDS = (
    "name_de",
    "name_en",
    "description_de",
    "description_en",
    "category_name",
    "muscles_primary",
    "muscles_secondary",
)

RELATIONAL_FIELDS = {
    # Field name -> (table, expression per row)
    # Each relation is aggregated into a sorted string so existing field comparison
    # includes it without special handling.
    "muscle_assignments": ("exercise_muscles", "role || ':' || muscle_id"),
    "equipment_assignments": ("exercise_equipment", "kind || ':' || equipment_id"),
    "usage_tags": ("exercise_tags", "tag"),
}

INVARIANT_22_MAX_ACTIVE_DROP_PERCENT = 5.0
"""Invariant 22. Matches the threshold previously used by workflow as
WGER_FAIL_ON_REMOVED_THRESHOLD."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare two generated OpenExerciseDB catalogs."
    )
    parser.add_argument("--old", required=True, help="Path to old database file")
    parser.add_argument("--new", required=True, help="Path to new database file")
    parser.add_argument("--json-out", help="Write full machine-readable diff report to JSON")
    parser.add_argument(
        "--examples",
        type=int,
        default=10,
        help="How many example IDs/rows to print in console output (default: 10)",
    )
    parser.add_argument(
        "--removed-severe-threshold",
        type=int,
        default=25,
        help="Removed ID count at or above this threshold is severe (default: 25)",
    )
    parser.add_argument(
        "--row-drop-warn-percent",
        type=float,
        default=5.0,
        help="Warn when total row count drop is at least this percent (default: 5.0)",
    )
    parser.add_argument(
        "--row-drop-severe-percent",
        type=float,
        default=20.0,
        help="Severe when total row count drop is at least this percent (default: 20.0)",
    )
    parser.add_argument(
        "--category-regression-threshold",
        type=int,
        default=10,
        help="Warn when category regressions reach this count (default: 10)",
    )
    parser.add_argument(
        "--muscle-regression-threshold",
        type=int,
        default=10,
        help="Warn when muscle regressions reach this count (default: 10)",
    )
    parser.add_argument(
        "--de-fallback-shift-threshold",
        type=int,
        default=10,
        help="Warn when DE-name losses with EN still present reach this count (default: 10)",
    )
    parser.add_argument(
        "--fail-on-breaking",
        action="store_true",
        help=(
            "Exit with non-zero status on dangerous changes "
            "(removed IDs or severe/suspicious regressions)."
        ),
    )
    parser.add_argument(
        "--fail-on-removed-threshold",
        type=int,
        default=30,
        help=(
            "With --fail-on-breaking, fail if removed ID count is above this value "
            "(default: 30)."
        ),
    )
    return parser.parse_args()


def normalize_value(value: Any) -> Any:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return value


def is_blank(value: Any) -> bool:
    return normalize_value(value) == ""


def load_catalog(db_path: str) -> Dict[str, Any]:
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Database not found: {db_path}")

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
        )
        tables = {row["name"] for row in cursor.fetchall()}
        missing_tables = [table for table in REQUIRED_TABLES if table not in tables]
        if missing_tables:
            raise ValueError(
                f"Missing required tables in {db_path}: {', '.join(missing_tables)}"
            )

        cursor.execute("PRAGMA table_info(exercises)")
        exercise_columns = {row["name"] for row in cursor.fetchall()}
        
        has_translations_table = "exercise_translations" in tables
        if has_translations_table:
            exercise_columns.update({"name_de", "name_en", "description_de", "description_en"})

        missing_columns = [
            column for column in REQUIRED_EXERCISE_COLUMNS if column not in exercise_columns
        ]
        if missing_columns:
            raise ValueError(
                f"Missing required exercise columns in {db_path}: {', '.join(missing_columns)}"
            )

        compare_fields = list(MAIN_COMPARE_FIELDS)
        for optional_field in OPTIONAL_EXERCISE_COLUMNS:
            if optional_field in exercise_columns:
                compare_fields.append(optional_field)

        cursor.execute("SELECT key, value FROM metadata")
        metadata = {row["key"]: row["value"] for row in cursor.fetchall()}

        select_columns = ["id"] + compare_fields
        if has_translations_table:
            base_columns = [c for c in select_columns if c not in ("name_de", "name_en", "description_de", "description_en")]
            select_list = [f"e.{c}" for c in base_columns]
            select_list.append("de.name AS name_de")
            select_list.append("de.description AS description_de")
            select_list.append("en.name AS name_en")
            select_list.append("en.description AS description_en")
            query = f"""
                SELECT {', '.join(select_list)}
                FROM exercises e
                LEFT JOIN exercise_translations de ON e.id = de.exercise_id AND de.language_code = 'de'
                LEFT JOIN exercise_translations en ON e.id = en.exercise_id AND en.language_code = 'en'
            """
            cursor.execute(query)
        else:
            column_sql = ", ".join(select_columns)
            cursor.execute(f"SELECT {column_sql} FROM exercises")

        rows = cursor.fetchall()

        exercises: Dict[str, Dict[str, Any]] = {}
        for row in rows:
            row_dict = dict(row)
            exercise_id = str(row_dict["id"])
            normalized = {
                field: normalize_value(row_dict.get(field)) for field in compare_fields
            }
            exercises[exercise_id] = normalized

        # --- Relationship tables as a single comparable value per exercise.
        for field, (table, expression) in RELATIONAL_FIELDS.items():
            if table not in tables:
                continue
            compare_fields.append(field)
            collected: Dict[str, List[str]] = {}
            for row in cursor.execute(
                f"SELECT exercise_id, {expression} AS value FROM {table}"
            ):
                collected.setdefault(str(row["exercise_id"]), []).append(str(row["value"]))
            for exercise_id, entry in exercises.items():
                entry[field] = ", ".join(sorted(collected.get(exercise_id, [])))

        # --- Translations: row count and license coverage per language. A language
        # losing rows between releases is significant.
        translations: Dict[str, Dict[str, int]] = {}
        if has_translations_table:
            # `license` exists only starting in schema v2; querying against a v1
            # database would fail with an error rather than returning zero.
            has_license = "license" in _columns(cursor, "exercise_translations")
            without_license = (
                "SUM(CASE WHEN license IS NULL OR TRIM(license) = '' THEN 1 ELSE 0 END)"
                if has_license
                else "0"
            )
            for row in cursor.execute(
                f"SELECT language_code, COUNT(*) AS rows, {without_license} AS without_license "
                "FROM exercise_translations GROUP BY language_code"
            ):
                translations[str(row["language_code"])] = {
                    "rows": int(row["rows"]),
                    "without_license": int(row["without_license"] or 0),
                }

        # --- Aliases: who points to whom. Basis for Invariant 21.
        aliases: Dict[str, str] = {}
        if "exercise_aliases" in tables:
            for row in cursor.execute("SELECT old_id, new_id FROM exercise_aliases"):
                aliases[str(row["old_id"])] = str(row["new_id"])
        for exercise_id, entry in exercises.items():
            merged_into = entry.get("merged_into")
            if merged_into:
                aliases.setdefault(exercise_id, str(merged_into))

        status_counts: Dict[str, int] = {}
        if "status" in exercise_columns:
            for entry in exercises.values():
                status = entry.get("status") or "active"
                status_counts[status] = status_counts.get(status, 0) + 1
        else:
            # v1 database: only active exercises exist.
            status_counts["active"] = len(exercises)

        return {
            "path": db_path,
            "version": metadata.get("version", ""),
            "schema_version": _int_or_none(metadata.get("schema_version")),
            "metadata": metadata,
            "compare_fields": compare_fields,
            "exercise_count": len(exercises),
            "active_count": status_counts.get("active", 0),
            "status_counts": status_counts,
            "translations": translations,
            "aliases": aliases,
            "exercises": exercises,
        }
    finally:
        conn.close()


def _columns(cursor: sqlite3.Cursor, table: str) -> set:
    return {row["name"] for row in cursor.execute(f"PRAGMA table_info({table})")}


def _int_or_none(value: Any) -> Any:
    try:
        return int(str(value))
    except (TypeError, ValueError):
        return None


def compare_catalogs(
    old_catalog: Dict[str, Any],
    new_catalog: Dict[str, Any],
    args: argparse.Namespace,
) -> Dict[str, Any]:
    old_ids = set(old_catalog["exercises"].keys())
    new_ids = set(new_catalog["exercises"].keys())

    removed_ids = sorted(old_ids - new_ids)
    added_ids = sorted(new_ids - old_ids)
    shared_ids = sorted(old_ids & new_ids)
    removed_threshold_exceeded = len(removed_ids) > args.fail_on_removed_threshold

    compare_fields = sorted(set(old_catalog["compare_fields"]) | set(new_catalog["compare_fields"]))
    changed_fields_by_id: Dict[str, Dict[str, Dict[str, Any]]] = {}
    changed_field_counts = {field: 0 for field in compare_fields}

    regressions = {
        "name_de_became_blank": 0,
        "name_en_became_blank": 0,
        "description_de_became_blank": 0,
        "description_en_became_blank": 0,
        "category_became_blank": 0,
        "muscles_primary_became_blank": 0,
        "muscles_secondary_became_blank": 0,
        "de_name_lost_en_still_present": 0,
        # --- Schema v2
        "muscle_assignments_became_blank": 0,
        "license_became_blank": 0,
        "became_inactive": 0,
        "slug_changed": 0,
    }

    for exercise_id in shared_ids:
        old_row = old_catalog["exercises"][exercise_id]
        new_row = new_catalog["exercises"][exercise_id]
        field_changes: Dict[str, Dict[str, Any]] = {}

        for field in compare_fields:
            old_value = normalize_value(old_row.get(field))
            new_value = normalize_value(new_row.get(field))
            if old_value != new_value:
                field_changes[field] = {"old": old_value, "new": new_value}
                changed_field_counts[field] += 1

            if field == "name_de" and not is_blank(old_value) and is_blank(new_value):
                regressions["name_de_became_blank"] += 1
            elif field == "name_en" and not is_blank(old_value) and is_blank(new_value):
                regressions["name_en_became_blank"] += 1
            elif field == "description_de" and not is_blank(old_value) and is_blank(new_value):
                regressions["description_de_became_blank"] += 1
            elif field == "description_en" and not is_blank(old_value) and is_blank(new_value):
                regressions["description_en_became_blank"] += 1
            elif field == "category_name" and not is_blank(old_value) and is_blank(new_value):
                regressions["category_became_blank"] += 1
            elif field == "muscles_primary" and not is_blank(old_value) and is_blank(new_value):
                regressions["muscles_primary_became_blank"] += 1
            elif field == "muscles_secondary" and not is_blank(old_value) and is_blank(new_value):
                regressions["muscles_secondary_became_blank"] += 1

            elif (
                field == "muscle_assignments"
                and not is_blank(old_value)
                and is_blank(new_value)
            ):
                regressions["muscle_assignments_became_blank"] += 1
            elif (
                field == "upstream_license"
                and not is_blank(old_value)
                and is_blank(new_value)
            ):
                regressions["license_became_blank"] += 1

        if not is_blank(old_row.get("name_de")) and is_blank(new_row.get("name_de")) and not is_blank(
            new_row.get("name_en")
        ):
            regressions["de_name_lost_en_still_present"] += 1

        # `slug` is a contract under SCHEMA.md §3 and should not change. If it does,
        # someone needs to review it before release.
        old_slug = old_row.get("slug")
        new_slug = new_row.get("slug")
        if not is_blank(old_slug) and not is_blank(new_slug) and old_slug != new_slug:
            regressions["slug_changed"] += 1

        # An exercise transitioning out of the active catalog without being deleted —
        # this is the intended path (SCHEMA.md §3), but still tracked.
        if old_row.get("status") in ("", "active") and new_row.get("status") in (
            "deprecated",
            "merged",
        ):
            regressions["became_inactive"] += 1

        if field_changes:
            changed_fields_by_id[exercise_id] = field_changes

    old_count = old_catalog["exercise_count"]
    new_count = new_catalog["exercise_count"]
    count_delta = new_count - old_count
    row_drop_percent = 0.0
    if old_count > 0 and new_count < old_count:
        row_drop_percent = ((old_count - new_count) / old_count) * 100.0

    warnings: List[Dict[str, Any]] = []

    if len(removed_ids) > 0:
        warnings.append(
            {
                "code": "REMOVED_IDS",
                "severity": "warning",
                "value": len(removed_ids),
                "message": f"Exercises removed: {len(removed_ids)}",
            }
        )

    if len(removed_ids) >= args.removed_severe_threshold:
        warnings.append(
            {
                "code": "REMOVED_IDS_SEVERE",
                "severity": "severe",
                "value": len(removed_ids),
                "message": (
                    f"Exercises removed exceeds severe threshold "
                    f"({len(removed_ids)} >= {args.removed_severe_threshold})"
                ),
            }
        )

    if regressions["name_de_became_blank"] > 0 or regressions["name_en_became_blank"] > 0:
        warnings.append(
            {
                "code": "NAME_REGRESSION",
                "severity": "warning",
                "value": {
                    "name_de_became_blank": regressions["name_de_became_blank"],
                    "name_en_became_blank": regressions["name_en_became_blank"],
                },
                "message": "Previously non-empty exercise names became blank.",
            }
        )

    category_loss = regressions["category_became_blank"]
    if category_loss > 0:
        severity = (
            "severe"
            if category_loss >= max(1, args.category_regression_threshold * 2)
            else "warning"
        )
        warnings.append(
            {
                "code": "CATEGORY_REGRESSION",
                "severity": severity,
                "value": category_loss,
                "message": f"Categories became blank for {category_loss} exercises.",
            }
        )

    muscle_loss = (
        regressions["muscles_primary_became_blank"]
        + regressions["muscles_secondary_became_blank"]
    )
    if muscle_loss > 0:
        severity = (
            "severe" if muscle_loss >= max(1, args.muscle_regression_threshold * 2) else "warning"
        )
        warnings.append(
            {
                "code": "MUSCLE_REGRESSION",
                "severity": severity,
                "value": {
                    "muscles_primary_became_blank": regressions["muscles_primary_became_blank"],
                    "muscles_secondary_became_blank": regressions["muscles_secondary_became_blank"],
                },
                "message": "Muscle lists became blank unexpectedly for shared IDs.",
            }
        )

    if regressions["de_name_lost_en_still_present"] >= args.de_fallback_shift_threshold:
        warnings.append(
            {
                "code": "DE_FALLBACK_SHIFT",
                "severity": "warning",
                "value": regressions["de_name_lost_en_still_present"],
                "message": (
                    "Large fallback shift detected: many DE names disappeared while EN remains."
                ),
            }
        )

    # --- Invariant 21: no active entry disappears without successor.
    new_aliases = new_catalog.get("aliases", {})
    unmapped_removals = sorted(
        exercise_id for exercise_id in removed_ids if exercise_id not in new_aliases
    )
    if unmapped_removals:
        warnings.append(
            {
                "code": "INVARIANT_21_UNMAPPED_REMOVAL",
                "severity": "severe",
                "value": len(unmapped_removals),
                "message": (
                    f"{len(unmapped_removals)} exercises disappeared without an alias "
                    f"or merged_into pointing to a successor. Logs referencing these IDs "
                    f"would become unresolvable (SCHEMA.md 3). Examples: "
                    f"{', '.join(unmapped_removals[:5])}"
                ),
            }
        )

    # --- Invariant 22: active exercise count never drops by more than 5%.
    old_active = old_catalog.get("active_count", old_count)
    new_active = new_catalog.get("active_count", new_count)
    active_drop_percent = 0.0
    if old_active > 0 and new_active < old_active:
        active_drop_percent = ((old_active - new_active) / old_active) * 100.0
    if active_drop_percent > INVARIANT_22_MAX_ACTIVE_DROP_PERCENT:
        warnings.append(
            {
                "code": "INVARIANT_22_ACTIVE_COUNT_DROP",
                "severity": "severe",
                "value": active_drop_percent,
                "message": (
                    f"Active exercises dropped by {active_drop_percent:.2f}% "
                    f"({old_active} -> {new_active}), allowed: "
                    f"{INVARIANT_22_MAX_ACTIVE_DROP_PERCENT:.0f}%."
                ),
            }
        )

    # --- License provenance. Distribution is not covered without it.
    if regressions["license_became_blank"] > 0:
        warnings.append(
            {
                "code": "LICENSE_REGRESSION",
                "severity": "severe",
                "value": regressions["license_became_blank"],
                "message": (
                    f"{regressions['license_became_blank']} exercises lost their license "
                    f"attribution (SCHEMA.md 3b)."
                ),
            }
        )
    lost_translation_licenses = sum(
        entry["without_license"] for entry in new_catalog.get("translations", {}).values()
    )
    if lost_translation_licenses:
        warnings.append(
            {
                "code": "TRANSLATION_LICENSE_MISSING",
                "severity": "warning",
                "value": lost_translation_licenses,
                "message": (
                    f"{lost_translation_licenses} translations without license attribution. "
                    f"wger licenses per entry; attribution is incomplete without it."
                ),
            }
        )

    # --- schema_version must never decrease (SCHEMA.md 9).
    old_schema = old_catalog.get("schema_version")
    new_schema = new_catalog.get("schema_version")
    if old_schema is not None and new_schema is not None and new_schema < old_schema:
        warnings.append(
            {
                "code": "SCHEMA_VERSION_REGRESSION",
                "severity": "severe",
                "value": {"old": old_schema, "new": new_schema},
                "message": (
                    f"schema_version dropped from {old_schema} to {new_schema}. Consumers "
                    f"already on {old_schema} cannot read this."
                ),
            }
        )

    if regressions["slug_changed"] > 0:
        warnings.append(
            {
                "code": "SLUG_CHANGED",
                "severity": "warning",
                "value": regressions["slug_changed"],
                "message": (
                    f"{regressions['slug_changed']} slugs changed. Slugs are stable per "
                    f"SCHEMA.md 3."
                ),
            }
        )

    if row_drop_percent >= args.row_drop_warn_percent:
        severity = "severe" if row_drop_percent >= args.row_drop_severe_percent else "warning"
        warnings.append(
            {
                "code": "ROW_COUNT_DROP",
                "severity": severity,
                "value": row_drop_percent,
                "message": (
                    f"Total exercise row count dropped by {row_drop_percent:.2f}% "
                    f"({old_count} -> {new_count})."
                ),
            }
        )

    changed_exercise_count = len(changed_fields_by_id)
    changed_field_counts = {
        field: count for field, count in changed_field_counts.items() if count > 0
    }

    report = {
        "old": {
            "path": old_catalog["path"],
            "version": old_catalog["version"],
            "schema_version": old_schema,
            "exercise_count": old_count,
            "active_count": old_active,
            "translations": old_catalog.get("translations", {}),
        },
        "new": {
            "path": new_catalog["path"],
            "version": new_catalog["version"],
            "schema_version": new_schema,
            "exercise_count": new_count,
            "active_count": new_active,
            "translations": new_catalog.get("translations", {}),
        },
        "delta": {
            "exercise_count": count_delta,
            "active_count": new_active - old_active,
        },
        "removed_ids": removed_ids,
        "added_ids": added_ids,
        "unmapped_removed_ids": unmapped_removals,
        "changed_fields_by_id": changed_fields_by_id,
        "summary": {
            "shared_id_count": len(shared_ids),
            "removed_count": len(removed_ids),
            "fail_on_removed_threshold": args.fail_on_removed_threshold,
            "removed_threshold_exceeded": removed_threshold_exceeded,
            "added_count": len(added_ids),
            "changed_exercise_count": changed_exercise_count,
            "changed_field_counts": changed_field_counts,
            "row_drop_percent": row_drop_percent,
            "active_drop_percent": active_drop_percent,
            "unmapped_removed_count": len(unmapped_removals),
            "regressions": regressions,
        },
        "warning_flags": warnings,
        "examples": {
            "removed_ids": removed_ids[: args.examples],
            "added_ids": added_ids[: args.examples],
            "changed_ids": sorted(changed_fields_by_id.keys())[: args.examples],
            "changed_rows": build_changed_row_examples(changed_fields_by_id, args.examples),
        },
    }
    return report


def build_changed_row_examples(
    changed_fields_by_id: Dict[str, Dict[str, Dict[str, Any]]], limit: int
) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for exercise_id in sorted(changed_fields_by_id.keys())[:limit]:
        for field, values in changed_fields_by_id[exercise_id].items():
            rows.append(
                {
                    "id": exercise_id,
                    "field": field,
                    "old": values["old"],
                    "new": values["new"],
                }
            )
            if len(rows) >= limit:
                return rows
    return rows


def print_console_report(report: Dict[str, Any], examples: int) -> None:
    old = report["old"]
    new = report["new"]
    summary = report["summary"]
    warnings = report["warning_flags"]

    print("=" * 72)
    print("WGER CATALOG DIFF REPORT")
    print("=" * 72)
    print("Metadata / Version:")
    print(f"  Old version: {old['version'] or '(missing)'}")
    print(f"  New version: {new['version'] or '(missing)'}")
    print(f"  Schema version: {old.get('schema_version')} -> {new.get('schema_version')}")
    print(f"  Old row count: {old['exercise_count']} ({old.get('active_count')} active)")
    print(f"  New row count: {new['exercise_count']} ({new.get('active_count')} active)")
    delta = report["delta"]["exercise_count"]
    print(f"  Total delta: {delta:+d}")
    print("")

    old_translations = old.get("translations") or {}
    new_translations = new.get("translations") or {}
    if old_translations or new_translations:
        print("Translations per language:")
        for language in sorted(set(old_translations) | set(new_translations)):
            before = old_translations.get(language, {}).get("rows", 0)
            after = new_translations.get(language, {}).get("rows", 0)
            marker = "  <-- disappeared" if before and not after else ""
            print(f"  {language}: {before} -> {after}{marker}")
        print("")

    print("ID-level catalog diff:")
    print(f"  Removed IDs: {summary['removed_count']}")
    print(f"  Fail-on-removed threshold: {summary['fail_on_removed_threshold']}")
    print(f"  Removed threshold exceeded: {summary['removed_threshold_exceeded']}")
    print(f"  Added IDs: {summary['added_count']}")
    if report["examples"]["removed_ids"]:
        print(f"  Removed examples ({min(examples, summary['removed_count'])}):")
        for exercise_id in report["examples"]["removed_ids"]:
            print(f"    - {exercise_id}")
    if report["examples"]["added_ids"]:
        print(f"  Added examples ({min(examples, summary['added_count'])}):")
        for exercise_id in report["examples"]["added_ids"]:
            print(f"    - {exercise_id}")
    print("")

    print("Field-level changes (shared IDs):")
    print(f"  Shared IDs: {summary['shared_id_count']}")
    print(f"  Exercises with any field changes: {summary['changed_exercise_count']}")
    changed_field_counts = summary["changed_field_counts"]
    if changed_field_counts:
        for field in sorted(changed_field_counts.keys()):
            print(f"  - {field}: {changed_field_counts[field]}")
    else:
        print("  No field changes detected on shared IDs.")
    print("")

    print("Suspicious regressions:")
    regressions = summary["regressions"]
    print(f"  name_de became blank: {regressions['name_de_became_blank']}")
    print(f"  name_en became blank: {regressions['name_en_became_blank']}")
    print(f"  description_de became blank: {regressions['description_de_became_blank']}")
    print(f"  description_en became blank: {regressions['description_en_became_blank']}")
    print(f"  category became blank: {regressions['category_became_blank']}")
    print(f"  muscles_primary became blank: {regressions['muscles_primary_became_blank']}")
    print(f"  muscles_secondary became blank: {regressions['muscles_secondary_became_blank']}")
    print(
        f"  de_name lost while en still present: {regressions['de_name_lost_en_still_present']}"
    )
    print(f"  muscle assignments became blank: {regressions.get('muscle_assignments_became_blank', 0)}")
    print(f"  license became blank: {regressions.get('license_became_blank', 0)}")
    print(f"  became deprecated or merged: {regressions.get('became_inactive', 0)}")
    print(f"  slug changed: {regressions.get('slug_changed', 0)}")
    print(f"  Row drop percent: {summary['row_drop_percent']:.2f}%")
    print(f"  Active drop percent: {summary.get('active_drop_percent', 0.0):.2f}%")
    print(
        f"  Removed without a successor (invariant 21): "
        f"{summary.get('unmapped_removed_count', 0)}"
    )
    print("")

    if warnings:
        print("Warning flags:")
        for warning in warnings:
            print(
                f"  [{warning['severity'].upper()}] {warning['code']}: {warning['message']}"
            )
    else:
        print("Warning flags: none")
    print("")

    if report["examples"]["changed_rows"]:
        print("Changed field examples:")
        for row in report["examples"]["changed_rows"][:examples]:
            print(
                f"  id={row['id']} field={row['field']} "
                f"old={json.dumps(row['old'], ensure_ascii=False)} "
                f"new={json.dumps(row['new'], ensure_ascii=False)}"
            )
        print("")


def should_fail(report: Dict[str, Any], args: argparse.Namespace) -> Tuple[bool, List[str]]:
    reasons: List[str] = []
    removed_count = report["summary"]["removed_count"]
    regressions = report["summary"]["regressions"]
    warnings = report["warning_flags"]

    if removed_count > args.fail_on_removed_threshold:
        reasons.append(
            f"removed_count={removed_count} > fail_on_removed_threshold={args.fail_on_removed_threshold}"
        )

    if regressions["name_de_became_blank"] > 0 or regressions["name_en_became_blank"] > 0:
        reasons.append("name regression detected (non-empty name became blank)")

    unmapped = report["summary"].get("unmapped_removed_count", 0)
    if unmapped:
        reasons.append(
            f"invariant 21: {unmapped} exercises removed without an alias to a successor"
        )

    severe_breaking_codes = {
        "CATEGORY_REGRESSION",
        "MUSCLE_REGRESSION",
        "ROW_COUNT_DROP",
        # --- Schema v2. All of these render distributed data unusable or
        # legally unprotected; none can be demoted to a mere warning.
        "INVARIANT_21_UNMAPPED_REMOVAL",
        "INVARIANT_22_ACTIVE_COUNT_DROP",
        "LICENSE_REGRESSION",
        "SCHEMA_VERSION_REGRESSION",
    }
    if any(
        warning["severity"] == "severe"
        and warning.get("code") in severe_breaking_codes
        for warning in warnings
    ):
        reasons.append("severe warning present")

    return len(reasons) > 0, reasons


def main() -> int:
    args = parse_args()
    try:
        old_catalog = load_catalog(args.old)
        new_catalog = load_catalog(args.new)
        report = compare_catalogs(
            old_catalog,
            new_catalog,
            args,
        )
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print_console_report(report, args.examples)

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"JSON report written to: {args.json_out}")

    if args.fail_on_breaking:
        fail, reasons = should_fail(report, args)
        if fail:
            print("")
            print("FAIL-ON-BREAKING triggered:")
            for reason in reasons:
                print(f"  - {reason}")
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
