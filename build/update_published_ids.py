#!/usr/bin/env python3
"""Maintains `data/published_ids.yaml` — the registry of all IDs ever distributed.

**Why this exists.** Invariant 21 originally compared against the *previous*
release. That has a ratchet effect: if a loss slips through once, the ID
disappears from the baseline and becomes invisible forever after. This exact
failure occurred — between the catalog version shipped in the app (852 IDs,
2026-06-15) and the 2026-08-31 release (862 IDs), 38 exercises disappeared,
including Chin-ups, Good Mornings, and Leg Extension. From that point on, every
subsequent diff reported "zero removals" because it no longer knew the 38.

The registry solves this: it only grows, resides in the repo, and verification
no longer requires a predecessor release asset. An ID once shipped to devices
is a contract with user data there (SCHEMA.md 3) — this contract belongs in
version control, not in an artifact that gets overwritten.

Usage:

    # Populate registry from existing databases (one-off)
    python3 build/update_published_ids.py --from-db old.db --from-db release.db

    # After a release: record newly distributed IDs
    python3 build/update_published_ids.py --from-db artifacts/openexercisedb.db \
        --release-version 202609022334

    # CI: verify that the registry is complete
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

HEADER = """data/published_ids.yaml — every ID ever distributed.

AUTOMATICALLY MAINTAINED by build/update_published_ids.py. Only grows, never
shrinks: an entry here means this ID may exist on user devices and be referenced
in `routine_exercises` and `set_logs` (SCHEMA.md 3).

Invariant 21 checks against this file rather than against the previous release —
otherwise a loss that slips through once would be invisible thereafter. Exactly
how 38 exercises were lost between 2026-06-15 and 2026-08-31.

Value per entry: earliest known release version in which the ID appeared.
"Known" means: from databases available during backfill — older releases
can no longer be retrieved."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--from-db",
        action="append",
        default=[],
        metavar="PATH",
        help="Distributed database whose IDs are recorded. Allowed multiple times.",
    )
    parser.add_argument(
        "--release-version",
        help="Version under which new IDs are recorded. Default: metadata.version of DB.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Dry run; exit code 1 if a registered ID is missing from data/exercises/.",
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
                f"{len(missing)} ever-distributed IDs missing in data/exercises/: "
                f"{', '.join(missing[:20])}"
                + (" ..." if len(missing) > 20 else ""),
                file=sys.stderr,
            )
            print(
                "Deletion is forbidden (SCHEMA.md 3). Entries must be restored as "
                "status: deprecated — run `python3 import/recover_removed_exercises.py`.",
                file=sys.stderr,
            )
            return 1
        print(f"Registry complete: {len(registry)} IDs, all present in data/exercises/.")
        return 0

    if not args.from_db:
        print("Nothing to do: specify --from-db or --check.", file=sys.stderr)
        return 2

    added: dict[str, list[str]] = {}
    for raw_path in args.from_db:
        path = Path(raw_path)
        if not path.exists():
            print(f"Database not found: {path}", file=sys.stderr)
            return 2
        ids, db_version = read_database(path)
        version = args.release_version or db_version
        new = sorted(ids - set(registry), key=str)
        for exercise_id in new:
            registry[exercise_id] = version
        added[str(path)] = new
        print(f"{path}: {len(ids)} IDs, of which {len(new)} are new in registry (version {version})")

    write_registry(registry)
    print(f"Registry: {len(registry)} IDs -> {PUBLISHED_IDS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
