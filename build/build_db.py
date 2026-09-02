#!/usr/bin/env python3
"""Baut aus `data/` die auszuliefernde SQLite-Datei (SCHEMA.md 8).

Zweite Haelfte des zerlegten `create_wger_exercise_db.py`. Der Unterschied zum
Altskript ist nicht die Ausgabe, sondern die Eingabe: hier wird nichts mehr
heruntergeladen. Der Build liest ausschliesslich die Textdateien im Repo und ist
damit offline, reproduzierbar und ueberhaupt erst testbar.

**Die vier Kompatibilitaetsspalten.** `id`, `category_name`, `muscles_primary`
und `muscles_secondary` — plus `exercise_translations` — sind exakt das, was
`_mapExerciseBundle` in der heutigen App liest. Solange sie befuellt sind, laeuft
die App unveraendert auf dieser Datenbank; das ist die Abnahmeschwelle fuer
Phase 1 und wird von `test/test_compat.py` gegen die veroeffentlichte
Referenz-DB geprueft.

Die Legacy-Muskelnamen werden dabei nicht durchgereicht, sondern aus dem neuen
Vokabular **zurueckgerechnet** (`MuscleVocabulary.legacy_wger_name`). Das kostet
in Phase 1 nichts und zahlt sich in Phase 2 aus: wird `trapezius` spaeter zu
`traps_upper` praezisiert, steht in der Kompatibilitaetsspalte weiterhin
`Trapezius`, ohne dass jemand daran denken muss.

Aufruf:

    python3 build/build_db.py --db-out artifacts/train_libre_training.db \\
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
"""Fallback des Altskripts fuer Uebungen ohne Kategorie. Beibehalten, weil die
heutige App darauf trifft."""

STRICT_WHEN_COMPLETE = (
    "modality",
    "mechanic",
    "force_vector",
    "movement_pattern",
    "laterality",
    "tracking_type",
    "primary_equipment",
)
"""In SCHEMA.md 8 als NOT NULL gefuehrt, in Phase 1 aber noch nicht befuellt.

Der Build setzt die Bedingung genau dann, wenn die Daten sie tragen — und
schreibt in `metadata.nullable_columns`, welche noch offen sind. Damit zieht
sich das Schema mit dem Fortschritt von Phase 2 von selbst fest, statt auf einen
Menschen zu warten, der daran denkt. Ein Platzhalterwert waere die Alternative
gewesen; der waere von einem echten Wert nicht zu unterscheiden."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--db-out",
        default="artifacts/train_libre_training.db",
        help="Zielpfad der SQLite-Datei (Default: artifacts/train_libre_training.db)",
    )
    parser.add_argument("--report-json-out", help="Pfad fuer den maschinenlesbaren Buildbericht")
    parser.add_argument(
        "--version",
        help="Inhaltsversion (Default: UTC-Zeitstempel YYYYMMDDHHMM, Format wie bisher)",
    )
    parser.add_argument(
        "--source-repo",
        default=os.environ.get("SOURCE_REPO", DEFAULT_SOURCE_REPO),
        help="Repo-URL fuer metadata.source_repo und die Attribution",
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
          force_vector          TEXT{null('force_vector')},
          movement_pattern      TEXT{null('movement_pattern')},
          laterality            TEXT{null('laterality')},
          difficulty            TEXT,
          tracking_type         TEXT{null('tracking_type')},
          supports_added_weight INTEGER NOT NULL DEFAULT 0,
          supports_assistance   INTEGER NOT NULL DEFAULT 0,
          primary_equipment     TEXT{null('primary_equipment')},
          body_region           TEXT,

          -- Kompatibilitaetsspalten fuer Schema-v1-Konsumenten (heutige App).
          category_name         TEXT,
          muscles_primary       TEXT,
          muscles_secondary     TEXT,
          image_path            TEXT,
          is_custom             INTEGER NOT NULL DEFAULT 0,
          created_by            TEXT DEFAULT 'system',
          source                TEXT DEFAULT 'base',

          -- Lizenz-Provenienz, SCHEMA.md 3b.
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
        # "Welche Uebungen treffen diesen Muskel?" ist die Kernabfrage von
        # Recovery und Volumenstatistik.
        "CREATE INDEX idx_ex_muscles_muscle ON exercise_muscles(muscle_id)",
    ]


# ------------------------------------------------------------------- helpers


def json_array(values: list[Any] | None) -> str | None:
    return json.dumps(values, ensure_ascii=False) if values else None


