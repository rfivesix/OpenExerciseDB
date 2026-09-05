#!/usr/bin/env python3
"""Builds the deliverable SQLite database from `data/` (SCHEMA.md §8).

Second half of the decomposed `create_wger_exercise_db.py`. The difference from
the legacy script is not the output, but the input: nothing is downloaded here.
The build reads exclusively from the text files in the repository and is
therefore offline, reproducible, and testable.

**The four compatibility columns.** `id`, `category_name`, `muscles_primary`,
and `muscles_secondary` — plus `exercise_translations` — are exactly what
`_mapExerciseBundle` in the current app reads. As long as they are populated,
the app runs unmodified on this database; this is the acceptance threshold for
Phase 1 and is verified by `test/test_compat.py` against the published
reference DB.

Legacy muscle names are not passed through directly, but reverse-mapped from
the new vocabulary (`MuscleVocabulary.legacy_wger_name`). This costs nothing in
Phase 1 and pays off in Phase 2: if `trapezius` is later refined to
`traps_upper`, the compatibility column still contains `Trapezius` without
anyone having to remember it.

Usage:

    python3 build/build_db.py --db-out artifacts/openexercisedb.db \\
        --report-json-out artifacts/build_report.json
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sqlite3
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from oedb import dataset as dataset_mod  # noqa: E402
from oedb.vocab import Vocabularies  # noqa: E402

SCHEMA_VERSION = 2
MIN_APP_SCHEMA_VERSION = 1
REPO_LICENSE = "CC-BY-SA-4.0"
DEFAULT_SOURCE_REPO = "https://github.com/rfivesix/openexercisedb"

CATEGORY_OTHER = "Andere"
"""Fallback from the legacy script for exercises without a category. Retained
because the current app expects it."""

STRICT_WHEN_COMPLETE = (
    "modality",
    "mechanic",
    "movement_pattern",
    "laterality",
    "tracking_type",
    "load_mode",
    "primary_equipment",
)
"""Marked as NOT NULL in SCHEMA.md §8, but not yet populated in Phase 1.

The build sets the NOT NULL constraint exactly when the data supports it — and
writes into `metadata.nullable_columns` which ones are still open. This tightens
the schema automatically as Phase 2 progresses, instead of waiting for someone
to remember. A placeholder value would have been an alternative, but would be
indistinguishable from a real value.

`force_vector` is intentionally NOT in this list: eight movement patterns map to
`null` by design (e.g. running is neither push nor pull). The column will therefore
never be completely populated — if it were here, `nullable_columns` could never
be empty, and the question "is v2 complete in content?" would be unanswerable."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--db-out",
        default="artifacts/openexercisedb.db",
        help="Output path for the SQLite database file (default: artifacts/openexercisedb.db)",
    )
    parser.add_argument("--report-json-out", help="Path for the machine-readable build report JSON")
    parser.add_argument(
        "--version",
        help="Content version (default: UTC timestamp YYYYMMDDHHMM, same format as before)",
    )
    parser.add_argument(
        "--source-repo",
        default=os.environ.get("SOURCE_REPO", DEFAULT_SOURCE_REPO),
        help="Repository URL for metadata.source_repo and attribution",
    )
    return parser.parse_args()


# ------------------------------------------------------------------------ DDL


