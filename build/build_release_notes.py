#!/usr/bin/env python3
"""Erzeugt die Release Notes aus Build-, Diff- und Validierungsbericht.

Aus einer frueheren Pipeline uebernommen und um das erweitert, was das neue Schema
mitbringt: Schemaversion, Sprachabdeckung, Lizenzverteilung und den offenen
Rest von Phase 2.

Die Notes sind fuer zwei Publikum gleichzeitig geschrieben: fuer Menschen, die
wissen wollen, was sich geaendert hat, und fuer die Person, die in sechs
Monaten herausfinden muss, warum eine bestimmte Zeile so aussieht, wie sie
aussieht.
"""
import json
import os


def load(path: str) -> dict:
    if not path or not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as handle:
        payload = json.load(handle)
    return payload if isinstance(payload, dict) else {}


def main() -> int:
    build = load(os.environ["BUILD_REPORT_PATH"])
    diff = load(os.environ["DIFF_REPORT_PATH"])
    validation = load(os.environ.get("VALIDATION_REPORT_PATH", ""))
    import_report = load(os.environ.get("IMPORT_REPORT_PATH", ""))
    out_path = os.environ["RELEASE_NOTES_PATH"]

    meta = build.get("build", {})
    summary = build.get("summary", {})
    diff_summary = diff.get("summary", {})

    lines = [
        "# Exercise catalog release",
        "",
        f"- Content version: `{meta.get('db_version', 'n/a')}`",
        f"- Schema version: `{meta.get('schema_version', 'n/a')}` "
        f"(minimum consumer: `{meta.get('min_app_schema_version', 'n/a')}`)",
        f"- Generated at: `{meta.get('generated_at', 'n/a')}`",
        f"- Source commit: `{meta.get('source_commit', 'n/a')}`",
        f"- Exercises: `{summary.get('imported_count', 'n/a')}` "
        f"(`{summary.get('active_count', 'n/a')}` active)",
        f"- Translations: `{summary.get('translation_count', 'n/a')}`",
        f"- Muscle assignments: `{summary.get('muscle_link_count', 'n/a')}`",
    ]

    if import_report:
        upstream = import_report.get("import", {})
        lines.append(
            f"- Upstream snapshot: `{upstream.get('snapshot_file', 'n/a')}` "
            f"(fetched `{upstream.get('snapshot_fetched_at', 'n/a')}`)"
        )

    # --- Was sich gegenueber dem letzten Release geaendert hat
    lines += ["", "## Changes against the previous release", ""]
    if diff.get("skipped"):
        lines.append("Diff skipped: no published reference database available.")
    elif diff_summary:
        lines += [
            f"- Removed IDs: `{diff_summary.get('removed_count', 'n/a')}` "
            f"(threshold `{diff_summary.get('fail_on_removed_threshold', 'n/a')}`, "
            f"exceeded: `{diff_summary.get('removed_threshold_exceeded', 'n/a')}`)",
            f"- Removed without a successor alias: "
            f"`{diff_summary.get('unmapped_removed_count', 0)}`",
            f"- Added IDs: `{diff_summary.get('added_count', 'n/a')}`",
            f"- Exercises with changed fields: "
            f"`{diff_summary.get('changed_exercise_count', 'n/a')}`",
        ]
        examples = diff.get("examples", {})
        if examples.get("added_ids"):
            lines.append(f"- Added examples: `{', '.join(examples['added_ids'])}`")
        if examples.get("removed_ids"):
            lines.append(f"- Removed examples: `{', '.join(examples['removed_ids'])}`")
        for warning in diff.get("warning_flags", []):
            lines.append(f"- **{warning['severity'].upper()}** {warning['code']}: {warning['message']}")
    else:
        lines.append("Diff summary unavailable.")

    # --- Sprachen
    languages = build.get("languages", {})
    if languages:
        lines += ["", "## Languages", "", "| Code | Tier | Translated | Filled from fallback | Shown |", "|---|---|---|---|---|"]
        for code in sorted(languages):
            entry = languages[code]
            lines.append(
                f"| `{code}` | {entry.get('tier', '')} | {entry.get('native', 0)} "
                f"| {entry.get('fallback', 0)} | {'yes' if entry.get('displayable') else 'no'} |"
            )

    # --- Lizenzen. Gehoert sichtbar ins Release, nicht in eine Fussnote.
    licenses = import_report.get("licenses") if import_report else None
    if licenses:
        lines += ["", "## Licensing", ""]
        for name, number in sorted(licenses.items()):
            lines.append(f"- `{name}`: {number} translations")
        authors = import_report.get("license_authors", {})
        if authors:
            lines.append(
                f"- {authors.get('distinct', 0)} distinct authors credited; "
                f"{authors.get('without_author', 0)} entries carry no author upstream"
            )
        lines.append("")
        lines.append("Upstream records keep their original per-entry license. See ATTRIBUTION.md.")

    # --- Was noch offen ist. Ein Release, das seine eigenen Luecken verschweigt,
    # macht sie unsichtbar statt kleiner.
    coverage = build.get("field_coverage", {})
    nullable = build.get("nullable_columns", [])
    if nullable:
        lines += ["", "## Not yet complete", ""]
        lines.append(
            "The following classification fields are not filled for every exercise. "
            "They are phase 2 work; consumers must treat them as nullable."
        )
        lines.append("")
        for column in nullable:
            entry = coverage.get(column, {})
            lines.append(
                f"- `{column}`: {entry.get('filled', 0)} of {entry.get('of', 0)} "
                f"({entry.get('share', 0) * 100:.0f}%)"
            )

    if validation:
        lines += [
            "",
            f"Validation profile `{validation.get('profile', 'n/a')}`: "
            f"{validation.get('error_count', 0)} errors, "
            f"{validation.get('warning_count', 0)} warnings.",
        ]

    lines += [
        "",
        "This is a data-artifact release channel consumed by app-side catalog refresh.",
    ]

    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
