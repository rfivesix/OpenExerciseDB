"""Reads the frozen wger snapshot.

The snapshot represents the raw source from which `data/` was created. It lives
in the repository so the import is reproducible and traceable if discrepancies
arise. It is fetched by `import/fetch_wger_snapshot.py` — the only pipeline step
that accesses the network.
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
        """The label from the filename, e.g. `2026-09-02`."""
        name = self.path.name
        return name.removeprefix("wger-").removesuffix(".json.gz")


def load(path: Path | None = None, *, verify: bool = True) -> Snapshot:
    """Loads the active snapshot (or the one at `path`).

    Without `path`, reads `snapshot/current.json` and verifies the recorded
    SHA-256. A silently modified snapshot would lead to untraceable build results.
    """
    expected: str | None = None
    if path is None:
        current_path = SNAPSHOT_DIR / CURRENT_FILE
        if not current_path.exists():
            raise FileNotFoundError(
                f"{current_path} is missing. Run `python3 import/fetch_wger_snapshot.py` first."
            )
        current = json.loads(current_path.read_text(encoding="utf-8"))
        path = SNAPSHOT_DIR / current["file"]
        expected = current.get("sha256")

    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Snapshot not found: {path}")

    digest = sha256_file(path)
    if verify and expected and digest != expected:
        raise ValueError(
            f"Snapshot checksum mismatch.\n  File:     {path}\n"
            f"  expected: {expected}\n  found:    {digest}"
        )

    with gzip.open(path, "rb") as handle:
        envelope = json.loads(handle.read().decode("utf-8"))

    version = envelope.get("snapshot_version")
    if version != SNAPSHOT_VERSION:
        raise ValueError(
            f"Snapshot format {version} is not supported (expected {SNAPSHOT_VERSION})."
        )

    return Snapshot(
        path=path,
        sha256=digest,
        fetched_at=envelope.get("fetched_at", ""),
        source=envelope.get("source", ""),
        endpoints=envelope.get("endpoints", {}),
        data=envelope.get("data", {}),
    )
