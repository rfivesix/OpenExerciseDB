#!/usr/bin/env python3
"""Sanity check on generated database directly before release.

Adopted from a legacy pipeline and extended with tables from SCHEMA.md 8.
The essential difference: the predecessor was a pure dump — it printed
tables, columns, and three sample rows, always exiting with code 0.
While useful as an external overview (`--inspect` remains available), that
does not serve as a gate: an empty translation table would only have been
noticed if someone read through the log.

Here, every assertion is a check with an exit code. What is verified is
deliberately what can go wrong between build and device — not what
`build/validate.py` already covered on the source files.

Usage:

    python3 build/check_database.py artifacts/openexercisedb.db
    python3 build/check_database.py --inspect artifacts/openexercisedb.db
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path

EXPECTED_TABLES = (
    "exercises",
    "exercise_muscles",
    "exercise_equipment",
    "exercise_tags",
    "exercise_translations",
    "muscles",
    "muscle_translations",
    "equipment",
    "equipment_translations",
    "languages",
    "exercise_aliases",
    "metadata",
)

REQUIRED_METADATA_KEYS = (
    "version",
    "schema_version",
    "generated_at",
    "source_repo",
    "source_commit",
    "license",
    "attribution_url",
)

APP_COMPAT_COLUMNS = ("id", "category_name", "muscles_primary", "muscles_secondary")
"""Read by `_mapExerciseBundle` in the existing app. If any is missing,
the app cannot load the database — the most expensive failure possible
because it is only discovered on-device."""

MIN_EXERCISES = 500
"""Lower bound from the manifest contract (`min_exercise_count`). A build
significantly below this is broken, not a new dataset."""


class Check:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.notes: list[str] = []

    def fail(self, message: str) -> None:
        self.failures.append(message)

    def note(self, message: str) -> None:
        self.notes.append(message)

    def expect(self, condition: bool, message: str) -> bool:
        if not condition:
            self.fail(message)
        return condition


def table_names(connection: sqlite3.Connection) -> set[str]:
    return {
        row[0]
        for row in connection.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
        )
    }


def columns(connection: sqlite3.Connection, table: str) -> dict[str, str]:
    return {row[1]: row[2] for row in connection.execute(f"PRAGMA table_info({table})")}


def count(connection: sqlite3.Connection, table: str) -> int:
    return int(connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0])


def run_checks(connection: sqlite3.Connection, check: Check) -> dict:
    connection.row_factory = sqlite3.Row
    tables = table_names(connection)
    stats: dict = {"tables": sorted(tables)}

    for table in EXPECTED_TABLES:
        check.expect(table in tables, f"Table {table} missing")

    if "exercises" not in tables:
        return stats

    # --- App contract
    exercise_columns = columns(connection, "exercises")
    for column in APP_COMPAT_COLUMNS:
        check.expect(
            column in exercise_columns,
            f"Compatibility column exercises.{column} missing — the app "
            f"could not load this database",
        )

    exercise_count = count(connection, "exercises")
    stats["exercise_count"] = exercise_count
    check.expect(
        exercise_count >= MIN_EXERCISES,
        f"only {exercise_count} exercises (expected at least {MIN_EXERCISES})",
    )

    blank = connection.execute(
        "SELECT COUNT(*) FROM exercises WHERE category_name IS NULL OR TRIM(category_name) = ''"
    ).fetchone()[0]
    check.expect(blank == 0, f"{blank} exercises without category_name")

    for column in ("muscles_primary", "muscles_secondary"):
        broken = []
        for row in connection.execute(f"SELECT id, {column} FROM exercises"):
            try:
                value = json.loads(row[column]) if row[column] is not None else None
            except (TypeError, ValueError):
                value = None
            if not isinstance(value, list):
                broken.append(row["id"])
        check.expect(
            not broken,
            f"{len(broken)} exercises with broken JSON in {column} "
            f"(e.g. {', '.join(str(i) for i in broken[:5])})",
        )

    # --- Uniqueness
    for column in ("id", "slug"):
        if column not in exercise_columns:
            continue
        duplicates = connection.execute(
            f"SELECT {column} FROM exercises GROUP BY {column} HAVING COUNT(*) > 1"
        ).fetchall()
        check.expect(not duplicates, f"{len(duplicates)} duplicate values in exercises.{column}")

    # --- Translations
    if "exercise_translations" in tables:
        stats["translations"] = {
            str(row["language_code"]): int(row["n"])
            for row in connection.execute(
                "SELECT language_code, COUNT(*) AS n FROM exercise_translations "
                "GROUP BY language_code ORDER BY n DESC"
            )
        }
        check.expect(
            count(connection, "exercise_translations") > 0, "exercise_translations is empty"
        )
        empty_names = connection.execute(
            "SELECT COUNT(*) FROM exercise_translations WHERE name IS NULL OR TRIM(name) = ''"
        ).fetchone()[0]
        check.expect(empty_names == 0, f"{empty_names} translations without name")

        for language in ("de", "en"):
            missing = connection.execute(
                "SELECT COUNT(*) FROM exercises e LEFT JOIN exercise_translations t "
                "ON t.exercise_id = e.id AND t.language_code = ? WHERE t.id IS NULL",
                (language,),
            ).fetchone()[0]
            check.expect(
                missing == 0,
                f"{missing} exercises without {language} text — the app expects both",
            )

        if "license" in columns(connection, "exercise_translations"):
            without_license = connection.execute(
                "SELECT COUNT(*) FROM exercise_translations "
                "WHERE license IS NULL OR TRIM(license) = ''"
            ).fetchone()[0]
            check.expect(
                without_license == 0,
                f"{without_license} translations without license attribution (SCHEMA.md 3b)",
            )

    # --- Vocabularies must be bundled, otherwise references are dangling
    for table in ("muscles", "equipment", "languages"):
        if table in tables:
            check.expect(count(connection, table) > 0, f"{table} is empty")

    # --- Referential integrity. FOREIGN KEY is disabled by default in SQLite;
    # without this switch the file would be distributed with dangling references.
    connection.execute("PRAGMA foreign_keys = ON")
    violations = connection.execute("PRAGMA foreign_key_check").fetchall()
    check.expect(
        not violations,
        f"{len(violations)} foreign key violations (e.g. {[tuple(v) for v in violations[:3]]})",
    )

    integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
    check.expect(integrity == "ok", f"integrity_check: {integrity}")

    # --- Metadata
    if "metadata" in tables:
        metadata = {row["key"]: row["value"] for row in connection.execute("SELECT * FROM metadata")}
        stats["metadata"] = metadata
        for key in REQUIRED_METADATA_KEYS:
            check.expect(
                metadata.get(key), f"metadata.{key} missing or empty (SCHEMA.md 8)"
            )
        nullable = metadata.get("nullable_columns")
        if nullable and nullable != "[]":
            check.note(
                f"Classification columns not yet comprehensively populated: {nullable}. "
                f"Expected by end of Phase 2."
            )

    # --- Muscle assignments: not an error, but count belongs in log
    if "exercise_muscles" in tables:
        stats["muscle_links"] = count(connection, "exercise_muscles")
        without = connection.execute(
            "SELECT COUNT(*) FROM exercises e WHERE NOT EXISTS ("
            "SELECT 1 FROM exercise_muscles m WHERE m.exercise_id = e.id AND m.role = 'primary')"
        ).fetchone()[0]
        stats["without_primary_muscle"] = without
        if without:
            check.note(f"{without} exercises without primary muscle (Phase 2 backlog)")

    return stats


def inspect(connection: sqlite3.Connection) -> None:
    """The legacy dump — still useful for manual inspection."""
    connection.row_factory = sqlite3.Row
    for table in sorted(table_names(connection)):
        print(f"--- {table} ---")
        for name, kind in columns(connection, table).items():
            print(f"    {name} ({kind})")
        total = count(connection, table)
        print(f"  Rows: {total}")
        if total:
            for row in connection.execute(f"SELECT * FROM {table} LIMIT 3"):
                print(f"    {dict(row)}")
        print()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("database", nargs="+", help="SQLite database file(s) to check")
    parser.add_argument(
        "--inspect", action="store_true", help="Also print tables and sample rows"
    )
    parser.add_argument("--json-out", help="Path for machine-readable report")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    reports: dict[str, dict] = {}
    exit_code = 0

    for raw_path in args.database:
        path = Path(raw_path)
        print(f"== {path}")
        if not path.exists():
            print("   ERROR: File does not exist")
            exit_code = 1
            continue

        check = Check()
        connection = sqlite3.connect(path)
        try:
            stats = run_checks(connection, check)
            if args.inspect:
                print()
                inspect(connection)
        finally:
            connection.close()

        for note in check.notes:
            print(f"   Note: {note}")
        for failure in check.failures:
            print(f"   ERROR: {failure}")
        if check.failures:
            exit_code = 1
        else:
            print(
                f"   OK: {stats.get('exercise_count', 0)} exercises, "
                f"{sum(stats.get('translations', {}).values())} texts in "
                f"{len(stats.get('translations', {}))} languages"
            )
        reports[str(path)] = {
            "stats": stats,
            "failures": check.failures,
            "notes": check.notes,
        }

    if args.json_out:
        out = Path(args.json_out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(reports, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Report: {out}")

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