def build_ddl(nullable: set[str]) -> list[str]:
    def null(column: str) -> str:
        return "" if column in nullable else " NOT NULL"

    return [
        f"""
        CREATE TABLE exercises (
          id                    TEXT PRIMARY KEY,
          slug                  TEXT NOT NULL UNIQUE,
          status                TEXT NOT NULL,
          merged_into           TEXT REFERENCES exercises(id),
          modality              TEXT{null('modality')},
          mechanic              TEXT{null('mechanic')},
          -- Always nullable: derived from movement_pattern, and eight patterns
          -- map to NULL by design (SCHEMA.md §6).
          force_vector          TEXT,
          movement_pattern      TEXT{null('movement_pattern')},
          laterality            TEXT{null('laterality')},
          difficulty            TEXT,
          tracking_type         TEXT{null('tracking_type')},
          load_mode             TEXT{null('load_mode')},
          supports_added_weight INTEGER NOT NULL DEFAULT 0,
          primary_equipment     TEXT{null('primary_equipment')},
          body_region           TEXT,

          -- Compatibility columns for schema v1 consumers (current app).
          category_name         TEXT,
          muscles_primary       TEXT,
          muscles_secondary     TEXT,
          image_path            TEXT,
          is_custom             INTEGER NOT NULL DEFAULT 0,
          created_by            TEXT DEFAULT 'system',
          source                TEXT DEFAULT 'base',

          -- License provenance, SCHEMA.md §3b.
          upstream_source         TEXT,
          upstream_id             TEXT,
          upstream_license        TEXT,
          upstream_license_author TEXT
        )""",
        """
        CREATE TABLE exercise_muscles (
          exercise_id  TEXT NOT NULL REFERENCES exercises(id) ON DELETE CASCADE,
          muscle_id    TEXT NOT NULL REFERENCES muscles(id),
          role         TEXT NOT NULL,
          contribution REAL,
          PRIMARY KEY (exercise_id, muscle_id)
        )""",
        """
        CREATE TABLE exercise_equipment (
          exercise_id  TEXT NOT NULL REFERENCES exercises(id) ON DELETE CASCADE,
          equipment_id TEXT NOT NULL REFERENCES equipment(id),
          kind         TEXT NOT NULL,
          PRIMARY KEY (exercise_id, equipment_id, kind)
        )""",
        """
        CREATE TABLE exercise_tags (
          exercise_id TEXT NOT NULL REFERENCES exercises(id) ON DELETE CASCADE,
          tag         TEXT NOT NULL,
          PRIMARY KEY (exercise_id, tag)
        )""",
        """
        CREATE TABLE exercise_translations (
          id              TEXT PRIMARY KEY,
          exercise_id     TEXT NOT NULL REFERENCES exercises(id) ON DELETE CASCADE,
          language_code   TEXT NOT NULL,
          name            TEXT NOT NULL,
          description     TEXT,
          instructions    TEXT,
          cues            TEXT,
          common_mistakes TEXT,
          search_terms    TEXT,
          status          TEXT,
          source_lang     TEXT,
          license         TEXT,
          license_author  TEXT
        )""",
        """
        CREATE TABLE muscles (
          id           TEXT PRIMARY KEY,
          parent_id    TEXT REFERENCES muscles(id),
          level        TEXT NOT NULL,
          group_id     TEXT NOT NULL REFERENCES muscles(id),
          legacy_group TEXT,
          body_slugs   TEXT
        )""",
        """
        CREATE TABLE muscle_translations (
          muscle_id     TEXT,
          language_code TEXT,
          name          TEXT,
          PRIMARY KEY (muscle_id, language_code)
        )""",
        "CREATE TABLE equipment (id TEXT PRIMARY KEY, kind TEXT NOT NULL)",
        """
        CREATE TABLE equipment_translations (
          equipment_id  TEXT,
          language_code TEXT,
          name          TEXT,
          PRIMARY KEY (equipment_id, language_code)
        )""",
        """
        CREATE TABLE languages (
          code         TEXT PRIMARY KEY,
          tier         TEXT NOT NULL,
          completeness REAL NOT NULL,
          displayable  INTEGER NOT NULL
        )""",
        """
        CREATE TABLE exercise_aliases (
          old_id        TEXT PRIMARY KEY,
          new_id        TEXT NOT NULL REFERENCES exercises(id),
          reason        TEXT,
          since_version TEXT NOT NULL
        )""",
        "CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT)",
        "CREATE INDEX idx_tr_exercise_lang ON exercise_translations(exercise_id, language_code)",
        # "Which exercises target this muscle?" is the core query of
        # recovery and volume statistics.
        "CREATE INDEX idx_ex_muscles_muscle ON exercise_muscles(muscle_id)",
    ]


# ------------------------------------------------------------------- helpers


def json_array(values: list[Any] | None) -> str | None:
    return json.dumps(values, ensure_ascii=False) if values else None


GROUP_TO_BODY_REGION: dict[str, str] = {
    "chest": "upper_body",
    "back": "upper_body",
    "shoulders": "upper_body",
    "biceps": "upper_body",
    "triceps": "upper_body",
    "forearms": "upper_body",
    "neck": "upper_body",
    "glutes": "lower_body",
    "quads": "lower_body",
    "hamstrings": "lower_body",
    "adductors": "lower_body",
    "calves": "lower_body",
    "abs": "core",
    "lower_back": "core",
}


