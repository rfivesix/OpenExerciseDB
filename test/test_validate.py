#!/usr/bin/env python3
"""Tests the validator against deliberately malformed data.

A ruleset that never triggers is indistinguishable from a ruleset that does not
run. Each invariant is provided a test case designed to trigger it — and the
catalog in the repository serves as counter-proof that it does not fire without reason.
"""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import support
from oedb import dataset as dataset_mod
from oedb import yamlio
from oedb.vocab import Vocabularies

validate = support.load_script("build/validate.py")

MINIMAL = {
    "id": "1",
    "slug": "some-exercise",
    "status": "active",
    "muscles": [{"id": "latissimus_dorsi", "role": "primary"}],
    "upstream": {"source": "wger", "license": "CC-BY-SA-4.0"},
}

MINIMAL_TEXT = {
    "exercise_id": "1",
    "language": "en",
    "status": "human",
    "name": "Some exercise",
    "upstream": {"license": "CC-BY-SA-4.0"},
}


class ValidatorTestCase(unittest.TestCase):
    """Writes fixtures to a temporary data/ directory and runs the validator."""

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.exercises_dir = self.root / "exercises"
        self.i18n_dir = self.root / "i18n"
        self.exercises_dir.mkdir(parents=True)
        self.i18n_dir.mkdir(parents=True)
        self.vocab = Vocabularies()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def write_exercise(self, **overrides) -> None:
        document = {**MINIMAL, **overrides}
        yamlio.write(self.exercises_dir / f"{document['id']}.yaml", document)

    def write_text(self, language: str = "en", **overrides) -> None:
        document = {**MINIMAL_TEXT, "language": language, **overrides}
        yamlio.write(
            self.i18n_dir / language / f"{document['exercise_id']}.yaml", document
        )

    def report(self, profile: str = "phase1") -> "validate.Report":
        data = dataset_mod.load(self.exercises_dir, self.i18n_dir)
        report = validate.Report(profile=profile)
        validate.check_vocabulary(data, self.vocab, report)
        validate.check_identity(data, report)
        validate.check_translation_coverage(data, self.vocab, report, profile=profile)
        validate.check_merges(data, report)
        validate.check_muscles(data, self.vocab, report, profile=profile)
        validate.check_plausibility(data, self.vocab, report)
        validate.check_pattern_expectations(data, self.vocab, report)
        return report

    def invariants(self, profile: str = "phase1", severity: str = validate.ERROR) -> set[str]:
        # open_findings: excused findings remain in the report, but do not
        # count as open — this is precisely the purpose of exceptions.
        return {
            finding.invariant
            for finding in self.report(profile).open_findings
            if finding.severity == severity
        }

    def assertTriggers(self, invariant: str, **overrides) -> None:
        self.write_exercise(**overrides)
        self.write_text()
        self.assertIn(invariant, self.invariants(), f"Invariant {invariant} did not trigger")

    # -- Structure ----------------------------------------------------------
    def test_clean_fixture_is_silent(self) -> None:
        self.write_exercise()
        self.write_text()
        self.assertEqual(set(), self.invariants())

    def test_2_unknown_vocabulary_value(self) -> None:
        self.assertTriggers("2", modality="hypertrophy")

    def test_2_unknown_muscle_node(self) -> None:
        self.assertTriggers("2", muscles=[{"id": "gluteus_maximums", "role": "primary"}])

    def test_2_unknown_license(self) -> None:
        self.assertTriggers("2", upstream={"source": "wger", "license": "WTFPL"})

    def test_2_language_directory_mismatch(self) -> None:
        """An English text in the de directory. This replicates the bug created
        by the legacy pipeline's incorrect LANGUAGE_ID_MAP."""
        self.write_exercise()
        yamlio.write(self.i18n_dir / "de" / "1.yaml", {**MINIMAL_TEXT, "language": "en"})
        self.assertIn("2", self.invariants())

    def test_3_duplicate_slug(self) -> None:
        self.write_exercise(id="1")
        self.write_exercise(id="2")
        self.write_text()
        self.assertIn("3", self.invariants())

    def test_3_id_does_not_match_filename(self) -> None:
        yamlio.write(self.exercises_dir / "99.yaml", {**MINIMAL, "id": "1"})
        self.assertIn("3", self.invariants())

    def test_5_text_without_exercise(self) -> None:
        self.write_text()
        self.assertIn("5", self.invariants())

    def test_6_merged_without_target(self) -> None:
        self.assertTriggers("6", status="merged")

    def test_6_merged_into_missing_exercise(self) -> None:
        self.assertTriggers("6", status="merged", merged_into="404")

    def test_6_merged_into_a_merged_exercise(self) -> None:
        self.write_exercise(id="1", slug="a", status="merged", merged_into="2")
        self.write_exercise(id="2", slug="b", status="merged", merged_into="3")
        self.write_exercise(id="3", slug="c")
        self.assertIn("6", self.invariants())

    def test_7_alias_chain(self) -> None:
        self.write_exercise(id="1", slug="a", aliases=["900"])
        self.write_exercise(id="2", slug="b", aliases=["1"])
        self.assertIn("7", self.invariants())

    # -- Content Plausibility -----------------------------------------------
    def test_8_is_a_warning_in_phase1_and_an_error_in_full(self) -> None:
        self.write_exercise(muscles=[{"id": "latissimus_dorsi", "role": "secondary"}])
        self.write_text()
        self.assertNotIn("8", self.invariants("phase1"))
        self.assertIn("8", self.invariants("phase1", severity=validate.WARNING))
        self.assertIn("8", self.invariants("full"))

    def test_9_same_muscle_twice(self) -> None:
        self.assertTriggers(
            "9",
            muscles=[
                {"id": "latissimus_dorsi", "role": "primary"},
                {"id": "latissimus_dorsi", "role": "primary"},
            ],
        )

    def test_9_same_muscle_in_both_roles(self) -> None:
        self.assertTriggers(
            "9",
            muscles=[
                {"id": "latissimus_dorsi", "role": "primary"},
                {"id": "latissimus_dorsi", "role": "secondary"},
            ],
        )

    def test_10_node_together_with_its_ancestor(self) -> None:
        self.assertTriggers(
            "10",
            muscles=[
                {"id": "trapezius", "role": "primary"},
                {"id": "traps_upper", "role": "secondary"},
            ],
        )

    def test_10_muscle_together_with_its_group(self) -> None:
        self.assertTriggers(
            "10",
            muscles=[
                {"id": "back", "role": "primary"},
                {"id": "latissimus_dorsi", "role": "secondary"},
            ],
        )

    def test_11_bodyweight_with_a_rack(self) -> None:
        self.assertTriggers("11", primary_equipment="bodyweight", setup=["power_rack"])

    def test_12_cardio_with_a_weight_tracker(self) -> None:
        self.assertTriggers("12", modality="cardio", tracking_type="weight_reps")

    def test_13_strength_measured_in_distance(self) -> None:
        self.assertTriggers("13", modality="strength", tracking_type="distance_only")

    def test_14_isolation_with_three_primary_muscles(self) -> None:
        self.assertTriggers(
            "14",
            mechanic="isolation",
            muscles=[
                {"id": "latissimus_dorsi", "role": "primary"},
                {"id": "teres_major", "role": "primary"},
                {"id": "rhomboids", "role": "primary"},
            ],
        )

    def test_15_compound_with_a_single_muscle(self) -> None:
        self.assertTriggers("15", mechanic="compound")

    def test_17_added_weight_requires_reps_or_time(self) -> None:
        self.assertTriggers("17", supports_added_weight=True, tracking_type="weight_reps")

    def test_19_cannot_be_violated_any_more(self) -> None:
        """force_vector is derived — a contradiction cannot be formulated.

        The test records that the derivation table knows every pattern.
        If a pattern enters the vocabulary later without an entry here,
        the build would silently write NULL instead of failing visibly.
        """
        vocab = Vocabularies()
        patterns = set(vocab.classification("movement_pattern"))
        table = set(vocab.force_vector_by_pattern)
        self.assertEqual(set(), patterns - table, "Patterns without entry in derivation table")
        self.assertEqual(set(), table - patterns, "Derivation table knows unknown patterns")
        allowed = set(vocab.classification("force_vector")) | {None}
        self.assertTrue(set(vocab.force_vector_by_pattern.values()) <= allowed)

    def test_20_pattern_muscle_expectations(self) -> None:
        self.write_exercise(
            movement_pattern="squat",
            muscles=[{"id": "biceps_brachii", "role": "primary"}],
        )
        self.write_text()
        warnings = self.invariants(severity=validate.WARNING)
        self.assertIn("20", warnings)

    def test_20_pattern_other_is_exempt(self) -> None:
        self.write_exercise(
            movement_pattern="other",
            muscles=[{"id": "biceps_brachii", "role": "primary"}],
        )
        self.write_text()
        warnings = self.invariants(severity=validate.WARNING)
        self.assertNotIn("20", warnings)


