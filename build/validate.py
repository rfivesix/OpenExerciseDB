#!/usr/bin/env python3
"""Prueft die Invarianten aus `schema/invariants.md`. Das CI-Gate.

Die Invarianten sind der eigentliche Qualitaetsmechanismus dieses Repos: sie
fangen den mechanischen Teil der Fehler automatisch ab, damit der menschliche
Review sich auf das konzentriert, was eine Maschine nicht entscheiden kann.

**Zwei Profile.** In Phase 1 existieren die Klassifikationsfelder noch gar
nicht — wger liefert sie nicht, und sie zu raten waere schlimmer als sie
wegzulassen (SCHEMA.md 11). Ein Regelwerk, das deshalb dauerhaft rot steht, wird
nach einer Woche ignoriert und ist damit wertlos. Also:

    --profile phase1   Struktur und Vokabular scharf; die inhaltlichen Regeln
                       greifen ueberall dort, wo die Felder vorhanden sind, und
                       schweigen, wo sie es noch nicht sind.
    --profile full     alles scharf. Das Ziel am Ende von Phase 2 — und der
                       Beleg dafuer, dass Phase 2 fertig ist.

Was in Phase 1 fehlt, ist damit kein stiller blinder Fleck, sondern eine Zahl im
Bericht: `--profile full` sagt jederzeit, wie weit es noch ist.

Aufruf:

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
"""Strukturell und referenziell: eine ID zeigt ins Leere, ein Vokabularwert
existiert nicht, ein Muskel steht zweimal da. Keine legitimen Ausnahmen."""

SOFT_INVARIANTS = {"11", "12", "13", "14", "15", "20"}
"""Plausibilitaet — Korrelationen, keine Gesetze.

Cardio wird nicht in Wiederholungen geloggt, ausser bei Burpees. Der Schaden
einer zu strengen Regel ist nicht der Fehlalarm — der ist sichtbar —, sondern
die still verbogene Annotation, die ihn vermeidet. Deshalb sind diese Regeln
pro Uebung entschaerfbar, mit Begruendung im Klartext."""

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
"""Felder, die wger nicht liefert und die Phase 1 deshalb leer laesst.

Im Profil `phase1` werden sie aus `required` des JSON-Schemas herausgenommen.
Ueberall sonst gilt: ist das Feld da, wird es voll geprueft."""

HEAVY_SETUP = ("squat_rack", "power_rack", "cable_tower", "landmine")
"""Invariante 11: mit reinem Koerpergewicht unvereinbares Setup."""

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
    """Begruendung, falls der Befund per `exceptions` entschaerft wurde."""

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
        """Alles, was nicht per Ausnahme entschaerft wurde."""
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
    """YAML-Werte in das ueberfuehren, was JSON Schema erwartet.

    YAML liest `at: 2026-09-02` als `datetime.date`, das Schema erwartet dort
    einen String mit `format: date`. Beide Schreibweisen sind fuer einen
    Beitragenden voellig gleichwertig — ein Validator, der die eine ablehnt
    (und zwar genau die, die in `examples/` steht), erzieht niemanden, er
    aergert nur.
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
    """Invariante 1: jede Datei validiert gegen ihr JSON-Schema."""
    try:
        import jsonschema
    except ImportError:
        report.skip("1", "jsonschema ist nicht installiert (pip install -r requirements.txt)")
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

    # 1c — die Beispieldatei ist Dokumentation und wird abgeschrieben. Sie wird
    # immer gegen das VOLLE Schema geprueft, auch im Profil phase1: ein Beispiel,
    # das nicht validiert, schickt jeden Beitragenden in denselben Fehler.
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
    """Invariante 2: jeder klassifizierende Wert steht in einer vocab/*.yaml."""
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
                report.add("2", ERROR, f"{field_name}: unbekannter Wert {value!r}", location)
        for tag in exercise.get("usage_tags") or []:
            if tag not in usage_tags:
                report.add("2", ERROR, f"usage_tags: unbekannter Wert {tag!r}", location)
        for item in exercise.get("setup") or []:
            if item not in setup_values:
                report.add("2", ERROR, f"setup: unbekannter Wert {item!r}", location)
        for entry in exercise.muscles:
            node = entry.get("id") if isinstance(entry, dict) else None
            if node is not None and node not in vocab.muscles:
                report.add("2", ERROR, f"muscles: unbekannter Knoten {node!r}", location)
        license_id = (exercise.upstream or {}).get("license")
        if license_id is not None and license_id not in licenses:
            report.add("2", ERROR, f"upstream.license: unbekannt {license_id!r}", location)

    for language, bucket in data.translations.items():
        if language not in vocab.languages:
            report.add(
                "2",
                ERROR,
                f"Sprache {language!r} ist nicht in vocab/languages.yaml registriert",
                f"data/i18n/{language}/",
            )
            continue
        for translation in bucket.values():
            location = relative(translation.path)
            if translation.data.get("language") != language:
                report.add(
                    "2",
                    ERROR,
                    f"language: {translation.data.get('language')!r} passt nicht zum Verzeichnis "
                    f"{language!r}",
                    location,
                )
            license_id = (translation.upstream or {}).get("license")
            if license_id is not None and license_id not in licenses:
                report.add("2", ERROR, f"upstream.license: unbekannt {license_id!r}", location)