def derive_body_region(vocab: Vocabularies, primary_muscle_ids: list[str]) -> str | None:
    """Derives the body region from primary muscles according to SCHEMA.md §6."""
    groups = {
        vocab.muscles.nodes[m].group_id
        for m in primary_muscle_ids
        if m in vocab.muscles.nodes
    }
    regions = {GROUP_TO_BODY_REGION[g] for g in groups if g in GROUP_TO_BODY_REGION}
    if not regions:
        return None
    if len(regions) == 1:
        return next(iter(regions))
    return "full_body"



def legacy_muscle_json(vocab: Vocabularies, node_ids: list[str]) -> str:
    """JSON array of wger legacy names as expected by the current app.

    Sorted and deduplicated — character-identical to `json.dumps(sorted({...}))`
    in the legacy script, otherwise the character comparison in test/test_compat.py
    fails. Nodes without a legacy name (such as erector spinae) are omitted: the
    current app would silently discard them anyway.
    """
    names = {
        name
        for name in (vocab.muscles.legacy_wger_name(node) for node in node_ids)
        if name is not None
    }
    return json.dumps(sorted(names))


def git_commit() -> str:
    for env_key in ("GITHUB_SHA", "SOURCE_COMMIT"):
        value = os.environ.get(env_key)
        if value:
            return value
    try:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
            cwd=Path(__file__).resolve().parents[1],
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def resolve_text(
    data: dataset_mod.Dataset, language: str, exercise_id: str, chain: tuple[str, ...]
) -> tuple[dataset_mod.Translation, str | None] | None:
    """Text in `language`, otherwise the first hit from the fallback chain.

    Returns: (text, source_lang_if_fallback). The second element is written to
    `exercise_translations.source_lang` — the legacy app did not provide this
    information, making it impossible to tell which rows were actually native.
    """
    native = data.translation(language, exercise_id)
    if native is not None:
        return native, None
    for fallback in chain:
        candidate = data.translation(fallback, exercise_id)
        if candidate is not None:
            return candidate, fallback
    return None


# --------------------------------------------------------------------- build


