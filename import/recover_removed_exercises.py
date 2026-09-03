#!/usr/bin/env python3
"""Holt Uebungen zurueck, die upstream geloescht wurden, aber schon ausgeliefert waren.

**Das Problem.** wger hat zwischen dem 2026-06-15 und dem 2026-08-31 aufgeraeumt
und dabei 38 Uebungen entfernt — teils zu Recht (`bicep`, `cabel`, `DB UCV`),
teils nicht (Chin-ups, Good Mornings, Leg Extension, Barbell Hip Thrust). Der
Import ist der Quelle treu gefolgt und hat sie damit auch nicht mehr.

Fuer die Quelle ist das eine Loeschung. Fuer uns nicht: diese IDs sind auf
Geraeten in `routine_exercises` und `set_logs` referenziert (SCHEMA.md 3). Der
App-Importer arbeitet zwar upsert-only und behaelt sie auf bestehenden
Installationen — aber bei einer Neuinstallation, einem Re-Seed oder einem
Backup-Restore auf eine frisch geseedete Datenbank zeigen die Referenzen ins
Leere.

**Die Regel.** Was einmal ausgeliefert war, verschwindet nie: es wird
`status: deprecated`. Die Zeile bleibt in der Datenbank und aufloesbar, faellt
aber aus Suche und Katalog. Ob eine dieser Uebungen zusaetzlich einen Nachfolger
bekommt (`status: merged` + `merged_into`), entscheidet ein Mensch —
`build/propose_aliases.py` macht Vorschlaege, dieses Skript nicht. Ein
Fuzzy-Treffer, der stillschweigend Nutzer-Logs umschreibt, waere schlimmer als
das Problem.

**Woher der Inhalt kommt.** Aus einer bereits ausgelieferten Datenbank — die
Quelle hat die Eintraege ja nicht mehr. Zwei Dinge sind dabei zu beachten:

* Die alte Pipeline hatte die wger-Sprach-IDs falsch verdrahtet. In einer
  v1-Datenbank enthaelt `fr` in Wahrheit Spanisch, `ja` Griechisch und `it`
  Russisch. Beim Zurueckholen wird das mitkorrigiert (`LEGACY_LANGUAGE_FIX`),
  statt die Texte unter falscher Flagge weiterzureichen oder wegzuwerfen.
* Lizenz und Autor sind nicht wiederherstellbar — die alte Pipeline hat sie
  verworfen, und der Upstream-Eintrag ist weg. Eingetragen wird deshalb
  konservativ die restriktivste im Bestand vorkommende Lizenz, mit einem
  Vermerk in `provenance`. Das ueberschaetzt die Auflage fuer uns selbst und
  kann niemandem Attribution wegnehmen.

Aufruf:

    python3 import/recover_removed_exercises.py --from-db <ausgelieferte.db>
    python3 import/recover_removed_exercises.py --from-db <db> --dry-run
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sqlite3
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from oedb import dataset as dataset_mod  # noqa: E402
from oedb import yamlio  # noqa: E402
from oedb.paths import EXERCISES_DIR, I18N_DIR, PUBLISHED_IDS  # noqa: E402
from oedb.vocab import Vocabularies  # noqa: E402

# Die Sprachcodes einer v1-Datenbank sind zum Teil falsch — siehe
# vocab/languages.yaml. Hier wird das beim Zurueckholen geradegezogen.
LEGACY_LANGUAGE_FIX = {
    "de": "de",
    "en": "en",
    "fr": "es",  # wger-Sprach-ID 4 ist Spanisch, nicht Franzoesisch
    "ja": "el",  # 8 ist Griechisch; Japanisch gibt es bei wger nicht
    "it": "ru",  # 5 ist Russisch
}

FALLBACK_LICENSE = "CC-BY-SA-4.0"
LICENSE_NOTE = (
    "Lizenz nicht wiederherstellbar: der Upstream-Eintrag ist geloescht und die "
    "alte Pipeline hat license/license_author verworfen. Konservativ auf die "
    "restriktivste im Bestand vorkommende Lizenz gesetzt."
)

EXERCISE_HEADER = """data/exercises/<id>.yaml — zurueckgeholter Eintrag.

