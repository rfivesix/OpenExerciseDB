#!/usr/bin/env python3
"""Einmal-Import: wger-Snapshot -> `data/exercises/` + `data/i18n/`.

Erste Haelfte des zerlegten `create_wger_exercise_db.py`. Die zweite ist
`build/build_db.py`. Der entscheidende Unterschied zum Altskript: hier endet der
Weg in Textdateien, nicht in einer `.db`. Ab dann ist die Datenpflege ein PR und
kein API-Abruf mehr.

Was dieses Skript **nicht** tut: irgendein Feld erfinden. `modality`,
`mechanic`, `force_vector`, `movement_pattern`, `laterality`, `usage_tags`,
`tracking_type`, `primary_equipment`, `setup` und `difficulty` liefert wger
nicht, also stehen sie nirgends. Ein Platzhalter waere von einem echten Wert
nicht zu unterscheiden — genau der Fehler, vor dem SCHEMA.md 11 warnt. Sie sind
Phase 2. Die Rohwerte, aus denen sie spaeter abgeleitet werden koennen
(Kategorie und Equipment), landen unter `upstream.source_fields`.

Drei Dinge, die das Altskript verlor und die hier ankommen:

* **Lizenz und Autor je Uebersetzung** (SCHEMA.md 3b). wger lizenziert pro
  Eintrag; die heute ausgelieferte DB enthaelt keinerlei Attribution.
* **Die richtigen Sprachen.** Das Altskript hatte die wger-Sprach-IDs fest
  verdrahtet und falsch: 4 galt als `fr`, 5 als `it`, 8 als `ja` — tatsaechlich
  sind das `es`, `ru` und `el`. Japanisch gibt es bei wger gar nicht. Die
  Zuordnung kommt jetzt aus `vocab/languages.yaml` und wird gegen den Snapshot
  geprueft.
* **Alle Sprachen**, nicht nur fuenf.

Aufruf:

    python3 import/wger_to_yaml.py                       # aktueller Snapshot
    python3 import/wger_to_yaml.py --report-json-out artifacts/import_report.json
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from oedb import snapshot as snapshot_mod  # noqa: E402
from oedb import yamlio  # noqa: E402
from oedb.paths import EXERCISES_DIR, I18N_DIR  # noqa: E402
from oedb.vocab import Vocabularies  # noqa: E402

EXERCISE_HEADER = """data/exercises/<id>.yaml — sprachneutrale Fakten.
Enthaelt KEINEN uebersetzbaren Text; der liegt unter data/i18n/<lang>/<id>.yaml.

Automatisch erzeugt von import/wger_to_yaml.py aus dem wger-Snapshot.
Ab hier ist die Datei von Hand pflegbar — der Importer laeuft nicht erneut.
Die Klassifikationsfelder (modality, tracking_type, primary_equipment, ...)
fehlen absichtlich: wger liefert sie nicht, und geraten waere schlimmer als
leer. Siehe SCHEMA.md 6 und 11."""

TRANSLATION_HEADER = """data/i18n/<lang>/<id>.yaml — Text zu genau einer Uebung.