def build(args: argparse.Namespace) -> tuple[int, dict[str, Any]]:
    vocab = Vocabularies()
    data = dataset_mod.load()

    if not data.exercises:
        print("No exercises found under data/exercises/.", file=sys.stderr)
        return 2, {}

    exercises = data.sorted_exercises()
    version = args.version or dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d%H%M")
    generated_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()

    # Which columns marked as NOT NULL in SCHEMA.md §8 are already fully
    # populated in the dataset today?
    nullable = {
        column
        for column in STRICT_WHEN_COMPLETE
        if any(not exercise.get(column) for exercise in exercises)
    }
    field_coverage = {
        column: sum(1 for exercise in exercises if exercise.get(column))
        for column in STRICT_WHEN_COMPLETE
    }

    db_path = Path(args.db_out)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if db_path.exists():
        db_path.unlink()

    connection = sqlite3.connect(db_path)
    # journal_mode=DELETE: the file is delivered as a single asset; a leftover
    # -wal file would be invisible data loss for the consumer.
    connection.execute("PRAGMA journal_mode=DELETE")
    cursor = connection.cursor()
    for statement in build_ddl(nullable):
        cursor.execute(statement)

    # ----------------------------------------------------------- Vocabularies
    muscle_rows = []
    muscle_translation_rows = []
    for node in vocab.muscles.nodes.values():
        muscle_rows.append(
            (
                node.id,
                node.parent_id,
                node.level,
                node.group_id,
                node.legacy_group,
                json.dumps(list(node.body_slugs), ensure_ascii=False),
            )
        )
        for language, name in sorted(node.names.items()):
            muscle_translation_rows.append((node.id, language, name))
    cursor.executemany("INSERT INTO muscles VALUES (?, ?, ?, ?, ?, ?)", muscle_rows)
    cursor.executemany("INSERT INTO muscle_translations VALUES (?, ?, ?)", muscle_translation_rows)

    equipment_rows = []
    equipment_translation_rows = []
    for equipment_id, kind in vocab.equipment_kinds.items():
        equipment_rows.append((equipment_id, kind))
        for language, name in sorted(vocab.equipment_names.get(equipment_id, {}).items()):
            equipment_translation_rows.append((equipment_id, language, name))
    cursor.executemany("INSERT INTO equipment VALUES (?, ?)", equipment_rows)
    cursor.executemany(
        "INSERT INTO equipment_translations VALUES (?, ?, ?)", equipment_translation_rows
    )

    # -------------------------------------------------------------- Exercises
    exercise_rows = []
    muscle_link_rows = []
    equipment_link_rows = []
    tag_rows = []
    alias_rows = []
    unknown_muscle_nodes: Counter = Counter()

    for exercise in exercises:
        upstream = exercise.upstream or {}
        primary = exercise.muscle_ids("primary")
        secondary = exercise.muscle_ids("secondary")
        for node_id in primary + secondary:
            if node_id not in vocab.muscles:
                unknown_muscle_nodes[node_id] += 1

        exercise_rows.append(
            (
                exercise.id,
                exercise.slug,
                exercise.status,
                exercise.get("merged_into"),
                exercise.get("modality"),
                exercise.get("mechanic"),
                # Derived, not copied from the source file: force_vector
                # is a function of movement_pattern (SCHEMA.md §6). The build
                # is the sole writer of this column — otherwise it drifts.
                vocab.force_vector_for(exercise.get("movement_pattern")),
                exercise.get("movement_pattern"),
                exercise.get("laterality"),
                exercise.get("difficulty"),
                exercise.get("tracking_type"),
                exercise.get("load_mode"),
                1 if exercise.get("supports_added_weight") else 0,
                exercise.get("primary_equipment"),
                exercise.get("body_region") or derive_body_region(vocab, primary),
                # --- Compatibility columns
                exercise.source_fields.get("category") or CATEGORY_OTHER,
                legacy_muscle_json(vocab, primary),
                legacy_muscle_json(vocab, secondary),
                # The legacy script writes "" here rather than NULL. The current app
                # receives an empty string; switching to NULL would be a behavioral
                # change without benefit as long as there are no media assets.
                "",
                0,
                "system",
                "base",
                # --- License provenance
                upstream.get("source"),
                upstream.get("source_id"),
                upstream.get("license"),
                upstream.get("license_author"),
            )
        )

        for role, node_ids in (("primary", primary), ("secondary", secondary)):
            for node_id in node_ids:
                muscle_link_rows.append((exercise.id, node_id, role, None))

        primary_equipment = exercise.get("primary_equipment")
        if primary_equipment:
            equipment_link_rows.append((exercise.id, primary_equipment, "primary"))
        for setup_item in exercise.get("setup") or []:
            equipment_link_rows.append((exercise.id, setup_item, "setup"))

        for tag in exercise.get("usage_tags") or []:
            tag_rows.append((exercise.id, tag))

        for old_id in exercise.get("aliases") or []:
            alias_rows.append((str(old_id), exercise.id, "renamed_id", version))
        if exercise.status == "merged" and exercise.get("merged_into"):
            alias_rows.append((exercise.id, str(exercise.get("merged_into")), "merged", version))

    cursor.executemany(
        f"INSERT INTO exercises VALUES ({', '.join('?' * len(exercise_rows[0]))})", exercise_rows
    )
    cursor.executemany("INSERT INTO exercise_muscles VALUES (?, ?, ?, ?)", muscle_link_rows)
    cursor.executemany("INSERT INTO exercise_equipment VALUES (?, ?, ?)", equipment_link_rows)
    cursor.executemany("INSERT INTO exercise_tags VALUES (?, ?)", tag_rows)
    cursor.executemany("INSERT INTO exercise_aliases VALUES (?, ?, ?, ?)", alias_rows)

    # ----------------------------------------------------------- Translations
    translation_rows = []
    native_counts: Counter = Counter()
    fallback_counts: Counter = Counter()

    for code, language in vocab.languages.items():
        for exercise in exercises:
            resolved = resolve_text(data, code, exercise.id, language.fallback_chain)
            if resolved is None:
                continue
            text, source_lang = resolved
            if source_lang is not None:
                if not language.complete_in_release:
                    # Without this guarantee, 20 languages would each generate
                    # English text under a foreign flag.
                    continue
                if exercise.status == "active":
                    fallback_counts[code] += 1
            else:
                if exercise.status == "active":
                    native_counts[code] += 1

            upstream = text.upstream
            translation_rows.append(
                (
                    f"{exercise.id}_{code}",
                    exercise.id,
                    code,
                    text.name,
                    # The legacy script writes "" instead of NULL when no
                    # description exists. Retained.
                    text.get("description") or "",
                    json_array(text.get("instructions")),
                    json_array(text.get("cues")),
                    json_array(text.get("common_mistakes")),
                    json_array(text.get("search_terms")),
                    text.get("status"),
                    source_lang,
                    upstream.get("license"),
                    upstream.get("license_author"),
                )
            )

    cursor.executemany(
        f"INSERT INTO exercise_translations VALUES ({', '.join('?' * 13)})", translation_rows
    )

    # -------------------------------------------------------------- Languages
    active_count = sum(1 for exercise in exercises if exercise.status == "active")
    language_rows = []
    completeness_report: dict[str, dict[str, Any]] = {}
    for code, language in vocab.languages.items():
        native = native_counts.get(code, 0)
        delivered = native + fallback_counts.get(code, 0)
        completeness = min(1.0, native / active_count) if active_count else 0.0
        delivered_share = min(1.0, delivered / active_count) if active_count else 0.0
        # `completeness` is the honest number: how much is actually translated.
        # `displayable` answers the other question: can the UI offer this
        # language without gaps? For a language with complete_in_release, this is
        # the case thanks to fallback even if `completeness` is low — and the app
        # sees row by row in `source_lang` what was actually translated.
        displayable = 1 if delivered_share >= vocab.min_completeness else 0
        language_rows.append((code, language.tier, round(completeness, 6), displayable))
        completeness_report[code] = {
            "tier": language.tier,
            "native": native,
            "fallback": fallback_counts.get(code, 0),
            "completeness": round(completeness, 4),
            "displayable": bool(displayable),
        }
    cursor.executemany("INSERT INTO languages VALUES (?, ?, ?, ?)", language_rows)

    # --------------------------------------------------------------- Metadata
    metadata = {
        "version": version,
        "schema_version": str(SCHEMA_VERSION),
        "min_app_schema_version": str(MIN_APP_SCHEMA_VERSION),
        "generated_at": generated_at,
        "source_repo": args.source_repo,
        "source_commit": git_commit(),
        "license": REPO_LICENSE,
        "attribution_url": f"{args.source_repo.rstrip('/')}/blob/main/ATTRIBUTION.md",
        "exercise_count": str(len(exercise_rows)),
        "translation_count": str(len(translation_rows)),
        # Columns marked as NOT NULL in SCHEMA.md §8 that are not yet
        # consistently populated. Empty means: v2 is achieved in content.
        "nullable_columns": json.dumps(sorted(nullable)),
    }
    cursor.executemany(
        "INSERT INTO metadata (key, value) VALUES (?, ?)", sorted(metadata.items())
    )

    connection.commit()
    connection.execute("PRAGMA optimize")
    connection.close()

    report = {
        "build": {
            "generated_at": generated_at,
            "db_version": version,
            "db_output_path": str(db_path),
            "schema_version": SCHEMA_VERSION,
            "min_app_schema_version": MIN_APP_SCHEMA_VERSION,
            "source_commit": metadata["source_commit"],
            "source_repo": args.source_repo,
        },
        "summary": {
            "imported_count": len(exercise_rows),
            "active_count": active_count,
            "rejected_count": 0,
            "translation_count": len(translation_rows),
            "muscle_link_count": len(muscle_link_rows),
            "equipment_link_count": len(equipment_link_rows),
            "tag_count": len(tag_rows),
            "alias_count": len(alias_rows),
        },
        "field_coverage": {
            column: {
                "filled": count,
                "of": len(exercises),
                "share": round(count / len(exercises), 4) if exercises else 0.0,
            }
            for column, count in sorted(field_coverage.items())
        },
        "nullable_columns": sorted(nullable),
        "languages": completeness_report,
        "unknown_muscle_nodes": dict(unknown_muscle_nodes),
    }
    return 0, report


def main() -> int:
    args = parse_args()
    code, report = build(args)
    if code != 0:
        return code

    summary = report["summary"]
    print(f"Database   {report['build']['db_output_path']} (Version {report['build']['db_version']})")
    print(f"Exercises  {summary['imported_count']} ({summary['active_count']} active)")
    print(f"Texts      {summary['translation_count']} rows")
    print(f"Muscles    {summary['muscle_link_count']} assignments")
    if report["nullable_columns"]:
        print(
            "Pending    not yet NOT NULL: " + ", ".join(report["nullable_columns"])
        )
    if report["unknown_muscle_nodes"]:
        print(f"WARNING    unknown muscle nodes: {report['unknown_muscle_nodes']}")

    if args.report_json_out:
        out = Path(args.report_json_out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Report     {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