def check_identity(data: dataset_mod.Dataset, report: Report) -> None:
    """Invariante 3: `id` und `slug` sind global eindeutig."""
    for exercise_id, path in data.duplicate_ids:
        report.add("3", ERROR, f"doppelte oder unlesbare Uebung {exercise_id!r}", path)

    slugs: dict[str, str] = {}
    for exercise in data.exercises.values():
        location = relative(exercise.path)
        if exercise.id != exercise.path.stem:
            report.add(
                "3", ERROR, f"id {exercise.id!r} passt nicht zum Dateinamen", location
            )
        if not exercise.slug:
            report.add("3", ERROR, "slug fehlt", location)
            continue
        if exercise.slug in slugs:
            report.add(
                "3",
                ERROR,
                f"slug {exercise.slug!r} ist schon von Uebung {slugs[exercise.slug]} belegt",
                location,
            )
        else:
            slugs[exercise.slug] = exercise.id


def check_vocab_id_uniqueness(vocab: Vocabularies, report: Report) -> None:
    """Invariante 3b: IDs sind innerhalb eines Vokabulars ebenenuebergreifend
    eindeutig — Gruppe, Muskel und Kopf teilen sich im Build eine Tabelle mit
    einem Primaerschluessel."""
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

    # Dieselbe Falle eine Ebene tiefer: das Legacy-Mapping darf nur auf Knoten
    # zeigen, die es auch gibt.
    for raw_name, node in vocab.muscles.legacy_wger_mapping.items():
        if node not in vocab.muscles:
            report.add(
                "3b",
                ERROR,
                f"legacy_wger_mapping: {raw_name!r} zeigt auf unbekannten Knoten {node!r}",
                "vocab/muscles.yaml",
            )


def _claim(seen: dict[str, str], key: str, level: str, report: Report, location: str) -> None:
    if key in seen:
        report.add("3b", ERROR, f"ID {key!r} doppelt ({seen[key]} und {level})", location)
    else:
        seen[key] = level


def check_translation_coverage(
    data: dataset_mod.Dataset, vocab: Vocabularies, report: Report, *, profile: str
) -> None:
    """Invarianten 4 und 5: Vollstaendigkeit und Gegenstueck."""
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
                f"Sprache {code!r} ist als curated markiert, aber {len(missing)} aktive Uebungen "
                f"haben keinen Text (z. B. {', '.join(missing[:5])})",
                f"data/i18n/{code}/",
            )

    for code, bucket in data.translations.items():
        for exercise_id, translation in bucket.items():
            if exercise_id not in data.exercises:
                report.add(
                    "5",
                    ERROR,
                    f"Text ohne zugehoerige Uebung {exercise_id!r}",
                    relative(translation.path),
                )
            elif translation.data.get("exercise_id") != exercise_id:
                report.add(
                    "5",
                    ERROR,
                    f"exercise_id {translation.data.get('exercise_id')!r} passt nicht zum "
                    f"Dateinamen {exercise_id!r}",
                    relative(translation.path),
                )
            elif code != "en" and translation.data.get("status") == "ai_raw":
                en_translation = data.translations.get("en", {}).get(exercise_id)
                if en_translation:
                    en_name = (en_translation.name or "").strip().lower()
                    tr_name = (translation.name or "").strip().lower()
                    if tr_name and en_name and tr_name == en_name:
                        # Nicht blockierend, aber als Warnliste im QA-Gate sichtbar
                        report.add(
                            "translation_identity",
                            WARNING,
                            f"Uebersetzter Name ({code}) ist identisch zum englischen Namen: {translation.name!r}",
                            relative(translation.path),
                            exercise_id,
                        )