Diese Uebung wurde upstream geloescht, war aber bereits ausgeliefert und ist
damit in Nutzerdaten referenziert (SCHEMA.md 3). Sie bleibt als
`status: deprecated` bestehen: aufloesbar, aber aus Suche und Katalog heraus.

Wiederhergestellt von import/recover_removed_exercises.py aus einer
ausgelieferten Datenbank, nicht aus der Quelle — die hat den Eintrag nicht mehr."""

TRANSLATION_HEADER = """data/i18n/<lang>/<id>.yaml — zurueckgeholter Text.

Wiederhergestellt aus einer ausgelieferten Datenbank, weil der Upstream-Eintrag
geloescht wurde. Lizenz und Autor waren dort nicht enthalten; siehe die
Uebungsdatei fuer den Vermerk."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--from-db",
        required=True,
        action="append",
        metavar="PFAD",
        help="Ausgelieferte Datenbank, aus der die Inhalte geholt werden. Mehrfach erlaubt; "
        "die erste, die eine ID enthaelt, gewinnt.",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Nur berichten, nichts schreiben."
    )
    parser.add_argument("--report-json-out", help="Pfad fuer den maschinenlesbaren Bericht")
    return parser.parse_args()


def load_registry() -> set[str]:
    if not PUBLISHED_IDS.exists():
        raise SystemExit(
            f"{PUBLISHED_IDS} fehlt. Zuerst `python3 build/update_published_ids.py "
            f"--from-db <ausgelieferte.db>` laufen lassen."
        )
    return {str(key) for key in (yamlio.read(PUBLISHED_IDS) or {}).get("ids", {})}


def read_source(path: Path) -> dict[str, dict[str, Any]]:
    """Liest eine ausgelieferte Datenbank zu {id: {row, translations}}."""
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    try:
        rows = {
            str(row["id"]): {"row": dict(row), "translations": {}}
            for row in connection.execute("SELECT * FROM exercises")
        }
        for row in connection.execute("SELECT * FROM exercise_translations"):
            entry = rows.get(str(row["exercise_id"]))
            if entry is not None:
                entry["translations"][str(row["language_code"])] = dict(row)
    finally:
        connection.close()
    return rows


def muscles_from_legacy(row: dict[str, Any], vocab: Vocabularies) -> list[dict[str, str]]:
    """Legacy-Muskelnamen zurueck auf Vokabular-Knoten."""
    mapping = vocab.muscles.legacy_wger_mapping
    out: list[dict[str, str]] = []
    seen: set[str] = set()
    for role, column in (("primary", "muscles_primary"), ("secondary", "muscles_secondary")):
        try:
            names = json.loads(row.get(column) or "[]")
        except (TypeError, ValueError):
            names = []
        for name in names:
            node = mapping.get(str(name))
            if node is None or node in seen:
                continue
            seen.add(node)
            out.append({"id": node, "role": role})
    return out


def slugify(name: str) -> str:
    import re
    import unicodedata

    ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_name).strip("-").lower()
    return re.sub(r"-+", "-", slug)


