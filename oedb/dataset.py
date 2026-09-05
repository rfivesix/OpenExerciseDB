"""Loads `data/` as a whole — the repository's source of truth.

Both the build pipeline and the validator operate on this dataset. It deliberately
only loads and indexes data without enforcing validation rules; all rules live in
`build/validate.py` so there is a single authoritative place to read them.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterator

from . import yamlio
from .paths import EXERCISES_DIR, I18N_DIR


@dataclass
class Document:
    path: Path
    data: dict[str, Any]

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)


@dataclass
class Exercise(Document):
    @property
    def id(self) -> str:
        return str(self.data.get("id", self.path.stem))

    @property
    def slug(self) -> str:
        return str(self.data.get("slug", ""))

    @property
    def status(self) -> str:
        return str(self.data.get("status", "active"))

    @property
    def muscles(self) -> list[dict[str, Any]]:
        return list(self.data.get("muscles") or [])

    def muscle_ids(self, role: str | None = None) -> list[str]:
        return [
            str(m["id"])
            for m in self.muscles
            if isinstance(m, dict) and "id" in m and (role is None or m.get("role") == role)
        ]

    @property
    def upstream(self) -> dict[str, Any]:
        return self.data.get("upstream") or {}

    @property
    def source_fields(self) -> dict[str, Any]:
        return self.upstream.get("source_fields") or {}


@dataclass
class Translation(Document):
    language: str = ""

    @property
    def exercise_id(self) -> str:
        return str(self.data.get("exercise_id", self.path.stem))

    @property
    def name(self) -> str:
        return str(self.data.get("name", ""))

    @property
    def upstream(self) -> dict[str, Any]:
        return self.data.get("upstream") or {}


@dataclass
class Dataset:
    exercises: dict[str, Exercise] = field(default_factory=dict)
    translations: dict[str, dict[str, Translation]] = field(default_factory=dict)
    """Language code -> exercise ID -> text document."""

    duplicate_ids: list[tuple[str, str]] = field(default_factory=list)
    """(ID, path) for files whose `id` does not match the filename or is duplicated.
    The validator reports them; loading does not abort."""

    @property
    def languages(self) -> list[str]:
        return sorted(self.translations)

    def active(self) -> Iterator[Exercise]:
        for exercise in self.exercises.values():
            if exercise.status == "active":
                yield exercise

    def sorted_exercises(self) -> list[Exercise]:
        """Sort by numeric ID where possible — otherwise '1000' would precede '9'."""

        def key(exercise: Exercise) -> tuple[int, str]:
            raw = exercise.id
            return (0, f"{int(raw):020d}") if raw.isdigit() else (1, raw)

        return sorted(self.exercises.values(), key=key)

    def translation(self, language: str, exercise_id: str) -> Translation | None:
        return self.translations.get(language, {}).get(exercise_id)


def load(exercises_dir: Path | None = None, i18n_dir: Path | None = None) -> Dataset:
    exercises_dir = Path(exercises_dir) if exercises_dir else EXERCISES_DIR
    i18n_dir = Path(i18n_dir) if i18n_dir else I18N_DIR

    dataset = Dataset()
    for path in sorted(exercises_dir.glob("*.yaml")):
        data = yamlio.read(path)
        if not isinstance(data, dict):
            dataset.duplicate_ids.append((path.stem, str(path)))
            continue
        exercise = Exercise(path=path, data=data)
        if exercise.id in dataset.exercises:
            dataset.duplicate_ids.append((exercise.id, str(path)))
            continue
        dataset.exercises[exercise.id] = exercise

    if i18n_dir.is_dir():
        for lang_dir in sorted(p for p in i18n_dir.iterdir() if p.is_dir()):
            language = lang_dir.name
            bucket: dict[str, Translation] = {}
            for path in sorted(lang_dir.glob("*.yaml")):
                data = yamlio.read(path)
                if not isinstance(data, dict):
                    continue
                translation = Translation(path=path, data=data, language=language)
                bucket[translation.exercise_id] = translation
            if bucket:
                dataset.translations[language] = bucket

    return dataset
