#!/usr/bin/env python3
"""Schlaegt Nachfolger fuer stillgelegte Uebungen vor. Anwenden tut es nichts.

Eine `status: deprecated`-Uebung bleibt aufloesbar, taucht aber nicht mehr auf.
Fuer einen Teil davon gibt es im Bestand einen offensichtlichen Nachfolger —
`154 Chin-ups` und `152 Chin Up` sind dieselbe Uebung, upstream doppelt gefuehrt
und dann halb geloescht. Wo das zutrifft, ist `status: merged` + `merged_into`
die bessere Antwort als `deprecated`: der Build erzeugt daraus einen Eintrag in
`exercise_aliases`, und die App zieht damit beim Import `routine_exercises` und
`set_logs` auf den Nachfolger um. Aus einer toten Zeile wird die richtige Uebung.

**Deshalb wird hier nichts automatisch angewandt.** Ein Merge schreibt
Trainingsdaten auf fremden Geraeten um. Ein Fuzzy-Treffer, der das
stillschweigend tut, ist schlimmer als die Luecke, die er schliesst. Das Skript
schreibt Vorschlaege mit Begruendung und Score; die Bestaetigung ist ein
bewusster, einzelner Schritt (`--apply` mit expliziter Liste).

Aufruf:

    python3 build/propose_aliases.py                       # Vorschlaege anzeigen
    python3 build/propose_aliases.py --out artifacts/alias_proposals.yaml
    python3 build/propose_aliases.py --apply 154=152 268=1392
"""
from __future__ import annotations

import argparse
import difflib
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from oedb import dataset as dataset_mod  # noqa: E402
from oedb import yamlio  # noqa: E402
from oedb.paths import ROOT  # noqa: E402
from oedb.vocab import Vocabularies  # noqa: E402

EXACT = 1.0
STRONG = 0.90
"""Ab hier ist ein Vorschlag es wert, angesehen zu werden. Darunter wird die
Trefferquote so schlecht, dass die Liste mehr Arbeit macht als sie spart."""


def words(name: str) -> list[str]:
    """Vergleichsform: ohne Akzente, ohne Satzzeichen, ohne Plural-s.

    `Chin-ups` und `Chin Up` sollen zusammenfallen, `Leg Extension` und
    `Leg Extension Machine` nicht.
    """
    ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    tokens = re.findall(r"[a-z0-9]+", ascii_name.lower())
    # Schwelle 3, nicht 4: sonst faellt ausgerechnet "ups" durch, und
    # `Chin-ups` trifft `Chin Up` nicht. Die Regel greift symmetrisch auf
    # beiden Seiten, "press" wird also ueberall zu "pres" — unschoen, aber
    # folgenlos, weil verglichen und nicht angezeigt wird.
    return [token[:-1] if len(token) >= 3 and token.endswith("s") else token for token in tokens]


def normalize(name: str) -> str:
    return " ".join(words(name))


def squash(name: str) -> str:
    """Alle Buchstaben ohne Trenner. Faengt die Wortgrenzen-Faelle:
    `Handstand Push Up` / `Handstand Pushup`, `Lat Pull Down` / `Lat Pulldown`."""
    return "".join(words(name))


