#!/usr/bin/env python3
"""Sanity-Check auf der erzeugten Datenbank, direkt vor dem Release.

Uebernommen aus `train-libre` und um die Tabellen aus SCHEMA.md 8 erweitert.
Der wesentliche Unterschied: das Vorbild war ein reiner Dump — es druckte
Tabellen, Spalten und drei Beispielzeilen und lief immer mit Exitcode 0 durch.
Das ist als Blick von aussen nuetzlich (`--inspect` gibt es weiterhin), taugt
aber nicht als Gate: eine leere Uebersetzungstabelle haette man nur gesehen,
wenn jemand hinschaut.

Hier ist jede Aussage eine Pruefung mit Exitcode. Was geprueft wird, ist
bewusst das, was zwischen Build und Geraet schiefgehen kann — nicht das, was
schon `build/validate.py` auf den Quelldateien abgedeckt hat.

Aufruf:

    python3 build/check_database.py artifacts/train_libre_training.db
    python3 build/check_database.py --inspect artifacts/train_libre_training.db
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
"""Was `_mapExerciseBundle` in der heutigen App liest. Fehlt eine davon, laedt
die App die Datenbank nicht — das ist der teuerste denkbare Fehler, weil er erst
auf dem Geraet auffaellt."""

MIN_EXERCISES = 500
"""Untergrenze aus dem Manifest-Vertrag (`min_exercise_count`). Ein Build, der
deutlich darunter liegt, ist kaputt und kein neuer Datenstand."""


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
        check.expect(table in tables, f"Tabelle {table} fehlt")

    if "exercises" not in tables:
        return stats

    # --- Der App-Vertrag
    exercise_columns = columns(connection, "exercises")
    for column in APP_COMPAT_COLUMNS:
        check.expect(
            column in exercise_columns,
            f"Kompatibilitaetsspalte exercises.{column} fehlt — die heutige App "
            f"koennte diese Datenbank nicht laden",
        )

    exercise_count = count(connection, "exercises")
    stats["exercise_count"] = exercise_count
    check.expect(
        exercise_count >= MIN_EXERCISES,
        f"nur {exercise_count} Uebungen (erwartet mindestens {MIN_EXERCISES})",
    )

    blank = connection.execute(
        "SELECT COUNT(*) FROM exercises WHERE category_name IS NULL OR TRIM(category_name) = ''"
    ).fetchone()[0]
    check.expect(blank == 0, f"{blank} Uebungen ohne category_name")

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
            f"{len(broken)} Uebungen mit kaputtem JSON in {column} "
            f"(z. B. {', '.join(str(i) for i in broken[:5])})",
        )

    # --- Eindeutigkeit
    for column in ("id", "slug"):
        if column not in exercise_columns:
            continue
        duplicates = connection.execute(
            f"SELECT {column} FROM exercises GROUP BY {column} HAVING COUNT(*) > 1"
        ).fetchall()
        check.expect(not duplicates, f"{len(duplicates)} doppelte Werte in exercises.{column}")

    # --- Uebersetzungen
    if "exercise_translations" in tables:
        stats["translations"] = {
            str(row["language_code"]): int(row["n"])
            for row in connection.execute(
                "SELECT language_code, COUNT(*) AS n FROM exercise_translations "
                "GROUP BY language_code ORDER BY n DESC"
            )
        }
        check.expect(
            count(connection, "exercise_translations") > 0, "exercise_translations ist leer"
        )
        empty_names = connection.execute(
            "SELECT COUNT(*) FROM exercise_translations WHERE name IS NULL OR TRIM(name) = ''"
        ).fetchone()[0]
        check.expect(empty_names == 0, f"{empty_names} Uebersetzungen ohne Namen")

        for language in ("de", "en"):
            missing = connection.execute(
                "SELECT COUNT(*) FROM exercises e LEFT JOIN exercise_translations t "
                "ON t.exercise_id = e.id AND t.language_code = ? WHERE t.id IS NULL",
                (language,),
            ).fetchone()[0]
            check.expect(
                missing == 0,
                f"{missing} Uebungen ohne {language}-Text — die heutige App erwartet beide",
            )

        if "license" in columns(connection, "exercise_translations"):
            without_license = connection.execute(
                "SELECT COUNT(*) FROM exercise_translations "
                "WHERE license IS NULL OR TRIM(license) = ''"
            ).fetchone()[0]
            check.expect(
                without_license == 0,
                f"{without_license} Uebersetzungen ohne Lizenzangabe (SCHEMA.md 3b)",
            )

    # --- Vokabulare muessen mitgeliefert sein, sonst sind die Verweise tot
    for table in ("muscles", "equipment", "languages"):
        if table in tables:
            check.expect(count(connection, table) > 0, f"{table} ist leer")

    # --- Verweisintegritaet. FOREIGN KEY ist in SQLite per Default aus; ohne
    # diesen Schalter wuerde die Datei mit toten Verweisen ausgeliefert.
    connection.execute("PRAGMA foreign_keys = ON")
    violations = connection.execute("PRAGMA foreign_key_check").fetchall()
    check.expect(
        not violations,
        f"{len(violations)} verletzte Fremdschluessel (z. B. {[tuple(v) for v in violations[:3]]})",
    )

    integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
    check.expect(integrity == "ok", f"integrity_check: {integrity}")

    # --- Metadaten
    if "metadata" in tables:
        metadata = {row["key"]: row["value"] for row in connection.execute("SELECT * FROM metadata")}
        stats["metadata"] = metadata
        for key in REQUIRED_METADATA_KEYS:
            check.expect(
                metadata.get(key), f"metadata.{key} fehlt oder ist leer (SCHEMA.md 8)"
            )
        nullable = metadata.get("nullable_columns")
        if nullable and nullable != "[]":
            check.note(
                f"Klassifikationsspalten noch nicht durchgaengig befuellt: {nullable}. "
                f"Erwartet bis zum Ende von Phase 2."
            )

    # --- Muskelzuweisungen: kein Fehler, aber die Zahl gehoert ins Log
    if "exercise_muscles" in tables:
        stats["muscle_links"] = count(connection, "exercise_muscles")
        without = connection.execute(
            "SELECT COUNT(*) FROM exercises e WHERE NOT EXISTS ("
            "SELECT 1 FROM exercise_muscles m WHERE m.exercise_id = e.id AND m.role = 'primary')"
        ).fetchone()[0]
        stats["without_primary_muscle"] = without
        if without:
            check.note(f"{without} Uebungen ohne primaeren Muskel (Arbeitsvorrat Phase 2)")

    return stats


def inspect(connection: sqlite3.Connection) -> None:
    """Der Dump des Vorbilds — als Blick von aussen weiterhin nuetzlich."""
    connection.row_factory = sqlite3.Row
    for table in sorted(table_names(connection)):
        print(f"--- {table} ---")
        for name, kind in columns(connection, table).items():
            print(f"    {name} ({kind})")
        total = count(connection, table)
        print(f"  Zeilen: {total}")
        if total:
            for row in connection.execute(f"SELECT * FROM {table} LIMIT 3"):
                print(f"    {dict(row)}")
        print()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("database", nargs="+", help="Zu pruefende SQLite-Datei(en)")
    parser.add_argument(
        "--inspect", action="store_true", help="Zusaetzlich Tabellen und Beispielzeilen ausgeben"
    )
    parser.add_argument("--json-out", help="Pfad fuer den maschinenlesbaren Bericht")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    reports: dict[str, dict] = {}
    exit_code = 0

    for raw_path in args.database:
        path = Path(raw_path)
        print(f"== {path}")
        if not path.exists():
            print("   FEHLER: Datei existiert nicht")
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
            print(f"   Hinweis: {note}")
        for failure in check.failures:
            print(f"   FEHLER: {failure}")
        if check.failures:
            exit_code = 1
        else:
            print(
                f"   OK: {stats.get('exercise_count', 0)} Uebungen, "
                f"{sum(stats.get('translations', {}).values())} Texte in "
                f"{len(stats.get('translations', {}))} Sprachen"
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
        print(f"Bericht: {out}")

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
