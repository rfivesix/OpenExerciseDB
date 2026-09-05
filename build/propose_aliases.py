#!/usr/bin/env python3
"""Proposes successors for deprecated exercises. Applies nothing automatically.

A `status: deprecated` exercise remains resolvable but no longer appears in listings.
For some of them, there is an obvious successor in the catalog —
`154 Chin-ups` and `152 Chin Up` are the same exercise, tracked twice upstream
and then partially deleted. Where this applies, `status: merged` + `merged_into`
is the better response than `deprecated`: the build creates an entry in
`exercise_aliases`, allowing the app to migrate `routine_exercises` and
`set_logs` to the successor upon import. A dead row becomes the correct exercise.

**Therefore, nothing is applied automatically here.** A merge rewrites workout
data on user devices. A fuzzy match performing this silently is far worse
than the gap it closes. The script generates proposals with justification and
score; confirmation is a deliberate, explicit step (`--apply` with an explicit list).

Usage:

    python3 build/propose_aliases.py                       # display proposals
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
"""Threshold above which a proposal warrants review. Below this, the false positive
rate makes the list more work than it saves."""


def words(name: str) -> list[str]:
    """Comparison format: stripped of accents, punctuation, and plural -s.

    `Chin-ups` and `Chin Up` should match, while `Leg Extension` and
    `Leg Extension Machine` should not.
    """
    ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    tokens = re.findall(r"[a-z0-9]+", ascii_name.lower())
    # Length threshold 3, not 4: otherwise "ups" is excluded and
    # `Chin-ups` does not match `Chin Up`. Applied symmetrically to both
    # sides, "press" becomes "pres" everywhere — inelegant but harmless
    # since it is used strictly for comparison, never displayed.
    return [token[:-1] if len(token) >= 3 and token.endswith("s") else token for token in tokens]


def normalize(name: str) -> str:
    return " ".join(words(name))


def squash(name: str) -> str:
    """All letters without delimiters. Catches word-boundary differences:
    `Handstand Push Up` / `Handstand Pushup`, `Lat Pull Down` / `Lat Pulldown`."""
    return "".join(words(name))


def propose(data: dataset_mod.Dataset, vocab: Vocabularies) -> list[dict[str, Any]]:
    """Three signals, intentionally kept separate.

    They carry different confidence levels, and combining them into a single score
    would obscure the exact information needed during review:

    * **exact_words** — same words, different order or punctuation
      (`Lying Leg Raise` / `Leg Raises, Lying`). Highly likely the same exercise.
    * **subset** — one word set is contained within the other
      (`Barbell Hip Thrust` / `Hip Thrust`). A double-edged sword: it identifies
      the successor, but just as often a *variant* of the original. For
      `Lat Pull Down` there are three equally good matches (Inverted, Underhand,
      Close-grip) — indicating none of them is the direct answer, which the script
      flags rather than picking one arbitrarily.
    * **similar** — character similarity >= 0.90, for typos and hyphens.
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
            add(candidate_id, name, "exact_words", EXACT)
        for candidate_id, name in by_squash.get(squash(translation.name), []):
            add(candidate_id, name, "exact_words", EXACT)

        if not matches:
            for candidate_id, name, wordset, _ in active:
                if own_words <= wordset or wordset <= own_words:
                    extra = sorted(wordset - own_words)
                    missing = sorted(own_words - wordset)
                    add(
                        candidate_id,
                        name,
                        "subset",
                        len(own_words & wordset) / max(len(own_words), len(wordset)),
                        # Exactly these words constitute the difference. Showing them
                        # provides half the review: "+assisted" immediately answers
                        # whether 154 Chin-ups belongs to 1737 with no.
                        diff=" ".join([f"+{w}" for w in extra] + [f"-{w}" for w in missing]),
                    )

        if not matches:
            for close in difflib.get_close_matches(own_key, keys, n=3, cutoff=STRONG):
                score = difflib.SequenceMatcher(None, own_key, close).ratio()
                for candidate_id, name in by_key.get(close, []):
                    add(candidate_id, name, "similar", score)

        matches.sort(key=lambda item: (-item["score"], not item["same_category"], item["id"]))
        top = matches[0]["score"] if matches else 0.0
        tied = [item for item in matches if item["score"] == top]
        proposals.append(
            {
                "id": exercise.id,
                "name": translation.name,
                "category": own_category,
                # Multiple equally ranked candidates mean "a machine cannot resolve this",
                # not "pick the first one".
                "ambiguous": len(tied) > 1,
                "candidates": matches[:4],
            }
        )

    order = {"exact_words": 0, "subset": 1, "similar": 2}
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
            print(f"Expected <old>=<new>, got: {pair!r}", file=sys.stderr)
            return 2
        old_id, new_id = (part.strip() for part in pair.split("=", 1))
        exercise = data.exercises.get(old_id)
        if exercise is None:
            print(f"Exercise {old_id} does not exist.", file=sys.stderr)
            return 2
        target = data.exercises.get(new_id)
        if target is None:
            print(f"Target {new_id} does not exist.", file=sys.stderr)
            return 2
        if target.status != "active":
            print(f"Target {new_id} is {target.status}, not active.", file=sys.stderr)
            return 2

        document = dict(exercise.data)
        document["status"] = "merged"
        document["merged_into"] = new_id
        provenance = dict(document.get("provenance") or {})
        provenance["merged_into"] = yamlio.inline(
            {"source": "human", "at": __import__("datetime").date.today().isoformat()}
        )
        document["provenance"] = provenance
        # Preserve order: merged_into belongs immediately after status.
        ordered = {}
        for key, value in document.items():
            ordered[key] = value
            if key == "status" and "merged_into" in document:
                ordered["merged_into"] = document["merged_into"]
        ordered.pop("merged_into", None)
        ordered["merged_into"] = document["merged_into"]
        yamlio.write(exercise.path, document)
        print(f"  {old_id} -> {new_id} recorded as merged")
        changed += 1
    print(f"{changed} merges recorded. Verify with `build/validate.py`.")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", help="Save proposals additionally as YAML")
    parser.add_argument(
        "--apply",
        nargs="+",
        metavar="OLD=NEW",
        help="Record confirmed merges. Rewrites user logs — explicitly "
        "provided individually, never applied en bloc from proposals.",
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
        print("No deprecated exercises without successors.")
        return 0

    def kind_of(item: dict[str, Any]) -> str:
        return item["candidates"][0]["kind"] if item["candidates"] else "none"

    same_name = [p for p in proposals if kind_of(p) == "exact_words"]
    contained = [p for p in proposals if kind_of(p) == "subset"]
    similar = [p for p in proposals if kind_of(p) == "similar"]
    none_found = [p for p in proposals if not p["candidates"]]

    print(f"{len(proposals)} deprecated exercises checked.\n")

    if same_name:
        print(f"Identical words ({len(same_name)}) — punctuation, order, or plural differences only:")
        for item in same_name:
            for candidate in item["candidates"] if item["ambiguous"] else item["candidates"][:1]:
                flag = "" if candidate["same_category"] else "  [different category]"
                print(
                    f"  {item['id']:>6} {item['name'][:34]:<34} -> {candidate['id']:>6} "
                    f"{candidate['name'][:34]:<34}{flag}"
                )
        print()

    if contained:
        print(f"Subsets / supersets ({len(contained)}) — WEAK SIGNAL, review each individually:")
        print(
            "  Word set is contained. Finds variants just as often as direct successors —\n"
            "  `Chin-ups` vs. `Assisted chin-ups` produces the same match as\n"
            "  `Barbell Hip Thrust` vs. `Hip Thrust`. The right-hand column shows\n"
            "  added (+) or removed (-) words; the distinction is usually obvious.\n"
        )
        for item in contained:
            print(f"  {item['id']:>6} {item['name']}")
            for candidate in item["candidates"]:
                flag = "" if candidate["same_category"] else "  [different category]"
                print(
                    f"           -> {candidate['id']:>6} {candidate['name'][:40]:<40} "
                    f"{candidate['diff']:<24}{flag}"
                )
        print()

    if similar:
        print(f"Similar spelling ({len(similar)}):")
        for item in similar:
            best = item["candidates"][0]
            print(
                f"  {item['id']:>6} {item['name'][:34]:<34} -> {best['id']:>6} "
                f"{best['name'][:34]:<34} {best['score']:.2f}"
            )
        print()

    if none_found:
        print(f"No candidate found ({len(none_found)}) — remain deprecated:")
        print("  " + ", ".join(f"{item['id']} {item['name'][:24]}" for item in none_found))
        print()

    print("None of these have been applied. Record confirmed pairs with:")
    print("  python3 build/propose_aliases.py --apply 154=152 268=1392")

    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        yamlio.write(
            out,
            {"proposals": proposals},
            header="Proposals from build/propose_aliases.py. NOT applied.\n"
            "A merge rewrites workout logs on user devices and must be confirmed\n"
            "individually: `build/propose_aliases.py --apply <old>=<new>`.",
        )
        print(f"\nProposals: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