def propose(data: dataset_mod.Dataset, vocab: Vocabularies) -> list[dict[str, Any]]:
    """Drei Signale, absichtlich getrennt gehalten.

    Sie sind unterschiedlich viel wert, und sie zu einem Score zu verrechnen
    wuerde genau das verstecken, worauf es beim Review ankommt:

    * **wortgleich** — dieselben Woerter, andere Reihenfolge oder Schreibweise
      (`Lying Leg Raise` / `Leg Raises, Lying`). Sehr wahrscheinlich dieselbe
      Uebung.
    * **enthalten** — die Wortmenge der einen steckt in der anderen
      (`Barbell Hip Thrust` / `Hip Thrust`). Das ist zweischneidig: es findet
      den Nachfolger, aber genauso oft eine *Variante* des Originals. Bei
      `Lat Pull Down` sind es drei gleich gute (Inverted, Underhand,
      Close-grip) — dann ist keiner davon die Antwort, und das Skript sagt das,
      statt den erstbesten zu nennen.
    * **aehnlich** — Zeichenaehnlichkeit ab 0.90, fuer Tippfehler und
      Bindestriche.
    """
    language = vocab.source_language

    active: list[tuple[str, str, frozenset[str], str]] = []
    by_wordset: dict[frozenset[str], list[tuple[str, str]]] = {}
    by_squash: dict[str, list[tuple[str, str]]] = {}
    for exercise in data.active():
        translation = data.translation(language, exercise.id)
        if translation is None:
            continue
        wordset = frozenset(words(translation.name))
        if not wordset:
            continue
        active.append((exercise.id, translation.name, wordset, normalize(translation.name)))
        by_wordset.setdefault(wordset, []).append((exercise.id, translation.name))
        by_squash.setdefault(squash(translation.name), []).append((exercise.id, translation.name))

    keys = [entry[3] for entry in active]
    by_key: dict[str, list[tuple[str, str]]] = {}
    for exercise_id, name, _, key in active:
        by_key.setdefault(key, []).append((exercise_id, name))

    proposals: list[dict[str, Any]] = []
    for exercise in data.exercises.values():
        if exercise.status != "deprecated":
            continue
        translation = data.translation(language, exercise.id)
        if translation is None:
            continue
        own_words = frozenset(words(translation.name))
        own_key = normalize(translation.name)
        own_category = exercise.source_fields.get("category")

        matches: list[dict[str, Any]] = []
        seen: set[str] = set()

        def add(
            candidate_id: str, name: str, kind: str, score: float, diff: str = ""
        ) -> None:
            if candidate_id in seen or candidate_id == exercise.id:
                return
            seen.add(candidate_id)
            other = data.exercises[candidate_id].source_fields.get("category")
            matches.append(
                {
                    "id": candidate_id,
                    "name": name,
                    "kind": kind,
                    "score": round(score, 3),
                    "diff": diff,
                    "same_category": bool(own_category and own_category == other),
                }
            )

        for candidate_id, name in by_wordset.get(own_words, []):
            add(candidate_id, name, "wortgleich", EXACT)
        for candidate_id, name in by_squash.get(squash(translation.name), []):
            add(candidate_id, name, "wortgleich", EXACT)

        if not matches:
            for candidate_id, name, wordset, _ in active:
                if own_words <= wordset or wordset <= own_words:
                    extra = sorted(wordset - own_words)
                    fehlt = sorted(own_words - wordset)
                    add(
                        candidate_id,
                        name,
                        "enthalten",
                        len(own_words & wordset) / max(len(own_words), len(wordset)),
                        # Genau diese Worte sind der Unterschied. Sie zu zeigen
                        # ist der halbe Review: "+assisted" beantwortet die
                        # Frage, ob 154 Chin-ups nach 1737 gehoert, sofort mit
                        # nein.
                        diff=" ".join([f"+{w}" for w in extra] + [f"-{w}" for w in fehlt]),
                    )

        if not matches:
            for close in difflib.get_close_matches(own_key, keys, n=3, cutoff=STRONG):
                score = difflib.SequenceMatcher(None, own_key, close).ratio()
                for candidate_id, name in by_key.get(close, []):
                    add(candidate_id, name, "aehnlich", score)

        matches.sort(key=lambda item: (-item["score"], not item["same_category"], item["id"]))
        top = matches[0]["score"] if matches else 0.0
        tied = [item for item in matches if item["score"] == top]
        proposals.append(
            {
                "id": exercise.id,
                "name": translation.name,
                "category": own_category,
                # Mehrere gleich gute Kandidaten heissen nicht "nimm den
                # ersten", sondern "eine Maschine kann das hier nicht".
                "ambiguous": len(tied) > 1,
                "candidates": matches[:4],
            }
        )

    order = {"wortgleich": 0, "enthalten": 1, "aehnlich": 2}
    proposals.sort(
        key=lambda item: (
            order.get(item["candidates"][0]["kind"], 9) if item["candidates"] else 9,
            item["ambiguous"],
            -(item["candidates"][0]["score"] if item["candidates"] else 0.0),
            item["id"],
        )
    )
    return proposals


