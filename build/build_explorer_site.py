#!/usr/bin/env python3
"""Build the static SQLite explorer used by GitHub Pages.

The browser loads ``catalog.db`` itself with sql.js. No API or server-side
database is involved, which keeps the published explorer identical to the
release database.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "artifacts" / "train_libre_training.db"
DEFAULT_OUTPUT = ROOT / "artifacts" / "explorer-site"
SOURCE = ROOT / "web"


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the static database explorer")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB, help="SQLite catalog to publish")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT, help="Output directory")
    args = parser.parse_args()

    database = args.db.resolve()
    output = args.out.resolve()
    if not database.is_file():
        raise SystemExit(f"Database not found: {database}. Run build/build_db.py first.")

    output.mkdir(parents=True, exist_ok=True)
    for name in ("index.html", "legal.html", "app.js", "style.css"):
        shutil.copy2(SOURCE / name, output / name)
    shutil.copy2(database, output / "catalog.db")
    (output / ".nojekyll").touch()
    try:
        shown_output = output.relative_to(ROOT)
    except ValueError:
        shown_output = output
    print(f"Wrote {shown_output} (using {database.name})")


if __name__ == "__main__":
    main()
