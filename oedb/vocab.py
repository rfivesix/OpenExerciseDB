"""Laedt die geschlossenen Vokabulare aus `vocab/` und macht sie abfragbar.

Einzige Stelle im Code, die die Struktur dieser Dateien kennt. Importer, Build
und Validator halten keine eigene Kopie — ein zweiter Satz Wahrheit waere
garantiert irgendwann inkonsistent (vgl. den Kommentarkopf von
`schema/exercise.schema.json`).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from functools import cached_property
from pathlib import Path
from typing import Any, Iterable

from . import yamlio
from .paths import VOCAB_DIR

LEVEL_GROUP = "group"
LEVEL_MUSCLE = "muscle"
LEVEL_HEAD = "head"


@dataclass(frozen=True)
class MuscleNode:
    id: str
    level: str
    parent_id: str | None
    group_id: str
    names: dict[str, str]
    body_slugs: tuple[str, ...]
    legacy_wger_name: str | None
    """Rohname aus dem alten wger-Vokabular, falls dieser Knoten selbst einen hat."""

    legacy_group: str
    """Gruppe, die die heutige App erwartet. Weicht bei `serratus_anterior` und
    `hip_flexors` bewusst von `group_id` ab — siehe SCHEMA.md 5."""


@dataclass
class MuscleVocabulary:
    nodes: dict[str, MuscleNode]
    legacy_wger_mapping: dict[str, str]
    """wger-Rohname -> Knoten-ID dieses Vokabulars."""

    _by_node: dict[str, str] = field(default_factory=dict, repr=False)

    def __post_init__(self) -> None:
        for raw_name, node_id in self.legacy_wger_mapping.items():
            # Erster Treffer gewinnt; das Mapping ist heute injektiv, aber ein
            # spaeterer zweiter Rohname fuer denselben Knoten darf den
            # Rueckweg nicht mehrdeutig machen.
            self._by_node.setdefault(node_id, raw_name)

    def __contains__(self, node_id: object) -> bool:
        return node_id in self.nodes

    def __getitem__(self, node_id: str) -> MuscleNode:
        return self.nodes[node_id]

    def ancestors(self, node_id: str) -> list[str]:
        """Vorfahren von unten nach oben, ohne den Knoten selbst."""
        out: list[str] = []
        current = self.nodes[node_id].parent_id
        while current is not None:
            out.append(current)
            current = self.nodes[current].parent_id
        return out

    def descendants(self, node_id: str) -> set[str]:
        out: set[str] = set()
        for candidate in self.nodes:
            if node_id in self.ancestors(candidate):
                out.add(candidate)
        return out

    def legacy_wger_name(self, node_id: str) -> str | None:
        """Der wger-Rohname, unter dem die heutige App diesen Knoten kennt.

        Laeuft vom Knoten nach oben, bis ein Knoten gefunden wird, der im
        `legacy_wger_mapping` vorkommt. Damit faellt spaeterer Feinschliff
        automatisch korrekt zurueck: wird `trapezius` zu `traps_upper`
        praezisiert, steht in der Kompatibilitaetsspalte weiterhin `Trapezius`.

        `None` heisst: die heutige App kennt diesen Muskel nicht und wuerde ihn
        ohnehin still verwerfen (`majorMuscleGroupFor` -> null). Er gehoert dann
        auch nicht in die Kompatibilitaetsspalte.
        """
        for candidate in [node_id, *self.ancestors(node_id)]:
            explicit = self.nodes[candidate].legacy_wger_name
            if explicit:
                return explicit
            name = self._by_node.get(candidate)
            if name is not None:
                return name
        return None


@dataclass(frozen=True)
class Language:
    code: str
    names: dict[str, str]
    tier: str
    wger_language_id: int | None
    fallback_chain: tuple[str, ...]
    complete_in_release: bool
    """Das Release garantiert eine Zeile je aktiver Uebung; fehlende Texte
    fuellt der Build ueber `fallback_chain`."""


def _entry_ids(entries: Iterable[Any]) -> list[str]:
    return [str(entry["id"]) for entry in entries]


class Vocabularies:
    """Alle Vokabulare, einmal geladen."""

    def __init__(self, vocab_dir: Path | None = None) -> None:
        self.dir = Path(vocab_dir) if vocab_dir else VOCAB_DIR

    def _load(self, name: str) -> dict[str, Any]:
        return yamlio.read(self.dir / f"{name}.yaml")

    # ---------------------------------------------------------------- muscles
    @cached_property
    def muscles(self) -> MuscleVocabulary:
        raw = self._load("muscles")
        nodes: dict[str, MuscleNode] = {}

        for group in raw.get("groups", []):
            gid = group["id"]
            nodes[gid] = MuscleNode(
                id=gid,
                level=LEVEL_GROUP,
                parent_id=None,
                group_id=gid,
                names=dict(group.get("names", {})),
                body_slugs=tuple(group.get("body_slugs") or []),
                legacy_wger_name=group.get("legacy_wger_name"),
                legacy_group=group.get("legacy_group") or gid,
            )

        for muscle in raw.get("muscles", []):
            mid = muscle["id"]
            gid = muscle["group"]
            group_legacy = nodes[gid].legacy_group if gid in nodes else gid
            legacy = muscle.get("legacy_group") or group_legacy
            nodes[mid] = MuscleNode(
                id=mid,
                level=LEVEL_MUSCLE,
                parent_id=gid,
                group_id=gid,
                names=dict(muscle.get("names", {})),
                body_slugs=tuple(muscle.get("body_slugs") or []),
                legacy_wger_name=muscle.get("legacy_wger_name"),
                legacy_group=legacy,
            )
            for head in muscle.get("heads", []) or []:
                hid = head["id"]
                nodes[hid] = MuscleNode(
                    id=hid,
                    level=LEVEL_HEAD,
                    parent_id=mid,
                    group_id=gid,
                    names=dict(head.get("names", {})),
                    body_slugs=tuple(head.get("body_slugs") or []),
                    legacy_wger_name=head.get("legacy_wger_name"),
                    legacy_group=head.get("legacy_group") or legacy,
                )

        mapping = {str(k): str(v) for k, v in (raw.get("legacy_wger_mapping") or {}).items()}
        return MuscleVocabulary(nodes=nodes, legacy_wger_mapping=mapping)

    # -------------------------------------------------------------- equipment
    @cached_property
    def _equipment_raw(self) -> dict[str, Any]:
        return self._load("equipment")

    @cached_property
    def primary_equipment(self) -> list[str]:
        return _entry_ids(self._equipment_raw.get("primary_equipment", []))

    @cached_property
    def setup(self) -> list[str]:
        return _entry_ids(self._equipment_raw.get("setup", []))

    @cached_property
    def equipment_names(self) -> dict[str, dict[str, str]]:
        out: dict[str, dict[str, str]] = {}
        for key in ("primary_equipment", "setup"):
            for entry in self._equipment_raw.get(key, []):
                out[str(entry["id"])] = dict(entry.get("names", {}))
        return out

    @cached_property
    def equipment_kinds(self) -> dict[str, str]:
        """Equipment-ID -> 'primary' | 'setup'. Die Achsen sind disjunkt
        (Invariante 3b), ein Wert kann also nur zu einer gehoeren."""
        kinds = {eid: "primary" for eid in self.primary_equipment}
        kinds.update({eid: "setup" for eid in self.setup})
        return kinds

    # --------------------------------------------------------- classification
    @cached_property
    def _classification_raw(self) -> dict[str, Any]:
        return self._load("classification")

    def classification(self, axis: str) -> list[str]:
        return _entry_ids(self._classification_raw.get(axis, []))

    @cached_property
    def force_vector_by_pattern(self) -> dict[str, str | None]:
        """movement_pattern -> force_vector. `None` heisst "keine ehrliche Antwort".

        force_vector ist eine Funktion von movement_pattern und wird deshalb
        abgeleitet statt annotiert (SCHEMA.md 6). Diese Tabelle ist die einzige
        Stelle, an der die Zuordnung steht.
        """
        return dict(self._classification_raw.get("force_vector_by_pattern") or {})

    def force_vector_for(self, pattern: str | None) -> str | None:
        return self.force_vector_by_pattern.get(pattern) if pattern else None

    @cached_property
    def classification_axes(self) -> list[str]:
        return [k for k, v in self._classification_raw.items() if isinstance(v, list)]

    # -------------------------------------------------------------- languages
    @cached_property
    def _languages_raw(self) -> dict[str, Any]:
        return self._load("languages")

    @cached_property
    def languages(self) -> dict[str, Language]:
        out: dict[str, Language] = {}
        for entry in self._languages_raw.get("languages", []):
            code = str(entry["code"])
            out[code] = Language(
                code=code,
                names=dict(entry.get("names", {})),
                tier=str(entry.get("tier", "upstream")),
                wger_language_id=entry.get("wger_language_id"),
                fallback_chain=tuple(entry.get("fallback_chain") or []),
                complete_in_release=bool(entry.get("complete_in_release", False)),
            )
        return out

    @cached_property
    def source_language(self) -> str:
        return str(self._languages_raw.get("source_language", "en"))

    @cached_property
    def min_completeness(self) -> float:
        return float(self._languages_raw.get("min_completeness", 0.95))

    @cached_property
    def wger_language_ids(self) -> dict[int, str]:
        """wger-Sprach-ID -> Sprachcode. Der Ersatz fuer die fest verdrahtete
        (und falsche) LANGUAGE_ID_MAP der alten Pipeline."""
        return {
            int(lang.wger_language_id): code
            for code, lang in self.languages.items()
            if lang.wger_language_id is not None
        }

    # --------------------------------------------------------------- licenses
    @cached_property
    def _licenses_raw(self) -> dict[str, Any]:
        return self._load("licenses")

    @cached_property
    def licenses(self) -> list[str]:
        return _entry_ids(self._licenses_raw.get("licenses", []))

    @cached_property
    def wger_license_ids(self) -> dict[int, str]:
        return {
            int(k): str(v)
            for k, v in (self._licenses_raw.get("legacy_wger_mapping") or {}).items()
        }


_default: Vocabularies | None = None


def load() -> Vocabularies:
    """Die Vokabulare des Repos, einmal geladen und danach zwischengespeichert."""
    global _default
    if _default is None:
        _default = Vocabularies()
    return _default