def apply_merges(pairs: list[str]) -> int:
    data = dataset_mod.load()
    changed = 0
    for pair in pairs:
        if "=" not in pair:
            print(f"Erwartet <alt>=<neu>, bekommen: {pair!r}", file=sys.stderr)
            return 2
        old_id, new_id = (part.strip() for part in pair.split("=", 1))
        exercise = data.exercises.get(old_id)
        if exercise is None:
            print(f"Uebung {old_id} existiert nicht.", file=sys.stderr)
            return 2
        target = data.exercises.get(new_id)
        if target is None:
            print(f"Ziel {new_id} existiert nicht.", file=sys.stderr)
            return 2
        if target.status != "active":
            print(f"Ziel {new_id} ist {target.status}, nicht active.", file=sys.stderr)
            return 2

        document = dict(exercise.data)
        document["status"] = "merged"
        document["merged_into"] = new_id
        provenance = dict(document.get("provenance") or {})
        provenance["merged_into"] = yamlio.inline(
            {"source": "human", "at": __import__("datetime").date.today().isoformat()}
        )
        document["provenance"] = provenance
        # Reihenfolge erhalten: merged_into gehoert direkt hinter status.
        ordered = {}
        for key, value in document.items():
            ordered[key] = value
            if key == "status" and "merged_into" in document:
                ordered["merged_into"] = document["merged_into"]
        ordered.pop("merged_into", None)
        ordered["merged_into"] = document["merged_into"]
        yamlio.write(exercise.path, document)
        print(f"  {old_id} -> {new_id} als merged eingetragen")
        changed += 1
    print(f"{changed} Zusammenlegungen eingetragen. `build/validate.py` gegenpruefen.")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", help="Vorschlaege zusaetzlich als YAML ablegen")
    parser.add_argument(
        "--apply",
        nargs="+",
        metavar="ALT=NEU",
        help="Bestaetigte Zusammenlegungen eintragen. Schreibt Nutzer-Logs um — bewusst "
        "einzeln anzugeben, nie aus der Vorschlagsliste uebernommen.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.apply:
        return apply_merges(args.apply)

    data = dataset_mod.load()
    vocab = Vocabularies()
    proposals = propose(data, vocab)

    if not proposals:
        print("Keine stillgelegten Uebungen ohne Nachfolger.")
        return 0

    def kind_of(item: dict[str, Any]) -> str:
        return item["candidates"][0]["kind"] if item["candidates"] else "keiner"

    same_name = [p for p in proposals if kind_of(p) == "wortgleich"]
    contained = [p for p in proposals if kind_of(p) == "enthalten"]
    similar = [p for p in proposals if kind_of(p) == "aehnlich"]
    none_found = [p for p in proposals if not p["candidates"]]

    print(f"{len(proposals)} stillgelegte Uebungen geprueft.\n")

    if same_name:
        print(f"Gleicher Name ({len(same_name)}) — nur Schreibweise, Reihenfolge oder Plural:")
        for item in same_name:
            for candidate in item["candidates"] if item["ambiguous"] else item["candidates"][:1]:
                flag = "" if candidate["same_category"] else "  [andere Kategorie]"
                print(
                    f"  {item['id']:>6} {item['name'][:34]:<34} -> {candidate['id']:>6} "
                    f"{candidate['name'][:34]:<34}{flag}"
                )
        print()

    if contained:
        print(f"Wortzusatz ({len(contained)}) — SCHWACHES SIGNAL, jeder Fall einzeln:")
        print(
            "  Die Wortmenge steckt ineinander. Das findet genauso oft eine andere Uebung\n"
            "  wie den Nachfolger — `Chin-ups` vs. `Assisted chin-ups` ist derselbe Treffer\n"
            "  wie `Barbell Hip Thrust` vs. `Hip Thrust`. Die Spalte rechts sagt, welche\n"
            "  Woerter dazukommen (+) oder wegfallen (-); danach ist es meist offensichtlich.\n"
        )
        for item in contained:
            print(f"  {item['id']:>6} {item['name']}")
            for candidate in item["candidates"]:
                flag = "" if candidate["same_category"] else "  [andere Kategorie]"
                print(
                    f"           -> {candidate['id']:>6} {candidate['name'][:40]:<40} "
                    f"{candidate['diff']:<24}{flag}"
                )
        print()

    if similar:
        print(f"Aehnlich geschrieben ({len(similar)}):")
        for item in similar:
            best = item["candidates"][0]
            print(
                f"  {item['id']:>6} {item['name'][:34]:<34} -> {best['id']:>6} "
                f"{best['name'][:34]:<34} {best['score']:.2f}"
            )
        print()

    if none_found:
        print(f"Ohne Kandidat ({len(none_found)}) — bleiben deprecated:")
        print("  " + ", ".join(f"{item['id']} {item['name'][:24]}" for item in none_found))
        print()

    print("Nichts davon ist angewandt. Bestaetigte Paare eintragen mit:")
    print("  python3 build/propose_aliases.py --apply 154=152 268=1392")

    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        yamlio.write(
            out,
            {"proposals": proposals},
            header="Vorschlaege von build/propose_aliases.py. NICHT angewandt.\n"
            "Ein Merge schreibt Trainingsdaten auf fremden Geraeten um und wird\n"
            "einzeln bestaetigt: `build/propose_aliases.py --apply <alt>=<neu>`.",
        )
        print(f"\nVorschlaege: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