def check_merges(data: dataset_mod.Dataset, report: Report) -> None:
    """Invarianten 6 und 7: Zusammenlegungen und Alias-Ketten."""
    alias_sources: dict[str, str] = {}
    for exercise in data.exercises.values():
        location = relative(exercise.path)
        if exercise.status == "merged":
            target = exercise.get("merged_into")
            if not target:
                report.add("6", ERROR, "status: merged ohne merged_into", location)
                continue
            target = str(target)
            if target not in data.exercises:
                report.add("6", ERROR, f"merged_into {target!r} existiert nicht", location)
            elif data.exercises[target].status != "active":
                report.add(
                    "6",
                    ERROR,
                    f"merged_into {target!r} ist selbst {data.exercises[target].status}",
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
                f"Alias-Kette: {old_id} -> {new_id} -> {alias_sources[new_id]}. "
                f"Beide muessen direkt auf {alias_sources[new_id]} zeigen.",
                relative(data.exercises[new_id].path) if new_id in data.exercises else None,
            )


def check_muscles(
    data: dataset_mod.Dataset, vocab: Vocabularies, report: Report, *, profile: str
) -> None:
    """Invarianten 8 bis 10."""
    muscles = vocab.muscles
    without_primary: list[str] = []

    for exercise in data.exercises.values():
        location = relative(exercise.path)
        entries = [entry for entry in exercise.muscles if isinstance(entry, dict)]
        node_ids = [str(entry["id"]) for entry in entries if "id" in entry]

        # 8 — mindestens ein primaerer Muskel (gilt fuer aktive Uebungen)
        if exercise.status == "active" and not any(
            entry.get("role") == "primary" for entry in entries
        ):
            if profile == "full":
                report.add("8", ERROR, "kein Muskel mit role: primary", location)
            else:
                without_primary.append(exercise.id)

        # 9 — kein Muskel doppelt, keiner in beiden Rollen
        roles: dict[str, set[str]] = defaultdict(set)
        for entry in entries:
            roles[str(entry.get("id"))].add(str(entry.get("role")))
        for node_id, node_roles in sorted(roles.items()):
            count = sum(1 for entry in entries if str(entry.get("id")) == node_id)
            if count > 1:
                report.add("9", ERROR, f"Muskel {node_id!r} {count}-mal genannt", location)
            if len(node_roles) > 1:
                report.add(
                    "9", ERROR, f"Muskel {node_id!r} ist primary und secondary", location
                )

        # 10 — kein Knoten zusammen mit Vorfahr oder Nachfahr
        present = {node_id for node_id in node_ids if node_id in muscles}
        for node_id in sorted(present):
            redundant = sorted(present & set(muscles.ancestors(node_id)))
            for other in redundant:
                report.add(
                    "10",
                    ERROR,
                    f"{node_id!r} und sein Vorfahr {other!r} sind beide genannt — redundant",
                    location,
                )

    if without_primary:
        report.add(
            "8",
            WARNING,
            f"{len(without_primary)} Uebungen ohne primaeren Muskel. Das ist die Ausgangslage "
            f"des Imports und die Hauptarbeit von Phase 2 (SCHEMA.md 11), kein Regelbruch.",
            "data/exercises/",
        )
    report.stats["without_primary_muscle"] = len(without_primary)


