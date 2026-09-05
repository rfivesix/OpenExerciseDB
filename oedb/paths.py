"""Central repository paths. The single location that resolves the repository root."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

VOCAB_DIR = ROOT / "vocab"
SCHEMA_DIR = ROOT / "schema"
DATA_DIR = ROOT / "data"
EXERCISES_DIR = DATA_DIR / "exercises"
PUBLISHED_IDS = DATA_DIR / "published_ids.yaml"
I18N_DIR = DATA_DIR / "i18n"
SNAPSHOT_DIR = ROOT / "snapshot"
EXAMPLES_DIR = ROOT / "examples"
GOLDEN_DIR = ROOT / "test" / "golden"
ARTIFACTS_DIR = ROOT / "artifacts"

EXERCISE_SCHEMA = SCHEMA_DIR / "exercise.schema.json"
TRANSLATION_SCHEMA = SCHEMA_DIR / "translation.schema.json"


def exercise_path(exercise_id: str) -> Path:
    return EXERCISES_DIR / f"{exercise_id}.yaml"


def translation_path(language: str, exercise_id: str) -> Path:
    return I18N_DIR / language / f"{exercise_id}.yaml"


def language_dirs() -> list[Path]:
    if not I18N_DIR.is_dir():
        return []
    return sorted(p for p in I18N_DIR.iterdir() if p.is_dir())
