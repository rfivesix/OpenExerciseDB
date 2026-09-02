"""Gemeinsame Helfer der Tests: Skripte laden, DB bauen, Referenz beschaffen."""
from __future__ import annotations

import importlib.util
import json
import os
import sqlite3
import sys
import urllib.request
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

REFERENCE_MANIFEST_URL = (
    "https://github.com/rfivesix/train-libre/releases/download/"
    "wger-catalog-stable/wger_catalog_manifest.json"
)
"""Der `stable`-Kanal, aus dem sich die heutige App bedient. Die daraus geladene
Datenbank ist die Referenz fuer den Abnahmetest: sie ist das, was auf Geraeten
da draussen tatsaechlich liegt."""

CACHE_DIR = ROOT / "artifacts" / "reference"


def load_script(relative: str) -> ModuleType:
    """Laedt ein Skript aus `build/` oder `import/` als Modul.

    Ueber den Pfad und nicht ueber den Namen, weil `import` ein
    Python-Schluesselwort ist und `import/` damit kein Paket sein kann.
    """
    path = ROOT / relative
    name = path.stem
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader, f"Kann {path} nicht laden"
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class Options:
    """Minimaler Ersatz fuer argparse.Namespace."""

    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)


def build_database(db_path: Path, *, version: str = "209912312359") -> dict:
    """Baut `data/` in eine frische SQLite-Datei unter `db_path`."""
    build_db = load_script("build/build_db.py")
    code, report = build_db.build(
        Options(
            db_out=str(db_path),
            report_json_out=None,
            version=version,
            source_repo=build_db.DEFAULT_SOURCE_REPO,
        )
    )
    assert code == 0, f"build_db meldete Code {code}"
    return report


def reference_database() -> Path | None:
    """Pfad zur veroeffentlichten Referenz-DB, oder None.

    Reihenfolge: `REFERENCE_DB_PATH` aus der Umgebung (so setzt die CI sie),
    dann ein lokaler Cache, dann — nur wenn `OEDB_ALLOW_DOWNLOAD=1` gesetzt ist —
    ein Download aus dem Release-Kanal. Ohne all das gibt die Funktion None
    zurueck und der Abnahmetest ueberspringt sich, statt rot zu werden, weil
    gerade kein Netz da ist.
    """
    from_env = os.environ.get("REFERENCE_DB_PATH")
    if from_env:
        path = Path(from_env)
        return path if path.exists() else None

    cached = CACHE_DIR / "train_libre_training.db"
    if cached.exists():
        return cached

    if os.environ.get("OEDB_ALLOW_DOWNLOAD") != "1":
        return None

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    try:
        with urllib.request.urlopen(REFERENCE_MANIFEST_URL, timeout=60) as response:
            manifest = json.loads(response.read().decode("utf-8"))
        db_url = manifest["db_url"]
        with urllib.request.urlopen(db_url, timeout=180) as response:
            cached.write_bytes(response.read())
    except Exception:  # noqa: BLE001 — offline ist kein Testfehler
        return None
    return cached


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