def main() -> int:
    args = parse_args()
    vocab = Vocabularies()
    data = dataset_mod.load()
    registry = load_registry()

    missing = sorted(registry - set(data.exercises), key=str)
    if not missing:
        print("Nichts zurueckzuholen: jede je ausgelieferte ID ist in data/exercises/ vorhanden.")
        return 0

    sources: list[dict[str, dict[str, Any]]] = []
    for raw_path in args.from_db:
        path = Path(raw_path)
        if not path.exists():
            print(f"Datenbank nicht gefunden: {path}", file=sys.stderr)
            return 2
        sources.append(read_source(path))

    today = dt.date.today().isoformat()
    taken_slugs = {exercise.slug for exercise in data.exercises.values()}

    recovered: list[dict[str, Any]] = []
    unrecoverable: list[str] = []

    for exercise_id in missing:
        entry = next((source[exercise_id] for source in sources if exercise_id in source), None)
        if entry is None:
            unrecoverable.append(exercise_id)
            continue

        row = entry["row"]
        raw_translations = entry["translations"]

        # Sprachcodes geraderuecken, bevor irgendetwas geschrieben wird.
        texts: dict[str, dict[str, Any]] = {}
        for legacy_code, translation in raw_translations.items():
            code = LEGACY_LANGUAGE_FIX.get(legacy_code)
            if code is None or code not in vocab.languages:
                continue
            name = (translation.get("name") or "").strip()
            if name:
                texts[code] = {
                    "name": name,
                    "description": (translation.get("description") or "").strip(),
                }

        if not texts:
            unrecoverable.append(exercise_id)
            continue

        source_name = texts.get(vocab.source_language, next(iter(texts.values())))["name"]
        slug = slugify(source_name) or f"exercise-{exercise_id}"
        if slug in taken_slugs:
            slug = f"{slug}-{exercise_id}"
        taken_slugs.add(slug)

        muscles = muscles_from_legacy(row, vocab)

        document: dict[str, Any] = {
            "id": exercise_id,
            "slug": slug,
            "status": "deprecated",
        }
        if muscles:
            document["muscles"] = [yamlio.inline(m) for m in muscles]
        document["provenance"] = {
            "id": yamlio.inline({"source": "wger"}),
            "slug": yamlio.inline({"source": "derived", "at": today}),
            "status": yamlio.inline(
                {
                    "source": "derived",
                    "at": today,
                    "note": "Upstream geloescht, aber bereits ausgeliefert — SCHEMA.md 3.",
                }
            ),
        }
        if muscles:
            document["provenance"]["muscles"] = yamlio.inline({"source": "wger", "at": today})
        document["provenance"]["upstream"] = yamlio.inline(
            {"source": "derived", "at": today, "note": LICENSE_NOTE}
        )

        upstream: dict[str, Any] = {
            "source": "wger",
            "source_id": exercise_id,
            "license": FALLBACK_LICENSE,
            "license_author": None,
            "imported_at": today,
        }
        category = (row.get("category_name") or "").strip()
        if category:
            upstream["source_fields"] = {"category": category}
        document["upstream"] = upstream

        if not args.dry_run:
            yamlio.write(EXERCISES_DIR / f"{exercise_id}.yaml", document, header=EXERCISE_HEADER)

        for code in sorted(texts):
            text = texts[code]
            doc: dict[str, Any] = {
                "exercise_id": exercise_id,
                "language": code,
                "status": "upstream_unreviewed",
                "name": text["name"],
            }
            if text["description"]:
                doc["description"] = text["description"]
            doc["upstream"] = {"license": FALLBACK_LICENSE}
            if not args.dry_run:
                yamlio.write(
                    I18N_DIR / code / f"{exercise_id}.yaml", doc, header=TRANSLATION_HEADER
                )

        recovered.append(
            {
                "id": exercise_id,
                "slug": slug,
                "name": source_name,
                "category": category,
                "languages": sorted(texts),
                "muscles": len(muscles),
            }
        )

    verb = "waeren zurueckzuholen" if args.dry_run else "zurueckgeholt"
    print(f"{len(recovered)} von {len(missing)} Eintraegen {verb}:")
    for item in recovered:
        print(
            f"  {item['id']:>6}  {item['name'][:46]:<46} "
            f"{item['category'] or '-':<10} {len(item['languages'])} Sprachen, "
            f"{item['muscles']} Muskeln"
        )
    if unrecoverable:
        print(
            f"\n{len(unrecoverable)} ohne Inhalt in den angegebenen Datenbanken: "
            f"{', '.join(unrecoverable)}"
        )
        print("  Eine aeltere ausgelieferte Datenbank ueber --from-db ergaenzen.")

    if args.report_json_out:
        out = Path(args.report_json_out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            json.dumps(
                {"recovered": recovered, "unrecoverable": unrecoverable},
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        print(f"Bericht: {out}")

    if not args.dry_run and recovered:
        print(
            "\nNaechster Schritt: `python3 build/propose_aliases.py` schlaegt Nachfolger vor. "
            "Ein Merge schreibt Nutzer-Logs um und wird deshalb einzeln bestaetigt."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