class RealDataTestCase(unittest.TestCase):
    """The repository data itself — end-to-end sanity check."""

    def test_repository_passes_the_phase1_profile(self) -> None:
        data = dataset_mod.load()
        vocab = Vocabularies()
        report = validate.Report(profile="phase1")
        validate.check_vocabulary(data, vocab, report)
        validate.check_identity(data, report)
        validate.check_vocab_id_uniqueness(vocab, report)
        validate.check_translation_coverage(data, vocab, report, profile="phase1")
        validate.check_merges(data, report)
        validate.check_muscles(data, vocab, report, profile="phase1")
        validate.check_plausibility(data, vocab, report)
        validate.check_pattern_expectations(data, vocab, report)
        # As in main(): last, and it does not decide findings, but whether they are explained.
        validate.apply_exceptions(data, report)
        self.assertEqual(
            [], [f.as_dict() for f in report.errors][:20], f"{len(report.errors)} errors"
        )

    def test_the_only_soft_invariant_that_fires_is_excused(self) -> None:
        """616 Squat Thrust — cardio exercise logged in repetitions."""
        data = dataset_mod.load()
        report = validate.Report(profile="phase1")
        validate.check_plausibility(data, Vocabularies(), report)
        validate.apply_exceptions(data, report)
        soft = report.stats["soft_invariants"]
        self.assertEqual(0, soft["12"]["open"])
        self.assertEqual(1, soft["12"]["excused"])
        self.assertEqual(1, soft["12"]["fired"])

    def test_every_legacy_wger_muscle_maps_back_to_its_own_name(self) -> None:
        """The compatibility columns stand and fall with this inverse mapping."""
        vocab = Vocabularies()
        for raw_name, node in vocab.muscles.legacy_wger_mapping.items():
            self.assertEqual(
                raw_name,
                vocab.muscles.legacy_wger_name(node),
                f"{raw_name!r} -> {node!r} did not roundtrip back to {raw_name!r}",
            )

    def test_muscle_heads_resolve_to_their_parents_legacy_name(self) -> None:
        """The main benefit: Phase 2 refinement does not break the app."""
        vocab = Vocabularies()
        self.assertEqual("Trapezius", vocab.muscles.legacy_wger_name("traps_upper"))
        self.assertEqual("Triceps", vocab.muscles.legacy_wger_name("triceps_long_head"))
        self.assertEqual("Quads", vocab.muscles.legacy_wger_name("vastus_medialis"))
        self.assertEqual("Hamstrings", vocab.muscles.legacy_wger_name("biceps_femoris"))
        # Muscles unknown to today's app must return None — otherwise they end up under a wrong name in statistics.
        self.assertIsNone(vocab.muscles.legacy_wger_name("erector_spinae"))
        self.assertIsNone(vocab.muscles.legacy_wger_name("hip_adductors"))