Automatisch erzeugt von import/wger_to_yaml.py aus dem wger-Snapshot.
Lizenz und Autor gelten fuer genau diesen Text, nicht fuer das Repo — wger
lizenziert pro Eintrag (SCHEMA.md 3b)."""

REJECTION_REASON_KEYS = (
    "malformed_payload",
    "missing_required_source_fields",
    "missing_usable_title",
    "unknown_language",
    "unknown_license",
    "duplicate_id",
    "slug_collision",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--snapshot", help="Pfad zum Snapshot (Default: snapshot/current.json)")
    parser.add_argument(
        "--out-exercises", default=str(EXERCISES_DIR), help="Zielverzeichnis fuer die Fakten"
    )
    parser.add_argument("--out-i18n", default=str(I18N_DIR), help="Zielverzeichnis fuer die Texte")
    parser.add_argument("--report-json-out", help="Pfad fuer den maschinenlesbaren Importbericht")
    parser.add_argument(
        "--report-max-examples",
        type=int,
        default=25,
        help="Maximale Zahl abgelehnter Beispiele im Bericht (Default: 25)",
    )
    parser.add_argument(
        "--prune",
        action="store_true",
        help="Zieldateien loeschen, die der Snapshot nicht mehr enthaelt. Standardmaessig aus: "
        "Loeschen ist laut SCHEMA.md 3 verboten, ein verschwundener Upstream-Eintrag wird "
        "spaeter als status: deprecated gefuehrt.",
    )
    return parser.parse_args()


# --------------------------------------------------------------------- helpers

_TAG_RE = re.compile("<.*?>")


def clean_html(raw: Any) -> str:
    """Entfernt Tags aus einem wger-Beschreibungsfeld.

    Bewusst zeichengleich zum Altskript (`create_wger_exercise_db.clean_html`),
    damit die erzeugte DB in Phase 1 nachweisbar dieselben Texte enthaelt wie
    die heute ausgelieferte. Das heisst auch: HTML-Entities bleiben stehen
    (`&nbsp;` in 93 Uebersetzungen). Das saubere Entschaerfen ist eine
    Inhaltsaenderung und gehoert nach Phase 2.
    """
    if not isinstance(raw, str):
        return ""
    return re.sub(_TAG_RE, "", raw).strip()


def normalize_text(value: Any) -> str:
    return value.strip() if isinstance(value, str) else ""


def ref_id(value: Any) -> Any:
    """wger liefert Relationen je nach Endpunkt als ID oder als Objekt."""
    return value.get("id") if isinstance(value, dict) else value


def slugify(name: str) -> str:
    ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_name).strip("-").lower()
    return re.sub(r"-+", "-", slug)


class Rejections:
    def __init__(self, max_examples: int) -> None:
        self.counts: Counter = Counter({key: 0 for key in REJECTION_REASON_KEYS})
        self.examples: list[dict[str, Any]] = []
        self.max_examples = max_examples

    def add(self, reason: str, **detail: Any) -> None:
        self.counts[reason] += 1
        if len(self.examples) < self.max_examples:
            self.examples.append({"reason": reason, **detail})

    @property
    def total(self) -> int:
        return sum(self.counts.values())


# ----------------------------------------------------------------------- import


def build_language_map(vocab: Vocabularies, snap: snapshot_mod.Snapshot) -> dict[int, str]:
    """Registry -> wger-Sprach-IDs, gegen den Snapshot geprueft.

    Bricht ab, wenn die Registry etwas anderes behauptet als die API. Genau
    diese Pruefung fehlte dem Altskript, weshalb dort seit Jahren spanische
    Texte als Franzoesisch ausgeliefert werden.
    """
    api = {int(row["id"]): str(row["short_name"]) for row in snap.data["language"]}
    mapping: dict[int, str] = {}
    problems: list[str] = []
    for wger_id, code in vocab.wger_language_ids.items():
        actual = api.get(wger_id)
        if actual is None:
            problems.append(f"  {code}: wger_language_id {wger_id} existiert in der API nicht")
        elif actual != code:
            problems.append(
                f"  {code}: wger_language_id {wger_id} ist in der API '{actual}', nicht '{code}'"
            )
        else:
            mapping[wger_id] = code
    if problems:
        raise SystemExit(
            "vocab/languages.yaml widerspricht dem Snapshot:\n" + "\n".join(problems)
        )
    return mapping


def collect_muscles(
    exercise: dict[str, Any],
    muscle_names: dict[Any, str],
    vocab: Vocabularies,
    unmapped: Counter,
) -> list[dict[str, str]]:
    """wger-Muskelwerte -> Knoten des neuen Vokabulars.

    Primaer gewinnt: taucht derselbe Knoten in beiden Listen auf, bleibt nur die
    primaere Zuweisung (Invariante 9). Im aktuellen Bestand kommt das nicht vor,
    die Regel ist Vorsorge.
    """
    mapping = vocab.muscles.legacy_wger_mapping
    out: list[dict[str, str]] = []
    seen: set[str] = set()
    for role, key in (("primary", "muscles"), ("secondary", "muscles_secondary")):
        for raw in exercise.get(key) or []:
            raw_name = muscle_names.get(ref_id(raw))
            if not raw_name:
                continue
            node = mapping.get(raw_name)
            if node is None:
                unmapped[raw_name] += 1
                continue
            if node in seen:
                continue
            seen.add(node)
            out.append({"id": node, "role": role})
    return out


def run(args: argparse.Namespace) -> tuple[int, dict[str, Any]]:
    vocab = Vocabularies()
    snap = snapshot_mod.load(Path(args.snapshot) if args.snapshot else None)
    imported_at = dt.date.fromisoformat(snap.fetched_at[:10]).isoformat()

    language_map = build_language_map(vocab, snap)
    license_map = vocab.wger_license_ids
    muscle_names = {row["id"]: (row.get("name_en") or row.get("name")) for row in snap.data["muscle"]}
    category_names = {row["id"]: row.get("name") for row in snap.data["exercisecategory"]}
    equipment_names = {row["id"]: row.get("name") for row in snap.data["equipment"]}

    exercises_dir = Path(args.out_exercises)
    i18n_dir = Path(args.out_i18n)

    rejections = Rejections(max(1, args.report_max_examples))
    unmapped_muscles: Counter = Counter()
    skipped_languages: Counter = Counter()
    written_exercises: dict[str, str] = {}  # id -> slug
    slugs: dict[str, str] = {}  # slug -> id
    translations_written: Counter = Counter()
    licenses_seen: Counter = Counter()
    authors: Counter = Counter()
    without_muscles = 0
    without_primary = 0
    without_source_language = 0

    for index, exercise in enumerate(snap.exercises):
        if not isinstance(exercise, dict):
            rejections.add("malformed_payload", raw_index=index, details="kein Objekt")
            continue

        raw_id = exercise.get("id")
        exercise_id = normalize_text(str(raw_id)) if raw_id is not None else ""
        if not exercise_id:
            rejections.add("missing_required_source_fields", raw_index=index, details="id fehlt")
            continue
        if exercise_id in written_exercises:
            rejections.add("duplicate_id", id=exercise_id, raw_index=index)
            continue

        raw_translations = exercise.get("translations") or []
        if not isinstance(raw_translations, list):
            rejections.add("malformed_payload", id=exercise_id, details="translations ist keine Liste")
            continue

        # ---- Texte einsammeln, nach Sprachcode
        texts: dict[str, dict[str, Any]] = {}
        for translation in raw_translations:
            if not isinstance(translation, dict):
                rejections.add("malformed_payload", id=exercise_id, details="Uebersetzung ist kein Objekt")
                continue
            code = language_map.get(ref_id(translation.get("language")))
            if code is None:
                skipped_languages[str(ref_id(translation.get("language")))] += 1
                rejections.add(
                    "unknown_language",
                    id=exercise_id,
                    language=ref_id(translation.get("language")),
                )
                continue
            name = normalize_text(translation.get("name"))
            if not name:
                continue
            if code in texts:
                # Kommt im Bestand nicht vor; erste Uebersetzung gewinnt, damit
                # das Ergebnis nicht von der Listenreihenfolge abhaengt.
                continue

            license_id = ref_id(translation.get("license"))
            spdx = license_map.get(license_id) if license_id is not None else None
            if spdx is None:
                rejections.add("unknown_license", id=exercise_id, language=code, license=license_id)
                continue

            texts[code] = {
                "name": name,
                "description": clean_html(translation.get("description")),
                "search_terms": [
                    alias
                    for alias in (
                        normalize_text(a.get("alias") if isinstance(a, dict) else a)
                        for a in translation.get("aliases") or []
                    )
                    if alias
                ],
                "license": spdx,
                "license_author": normalize_text(translation.get("license_author")) or None,
                "source_id": str(translation.get("id")) if translation.get("id") is not None else None,
            }

        if not texts:
            rejections.add("missing_usable_title", id=exercise_id)
            continue

        # ---- Slug: aus der Quellsprache, sonst aus der ersten verfuegbaren
        name_order = [vocab.source_language, *sorted(texts)]
        slug_source = next(code for code in name_order if code in texts)
        if slug_source != vocab.source_language:
            without_source_language += 1
        slug = slugify(texts[slug_source]["name"])
        if not slug:
            slug = f"exercise-{exercise_id}"
        if slug in slugs:
            # Deterministisch und stabil: die ID haengt hinten dran. Der Slug ist
            # laut SCHEMA.md 3 ein Vertrag und darf sich spaeter nicht mehr
            # aendern, also darf die Aufloesung nicht von der Reihenfolge
            # abhaengen, in der die Kollision auftritt.
            rejections.add("slug_collision", id=exercise_id, slug=slug, other=slugs[slug])
            slug = f"{slug}-{exercise_id}"
        slugs[slug] = exercise_id

        # ---- Fakten
        muscles = collect_muscles(exercise, muscle_names, vocab, unmapped_muscles)
        if not muscles:
            without_muscles += 1
        if not any(m["role"] == "primary" for m in muscles):
            without_primary += 1

        exercise_license = license_map.get(ref_id(exercise.get("license")))
        if exercise_license is None:
            rejections.add("unknown_license", id=exercise_id, license=ref_id(exercise.get("license")))
            continue

        source_fields: dict[str, Any] = {}
        category = category_names.get(ref_id(exercise.get("category")))
        if category:
            source_fields["category"] = category
        equipment = sorted(
            {
                name
                for name in (equipment_names.get(ref_id(e)) for e in exercise.get("equipment") or [])
                if name
            }
        )
        if equipment:
            source_fields["equipment"] = equipment

        document: dict[str, Any] = {
            "id": exercise_id,
            "slug": slug,
            "status": "active",
        }
        if muscles:
            document["muscles"] = [yamlio.inline(m) for m in muscles]
        document["provenance"] = {
            "id": yamlio.inline({"source": "wger"}),
            "slug": yamlio.inline({"source": "derived", "at": imported_at}),
        }
        if muscles:
            document["provenance"]["muscles"] = yamlio.inline(
                {"source": "wger", "at": imported_at}
            )
        upstream: dict[str, Any] = {
            "source": "wger",
            "source_id": exercise_id,
            "license": exercise_license,
            "license_author": normalize_text(exercise.get("license_author")) or None,
            "imported_at": imported_at,
        }
        if source_fields:
            upstream["source_fields"] = source_fields
        document["upstream"] = upstream

        yamlio.write(exercises_dir / f"{exercise_id}.yaml", document, header=EXERCISE_HEADER)
        written_exercises[exercise_id] = slug

        # ---- Texte
        for code in sorted(texts):
            text = texts[code]
            doc: dict[str, Any] = {
                "exercise_id": exercise_id,
                "language": code,
                # Von Menschen aus der wger-Community geschrieben, aber von
                # diesem Projekt nie abgenommen — und bei 511 Eintraegen ohne
                # jede Autorenangabe. `human` wuerde in sechs Monaten als "das
                # hat jemand geprueft" gelesen; der Unterschied waere dann nicht
                # mehr rekonstruierbar.
                "status": "upstream_unreviewed",
                "name": text["name"],
            }
            if text["description"]:
                doc["description"] = text["description"]
            if text["search_terms"]:
                doc["search_terms"] = text["search_terms"]
            upstream_text: dict[str, Any] = {"license": text["license"]}
            if text["license_author"]:
                upstream_text["license_author"] = text["license_author"]
            if text["source_id"]:
                upstream_text["source_id"] = text["source_id"]
            doc["upstream"] = upstream_text

            yamlio.write(i18n_dir / code / f"{exercise_id}.yaml", doc, header=TRANSLATION_HEADER)
            translations_written[code] += 1
            licenses_seen[text["license"]] += 1
            authors[text["license_author"] or ""] += 1

    removed = prune(exercises_dir, i18n_dir, written_exercises, enabled=args.prune)

    report = {
        "import": {
            "generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
            "snapshot_file": snap.path.name,
            "snapshot_sha256": snap.sha256,
            "snapshot_fetched_at": snap.fetched_at,
            "source": snap.source,
        },
        "summary": {
            "raw_exercise_count": len(snap.exercises),
            "imported_count": len(written_exercises),
            "rejected_count": rejections.total,
            "translations_written": sum(translations_written.values()),
            "languages_written": len(translations_written),
        },
        "content_gaps": {
            "without_any_muscle": without_muscles,
            "without_primary_muscle": without_primary,
            "without_source_language_text": without_source_language,
            "unmapped_wger_muscles": dict(unmapped_muscles),
        },
        "translations_per_language": dict(sorted(translations_written.items())),
        "licenses": dict(sorted(licenses_seen.items())),
        "license_authors": {
            "distinct": len([a for a in authors if a]),
            "without_author": authors.get("", 0),
            "top": authors.most_common(10),
        },
        "skipped_wger_languages": dict(skipped_languages),
        "rejection_reasons": {key: int(rejections.counts[key]) for key in REJECTION_REASON_KEYS},
        "rejected_examples": rejections.examples,
        "pruned_files": removed,
    }
    return 0, report


def prune(
    exercises_dir: Path, i18n_dir: Path, keep: dict[str, str], *, enabled: bool
) -> list[str]:
    """Entfernt Dateien, die der Snapshot nicht mehr enthaelt — nur auf Ansage."""
    stale: list[str] = []
    for path in sorted(exercises_dir.glob("*.yaml")):
        if path.stem not in keep:
            stale.append(str(path.relative_to(exercises_dir.parent.parent)))
    for lang_dir in sorted(p for p in i18n_dir.glob("*") if p.is_dir()):
        for path in sorted(lang_dir.glob("*.yaml")):
            if path.stem not in keep:
                stale.append(str(path.relative_to(i18n_dir.parent.parent)))
    if enabled:
        for relative in stale:
            (exercises_dir.parent.parent / relative).unlink()
    return stale


def main() -> int:
    args = parse_args()
    code, report = run(args)

    summary = report["summary"]
    gaps = report["content_gaps"]
    print(f"Snapshot   {report['import']['snapshot_file']} ({report['import']['snapshot_fetched_at']})")
    print(f"Uebungen   {summary['imported_count']} von {summary['raw_exercise_count']} importiert, "
          f"{summary['rejected_count']} abgelehnt")
    print(f"Texte      {summary['translations_written']} in {summary['languages_written']} Sprachen")
    for language, count in report["translations_per_language"].items():
        print(f"             {language}: {count}")
    print(f"Lizenzen   {report['licenses']}")
    print(f"Autoren    {report['license_authors']['distinct']} verschiedene, "
          f"{report['license_authors']['without_author']} Texte ohne Angabe")
    print(f"Luecken    {gaps['without_any_muscle']} Uebungen ohne Muskel, "
          f"{gaps['without_primary_muscle']} ohne primaeren")
    if gaps["unmapped_wger_muscles"]:
        print(f"           nicht abgebildete wger-Muskeln: {gaps['unmapped_wger_muscles']}")
    if report["rejected_examples"]:
        print("Abgelehnt  " + json.dumps(report["rejection_reasons"], ensure_ascii=False))
    if report["pruned_files"]:
        print(f"Verwaist   {len(report['pruned_files'])} Dateien ohne Snapshot-Eintrag")

    if args.report_json_out:
        out = Path(args.report_json_out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Bericht    {out}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
