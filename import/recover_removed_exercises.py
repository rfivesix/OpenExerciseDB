#!/usr/bin/env python3
"""Recovers exercises that were deleted upstream, but were already published.

**The problem.** wger cleaned up between 2026-06-15 and 2026-08-31, removing 38
exercises — some legitimately (`bicep`, `cabel`, `DB UCV`), others mistakenly
(Chin-ups, Good Mornings, Leg Extension, Barbell Hip Thrust). The import followed
upstream faithfully and therefore did not receive them.

For upstream this was a simple deletion. For our catalog it is not: these IDs
are referenced in user devices in `routine_exercises` and `set_logs` (SCHEMA.md §3).
While the app importer is upsert-only and retains them on existing installs, a fresh
install, re-seed, or backup restore onto a newly seeded database would leave those
references dangling.

**The rule.** What was once published never disappears: it receives
`status: deprecated`. The row remains in the database and resolves correctly,
but is excluded from search and catalog browsers. Whether any of these exercises
additionally receives a successor (`status: merged` + `merged_into`) is decided
by human review — `build/propose_aliases.py` proposes suggestions, but this script
does not apply them automatically. A fuzzy match silently rewriting user logs would
be worse than the problem.

**Where content comes from.** From an already published database — upstream no
longer has the records. Two details apply:

* The legacy pipeline had wired wger language IDs incorrectly. In a v1 database,
  `fr` contains Spanish, `ja` Greek, and `it` Russian. During recovery this is
  corrected (`LEGACY_LANGUAGE_FIX`) rather than propagating mislabeled text.
* License and author are unrecoverable — the legacy pipeline discarded them, and
  the upstream entry is gone. They are conservatively marked with the most
  restrictive license in the corpus, with a note in `provenance`.

Usage:

    python3 import/recover_removed_exercises.py --from-db <published.db>
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

# Language codes in a v1 database are partially erroneous — see vocab/languages.yaml.
# Here they are corrected during recovery.
LEGACY_LANGUAGE_FIX = {
    "de": "de",
    "en": "en",
    "fr": "es",  # wger language ID 4 is Spanish, not French
    "ja": "el",  # 8 is Greek; Japanese does not exist in wger
    "it": "ru",  # 5 is Russian
}

FALLBACK_LICENSE = "CC-BY-SA-4.0"
LICENSE_NOTE = (
    "License not recoverable: upstream entry was deleted and legacy pipeline "
    "discarded license/license_author. Conservatively set to the most restrictive "
    "license present in the corpus."
)

EXERCISE_HEADER = """data/exercises/<id>.yaml — recovered entry.

This exercise was deleted upstream, but was already published and is therefore
referenced in user workout logs (SCHEMA.md §3). It is preserved as
`status: deprecated`: resolvable, but excluded from search and catalog views.

Recovered by import/recover_removed_exercises.py from a published database,
not from upstream — upstream no longer has this entry."""

TRANSLATION_HEADER = """data/i18n/<lang>/<id>.yaml — recovered text.

Recovered from a published database because the upstream entry was deleted.
License and author were not included there; see the exercise file for attribution."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--from-db",
        required=True,
        action="append",
        metavar="PATH",
        help="Published database from which contents are retrieved. Allowed multiple times; "
        "first database containing an ID wins.",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Report only without writing files."
    )
    parser.add_argument("--report-json-out", help="Path for machine-readable JSON report")
    return parser.parse_args()


def load_registry() -> set[str]:
    if not PUBLISHED_IDS.exists():
        raise SystemExit(
            f"{PUBLISHED_IDS} is missing. Run `python3 build/update_published_ids.py "
            f"--from-db <published.db>` first."
        )
    return {str(key) for key in (yamlio.read(PUBLISHED_IDS) or {}).get("ids", {})}


def read_source(path: Path) -> dict[str, dict[str, Any]]:
    """Reads a published database into {id: {row, translations}}."""
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
    """Maps legacy muscle names back to vocabulary nodes."""
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
        print("Nothing to recover: every published ID is present in data/exercises/.")
        return 0

    sources: list[dict[str, dict[str, Any]]] = []
    for raw_path in args.from_db:
        path = Path(raw_path)
        if not path.exists():
            print(f"Database not found: {path}", file=sys.stderr)
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

        # Normalize language codes before writing anything.
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
                    "note": "Deleted upstream, but already published — SCHEMA.md §3.",
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

    verb = "would be recovered" if args.dry_run else "recovered"
    print(f"{len(recovered)} of {len(missing)} entries {verb}:")
    for item in recovered:
        print(
            f"  {item['id']:>6}  {item['name'][:46]:<46} "
            f"{item['category'] or '-':<10} {len(item['languages'])} languages, "
            f"{item['muscles']} muscles"
        )
    if unrecoverable:
        print(
            f"\n{len(unrecoverable)} without content in the specified databases: "
            f"{', '.join(unrecoverable)}"
        )
        print("  Supply an older published database via --from-db.")

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
        print(f"Report: {out}")

    if not args.dry_run and recovered:
        print(
            "\nNext step: `python3 build/propose_aliases.py` proposes successors. "
            "A merge rewrites user logs and is therefore confirmed individually."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
