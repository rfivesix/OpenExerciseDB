#!/usr/bin/env python3
"""Schreibt die GitHub-Step-Summary des Build-Laufs.

Aus einer frueheren Pipeline uebernommen, um Validierung und Schemaversion erweitert. Der
Bericht laeuft auch dann, wenn vorher etwas fehlgeschlagen ist — er ist oft die
einzige Stelle, an der jemand sieht, wo genau es aufgehoert hat.
"""
import json
import os


def load(path: str) -> dict:
    if not path or not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except (OSError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


def main() -> int:
    build = load(os.environ.get("BUILD_REPORT_PATH", ""))
    diff = load(os.environ.get("DIFF_REPORT_PATH", ""))
    validation = load(os.environ.get("VALIDATION_REPORT_PATH", ""))
    release_page_url = os.environ.get("RELEASE_PAGE_URL", "")
    publish_outcome = os.environ.get("PUBLISH_OUTCOME", "skipped")
    generator_success = os.environ.get("GENERATOR_SUCCESS", "false")
    generate_outcome = os.environ.get("GENERATE_OUTCOME", "unknown")
    summary_path = os.environ["GITHUB_STEP_SUMMARY"]

    lines = ["## Catalog build summary", ""]

    if validation:
        errors = validation.get("error_count", 0)
        marker = "FAILED" if errors else "passed"
        lines.append(
            f"- Invariants (`{validation.get('profile', 'n/a')}`): **{marker}** — "
            f"{errors} errors, {validation.get('warning_count', 0)} warnings"
        )
        for invariant, reason in sorted((validation.get("skipped") or {}).items()):
            lines.append(f"  - invariant {invariant} skipped: {reason}")

    lines.append(f"- Database build: `{generate_outcome}`")

    if generator_success == "true" and build:
        meta = build.get("build", {})
        summary = build.get("summary", {})
        lines += [
            f"- Content version: `{meta.get('db_version', 'n/a')}`",
            f"- Schema version: `{meta.get('schema_version', 'n/a')}`",
            f"- Generated at: `{meta.get('generated_at', 'n/a')}`",
            f"- Exercises: `{summary.get('imported_count', 'n/a')}` "
            f"(`{summary.get('active_count', 'n/a')}` active)",
            f"- Translations: `{summary.get('translation_count', 'n/a')}`",
        ]
        if build.get("nullable_columns"):
            lines.append(
                f"- Still nullable (phase 2): `{', '.join(build['nullable_columns'])}`"
            )
    else:
        lines.append("- No artifacts were produced; downstream steps were skipped.")

    if generator_success == "true" and diff:
        if diff.get("skipped"):
            lines.append("- Diff: skipped (no published reference database)")
        else:
            diff_summary = diff.get("summary", {})
            examples = diff.get("examples", {})
            lines += [
                f"- Removed IDs: `{diff_summary.get('removed_count', 'n/a')}` "
                f"(threshold `{diff_summary.get('fail_on_removed_threshold', 'n/a')}`, "
                f"exceeded: `{diff_summary.get('removed_threshold_exceeded', 'n/a')}`)",
                f"- Removed without a successor: "
                f"`{diff_summary.get('unmapped_removed_count', 0)}`",
                f"- Added IDs: `{diff_summary.get('added_count', 'n/a')}`",
            ]
            if examples.get("removed_ids"):
                lines.append(f"- Removed examples: `{', '.join(examples['removed_ids'])}`")
            for warning in diff.get("warning_flags", []):
                if warning.get("severity") == "severe":
                    lines.append(f"- **SEVERE** {warning['code']}: {warning['message']}")

    lines.append(f"- Release publication: `{publish_outcome}`")
    if release_page_url:
        lines.append(f"- Release page: {release_page_url}")

    with open(summary_path, "a", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
