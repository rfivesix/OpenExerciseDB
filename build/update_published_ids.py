#!/usr/bin/env python3
"""Fuehrt `data/published_ids.yaml` — das Register aller je ausgelieferten IDs.

**Warum es das gibt.** Invariante 21 verglich urspruenglich gegen das *vorige*
Release. Das hat eine Ratsche: rutscht ein Verlust einmal durch, ist die ID aus
der Baseline verschwunden und danach fuer immer unsichtbar. Genau das ist
passiert — zwischen dem in der App ausgelieferten Stand (852 IDs, 2026-06-15)
und dem Release vom 2026-08-31 (862 IDs) sind 38 Uebungen verschwunden, darunter
Chin-ups, Good Mornings und Leg Extension. Ab dem Moment meldete jeder folgende
Diff korrekt "null Entfernungen", weil er die 38 nicht mehr kannte.

Das Register loest das: es waechst nur, liegt im Repo, und die Pruefung braucht
kein Vorgaenger-Release mehr. Eine ID, die einmal auf einem Geraet gelandet ist,
ist ein Vertrag mit den Nutzerdaten dort (SCHEMA.md 3) — dieser Vertrag gehoert
in die Versionsverwaltung und nicht in ein Artefakt, das ueberschrieben wird.

Aufruf:

    # Register aus vorhandenen Datenbanken auffuellen (einmalig)
    python3 build/update_published_ids.py --from-db alt.db --from-db release.db

    # nach einem Release: die gerade ausgelieferten IDs aufnehmen
    python3 build/update_published_ids.py --from-db artifacts/train_libre_training.db \\
        --release-version 202609022334

    # CI: nur pruefen, ob das Register vollstaendig ist
    python3 build/update_published_ids.py --check
"""
from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from oedb import yamlio  # noqa: E402
from oedb.paths import PUBLISHED_IDS  # noqa: E402

HEADER = """data/published_ids.yaml — jede ID, die je ausgeliefert wurde.

AUTOMATISCH GEPFLEGT von build/update_published_ids.py. Nur wachsen, nie
kuerzen: ein Eintrag hier heisst, dass diese ID auf Geraeten liegen kann und in
`routine_exercises` sowie `set_logs` referenziert sein kann (SCHEMA.md 3).

Invariante 21 prueft gegen diese Datei und nicht gegen das vorige Release —
sonst waere ein einmal durchgerutschter Verlust danach unsichtbar. Genau so
sind 38 Uebungen zwischen 2026-06-15 und 2026-08-31 verlorengegangen.

Wert je Eintrag: die frueheste bekannte Release-Version, in der die ID auftrat.
"Bekannt" heisst: aus den Datenbanken, die beim Auffuellen vorlagen — aeltere
Releases sind nicht mehr beschaffbar."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--from-db",
        action="append",
        default=[],
        metavar="PFAD",
        help="Ausgelieferte Datenbank, deren IDs aufgenommen werden. Mehrfach erlaubt.",
    )
    parser.add_argument(
        "--release-version",
        help="Version, unter der neue IDs vermerkt werden. Default: metadata.version der DB.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Nichts schreiben; Exitcode 1, wenn eine registrierte ID in data/exercises/ fehlt.",
    )
    return parser.parse_args()


def load_registry() -> dict[str, str]:
    if not PUBLISHED_IDS.exists():
        return {}
    data = yamlio.read(PUBLISHED_IDS) or {}
    return {str(key): str(value) for key, value in (data.get("ids") or {}).items()}


def write_registry(ids: dict[str, str]) -> None:
    def sort_key(item: tuple[str, str]) -> tuple[int, str]:
        raw = item[0]
        return (0, f"{int(raw):020d}") if raw.isdigit() else (1, raw)

    yamlio.write(
        PUBLISHED_IDS,
        {"version": 1, "count": len(ids), "ids": dict(sorted(ids.items(), key=sort_key))},
        header=HEADER,
    )


def read_database(path: Path) -> tuple[set[str], str]:
    connection = sqlite3.connect(path)
    try:
        ids = {str(row[0]) for row in connection.execute("SELECT id FROM exercises")}
        version_row = connection.execute(
            "SELECT value FROM metadata WHERE key = 'version'"
        ).fetchone()
    finally:
        connection.close()
    return ids, str(version_row[0]) if version_row else "unknown"


def main() -> int:
    args = parse_args()
    registry = load_registry()

    if args.check:
        from oedb import dataset as dataset_mod

        data = dataset_mod.load()
        missing = sorted(set(registry) - set(data.exercises), key=str)
        if missing:
            print(
                f"{len(missing)} je ausgelieferte IDs fehlen in data/exercises/: "
                f"{', '.join(missing[:20])}"
                + (" ..." if len(missing) > 20 else ""),
                file=sys.stderr,
            )
            print(
                "Loeschen ist verboten (SCHEMA.md 3). Die Eintraege gehoeren als "
                "status: deprecated zurueck — `python3 import/recover_removed_exercises.py`.",
                file=sys.stderr,
            )
            return 1
        print(f"Register vollstaendig: {len(registry)} IDs, alle in data/exercises/ vorhanden.")
        return 0

    if not args.from_db:
        print("Nichts zu tun: --from-db oder --check angeben.", file=sys.stderr)
        return 2

    added: dict[str, list[str]] = {}
    for raw_path in args.from_db:
        path = Path(raw_path)
        if not path.exists():
            print(f"Datenbank nicht gefunden: {path}", file=sys.stderr)
            return 2
        ids, db_version = read_database(path)
        version = args.release_version or db_version
        new = sorted(ids - set(registry), key=str)
        for exercise_id in new:
            registry[exercise_id] = version
        added[str(path)] = new
        print(f"{path}: {len(ids)} IDs, davon {len(new)} neu im Register (Version {version})")

    write_registry(registry)
    print(f"Register: {len(registry)} IDs -> {PUBLISHED_IDS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