class PublishedIdsTestCase(unittest.TestCase):
    """Invariant 21 against the registry — the rule safeguarding previously published exercises.

    The original draft compared against the *previous* release. That had a
    ratchet effect: once a deletion slipped through, the next baseline no longer
    knew the ID, and every subsequent diff correctly reported zero deletions.
    These tests ensure validation checks against an inventory that can only grow.
    """

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.exercises_dir = self.root / "exercises"
        self.i18n_dir = self.root / "i18n"
        self.exercises_dir.mkdir(parents=True)
        self.i18n_dir.mkdir(parents=True)
        self.registry = self.root / "published_ids.yaml"
        self._real_registry = validate.PUBLISHED_IDS
        validate.PUBLISHED_IDS = self.registry

    def tearDown(self) -> None:
        validate.PUBLISHED_IDS = self._real_registry
        self.tmp.cleanup()

    def write(self, exercise_id: str, status: str = "active", with_text: bool = True) -> None:
        yamlio.write(
            self.exercises_dir / f"{exercise_id}.yaml",
            {**MINIMAL, "id": exercise_id, "slug": f"slug-{exercise_id}", "status": status},
        )
        if with_text:
            yamlio.write(
                self.i18n_dir / "en" / f"{exercise_id}.yaml",
                {**MINIMAL_TEXT, "exercise_id": exercise_id},
            )

    def register(self, *ids: str) -> None:
        yamlio.write(self.registry, {"version": 1, "ids": {i: "202601010000" for i in ids}})

    def findings(self) -> list:
        data = dataset_mod.load(self.exercises_dir, self.i18n_dir)
        report = validate.Report(profile="phase1")
        validate.check_published_ids(data, report)
        return [f for f in report.findings if f.severity == validate.ERROR]

    def test_a_published_id_that_disappeared_is_an_error(self) -> None:
        self.register("1", "2")
        self.write("1")
        self.assertEqual(1, len(self.findings()))
        self.assertIn("2", self.findings()[0].message)

    def test_a_deprecated_entry_satisfies_the_rule(self) -> None:
        """The intended path: deprecate rather than delete."""
        self.register("1", "2")
        self.write("1")
        self.write("2", status="deprecated")
        self.assertEqual([], self.findings())

    def test_a_merged_entry_satisfies_the_rule(self) -> None:
        self.register("1", "2")
        self.write("1")
        self.write("2", status="merged")
        self.assertEqual([], self.findings())

    def test_a_silenced_entry_without_any_text_is_an_error(self) -> None:
        """A row that the app cannot display is not a valid rescue."""
        self.register("1", "2")
        self.write("1")
        self.write("2", status="deprecated", with_text=False)
        self.assertEqual(1, len(self.findings()))

    def test_new_ids_outside_the_registry_are_fine(self) -> None:
        """The registry grows after the release, not before."""
        self.register("1")
        self.write("1")
        self.write("2")
        self.assertEqual([], self.findings())

    def test_the_repository_registry_is_complete(self) -> None:
        """The repository data itself — end-to-end check for the 38 recovered exercises."""
        validate.PUBLISHED_IDS = self._real_registry
        data = dataset_mod.load()
        report = validate.Report(profile="phase1")
        validate.check_published_ids(data, report)
        self.assertEqual([], [f.as_dict() for f in report.errors][:10])
        self.assertGreaterEqual(report.stats["deprecated"] + report.stats["merged"], 38)