def legacy_muscle_json(vocab: Vocabularies, node_ids: list[str]) -> str:
    """JSON-Array der wger-Legacy-Namen, wie die heutige App sie erwartet.

    Sortiert und dupliktfrei — zeichengleich zu `json.dumps(sorted({...}))` im
    Altskript, sonst schlaegt der Zeichenvergleich in test/test_compat.py an.
    Knoten, fuer die es keinen Legacy-Namen gibt (Rueckenstrecker etwa), fallen
    heraus: die heutige App wuerde sie ohnehin still verwerfen.
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
    """Text in `language`, sonst der erste Treffer aus der Fallback-Kette.

    Rueckgabe: (Text, Quellsprache-falls-Fallback). Das zweite Element landet in
    `exercise_translations.source_lang` — die heutige App liefert diese
    Information nicht mit und niemand kann hinterher sagen, welche der 862
    deutschen Zeilen tatsaechlich deutsch sind.
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
        print("Keine Uebungen unter data/exercises/ gefunden.", file=sys.stderr)
        return 2, {}

    exercises = data.sorted_exercises()
    version = args.version or dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d%H%M")
    generated_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()

    # Welche der in SCHEMA.md 8 als NOT NULL gefuehrten Spalten traegt der
    # Datenbestand heute schon?
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
    # journal_mode=DELETE: die Datei wird als einzelnes Asset ausgeliefert, ein
    # zurueckbleibendes -wal waere fuer den Konsumenten unsichtbarer Datenverlust.
    connection.execute("PRAGMA journal_mode=DELETE")
    cursor = connection.cursor()
    for statement in build_ddl(nullable):
        cursor.execute(statement)

    # ---------------------------------------------------------- Vokabulare
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

    # ------------------------------------------------------------- Uebungen
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
                exercise.get("force_vector"),
                exercise.get("movement_pattern"),
                exercise.get("laterality"),
                exercise.get("difficulty"),
                exercise.get("tracking_type"),
                1 if exercise.get("supports_added_weight") else 0,
                1 if exercise.get("supports_assistance") else 0,
                exercise.get("primary_equipment"),
                exercise.get("body_region"),
                # --- Kompatibilitaetsspalten
                exercise.source_fields.get("category") or CATEGORY_OTHER,
                legacy_muscle_json(vocab, primary),
                legacy_muscle_json(vocab, secondary),
                # Das Altskript schreibt hier "" und nicht NULL. Die heutige App
                # bekommt damit einen leeren String; auf NULL umzustellen waere
                # eine Verhaltensaenderung ohne Gegenwert, solange es keine
                # Medien gibt.
                "",
                0,
                "system",
                "base",
                # --- Lizenz-Provenienz
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
            alias_rows.append((exercise.id, str(exercise["merged_into"]), "merged", version))

    cursor.executemany(
        f"INSERT INTO exercises VALUES ({', '.join('?' * len(exercise_rows[0]))})", exercise_rows
    )
    cursor.executemany("INSERT INTO exercise_muscles VALUES (?, ?, ?, ?)", muscle_link_rows)
    cursor.executemany("INSERT INTO exercise_equipment VALUES (?, ?, ?)", equipment_link_rows)
    cursor.executemany("INSERT INTO exercise_tags VALUES (?, ?)", tag_rows)
    cursor.executemany("INSERT INTO exercise_aliases VALUES (?, ?, ?, ?)", alias_rows)

    # --------------------------------------------------------- Uebersetzungen
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
                    # Ohne die Garantie wuerden hier 20 Sprachen je 871 Zeilen
                    # englischen Text unter fremder Flagge erzeugen.
                    continue
                fallback_counts[code] += 1
            else:
                native_counts[code] += 1

            upstream = text.upstream
            translation_rows.append(
                (
                    f"{exercise.id}_{code}",
                    exercise.id,
                    code,
                    text.name,
                    # Das Altskript schreibt "" statt NULL, wenn kein
                    # Beschreibungstext existiert. Beibehalten.
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

    # --------------------------------------------------------------- Sprachen
    active_count = sum(1 for exercise in exercises if exercise.status == "active")
    language_rows = []
    completeness_report: dict[str, dict[str, Any]] = {}
    for code, language in vocab.languages.items():
        native = native_counts.get(code, 0)
        delivered = native + fallback_counts.get(code, 0)
        completeness = native / active_count if active_count else 0.0
        delivered_share = delivered / active_count if active_count else 0.0
        # `completeness` ist die ehrliche Zahl: wie viel ist wirklich uebersetzt.
        # `displayable` beantwortet die andere Frage: kann die Oberflaeche diese
        # Sprache ohne Loecher anbieten? Fuer eine Sprache mit
        # complete_in_release ist das dank Fallback auch dann der Fall, wenn
        # `completeness` niedrig ist — und die App sieht an `source_lang`
        # zeilenweise, was tatsaechlich uebersetzt wurde.
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

    # -------------------------------------------------------------- metadata
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
        # Welche der in SCHEMA.md 8 als NOT NULL gefuehrten Spalten noch nicht
        # durchgaengig befuellt sind. Leer heisst: v2 ist inhaltlich erreicht.
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
    print(f"Datenbank  {report['build']['db_output_path']} (Version {report['build']['db_version']})")
    print(f"Uebungen   {summary['imported_count']} ({summary['active_count']} aktiv)")
    print(f"Texte      {summary['translation_count']} Zeilen")
    print(f"Muskeln    {summary['muscle_link_count']} Zuweisungen")
    if report["nullable_columns"]:
        print(
            "Offen      noch ohne NOT NULL: " + ", ".join(report["nullable_columns"])
        )
    if report["unknown_muscle_nodes"]:
        print(f"WARNUNG    unbekannte Muskelknoten: {report['unknown_muscle_nodes']}")

    if args.report_json_out:
        out = Path(args.report_json_out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Bericht    {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
