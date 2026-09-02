"""Lesen des eingefrorenen wger-Snapshots.

Der Snapshot ist der Rohstand, aus dem `data/` erzeugt wurde. Er liegt im Repo,
damit der Import reproduzierbar ist und bei einer Abweichung nachlesbar bleibt,
woher eine Zeile kam. Geschrieben wird er von `import/fetch_wger_snapshot.py` —
dem einzigen Schritt der Pipeline, der ins Netz geht.
"""
from __future__ import annotations

import gzip
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .paths import SNAPSHOT_DIR

SNAPSHOT_VERSION = 1
CURRENT_FILE = "current.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


@dataclass
class Snapshot:
    path: Path
    sha256: str
    fetched_at: str
    source: str
    endpoints: dict[str, Any]
    data: dict[str, list[dict[str, Any]]]

    @property
    def exercises(self) -> list[dict[str, Any]]:
        return self.data["exerciseinfo"]

    def index(self, endpoint: str, key: str = "id") -> dict[Any, dict[str, Any]]:
        return {row[key]: row for row in self.data[endpoint] if key in row}

    @property
    def label(self) -> str:
        """Der Bezeichner aus dem Dateinamen, z. B. `2026-09-02`."""
        name = self.path.name
        return name.removeprefix("wger-").removesuffix(".json.gz")


def load(path: Path | None = None, *, verify: bool = True) -> Snapshot:
    """Laedt den aktuellen Snapshot (oder den unter `path`).

    Ohne `path` wird `snapshot/current.json` gelesen und der dort genannte
    SHA-256 geprueft. Ein stillschweigend veraenderter Snapshot waere ein
    Build, dessen Ergebnis niemand mehr erklaeren kann.
    """
    expected: str | None = None
    if path is None:
        current_path = SNAPSHOT_DIR / CURRENT_FILE
        if not current_path.exists():
            raise FileNotFoundError(
                f"{current_path} fehlt. Zuerst `python3 import/fetch_wger_snapshot.py` laufen lassen."
            )
        current = json.loads(current_path.read_text(encoding="utf-8"))
        path = SNAPSHOT_DIR / current["file"]
        expected = current.get("sha256")

    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Snapshot nicht gefunden: {path}")

    digest = sha256_file(path)
    if verify and expected and digest != expected:
        raise ValueError(
            f"Snapshot-Pruefsumme weicht ab.\n  Datei:    {path}\n"
            f"  erwartet: {expected}\n  gefunden: {digest}"
        )

    with gzip.open(path, "rb") as handle:
        envelope = json.loads(handle.read().decode("utf-8"))

    version = envelope.get("snapshot_version")
    if version != SNAPSHOT_VERSION:
        raise ValueError(
            f"Snapshot-Format {version} wird nicht unterstuetzt (erwartet {SNAPSHOT_VERSION})."
        )

    return Snapshot(
        path=path,
        sha256=digest,
        fetched_at=envelope.get("fetched_at", ""),
        source=envelope.get("source", ""),
        endpoints=envelope.get("endpoints", {}),
        data=envelope.get("data", {}),
    )