class ExceptionsTestCase(ValidatorTestCase):
    """The exception mechanism: dismiss with cause, but never silently or arbitrarily.

    This exists because an overly rigid rule does not create a visible error,
    but a silently distorted annotation — e.g. exercise 1103 swapped
    `anti_extension` for `other` just to satisfy the rule chain. The result
    was green CI with incorrect data.
    """

    def report(self, profile: str = "phase1") -> "validate.Report":
        report = super().report(profile)
        data = dataset_mod.load(self.exercises_dir, self.i18n_dir)
        validate.apply_exceptions(data, report)
        return report

    def test_a_soft_invariant_can_be_excused(self) -> None:
        """Squat Thrust: cardio exercise logged in reps."""
        self.write_exercise(modality="cardio", tracking_type="bodyweight_reps")
        self.write_text()
        self.assertIn("12", self.invariants())

        self.write_exercise(
            modality="cardio",
            tracking_type="bodyweight_reps",
            exceptions={"invariant_12": "Cardio in reps."},
        )
        self.assertNotIn("12", self.invariants())

    def test_the_excused_finding_is_kept_with_its_reason(self) -> None:
        """Excused does not mean gone — the report retains both."""
        self.write_exercise(
            modality="cardio",
            tracking_type="bodyweight_reps",
            exceptions={"invariant_12": "Cardio in reps."},
        )
        self.write_text()
        report = self.report()
        excused = [f for f in report.findings if f.invariant == "12"]
        self.assertEqual(1, len(excused))
        self.assertIn("Cardio", excused[0].excused or "")
        self.assertEqual({"fired": 1, "excused": 1, "open": 0}, report.stats["soft_invariants"]["12"])

    def test_an_exception_on_a_hard_invariant_is_an_error(self) -> None:
        self.write_exercise(
            supports_added_weight=True,
            tracking_type="weight_reps",
            exceptions={"invariant_17": "Because I want it, really."},
        )
        self.write_text()
        invariants = self.invariants()
        self.assertIn("exceptions", invariants)
        self.assertIn("17", invariants, "the hard rule still triggers")

    def test_an_exception_without_a_reason_is_an_error(self) -> None:
        self.write_exercise(
            modality="cardio",
            tracking_type="bodyweight_reps",
            exceptions={"invariant_12": "   "},
        )
        self.write_text()
        self.assertIn("exceptions", self.invariants())
        self.assertIn("12", self.invariants(), "not excused without a reason")

    def test_an_exception_that_never_fires_is_a_warning(self) -> None:
        """Stale exceptions mislead the next developer."""
        self.write_exercise(
            modality="cardio",
            tracking_type="time",
            exceptions={"invariant_12": "Once needed, no longer required."},
        )
        self.write_text()
        self.assertNotIn("exceptions", self.invariants())
        self.assertIn("exceptions", self.invariants(severity=validate.WARNING))

    def test_an_exception_on_an_unknown_invariant_is_an_error(self) -> None:
        self.write_exercise(exceptions={"invariant_99": "Does not exist, should be flagged."})
        self.write_text()
        self.assertIn("exceptions", self.invariants())

    def test_an_exception_only_covers_its_own_exercise(self) -> None:
        self.write_exercise(
            id="1",
            slug="a",
            modality="cardio",
            tracking_type="bodyweight_reps",
            exceptions={"invariant_12": "Justified here, not there."},
        )
        self.write_exercise(
            id="2", slug="b", modality="cardio", tracking_type="bodyweight_reps"
        )
        self.write_text()
        open_12 = [f for f in self.report().errors if f.invariant == "12"]
        self.assertEqual(["2"], [f.exercise_id for f in open_12])


