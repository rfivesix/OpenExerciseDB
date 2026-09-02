#!/usr/bin/env python3
"""Erzeugt den generierten Teil von ATTRIBUTION.md aus den Daten.

wger lizenziert Uebungsdaten pro Eintrag, nicht pauschal (SCHEMA.md 3b). Die
Attribution ist damit einzelnen Beitragenden geschuldet — im aktuellen Bestand
250 verschiedenen Personen — und nicht "wger" als Projekt.

Bei dieser Groessenordnung ist eine handgepflegte Liste die einzige Variante,
die garantiert irgendwann falsch ist. Also wird sie gerechnet: aus
`upstream.license_author` jeder Uebung und jeder Uebersetzung, bei jedem Build.

Das Skript schreibt ausschliesslich zwischen die Marker in ATTRIBUTION.md; der
erklaerende Text drumherum bleibt handgepflegt.

Aufruf:

    python3 build/build_attribution.py
    python3 build/build_attribution.py --check   # nur pruefen, nichts schreiben
"""
from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from oedb import dataset as dataset_mod  # noqa: E402
from oedb.paths import ROOT  # noqa: E402

ATTRIBUTION_FILE = ROOT / "ATTRIBUTION.md"
BEGIN = "<!-- BEGIN GENERATED LIST -->"
END = "<!-- END GENERATED LIST -->"

NO_AUTHOR = "the wger project and its contributors"


def collect(data: dataset_mod.Dataset) -> tuple[Counter, Counter, dict[str, Counter]]:
    """Autoren zaehlen, getrennt nach Uebungen und Texten.

    Getrennt, weil es zwei verschiedene Beitraege sind: wer eine Uebung angelegt
    hat, und wer sie in eine Sprache uebersetzt hat. Beide sind zu nennen.
    """
    authors: Counter = Counter()
    licenses: Counter = Counter()
    per_language: dict[str, Counter] = {}

    for exercise in data.exercises.values():
        upstream = exercise.upstream or {}
        if not upstream:
            continue
        authors[(upstream.get("license_author") or "").strip()] += 1
        if upstream.get("license"):
            licenses[str(upstream["license"])] += 1

    for language, bucket in data.translations.items():
        counter = per_language.setdefault(language, Counter())
        for translation in bucket.values():
            upstream = translation.upstream or {}
            if not upstream:
                continue
            author = (upstream.get("license_author") or "").strip()
            authors[author] += 1
            counter[author] += 1
            if upstream.get("license"):
                licenses[str(upstream["license"])] += 1

    return authors, licenses, per_language


def render(data: dataset_mod.Dataset) -> str:
    authors, licenses, per_language = collect(data)
    named = {name: count for name, count in authors.items() if name}
    anonymous = authors.get("", 0)
    total_records = sum(authors.values())

    lines: list[str] = []
    lines.append("")
    lines.append(
        f"Across {len(data.exercises)} exercises and "
        f"{sum(len(bucket) for bucket in data.translations.values())} translations, "
        f"**{len(named)} distinct upstream authors** are credited. "
        f"{anonymous} of {total_records} records carry no author upstream."
    )
    lines.append("")

    lines.append("### Original licenses")
    lines.append("")
    lines.append("| License | Records |")
    lines.append("|---|---|")
    for name, count in sorted(licenses.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"| `{name}` | {count} |")
    lines.append("")

    lines.append("### Languages")
    lines.append("")
    lines.append("| Language | Translations | Distinct authors |")
    lines.append("|---|---|---|")
    for language in sorted(per_language):
        counter = per_language[language]
        distinct = len([name for name in counter if name])
        lines.append(f"| `{language}` | {sum(counter.values())} | {distinct} |")
    lines.append("")

    lines.append("### Contributors")
    lines.append("")
    lines.append(
        "Listed by the name each contributor recorded upstream, with the number of "
        "records they authored. Sorted alphabetically, case-insensitively."
    )
    lines.append("")
    for name in sorted(named, key=lambda value: (value.lower(), value)):
        lines.append(f"- {name} ({named[name]})")
    lines.append("")

    if anonymous:
        lines.append(
            f"A further {anonymous} records carry no author upstream and are attributed to "
            f"*{NO_AUTHOR}*. They are counted here rather than dropped, so the gap stays "
            f"visible."
        )
        lines.append("")

    return "\n".join(lines)


def splice(text: str, generated: str) -> str:
    start = text.index(BEGIN) + len(BEGIN)
    end = text.index(END)
    return text[:start] + generated + text[end:]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check",
        action="store_true",
        help="Nur pruefen, ob die Datei aktuell ist. Exitcode 1, wenn nicht. Fuer die CI.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    data = dataset_mod.load()
    if not data.exercises:
        print("Keine Daten unter data/exercises/ — nichts zu erzeugen.", file=sys.stderr)
        return 2

    current = ATTRIBUTION_FILE.read_text(encoding="utf-8")
    if BEGIN not in current or END not in current:
        print(f"Marker {BEGIN} / {END} fehlen in {ATTRIBUTION_FILE}", file=sys.stderr)
        return 2

    updated = splice(current, render(data))

    if args.check:
        if updated != current:
            print(
                "ATTRIBUTION.md ist nicht auf dem Stand der Daten. "
                "`python3 build/build_attribution.py` laufen lassen und committen.",
                file=sys.stderr,
            )
            return 1
        print("ATTRIBUTION.md ist aktuell.")
        return 0

    if updated == current:
        print("ATTRIBUTION.md war bereits aktuell.")
        return 0

    ATTRIBUTION_FILE.write_text(updated, encoding="utf-8")
    authors, _, _ = collect(data)
    print(
        f"ATTRIBUTION.md geschrieben: {len([a for a in authors if a])} Beitragende genannt."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
