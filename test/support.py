"""Common test helpers: load scripts, build DB, retrieve reference DB."""
from __future__ import annotations

import importlib.util
import os
import sqlite3
import sys
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

CACHE_DIR = ROOT / "artifacts" / "reference"


def load_script(relative: str) -> ModuleType:
    """Loads a script from `build/` or `import/` as a module.

    Loaded via file path rather than module name because `import` is a
    Python keyword, preventing `import/` from being a regular package.
    """
    path = ROOT / relative
    name = path.stem
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader, f"Cannot load {path}"
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class Options:
    """Minimal replacement for argparse.Namespace."""

    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)


def build_database(db_path: Path, *, version: str = "209912312359") -> dict:
    """Builds `data/` into a fresh SQLite database at `db_path`."""
    build_db = load_script("build/build_db.py")
    code, report = build_db.build(
        Options(
            db_out=str(db_path),
            report_json_out=None,
            version=version,
            source_repo=build_db.DEFAULT_SOURCE_REPO,
        )
    )
    assert code == 0, f"build_db exited with code {code}"
    return report


def reference_database() -> Path | None:
    """Path to the published reference DB, or None.

    Resolution order: `REFERENCE_DB_PATH` from environment (as set by CI),
    then local cache. Without either, returns None and tests requiring the
    reference will skip themselves.
    """
    from_env = os.environ.get("REFERENCE_DB_PATH")
    if from_env:
        path = Path(from_env)
        return path if path.exists() else None

    cached = CACHE_DIR / "openexercisedb.db"
    if cached.exists():
        return cached

    return None


def rows(connection: sqlite3.Connection, query: str, *params) -> list[sqlite3.Row]:
    connection.row_factory = sqlite3.Row
    return list(connection.execute(query, params))


def table_columns(connection: sqlite3.Connection, table: str) -> dict[str, str]:
    return {row[1]: row[2] for row in connection.execute(f"PRAGMA table_info({table})")}


def table_names(connection: sqlite3.Connection) -> set[str]:
    return {
        row[0]
        for row in connection.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
        )
    }
