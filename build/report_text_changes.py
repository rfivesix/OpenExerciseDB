#!/usr/bin/env python3
"""Document curated de/en text changes against the shipped reference catalog."""
from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from oedb.paths import ARTIFACTS_DIR, ROOT


LANGUAGES = ("de", "en")
DEFAULT_REFERENCE = ARTIFACTS_DIR / "reference" / "openexercisedb.db"
DEFAULT_DATABASE = ARTIFACTS_DIR / "openexercisedb.db"
DEFAULT_OUTPUT = ROOT / "reports" / "text_changes_phase2.md"
PROVENANCE_MARKER = "AI review provenance: GPT-5, 2026-09-03."


def rows(connection: sqlite3.Connection, language: str) -> dict[str, sqlite3.Row]:
    connection.row_factory = sqlite3.Row
    return {
        row["exercise_id"]: row
        for row in connection.execute(
            "SELECT exercise_id, name, description FROM exercise_translations WHERE language_code = ?",
            (language,),
        )
    }


def sort_id(value: str) -> tuple[int, str]:
    return (0, f"{int(value):020d}") if value.isdigit() else (1, value)


def text(value: str | None) -> str:
    return (value or "").replace("\r\n", "\n").strip()


def block(value: str) -> str:
    return f"```text\n{value}\n```" if value else "_leer_"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reference", type=Path, default=DEFAULT_REFERENCE)
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    if not args.reference.exists():
        raise SystemExit(f"Referenz-DB fehlt: {args.reference}")
    if not args.database.exists():
        raise SystemExit(f"Katalog-DB fehlt: {args.database}")

    with sqlite3.connect(args.reference) as reference, sqlite3.connect(args.database) as database:
        changed_names: list[tuple[str, str, str, str]] = []
        changed_descriptions: list[tuple[str, str, str, str]] = []
        for language in LANGUAGES:
            old, new = rows(reference, language), rows(database, language)
            for exercise_id in sorted(set(old) & set(new), key=sort_id):
                source_path = ROOT / "data" / "i18n" / language / f"{exercise_id}.yaml"
                if not source_path.exists() or PROVENANCE_MARKER not in source_path.read_text(encoding="utf-8"):
                    continue
                old_name, new_name = text(old[exercise_id]["name"]), text(new[exercise_id]["name"])
                old_description = text(old[exercise_id]["description"])
                new_description = text(new[exercise_id]["description"])
                if old_name != new_name:
                    changed_names.append((language, exercise_id, old_name, new_name))
                if old_description != new_description:
                    changed_descriptions.append((language, exercise_id, old_description, new_description))

    lines = [
        "# Phase-2 text changes",
        "",
        "This report compares the Job-A-reviewed source documents with the released reference database. "
        "It records intentional curated changes visible to existing users; it is not a compatibility failure.",
        "",
        f"- Changed names: **{len(changed_names)}**",
        f"- Changed descriptions: **{len(changed_descriptions)}**",
        "",
        "## Names",
        "",
        "| Language | ID | Previous | Current |",
        "|---|---:|---|---|",
    ]
    lines.extend(f"| {language} | `{exercise_id}` | {old} | {new} |" for language, exercise_id, old, new in changed_names)
    lines.extend(["", "## Descriptions", ""])
    for language, exercise_id, old, new in changed_descriptions:
        lines.extend([
            f"### `{exercise_id}` ({language})",
            "",
            "Previous:",
            "",
            block(old),
            "",
            "Current:",
            "",
            block(new),
            "",
        ])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines), encoding="utf-8")
    print(f"{args.output}: {len(changed_names)} names, {len(changed_descriptions)} descriptions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