class HardSoftSplitTestCase(unittest.TestCase):
    def test_every_invariant_is_classified_exactly_once(self) -> None:
        overlap = validate.HARD_INVARIANTS & validate.SOFT_INVARIANTS
        self.assertEqual(set(), overlap, "a rule cannot be both hard and soft")

    def test_the_split_matches_the_documented_one(self) -> None:
        """Against schema/invariants.md, ensuring code and documentation stay in sync."""
        self.assertEqual(
            {"11", "12", "13", "14", "15", "20"}, validate.SOFT_INVARIANTS
        )
        for hard in ("1", "2", "3", "8", "9", "17", "21", "24", "25"):
            self.assertIn(hard, validate.HARD_INVARIANTS)


class NewLoadModeInvariantsTestCase(ValidatorTestCase):
    def test_24_added_weight_requires_bodyweight_load_mode(self) -> None:
        self.assertTriggers("24", supports_added_weight=True, load_mode="external",
                            tracking_type="bodyweight_reps")

    def test_24_accepts_bodyweight(self) -> None:
        self.write_exercise(
            supports_added_weight=True, load_mode="bodyweight", tracking_type="bodyweight_reps"
        )
        self.write_text()
        self.assertNotIn("24", self.invariants())

    def test_25_assisted_requires_a_machine_or_a_band(self) -> None:
        self.assertTriggers("25", load_mode="assisted", primary_equipment="barbell")

    def test_25_accepts_a_machine(self) -> None:
        self.write_exercise(load_mode="assisted", primary_equipment="machine")
        self.write_text()
        self.assertNotIn("25", self.invariants())

    def test_25_accepts_a_band(self) -> None:
        self.write_exercise(load_mode="assisted", primary_equipment="resistance_band")
        self.write_text()
        self.assertNotIn("25", self.invariants())


class TranslationIdentityTestCase(ValidatorTestCase):
    def test_translation_identity_triggers_warning_for_identical_ai_raw_name(self) -> None:
        self.write_exercise(id="1")
        self.write_text(language="en", exercise_id="1", name="Plank Hold", status="human")
        self.write_text(language="de", exercise_id="1", name="Plank Hold", status="ai_raw")
        findings = [f for f in self.report().warnings if f.invariant == "translation_identity"]
        self.assertEqual(1, len(findings))
        self.assertIn("Plank Hold", findings[0].message)

    def test_translation_identity_does_not_trigger_when_names_differ(self) -> None:
        self.write_exercise(id="1")
        self.write_text(language="en", exercise_id="1", name="Bench Press", status="human")
        self.write_text(language="de", exercise_id="1", name="Bankdrücken", status="ai_raw")
        findings = [f for f in self.report().warnings if f.invariant == "translation_identity"]
        self.assertEqual(0, len(findings))


if __name__ == "__main__":
    unittest.main(verbosity=2)
