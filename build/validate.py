#!/usr/bin/env python3
"""Validates the invariants from `schema/invariants.md`. The CI gate.

The invariants are the core quality mechanism of this repository: they catch
the mechanical portion of errors automatically, allowing human review to focus
on what a machine cannot decide.

**Two profiles.** In Phase 1, classification fields do not exist yet — wger does
not provide them, and guessing them would be worse than leaving them empty
(SCHEMA.md §11). A ruleset that is permanently red is ignored after a week and
thus worthless. Therefore:

    --profile phase1   Structure and vocabulary strictly enforced; content rules
                       apply wherever fields exist, and remain silent where they
                       do not yet exist.
    --profile full     Everything strictly enforced. The target state at the end
                       of Phase 2 — and proof that Phase 2 is complete.

What is missing in Phase 1 is not a silent blind spot, but a number in the
report: `--profile full` indicates at any time how much remains to be done.

Usage:

    python3 build/validate.py
    python3 build/validate.py --profile full --json-out artifacts/validation.json
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from oedb import dataset as dataset_mod  # noqa: E402
from oedb import yamlio  # noqa: E402
from oedb.paths import (  # noqa: E402
    EXAMPLES_DIR,
    EXERCISE_SCHEMA,
    GOLDEN_DIR,
    PUBLISHED_IDS,
    ROOT,
    TRANSLATION_SCHEMA,
    VOCAB_DIR,
)
from oedb.vocab import Vocabularies  # noqa: E402

ERROR = "error"
WARNING = "warning"

HARD_INVARIANTS = {
    "1", "1b", "1c", "2", "3", "3b", "4", "5", "6", "7",
    "8", "9", "10", "17", "21", "22", "23", "24", "25",
}
"""Structural and referential invariants: an ID points to nothing, a vocabulary
value does not exist, a muscle is listed twice. No legitimate exceptions."""

SOFT_INVARIANTS = {"11", "12", "13", "14", "15", "20"}
"""Plausibility invariants — correlations, not absolute laws.

Cardio is not logged in reps, except for burpees. The damage of an overly strict
rule is not the false alarm — which is visible —, but the silently distorted
annotation made to avoid it. Therefore, these rules can be excused per exercise,
with an explicit plain-text justification."""

EXCEPTION_PREFIX = "invariant_"

PHASE2_FIELDS = (
    "modality",
    "mechanic",
    "force_vector",
    "movement_pattern",
    "laterality",
    "usage_tags",
    "tracking_type",
    "load_mode",
    "primary_equipment",
    "setup",
    "muscles",
)
"""Fields that wger does not provide and that Phase 1 leaves empty.

