"""YAML input and output with stable, diff-friendly formatting.

The source files are the primary product of this repository — they are read,
reviewed, and modified via pull requests. The serializer therefore does not use
PyYAML defaults (alphabetically sorted, ASCII-escaped, hard-wrapped at 80 columns),
but enforces a clean, predictable human-friendly format:

* Keys in insertion order — not sorted alphabetically.
* Unicode remains Unicode: "Rückenstrecker", not "R\\u00fcckenstrecker".
* Multiline text as literal block scalars, keeping line-by-line diffs readable.
* No wrapping inside list entries.

This predictability ensures that repeated serialization does not generate noisy
git diffs.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


class inline(dict):
    """A mapping written in flow style on a single line: `{ id: lats, role: primary }`.

    For short, uniformly structured entries such as muscle assignments, a single
    line per entry is far easier to review than three lines.
    """


class _Dumper(yaml.SafeDumper):
    """SafeDumper with indentation for list items (PyYAML does not indent by default)."""

    def increase_indent(self, flow: bool = False, indentless: bool = False):  # noqa: D102
        return super().increase_indent(flow, False)


def _inline_representer(dumper: yaml.Dumper, data: inline):
    return dumper.represent_mapping("tag:yaml.org,2002:map", data, flow_style=True)


_Dumper.add_representer(inline, _inline_representer)


LITERAL_THRESHOLD = 80
"""Strings exceeding this length or containing newlines are emitted as literal blocks."""


def _str_representer(dumper: yaml.Dumper, data: str):
    # Longer text as literal block, not as wrapped plain scalar:
    # re-wrapping paragraphs causes small word edits to touch multiple lines in diffs.
    if "\n" in data or len(data) > LITERAL_THRESHOLD:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


_Dumper.add_representer(str, _str_representer)


def dump(data: Any) -> str:
    """Serializes `data` into canonical repository YAML formatting."""
    return yaml.dump(
        data,
        Dumper=_Dumper,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
        width=10 ** 6,
    )


def write(path: Path, data: Any, header: str | None = None) -> None:
    """Writes `data` to `path`, optionally with a comment header.

    Creates missing directories and only writes if content has changed,
    preserving file modification timestamps.
    """
    text = dump(data)
    if header:
        text = "".join(f"# {line}\n" if line else "#\n" for line in header.splitlines()) + text
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return
    path.write_text(text, encoding="utf-8")


try:  # libyaml is significantly faster when reading thousands of files
    _Loader: type = yaml.CSafeLoader  # type: ignore[attr-defined]
except AttributeError:  # pragma: no cover — only without libyaml
    _Loader = yaml.SafeLoader


def read(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.load(handle, Loader=_Loader)