def check_plausibility(data: dataset_mod.Dataset, vocab: Vocabularies, report: Report) -> None:
    """Invarianten 11 bis 18 (weich) sowie 24 und 25 (hart).

    Alle konditional: was nicht da ist, wird nicht geprueft. Sobald Phase 2 ein
    Feld befuellt, greift die zugehoerige Regel automatisch fuer genau diese
    Uebung.

    Die weichen Regeln sind ueber `exceptions` entschaerfbar — sie beschreiben,
    was ueblich ist, nicht was gelten muss. Die harten nicht.
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

        # --- 11 (weich)
        if equipment == "bodyweight":
            for item in sorted(set(setup) & set(HEAVY_SETUP)):
                report.add(
                    "11",
                    ERROR,
                    f"primary_equipment: bodyweight, aber setup enthaelt {item!r}",
                    location,
                    eid,
                )
        # --- 12 (weich) — Burpees sind Cardio in Wiederholungen.
        if modality == "cardio" and tracking and tracking not in CARDIO_TRACKING:
            report.add(
                "12",
                ERROR,
                f"modality: cardio verlangt tracking_type aus {sorted(CARDIO_TRACKING)}, "
                f"ist {tracking!r}",
                location,
                eid,
            )
        # --- 13 (weich)
        if modality == "strength" and tracking == "distance_only":
            report.add(
                "13", ERROR, "modality: strength mit tracking_type: distance_only", location, eid
            )
        # --- 14 (weich)
        if mechanic == "isolation" and len(primary) > 2:
            report.add(
                "14",
                ERROR,
                f"mechanic: isolation mit {len(primary)} primaeren Muskeln (hoechstens 2)",
                location,
                eid,
            )
        # --- 15 (weich)
        if mechanic == "compound" and entries and len(entries) < 2:
            report.add(
                "15", ERROR, "mechanic: compound mit nur einem beteiligten Muskel", location, eid
            )
        # --- 17 (hart)
        if (
            exercise.get("supports_added_weight")
            and tracking
            and tracking not in ADDED_WEIGHT_TRACKING
        ):
            report.add(
                "17",
                ERROR,
                f"supports_added_weight verlangt tracking_type aus "
                f"{sorted(ADDED_WEIGHT_TRACKING)}, ist {tracking!r}",
                location,
                eid,
            )
        # --- 24 (hart) — etwas dazuzuladen setzt voraus, dass die Grundform das
        # eigene Koerpergewicht ist.
        if exercise.get("supports_added_weight") and load_mode and load_mode != "bodyweight":
            report.add(
                "24",
                ERROR,
                f"supports_added_weight verlangt load_mode: bodyweight, ist {load_mode!r}",
                location,
                eid,
            )
        # --- 25 (hart) — Entlastung erzeugt eine Maschine oder ein Band.
        if load_mode == "assisted" and equipment and equipment not in ASSISTED_EQUIPMENT:
            report.add(
                "25",
                ERROR,
                f"load_mode: assisted verlangt primary_equipment aus "
                f"{sorted(ASSISTED_EQUIPMENT)}, ist {equipment!r}",
                location,
                eid,
            )
        # Muskelknoten muessen aufloesbar sein, sonst laufen 10 und 20 ins Leere.
        for node_id in primary:
            if node_id not in muscles:
                report.add("2", ERROR, f"muscles: unbekannter Knoten {node_id!r}", location, eid)


def apply_exceptions(data: dataset_mod.Dataset, report: Report) -> None:
    """Wertet `exceptions` aus: entschaerfen, pruefen, zaehlen.

    Muss nach allen anderen Pruefungen laufen — sie entscheidet nicht, ob etwas
    ein Befund ist, sondern ob ein Befund erklaert ist.

    Drei Regeln, jede mit einem Grund:

    * Eine Ausnahme auf eine **harte** Invariante ist ein Fehler. Harte Regeln
      sind strukturell; eine Ausnahme davon waere kein Sonderfall, sondern ein
      kaputter Datensatz mit Zettel dran.
    * Eine Ausnahme **ohne Begruendung** ist ein Fehler. Der Text ist der ganze
      Zweck: er ist das, was ein Reviewer in einem Jahr liest.
    * Eine Ausnahme, die **nicht greift**, ist eine Warnung. Sie wurde entweder
      nie gebraucht oder ihr Anlass ist behoben — so oder so ist sie ab jetzt
      eine Karteileiche, die den naechsten Leser in die Irre schickt.
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
                    f"{key!r} ist kein gueltiger Schluessel — erwartet "
                    f"`{EXCEPTION_PREFIX}<nummer>`",
                    location,
                    exercise.id,
                )
                continue
            if not isinstance(reason, str) or not reason.strip():
                report.add(
                    "exceptions",
                    ERROR,
                    f"Ausnahme auf Invariante {invariant} ohne Begruendung",
                    location,
                    exercise.id,
                )
                continue
            if invariant in HARD_INVARIANTS:
                report.add(
                    "exceptions",
                    ERROR,
                    f"Invariante {invariant} ist hart und nicht entschaerfbar. Harte Regeln "
                    f"sind strukturell — eine Ausnahme waere ein kaputter Datensatz mit "
                    f"Zettel dran.",
                    location,
                    exercise.id,
                )
                continue
            if invariant not in SOFT_INVARIANTS:
                report.add(
                    "exceptions",
                    ERROR,
                    f"Invariante {invariant} gibt es nicht",
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
            f"Ausnahme auf Invariante {invariant} greift nicht — die Regel feuert hier gar "
            f"nicht. Entweder wurde sie nie gebraucht oder ihr Anlass ist behoben; so oder "
            f"so gehoert sie geloescht. ({reason[:60]})",
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
    """Invariante 20: Primaermuskel-Gruppe passt zum `movement_pattern`.

    Warnung, kein Fehler — Ausnahmen existieren, aber jede will einmal
    angeschaut werden.
    """
    table_path = VOCAB_DIR / "pattern_muscle_expectations.yaml"
    if not table_path.exists():
        report.skip(
            "20",
            f"{relative(table_path)} existiert noch nicht. Die Tabelle setzt "
            "movement_pattern voraus und gehoert damit zu Phase 2.",
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
                f"movement_pattern {pattern!r} erwartet Primaermuskeln aus {sorted(expected)}, "
                f"unerwartete Gruppe(n): {unexpected}",
                relative(exercise.path),
                exercise.id,
            )


def check_published_ids(data: dataset_mod.Dataset, report: Report) -> None:
    """Invariante 21: keine je ausgelieferte ID verschwindet.

    Geprueft wird gegen `data/published_ids.yaml`, **nicht** gegen das vorige
    Release. Der Unterschied ist der Punkt: ein Vergleich mit dem Vorgaenger hat
    eine Ratsche. Rutscht ein Verlust einmal durch, ist die ID aus der Baseline
    verschwunden und danach fuer immer unsichtbar — jeder folgende Diff meldet
    voellig korrekt "null Entfernungen".

    Genau so sind 38 Uebungen verlorengegangen: sie standen im ausgelieferten
    Stand vom 2026-06-15 (852 IDs), fehlten im Release vom 2026-08-31 (862) und
    waren ab da nicht mehr nachweisbar. Ein Register im Repo kann das nicht
    passieren.
    """
    if not PUBLISHED_IDS.exists():
        report.skip(
            "21",
            f"{relative(PUBLISHED_IDS)} existiert noch nicht. Anlegen mit "
            f"`build/update_published_ids.py --from-db <ausgelieferte.db>`.",
        )
        return

    registry = (yamlio.read(PUBLISHED_IDS) or {}).get("ids") or {}
    missing = sorted((str(key) for key in registry if str(key) not in data.exercises), key=str)
    for exercise_id in missing:
        report.add(
            "21",
            ERROR,
            f"Uebung {exercise_id} wurde einmal ausgeliefert, fehlt aber in data/exercises/. "
            f"Loeschen ist verboten (SCHEMA.md 3) — sie gehoert als status: deprecated zurueck.",
            relative(PUBLISHED_IDS),
        )
    report.stats["published_ids"] = len(registry)
    report.stats["deprecated"] = sum(
        1 for exercise in data.exercises.values() if exercise.status == "deprecated"
    )
    report.stats["merged"] = sum(
        1 for exercise in data.exercises.values() if exercise.status == "merged"
    )

    # Der zweite Teil von 21: ein `merged` braucht ein auflösbares Ziel — das
    # prueft check_merges. Hier bleibt die Frage, ob ein stillgelegter Eintrag
    # ueberhaupt noch Text hat, sonst zeigt die App eine leere Zeile.
    for exercise in data.exercises.values():
        if exercise.status == "active":
            continue
        if not any(exercise.id in bucket for bucket in data.translations.values()):
            report.add(
                "21",
                ERROR,
                f"{exercise.status}-Eintrag ohne jeden Text — die App haette nichts anzuzeigen",
                relative(exercise.path),
            )


def check_regression(report: Report) -> None:
    """Invariante 22 braucht zwei Datenbanken; 19 ist strukturell erfuellt."""
    report.skip(
        "19",
        "strukturell erfuellt: force_vector wird nicht annotiert, sondern aus "
        "movement_pattern abgeleitet (vocab/classification.yaml). Ein Verstoss "
        "ist nicht mehr formulierbar.",
    )
    report.skip(
        "22",
        "Mengenvergleich zweier Releases — laeuft in build/catalog_diff.py "
        "(INVARIANT_22_ACTIVE_COUNT_DROP), nicht hier.",
    )


def check_golden_set(data: dataset_mod.Dataset, report: Report) -> None:
    """Invariante 23: das Golden Set stimmt feldweise."""
    golden = sorted(GOLDEN_DIR.glob("*.yaml"))
    if not golden:
        report.skip(
            "23",
            f"{relative(GOLDEN_DIR)} ist leer. Das Golden Set wird zu Beginn von Phase 2 "
            "aufgebaut und ist erst dann pruefbar.",
        )
        return

    for path in golden:
        expected = yamlio.read(path)
        exercise_id = str(expected.get("id", path.stem))
        actual = data.exercises.get(exercise_id)
        if actual is None:
            report.add("23", ERROR, f"Golden-Eintrag {exercise_id!r} fehlt in data/", relative(path))
            continue
        for key, value in expected.items():
            if key == "provenance":
                continue  # Herkunft aendert sich legitim, der Inhalt nicht.
            if actual.data.get(key) != value:
                report.add(
                    "23",
                    ERROR,
                    f"{key}: erwartet {value!r}, gefunden {actual.data.get(key)!r}",
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
    print(f"Profil     {report.profile}")
    print(
        f"Bestand    {stats.get('exercises', 0)} Uebungen ({stats.get('active', 0)} aktiv), "
        f"{stats.get('translations', 0)} Texte in {stats.get('languages', 0)} Sprachen"
    )
    print()

    for invariant in sorted(by_invariant, key=_invariant_key):
        findings = by_invariant[invariant]
        errors = sum(1 for f in findings if f.severity == ERROR)
        warnings = len(findings) - errors
        label = f"Invariante {invariant}"
        if invariant in SOFT_INVARIANTS:
            label += " (weich)"
        elif invariant == "exceptions":
            label = "Ausnahmen"
        marker = "FEHLER " if errors else "WARNUNG"
        print(f"{marker} {label}: {errors} Fehler, {warnings} Warnungen")
        for finding in findings[:limit]:
            where = f"  [{finding.location}]" if finding.location else ""
            print(f"        {finding.message}{where}")
        if len(findings) > limit:
            print(f"        ... und {len(findings) - limit} weitere")
        print()

    soft = report.stats.get("soft_invariants") or {}
    if soft:
        # Haeufung ist ein Signal, dass die Regel falsch ist und nicht die Daten.
        print("Weiche Invarianten:")
        print(f"  {'Regel':<8} {'gefeuert':>9} {'entschaerft':>12} {'offen':>7}")
        for invariant, counts in soft.items():
            print(
                f"  {invariant:<8} {counts['fired']:>9} {counts['excused']:>12} "
                f"{counts['open']:>7}"
            )
        loud = [i for i, c in soft.items() if c["excused"] >= 5]
        if loud:
            print(
                f"  Haeufig entschaerft: {', '.join(loud)}. Das ist ein Signal, dass die "
                f"Regel falsch ist und nicht die Daten."
            )
        print()

    if report.skipped:
        print("Uebersprungen:")
        for invariant in sorted(report.skipped, key=_invariant_key):
            print(f"  {invariant}: {report.skipped[invariant]}")
        print()

    print(f"Ergebnis   {len(report.errors)} Fehler, {len(report.warnings)} Warnungen")


def _invariant_key(value: str) -> tuple[int, str]:
    digits = "".join(ch for ch in value if ch.isdigit())
    return (int(digits) if digits else 0, value)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--profile",
        choices=("phase1", "full"),
        default="phase1",
        help="phase1: inhaltliche Regeln nur wo die Felder existieren. full: alles scharf.",
    )
    parser.add_argument("--json-out", help="Pfad fuer den maschinenlesbaren Bericht")
    parser.add_argument(
        "--examples", type=int, default=10, help="Befunde je Invariante in der Konsole (Default: 10)"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Auch Warnungen fuehren zu Exitcode 1.",
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
    # Zuletzt: entscheidet nicht, ob etwas ein Befund ist, sondern ob er erklaert ist.
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
        print(f"Bericht    {out}")

    if report.errors:
        return 1
    if args.strict and report.warnings:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
