"""YAML-Ein- und Ausgabe mit stabiler, diffbarer Formatierung.

Die Quelldateien sind das eigentliche Produkt dieses Repos — sie werden gelesen,
review't und per PR geaendert. Deshalb schreibt der Importer sie nicht mit den
PyYAML-Standardeinstellungen (alphabetisch sortiert, ASCII-escaped, 80 Zeichen
hart umgebrochen), sondern in einer festen, menschenfreundlichen Form:

* Schluessel in der Reihenfolge, in der sie gesetzt wurden — nicht alphabetisch.
* Unicode bleibt Unicode. "Rückenstrecker", nicht "R\\u00fcckenstrecker".
* Mehrzeilige Texte als Literal-Block, damit Diffs zeilenweise lesbar bleiben.
* Keine Zeilenumbrueche in Listen-Eintraegen.

Das ist keine Kosmetik: ein Importer, der bei jedem Lauf dieselbe Datei anders
formatiert, macht jeden Folge-Diff unbrauchbar.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


class inline(dict):
    """Ein Mapping, das einzeilig geschrieben wird: `{ id: lats, role: primary }`.

    Fuer kurze, immer gleich aufgebaute Eintraege — Muskelzuweisungen etwa —
    ist eine Zeile je Eintrag deutlich besser review-bar als drei.
    """


class _Dumper(yaml.SafeDumper):
    """SafeDumper mit Einrueckung fuer Listen (PyYAML tut das per Default nicht)."""

    def increase_indent(self, flow: bool = False, indentless: bool = False):  # noqa: D102
        return super().increase_indent(flow, False)


def _inline_representer(dumper: yaml.Dumper, data: inline):
    return dumper.represent_mapping("tag:yaml.org,2002:map", data, flow_style=True)


_Dumper.add_representer(inline, _inline_representer)


LITERAL_THRESHOLD = 80
"""Ab dieser Laenge wird ein String als Literal-Block geschrieben."""


def _str_representer(dumper: yaml.Dumper, data: str):
    # Laengere Texte als Literal-Block, nicht als umgebrochener Plain-Scalar:
    # ein umgebrochener Absatz wird bei jeder Wortaenderung komplett neu
    # umbrochen, und der Diff faerbt dann drei Zeilen statt einer.
    if "\n" in data or len(data) > LITERAL_THRESHOLD:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


_Dumper.add_representer(str, _str_representer)


def dump(data: Any) -> str:
    """Serialisiert `data` in die kanonische Repo-Form."""
    return yaml.dump(
        data,
        Dumper=_Dumper,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
        width=10 ** 6,
    )


def write(path: Path, data: Any, header: str | None = None) -> None:
    """Schreibt `data` nach `path`, optional mit einem Kommentarkopf.

    Legt fehlende Verzeichnisse an und schreibt nur, wenn sich der Inhalt
    aendert — sonst wuerde jeder Importlauf 871 Dateien anfassen und die
    mtime-basierte Zwischenspeicherung von Werkzeugen entwerten.
    """
    text = dump(data)
    if header:
        text = "".join(f"# {line}\n" if line else "#\n" for line in header.splitlines()) + text
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return
    path.write_text(text, encoding="utf-8")


try:  # libyaml ist rund zehnmal schneller und beim Einlesen von 4.200 Dateien spuerbar
    _Loader: type = yaml.CSafeLoader  # type: ignore[attr-defined]
except AttributeError:  # pragma: no cover — nur ohne libyaml
    _Loader = yaml.SafeLoader


def read(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.load(handle, Loader=_Loader)
