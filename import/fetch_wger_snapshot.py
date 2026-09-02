#!/usr/bin/env python3
"""Holt einen Snapshot der wger-API und legt ihn im Repo ab.

Das ist der **einzige** Schritt der Pipeline, der ins Netz geht. Der Build zieht
nicht mehr live von wger — er liest ausschliesslich `data/`, und `data/` wird
aus diesem Snapshot erzeugt. Zwei Gruende:

1. **Reproduzierbarkeit.** Ein Build, dessen Ergebnis vom Tagesstand einer
   fremden API abhaengt, ist nicht testbar. Der Abnahmetest aus Phase 1 haengt
   genau daran.
2. **Nachvollziehbarkeit.** Bei einer Abweichung ist der Rohstand, aus dem eine
   Zeile entstanden ist, im Repo nachlesbar statt weg.

Aufruf:

    python3 import/fetch_wger_snapshot.py                 # neuer Snapshot von heute
    python3 import/fetch_wger_snapshot.py --label 2026-09-02
"""
from __future__ import annotations

import argparse
import datetime as dt
import gzip
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from oedb.paths import SNAPSHOT_DIR  # noqa: E402
from oedb.snapshot import CURRENT_FILE, SNAPSHOT_VERSION, sha256_file  # noqa: E402

API_BASE = "https://wger.de/api/v2"

# Reihenfolge ist Absicht: die kleinen Vokabular-Endpunkte zuerst, damit ein
# Ausfall auffliegt, bevor 5 MB Uebungsdaten uebertragen wurden.
ENDPOINTS: dict[str, str] = {
    "license": f"{API_BASE}/license/?limit=100",
    "language": f"{API_BASE}/language/?limit=100",
    "exercisecategory": f"{API_BASE}/exercisecategory/?limit=100",
    "muscle": f"{API_BASE}/muscle/?limit=100",
    "equipment": f"{API_BASE}/equipment/?limit=100",
    "exerciseinfo": f"{API_BASE}/exerciseinfo/?limit=100",
}

USER_AGENT = "openexercisedb-import/1.0 (+https://github.com/rfivesix/openexercisedb)"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--out-dir",
        default=str(SNAPSHOT_DIR),
        help=f"Zielverzeichnis (Default: {SNAPSHOT_DIR})",
    )
    parser.add_argument(
        "--label",
        default=dt.date.today().isoformat(),
        help="Bezeichner im Dateinamen (Default: heutiges Datum)",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=60.0,
        help="Timeout je HTTP-Anfrage in Sekunden (Default: 60)",
    )
    return parser.parse_args()


def fetch_all(session: Any, url: str, timeout: float) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Folgt der `next`-Verkettung, bis alle Seiten geholt sind."""
    results: list[dict[str, Any]] = []
    meta: dict[str, Any] = {"url": url, "pages": 0}
    next_url: str | None = url
    while next_url:
        response = session.get(next_url, timeout=timeout)
        response.raise_for_status()
        payload = response.json()
        if not isinstance(payload, dict) or not isinstance(payload.get("results"), list):
            raise ValueError(f"Unerwartete Antwortstruktur von {next_url}")
        results.extend(payload["results"])
        meta["pages"] += 1
        meta.setdefault("status_code", response.status_code)
        meta.setdefault("source_date_header", response.headers.get("Date", ""))
        meta["count"] = payload.get("count")
        next_url = payload.get("next")
    meta["fetched"] = len(results)
    return results, meta


def main() -> int:
    try:
        import requests
    except ImportError:
        print("requests fehlt. `pip install -r requirements.txt`", file=sys.stderr)
        return 2

    args = parse_args()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers["User-Agent"] = USER_AGENT

    data: dict[str, list[dict[str, Any]]] = {}
    endpoints: dict[str, dict[str, Any]] = {}
    for name, url in ENDPOINTS.items():
        print(f"  {name} ...", end="", flush=True)
        try:
            results, meta = fetch_all(session, url, args.timeout)
        except Exception as exc:  # noqa: BLE001 — jeder Fehler ist hier fatal
            print(f" FEHLER: {exc}", file=sys.stderr)
            return 2
        data[name] = results
        endpoints[name] = meta
        print(f" {len(results)}")

        if meta.get("count") is not None and meta["count"] != len(results):
            print(
                f"    Abbruch: {name} meldet count={meta['count']}, geholt {len(results)}",
                file=sys.stderr,
            )
            return 2

    envelope = {
        "snapshot_version": SNAPSHOT_VERSION,
        "source": API_BASE,
        "fetched_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "endpoints": endpoints,
        "data": data,
    }

    out_path = out_dir / f"wger-{args.label}.json.gz"
    payload = json.dumps(envelope, ensure_ascii=False, sort_keys=True, indent=1).encode("utf-8")
    # mtime=0: sonst aendert sich der Hash der Datei bei identischem Inhalt.
    with gzip.GzipFile(filename="", mode="wb", fileobj=out_path.open("wb"), mtime=0) as handle:
        handle.write(payload)

    digest = sha256_file(out_path)
    current = {
        "file": out_path.name,
        "sha256": digest,
        "fetched_at": envelope["fetched_at"],
        "counts": {name: len(rows) for name, rows in data.items()},
    }
    (out_dir / CURRENT_FILE).write_text(
        json.dumps(current, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    size_mb = out_path.stat().st_size / (1024 * 1024)
    print(f"\nSnapshot geschrieben: {out_path} ({size_mb:.2f} MB)")
    print(f"  sha256 {digest}")
    for name, count in current["counts"].items():
        print(f"  {name:18} {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