In profile `phase1`, they are removed from the JSON schema's `required` list.
Everywhere else: if the field is present, it is fully validated."""

HEAVY_SETUP = ("squat_rack", "power_rack", "cable_tower", "landmine")
"""Invariant 11: setup incompatible with pure bodyweight."""

CARDIO_TRACKING = {"time", "distance_time", "distance_only"}
ADDED_WEIGHT_TRACKING = {"bodyweight_reps", "time"}
ASSISTED_EQUIPMENT = {"machine", "resistance_band"}


@dataclass
class Finding:
    invariant: str
    severity: str
    message: str
    location: str | None = None
    exercise_id: str | None = None
    excused: str | None = None
    """Justification if this finding was excused via `exceptions`."""

    def as_dict(self) -> dict[str, Any]:
        return {
            "invariant": self.invariant,
            "severity": self.severity,
            "message": self.message,
            "location": self.location,
            "exercise_id": self.exercise_id,
            "excused": self.excused,
        }


@dataclass
class Report:
    profile: str
    findings: list[Finding] = field(default_factory=list)
    skipped: dict[str, str] = field(default_factory=dict)
    stats: dict[str, Any] = field(default_factory=dict)

    def add(
        self,
        invariant: str,
        severity: str,
        message: str,
        location: str | None = None,
        exercise_id: str | None = None,
    ) -> None:
        self.findings.append(Finding(invariant, severity, message, location, exercise_id))

    @property
    def open_findings(self) -> list[Finding]:
        """All findings that have not been excused by an exception."""
        return [f for f in self.findings if f.excused is None]

    def skip(self, invariant: str, reason: str) -> None:
        self.skipped[invariant] = reason

    @property
    def errors(self) -> list[Finding]:
        return [f for f in self.open_findings if f.severity == ERROR]

    @property
    def warnings(self) -> list[Finding]:
        return [f for f in self.open_findings if f.severity == WARNING]


# --------------------------------------------------------------------- checks


def relative(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def jsonify(value: Any) -> Any:
    """Convert YAML values to what JSON Schema expects.

    YAML parses `at: 2026-09-02` as `datetime.date`, but the schema expects a
    string with `format: date`. Both representations are completely equivalent
    for a contributor — a validator that rejects one (namely the one shown in
    `examples/`) teaches no one, it only frustrates.
    """
    if isinstance(value, dict):
        return {key: jsonify(item) for key, item in value.items()}
    if isinstance(value, list):
        return [jsonify(item) for item in value]
    if isinstance(value, (dt.date, dt.datetime)):
        return value.isoformat()
    return value


def check_schemas(
    data: dataset_mod.Dataset, report: Report, *, profile: str
) -> None:
    """Invariant 1: each file validates against its JSON schema."""
    try:
        import jsonschema
    except ImportError:
        report.skip("1", "jsonschema is not installed (pip install -r requirements.txt)")
        return

    full_exercise_schema = json.loads(EXERCISE_SCHEMA.read_text(encoding="utf-8"))
    translation_schema = json.loads(TRANSLATION_SCHEMA.read_text(encoding="utf-8"))

    exercise_schema = full_exercise_schema
    if profile == "phase1":
        exercise_schema = dict(full_exercise_schema)
        exercise_schema["required"] = [
            key for key in exercise_schema.get("required", []) if key not in PHASE2_FIELDS
        ]

    for schema, documents, invariant in (
        (exercise_schema, data.exercises.values(), "1"),
        (
            translation_schema,
            [t for bucket in data.translations.values() for t in bucket.values()],
            "1b",
        ),
    ):
        validator = jsonschema.Draft202012Validator(schema)
        for document in documents:
            for error in validator.iter_errors(jsonify(document.data)):
                location = ".".join(str(part) for part in error.absolute_path) or "<root>"
                report.add(
                    invariant,
                    ERROR,
                    f"{location}: {error.message}",
                    relative(document.path),
                )

    # 1c — the example file is documentation and is copied by contributors. It is
    # always validated against the FULL schema, even in profile phase1: an example
    # that does not validate leads every contributor into the same mistake.
    for path, schema in [
        (EXAMPLES_DIR / "exercises" / "475.yaml", full_exercise_schema),
        *[
            (path, translation_schema)
            for path in sorted((EXAMPLES_DIR / "i18n").glob("*/*.yaml"))
        ],
    ]:
        if not path.exists():
            continue
        validator = jsonschema.Draft202012Validator(schema)
        for error in validator.iter_errors(jsonify(yamlio.read(path))):
            location = ".".join(str(part) for part in error.absolute_path) or "<root>"
            report.add("1c", ERROR, f"{location}: {error.message}", relative(path))


def check_vocabulary(data: dataset_mod.Dataset, vocab: Vocabularies, report: Report) -> None:
    """Invariant 2: every classifying value exists in a vocab/*.yaml file."""
    single_axes = {
        "status": set(vocab.classification("status")),
        "modality": set(vocab.classification("modality")),
        "mechanic": set(vocab.classification("mechanic")),
        "movement_pattern": set(vocab.classification("movement_pattern")),
        "laterality": set(vocab.classification("laterality")),
        "difficulty": set(vocab.classification("difficulty")),
        "tracking_type": set(vocab.classification("tracking_type")),
        "load_mode": set(vocab.classification("load_mode")),
        "primary_equipment": set(vocab.primary_equipment),
    }
    usage_tags = set(vocab.classification("usage_tags"))
    setup_values = set(vocab.setup)
    licenses = set(vocab.licenses)

    for exercise in data.exercises.values():
        location = relative(exercise.path)
        for field_name, allowed in single_axes.items():
            value = exercise.get(field_name)
            if value is not None and value not in allowed:
                report.add("2", ERROR, f"{field_name}: unknown value {value!r}", location)
        for tag in exercise.get("usage_tags") or []:
            if tag not in usage_tags:
                report.add("2", ERROR, f"usage_tags: unknown value {tag!r}", location)
        for item in exercise.get("setup") or []:
            if item not in setup_values:
                report.add("2", ERROR, f"setup: unknown value {item!r}", location)
        for entry in exercise.muscles:
            node = entry.get("id") if isinstance(entry, dict) else None
            if node is not None and node not in vocab.muscles:
                report.add("2", ERROR, f"muscles: unknown node {node!r}", location)
        license_id = (exercise.upstream or {}).get("license")
        if license_id is not None and license_id not in licenses:
            report.add("2", ERROR, f"upstream.license: unknown {license_id!r}", location)

    for language, bucket in data.translations.items():
        if language not in vocab.languages:
            report.add(
                "2",
                ERROR,
                f"Language {language!r} is not registered in vocab/languages.yaml",
                f"data/i18n/{language}/",
            )
            continue
        for translation in bucket.values():
            location = relative(translation.path)
            if translation.data.get("language") != language:
                report.add(
                    "2",
                    ERROR,
                    f"language: {translation.data.get('language')!r} does not match directory "
                    f"{language!r}",
                    location,
                )
            license_id = (translation.upstream or {}).get("license")
            if license_id is not None and license_id not in licenses:
                report.add("2", ERROR, f"upstream.license: unknown {license_id!r}", location)


def check_identity(data: dataset_mod.Dataset, report: Report) -> None:
    """Invariant 3: `id` and `slug` are globally unique."""
    for exercise_id, path in data.duplicate_ids:
        report.add("3", ERROR, f"duplicate or unreadable exercise {exercise_id!r}", path)

    slugs: dict[str, str] = {}
    for exercise in data.exercises.values():
        location = relative(exercise.path)
        if exercise.id != exercise.path.stem:
            report.add(
                "3", ERROR, f"id {exercise.id!r} does not match filename", location
            )
        if not exercise.slug:
            report.add("3", ERROR, "slug is missing", location)
            continue
        if exercise.slug in slugs:
            report.add(
                "3",
                ERROR,
                f"slug {exercise.slug!r} is already used by exercise {slugs[exercise.slug]}",
                location,
            )
        else:
            slugs[exercise.slug] = exercise.id


def check_vocab_id_uniqueness(vocab: Vocabularies, report: Report) -> None:
    """Invariant 3b: IDs within a vocabulary are unique across hierarchy levels
    — group, muscle, and head share a single primary-keyed table in the build."""
    raw = yamlio.read(VOCAB_DIR / "muscles.yaml")
    seen: dict[str, str] = {}
    for group in raw.get("groups", []):
        _claim(seen, str(group["id"]), "group", report, "vocab/muscles.yaml")
    for muscle in raw.get("muscles", []):
        _claim(seen, str(muscle["id"]), "muscle", report, "vocab/muscles.yaml")
        for head in muscle.get("heads") or []:
            _claim(seen, str(head["id"]), "head", report, "vocab/muscles.yaml")

    raw = yamlio.read(VOCAB_DIR / "equipment.yaml")
    seen = {}
    for axis in ("primary_equipment", "setup"):
        for entry in raw.get(axis, []):
            _claim(seen, str(entry["id"]), axis, report, "vocab/equipment.yaml")

    # The same trap one level deeper: legacy mapping must only point to nodes
    # that actually exist.
    for raw_name, node in vocab.muscles.legacy_wger_mapping.items():
        if node not in vocab.muscles:
            report.add(
                "3b",
                ERROR,
                f"legacy_wger_mapping: {raw_name!r} points to unknown node {node!r}",
                "vocab/muscles.yaml",
            )


def _claim(seen: dict[str, str], key: str, level: str, report: Report, location: str) -> None:
    if key in seen:
        report.add("3b", ERROR, f"ID {key!r} duplicated ({seen[key]} and {level})", location)
    else:
        seen[key] = level


def check_translation_coverage(
    data: dataset_mod.Dataset, vocab: Vocabularies, report: Report, *, profile: str
) -> None:
    """Invariants 4 and 5: completeness and counterpart matching."""
    active = {exercise.id for exercise in data.active()}

    for code, language in vocab.languages.items():
        if language.tier != "curated":
            continue
        bucket = data.translations.get(code, {})
        missing = sorted(active - set(bucket), key=str)
        if missing:
            severity = ERROR if profile == "full" else WARNING
            report.add(
                "4",
                severity,
                f"Language {code!r} is marked as curated, but {len(missing)} active exercises "
                f"have no translation (e.g. {', '.join(missing[:5])})",
                f"data/i18n/{code}/",
            )

    for code, bucket in data.translations.items():
        for exercise_id, translation in bucket.items():
            if exercise_id not in data.exercises:
                report.add(
                    "5",
                    ERROR,
                    f"Translation without corresponding exercise {exercise_id!r}",
                    relative(translation.path),
                )
            elif translation.data.get("exercise_id") != exercise_id:
                report.add(
                    "5",
                    ERROR,
                    f"exercise_id {translation.data.get('exercise_id')!r} does not match "
                    f"filename {exercise_id!r}",
                    relative(translation.path),
                )
            elif code != "en" and translation.data.get("status") == "ai_raw":
                en_translation = data.translations.get("en", {}).get(exercise_id)
                if en_translation:
                    en_name = (en_translation.name or "").strip().lower()
                    tr_name = (translation.name or "").strip().lower()
                    if tr_name and en_name and tr_name == en_name:
                        # Non-blocking, but visible as a warning in the QA gate
                        report.add(
                            "translation_identity",
                            WARNING,
                            f"Translated name ({code}) is identical to English name: {translation.name!r}",
                            relative(translation.path),
                            exercise_id,
                        )


def check_merges(data: dataset_mod.Dataset, report: Report) -> None:
    """Invariants 6 and 7: merges and alias chains."""
    alias_sources: dict[str, str] = {}
    for exercise in data.exercises.values():
        location = relative(exercise.path)
        if exercise.status == "merged":
            target = exercise.get("merged_into")
            if not target:
                report.add("6", ERROR, "status: merged without merged_into", location)
                continue
            target = str(target)
            if target not in data.exercises:
                report.add("6", ERROR, f"merged_into {target!r} does not exist", location)
            elif data.exercises[target].status != "active":
                report.add(
                    "6",
                    ERROR,
                    f"merged_into {target!r} is itself {data.exercises[target].status}",
                    location,
                )
            alias_sources[exercise.id] = target
        for old_id in exercise.get("aliases") or []:
            alias_sources[str(old_id)] = exercise.id

    for old_id, new_id in sorted(alias_sources.items()):
        if new_id in alias_sources:
            report.add(
                "7",
                ERROR,
                f"Alias chain: {old_id} -> {new_id} -> {alias_sources[new_id]}. "
                f"Both must point directly to {alias_sources[new_id]}.",
                relative(data.exercises[new_id].path) if new_id in data.exercises else None,
            )


def check_muscles(
    data: dataset_mod.Dataset, vocab: Vocabularies, report: Report, *, profile: str
) -> None:
    """Invariants 8 to 10."""
    muscles = vocab.muscles
    without_primary: list[str] = []

    for exercise in data.exercises.values():
        location = relative(exercise.path)
        entries = [entry for entry in exercise.muscles if isinstance(entry, dict)]
        node_ids = [str(entry["id"]) for entry in entries if "id" in entry]

        # 8 — at least one primary muscle (applies to active exercises)
        if exercise.status == "active" and not any(
            entry.get("role") == "primary" for entry in entries
        ):
            if profile == "full":
                report.add("8", ERROR, "no muscle with role: primary", location)
            else:
                without_primary.append(exercise.id)

        # 9 — no duplicate muscles, none in both roles
        roles: dict[str, set[str]] = defaultdict(set)
        for entry in entries:
            roles[str(entry.get("id"))].add(str(entry.get("role")))
        for node_id, node_roles in sorted(roles.items()):
            count = sum(1 for entry in entries if str(entry.get("id")) == node_id)
            if count > 1:
                report.add("9", ERROR, f"muscle {node_id!r} listed {count} times", location)
            if len(node_roles) > 1:
                report.add(
                    "9", ERROR, f"muscle {node_id!r} is both primary and secondary", location
                )

        # 10 — no node together with ancestor or descendant
        present = {node_id for node_id in node_ids if node_id in muscles}
        for node_id in sorted(present):
            redundant = sorted(present & set(muscles.ancestors(node_id)))
            for other in redundant:
                report.add(
                    "10",
                    ERROR,
                    f"{node_id!r} and its ancestor {other!r} are both listed — redundant",
                    location,
                )

    if without_primary:
        report.add(
            "8",
            WARNING,
            f"{len(without_primary)} exercises without a primary muscle. This is the baseline "
            f"state of the import and the main work of Phase 2 (SCHEMA.md §11), not a violation.",
            "data/exercises/",
        )
    report.stats["without_primary_muscle"] = len(without_primary)


def check_plausibility(data: dataset_mod.Dataset, vocab: Vocabularies, report: Report) -> None:
    """Invariants 11 to 18 (soft) as well as 24 and 25 (hard).

    All conditional: what is not present is not checked. As soon as Phase 2
    populates a field, the corresponding rule applies automatically for that
    specific exercise.

    Soft rules can be excused via `exceptions` — they describe what is standard,
    not what is strictly mandated. Hard rules cannot.
    """
    muscles = vocab.muscles

    for exercise in data.exercises.values():
        location = relative(exercise.path)
        eid = exercise.id
        equipment = exercise.get("primary_equipment")
        setup = list(exercise.get("setup") or [])
        modality = exercise.get("modality")
        mechanic = exercise.get("mechanic")
        tracking = exercise.get("tracking_type")
        load_mode = exercise.get("load_mode")
        pattern = exercise.get("movement_pattern")
        primary = exercise.muscle_ids("primary")
        entries = [entry for entry in exercise.muscles if isinstance(entry, dict)]

        # --- 11 (soft)
        if equipment == "bodyweight":
            for item in sorted(set(setup) & set(HEAVY_SETUP)):
                report.add(
                    "11",
                    ERROR,
                    f"primary_equipment: bodyweight, but setup contains {item!r}",
                    location,
                    eid,
                )
        # --- 12 (soft) — Burpees are cardio logged in repetitions.
        if modality == "cardio" and tracking and tracking not in CARDIO_TRACKING:
            report.add(
                "12",
                ERROR,
                f"modality: cardio requires tracking_type from {sorted(CARDIO_TRACKING)}, "
                f"got {tracking!r}",
                location,
                eid,
            )
        # --- 13 (soft)
        if modality == "strength" and tracking == "distance_only":
            report.add(
                "13", ERROR, "modality: strength with tracking_type: distance_only", location, eid
            )
        # --- 14 (soft)
        if mechanic == "isolation" and len(primary) > 2:
            report.add(
                "14",
                ERROR,
                f"mechanic: isolation with {len(primary)} primary muscles (at most 2)",
                location,
                eid,
            )
        # --- 15 (soft)
        if mechanic == "compound" and entries and len(entries) < 2:
            report.add(
                "15", ERROR, "mechanic: compound with only one involved muscle", location, eid
            )
        # --- 17 (hard)
        if (
            exercise.get("supports_added_weight")
            and tracking
            and tracking not in ADDED_WEIGHT_TRACKING
        ):
            report.add(
                "17",
                ERROR,
                f"supports_added_weight requires tracking_type from "
                f"{sorted(ADDED_WEIGHT_TRACKING)}, got {tracking!r}",
                location,
                eid,
            )
        # --- 24 (hard) — adding weight requires that the base form is bodyweight.
        if exercise.get("supports_added_weight") and load_mode and load_mode != "bodyweight":
            report.add(
                "24",
                ERROR,
                f"supports_added_weight requires load_mode: bodyweight, got {load_mode!r}",
                location,
                eid,
            )
        # --- 25 (hard) — assistance requires a machine or band.
        if load_mode == "assisted" and equipment and equipment not in ASSISTED_EQUIPMENT:
            report.add(
                "25",
                ERROR,
                f"load_mode: assisted requires primary_equipment from "
                f"{sorted(ASSISTED_EQUIPMENT)}, got {equipment!r}",
                location,
                eid,
            )
        # Muscle nodes must be resolvable, otherwise 10 and 20 fail silently.
        for node_id in primary:
            if node_id not in muscles:
                report.add("2", ERROR, f"muscles: unknown node {node_id!r}", location, eid)


def apply_exceptions(data: dataset_mod.Dataset, report: Report) -> None:
    """Evaluates `exceptions`: excuse, validate, count.

    Must run after all other checks — it does not decide whether something is a
    finding, but whether a finding is accounted for.

    Three rules, each with a reason:

    * An exception on a **hard** invariant is an error. Hard rules are
      structural; an exception would not be a special case, but a broken record
      with a note attached.
    * An exception **without a justification** is an error. The explanation is
      the entire point: it is what a reviewer reads a year from now.
    * An exception that **does not fire** is a warning. It was either never
      needed or its underlying issue was fixed — either way, it is now obsolete
      and misleads future readers.
    """
    declared: dict[tuple[str, str], str] = {}

    for exercise in data.exercises.values():
        location = relative(exercise.path)
        for key, reason in (exercise.get("exceptions") or {}).items():
            invariant = str(key)[len(EXCEPTION_PREFIX):] if str(key).startswith(
                EXCEPTION_PREFIX
            ) else None
            if invariant is None:
                report.add(
                    "exceptions",
                    ERROR,
                    f"{key!r} is not a valid key — expected "
                    f"`{EXCEPTION_PREFIX}<number>`",
                    location,
                    exercise.id,
                )
                continue
            if not isinstance(reason, str) or not reason.strip():
                report.add(
                    "exceptions",
                    ERROR,
                    f"Exception on invariant {invariant} without justification",
                    location,
                    exercise.id,
                )
                continue
            if invariant in HARD_INVARIANTS:
                report.add(
                    "exceptions",
                    ERROR,
                    f"Invariant {invariant} is hard and cannot be excused. Hard rules "
                    f"are structural — an exception would be a broken record with "
                    f"a note attached.",
                    location,
                    exercise.id,
                )
                continue
            if invariant not in SOFT_INVARIANTS:
                report.add(
                    "exceptions",
                    ERROR,
                    f"Invariant {invariant} does not exist",
                    location,
                    exercise.id,
                )
                continue
            declared[(exercise.id, invariant)] = reason.strip()

    fired: dict[str, int] = {}
    excused: dict[str, int] = {}
    used: set[tuple[str, str]] = set()

    for finding in report.findings:
        if finding.invariant not in SOFT_INVARIANTS:
            continue
        fired[finding.invariant] = fired.get(finding.invariant, 0) + 1
        key = (finding.exercise_id or "", finding.invariant)
        reason = declared.get(key)
        if reason is not None:
            finding.excused = reason
            excused[finding.invariant] = excused.get(finding.invariant, 0) + 1
            used.add(key)

    for (exercise_id, invariant), reason in sorted(declared.items()):
        if (exercise_id, invariant) in used:
            continue
        exercise = data.exercises.get(exercise_id)
        report.add(
            "exceptions",
            WARNING,
            f"Exception on invariant {invariant} does not take effect — the rule does not "
            f"fire here. Either it was never needed or its cause was resolved; either way "
            f"it should be removed. ({reason[:60]})",
            relative(exercise.path) if exercise else None,
            exercise_id,
        )

    report.stats["soft_invariants"] = {
        invariant: {
            "fired": fired.get(invariant, 0),
            "excused": excused.get(invariant, 0),
            "open": fired.get(invariant, 0) - excused.get(invariant, 0),
        }
        for invariant in sorted(SOFT_INVARIANTS, key=_invariant_key)
        if fired.get(invariant, 0)
    }


def check_pattern_expectations(
    data: dataset_mod.Dataset, vocab: Vocabularies, report: Report
) -> None:
    """Invariant 20: Primary muscle group matches `movement_pattern`.

    Warning, not an error — exceptions exist, but each should be inspected.
    """
    table_path = VOCAB_DIR / "pattern_muscle_expectations.yaml"
    if not table_path.exists():
        report.skip(
            "20",
            f"{relative(table_path)} does not exist yet. The table requires "
            "movement_pattern and belongs to Phase 2.",
        )
        return

    expectations = yamlio.read(table_path).get("expectations") or {}
    for exercise in data.exercises.values():
        pattern = exercise.get("movement_pattern")
        if not pattern or pattern == "other":
            continue
        expected = expectations.get(pattern)
        if not expected:
            continue
        groups = {
            vocab.muscles[node].group_id
            for node in exercise.muscle_ids("primary")
            if node in vocab.muscles
        }
        if groups and not groups.issubset(set(expected)):
            unexpected = sorted(groups - set(expected))
            report.add(
                "20",
                WARNING,
                f"movement_pattern {pattern!r} expects primary muscles from {sorted(expected)}, "
                f"unexpected group(s): {unexpected}",
                relative(exercise.path),
                exercise.id,
            )


def check_published_ids(data: dataset_mod.Dataset, report: Report) -> None:
    """Invariant 21: no previously published ID may disappear.

    Validated against `data/published_ids.yaml`, **not** against the previous
    release. The difference is the point: comparing with the predecessor has a
    ratchet effect. If a deletion slips through once, the ID vanishes from the
    baseline and becomes permanently invisible — every subsequent diff correctly
    reports "zero removals".

    This is precisely how 38 exercises were lost: they were present in the
    published dataset from 2026-06-15 (852 IDs), missing from the 2026-08-31
    release (862), and untraceable from that point on. A repository registry
    prevents this.
    """
    if not PUBLISHED_IDS.exists():
        report.skip(
            "21",
            f"{relative(PUBLISHED_IDS)} does not exist yet. Create with "
            f"`build/update_published_ids.py --from-db <published.db>`.",
        )
        return

    registry = (yamlio.read(PUBLISHED_IDS) or {}).get("ids") or {}
    missing = sorted((str(key) for key in registry if str(key) not in data.exercises), key=str)
    for exercise_id in missing:
        report.add(
            "21",
            ERROR,
            f"Exercise {exercise_id} was previously published, but is missing from data/exercises/. "
            f"Deletion is prohibited (SCHEMA.md §3) — restore it with status: deprecated.",
            relative(PUBLISHED_IDS),
        )
    report.stats["published_ids"] = len(registry)
    report.stats["deprecated"] = sum(
        1 for exercise in data.exercises.values() if exercise.status == "deprecated"
    )
    report.stats["merged"] = sum(
        1 for exercise in data.exercises.values() if exercise.status == "merged"
    )

    # The second part of 21: a `merged` entry needs a resolvable target — checked
    # by check_merges. Here the question is whether a silenced entry still has any
    # text, otherwise the app displays a blank row.
    for exercise in data.exercises.values():
        if exercise.status == "active":
            continue
        if not any(exercise.id in bucket for bucket in data.translations.values()):
            report.add(
                "21",
                ERROR,
                f"{exercise.status} entry without any text — the app would have nothing to display",
                relative(exercise.path),
            )


def check_regression(report: Report) -> None:
    """Invariant 22 requires two databases; 19 is structurally fulfilled."""
    report.skip(
        "19",
        "structurally fulfilled: force_vector is not annotated, but derived from "
        "movement_pattern (vocab/classification.yaml). A violation cannot be formulated.",
    )
    report.skip(
        "22",
        "set comparison of two releases — runs in build/catalog_diff.py "
        "(INVARIANT_22_ACTIVE_COUNT_DROP), not here.",
    )


def check_golden_set(data: dataset_mod.Dataset, report: Report) -> None:
    """Invariant 23: golden set matches field-by-field."""
    golden = sorted(GOLDEN_DIR.glob("*.yaml"))
    if not golden:
        report.skip(
            "23",
            f"{relative(GOLDEN_DIR)} is empty. The golden set is established at the start of Phase 2 "
            "and can only be validated then.",
        )
        return

    for path in golden:
        expected = yamlio.read(path)
        exercise_id = str(expected.get("id", path.stem))
        actual = data.exercises.get(exercise_id)
        if actual is None:
            report.add("23", ERROR, f"Golden entry {exercise_id!r} missing from data/", relative(path))
            continue
        for key, value in expected.items():
            if key == "provenance":
                continue  # Provenance changes legitimately, content does not.
            if actual.data.get(key) != value:
                report.add(
                    "23",
                    ERROR,
                    f"{key}: expected {value!r}, got {actual.data.get(key)!r}",
                    relative(path),
                )


# ------------------------------------------------------------------- reporting


def summarize(report: Report, data: dataset_mod.Dataset) -> None:
    report.stats.update(
        {
            "exercises": len(data.exercises),
            "active": sum(1 for _ in data.active()),
            "languages": len(data.translations),
            "translations": sum(len(bucket) for bucket in data.translations.values()),
        }
    )


def print_report(report: Report, limit: int) -> None:
    by_invariant: dict[str, list[Finding]] = defaultdict(list)
    for finding in report.open_findings:
        by_invariant[finding.invariant].append(finding)

    stats = report.stats
    print(f"Profile    {report.profile}")
    print(
        f"Inventory  {stats.get('exercises', 0)} exercises ({stats.get('active', 0)} active), "
        f"{stats.get('translations', 0)} translations in {stats.get('languages', 0)} languages"
    )
    print()

    for invariant in sorted(by_invariant, key=_invariant_key):
        findings = by_invariant[invariant]
        errors = sum(1 for f in findings if f.severity == ERROR)
        warnings = len(findings) - errors
        label = f"Invariant {invariant}"
        if invariant in SOFT_INVARIANTS:
            label += " (soft)"
        elif invariant == "exceptions":
            label = "Exceptions"
        marker = "ERROR  " if errors else "WARNING"
        print(f"{marker} {label}: {errors} errors, {warnings} warnings")
        for finding in findings[:limit]:
            where = f"  [{finding.location}]" if finding.location else ""
            print(f"        {finding.message}{where}")
        if len(findings) > limit:
            print(f"        ... and {len(findings) - limit} more")
        print()

    soft = report.stats.get("soft_invariants") or {}
    if soft:
        # Clustering is a signal that the rule is wrong, not the data.
        print("Soft invariants:")
        print(f"  {'Rule':<8} {'fired':>9} {'excused':>12} {'open':>7}")
        for invariant, counts in soft.items():
            print(
                f"  {invariant:<8} {counts['fired']:>9} {counts['excused']:>12} "
                f"{counts['open']:>7}"
            )
        loud = [i for i, c in soft.items() if c["excused"] >= 5]
        if loud:
            print(
                f"  Frequently excused: {', '.join(loud)}. This signals that the "
                f"rule is incorrect rather than the data."
            )
        print()

    if report.skipped:
        print("Skipped:")
        for invariant in sorted(report.skipped, key=_invariant_key):
            print(f"  {invariant}: {report.skipped[invariant]}")
        print()

    print(f"Result     {len(report.errors)} errors, {len(report.warnings)} warnings")


def _invariant_key(value: str) -> tuple[int, str]:
    digits = "".join(ch for ch in value if ch.isdigit())
    return (int(digits) if digits else 0, value)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--profile",
        choices=("phase1", "full"),
        default="phase1",
        help="phase1: content rules only where fields exist. full: everything strictly enforced.",
    )
    parser.add_argument("--json-out", help="Path for the machine-readable report JSON")
    parser.add_argument(
        "--examples", type=int, default=10, help="Findings per invariant in the console (default: 10)"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Warnings also cause exit code 1.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    vocab = Vocabularies()
    data = dataset_mod.load()
    report = Report(profile=args.profile)

    check_schemas(data, report, profile=args.profile)
    check_vocabulary(data, vocab, report)
    check_identity(data, report)
    check_vocab_id_uniqueness(vocab, report)
    check_translation_coverage(data, vocab, report, profile=args.profile)
    check_merges(data, report)
    check_muscles(data, vocab, report, profile=args.profile)
    check_plausibility(data, vocab, report)
    check_pattern_expectations(data, vocab, report)
    check_published_ids(data, report)
    check_regression(report)
    # Lastly: does not decide if something is a finding, but whether it is explained.
    apply_exceptions(data, report)
    check_golden_set(data, report)
    summarize(report, data)

    print_report(report, args.examples)

    if args.json_out:
        out = Path(args.json_out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            json.dumps(
                {
                    "profile": report.profile,
                    "stats": report.stats,
                    "error_count": len(report.errors),
                    "warning_count": len(report.warnings),
                    "skipped": report.skipped,
                    "soft_invariants": report.stats.get("soft_invariants", {}),
                    "findings": [f.as_dict() for f in report.findings],
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        print(f"Report     {out}")

    if report.errors:
        return 1
    if args.strict and report.warnings:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

