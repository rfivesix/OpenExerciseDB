#!/usr/bin/env python3
"""Prueft den Validator gegen absichtlich kaputte Daten.

Ein Regelwerk, das nie anschlaegt, ist von einem Regelwerk, das nicht laeuft,
nicht zu unterscheiden. Jede Invariante bekommt hier einen Fall, der sie
ausloesen muss — und der Bestand im Repo ist der Gegenbeweis, dass sie nicht
grundlos anschlaegt.
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
    """Schreibt Fixtures in ein temporaeres data/ und laesst den Validator los."""

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
        return report

    def invariants(self, profile: str = "phase1", severity: str = validate.ERROR) -> set[str]:
        return {
            finding.invariant
            for finding in self.report(profile).findings
            if finding.severity == severity
        }

    def assertTriggers(self, invariant: str, **overrides) -> None:
        self.write_exercise(**overrides)
        self.write_text()
        self.assertIn(invariant, self.invariants(), f"Invariante {invariant} hat nicht ausgeloest")

    # -- Struktur -----------------------------------------------------------
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
        """Ein englischer Text im de-Verzeichnis. Genau so entsteht der Fehler,
        den die alte Pipeline ueber die falsche LANGUAGE_ID_MAP eingebaut hat."""
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

    # -- Inhaltliche Plausibilitaet -----------------------------------------
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

    def test_17_added_weight_with_the_wrong_tracker(self) -> None:
        self.assertTriggers("17", supports_added_weight=True, tracking_type="weight_reps")

    def test_18_static_hold_counted_in_reps(self) -> None:
        self.assertTriggers("18", force_vector="static", tracking_type="bodyweight_reps")

    def test_19_pattern_contradicts_force_vector(self) -> None:
        self.assertTriggers("19", movement_pattern="vertical_pull", force_vector="push")

    def test_19_anti_pattern_must_be_static(self) -> None:
        self.assertTriggers("19", movement_pattern="anti_rotation", force_vector="pull")

    def test_19_accepts_a_matching_pair(self) -> None:
        self.write_exercise(movement_pattern="vertical_pull", force_vector="pull")
        self.write_text()
        self.assertNotIn("19", self.invariants())


class RealDataTestCase(unittest.TestCase):
    """Der Bestand im Repo selbst — die Gegenprobe."""

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
        self.assertEqual(
            [], [f.as_dict() for f in report.errors][:20], f"{len(report.errors)} Fehler"
        )

    def test_every_legacy_wger_muscle_maps_back_to_its_own_name(self) -> None:
        """Die Kompatibilitaetsspalten stehen und fallen mit dieser Umkehrung."""
        vocab = Vocabularies()
        for raw_name, node in vocab.muscles.legacy_wger_mapping.items():
            self.assertEqual(
                raw_name,
                vocab.muscles.legacy_wger_name(node),
                f"{raw_name!r} -> {node!r} kommt nicht als {raw_name!r} zurueck",
            )

    def test_muscle_heads_resolve_to_their_parents_legacy_name(self) -> None:
        """Der eigentliche Gewinn: Phase-2-Feinschliff bricht die App nicht."""
        vocab = Vocabularies()
        self.assertEqual("Trapezius", vocab.muscles.legacy_wger_name("traps_upper"))
        self.assertEqual("Triceps", vocab.muscles.legacy_wger_name("triceps_long_head"))
        self.assertEqual("Quads", vocab.muscles.legacy_wger_name("vastus_medialis"))
        self.assertEqual("Hamstrings", vocab.muscles.legacy_wger_name("biceps_femoris"))
        # Muskeln, die die heutige App gar nicht kennt, duerfen nichts liefern —
        # sonst landen sie unter einem falschen Namen in der Statistik.
        self.assertIsNone(vocab.muscles.legacy_wger_name("erector_spinae"))
        self.assertIsNone(vocab.muscles.legacy_wger_name("hip_adductors"))


if __name__ == "__main__":
    unittest.main(verbosity=2)


class PublishedIdsTestCase(unittest.TestCase):
    """Invariante 21 gegen das Register — die Regel, die 38 Uebungen gekostet hat.

    Der urspruengliche Entwurf verglich gegen das *vorige* Release. Das hat eine
    Ratsche: ist ein Verlust einmal durch, kennt die naechste Baseline die ID
    nicht mehr, und jeder folgende Diff meldet voellig korrekt null
    Entfernungen. Diese Tests halten fest, dass die Pruefung jetzt gegen einen
    Bestand laeuft, der nur wachsen kann.
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
        """Der vorgesehene Weg: nicht loeschen, sondern stilllegen."""
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
        """Eine Zeile, die die App nicht anzeigen kann, ist keine Rettung."""
        self.register("1", "2")
        self.write("1")
        self.write("2", status="deprecated", with_text=False)
        self.assertEqual(1, len(self.findings()))

    def test_new_ids_outside_the_registry_are_fine(self) -> None:
        """Das Register waechst nach dem Release, nicht davor."""
        self.register("1")
        self.write("1")
        self.write("2")
        self.assertEqual([], self.findings())

    def test_the_repository_registry_is_complete(self) -> None:
        """Der Bestand selbst — die Gegenprobe zur Wiederherstellung der 38."""
        validate.PUBLISHED_IDS = self._real_registry
        data = dataset_mod.load()
        report = validate.Report(profile="phase1")
        validate.check_published_ids(data, report)
        self.assertEqual([], [f.as_dict() for f in report.errors][:10])
        self.assertGreaterEqual(report.stats["deprecated"], 38)
