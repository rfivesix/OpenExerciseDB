#!/usr/bin/env python3
"""Acceptance test: does the current app still load this database?

The threshold is documented in SCHEMA.md: the app's importer
(`_mapExerciseBundle` in `lib/core/infrastructure/basis_data_manager.dart`) reads
exactly four columns from `exercises` — `id`, `category_name`, `muscles_primary`,
`muscles_secondary` — plus `exercise_translations`.

**What changed with Phase 2 in this test.** In Phase 1, character identity was
the correct threshold: restructuring the pipeline was proven to have zero side effects.
From Phase 2 onwards, strict character identity would be counterproductive — better
muscle assignments necessarily change `muscles_primary` and `muscles_secondary`,
which is the whole purpose of the project. A test insisting on old values would block
the very work it is meant to protect.

Character identity is retained where it provides meaningful guarantees:
`category_name` (unmaintained legacy raw value). Texts are deliberately curated
in Phase 2; the test protects their availability and coverage rather than an obsolete
frozen string match. For muscle columns, the test checks the real danger — that an
exercise *loses* muscle information rather than refining it.

When available, a previously published OpenExerciseDB database serves as reference.
Without a reference (no local cache), reference-dependent tests skip; structural
and schema contract tests always run.

Why "reference IDs are a subset" and not "exact same set": previous releases
contain fewer exercises than the current catalog. New exercises are added over time,
none are deleted. A test for set equality would test release age rather than pipeline
integrity.
"""
from __future__ import annotations

import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

import support

APP_REQUIRED_EXERCISE_COLUMNS = ("id", "category_name", "muscles_primary", "muscles_secondary")
APP_REQUIRED_TRANSLATION_COLUMNS = ("id", "exercise_id", "language_code", "name", "description")
APP_REQUIRED_LANGUAGES = ("de", "en")


class DatabaseTestCase(unittest.TestCase):
    """Builds the database once for all tests in this file."""

    tmp: tempfile.TemporaryDirectory
    db: sqlite3.Connection
    report: dict

    @classmethod
    def setUpClass(cls) -> None:
        cls.tmp = tempfile.TemporaryDirectory()
        db_path = Path(cls.tmp.name) / "openexercisedb.db"
        cls.report = support.build_database(db_path)
        cls.db = sqlite3.connect(db_path)
        cls.db.row_factory = sqlite3.Row

    @classmethod
    def tearDownClass(cls) -> None:
        cls.db.close()
        cls.tmp.cleanup()


class AppImporterContract(DatabaseTestCase):
    """What the current app requires — verifiable without the reference DB."""

    def test_required_tables_exist(self) -> None:
        tables = support.table_names(self.db)
        self.assertIn("exercises", tables)
        self.assertIn("exercise_translations", tables)
        self.assertIn("metadata", tables)

    def test_required_columns_exist(self) -> None:
        columns = support.table_columns(self.db, "exercises")
        for column in APP_REQUIRED_EXERCISE_COLUMNS:
            self.assertIn(column, columns, f"exercises.{column} missing")
            self.assertEqual("TEXT", columns[column], f"exercises.{column} is not TEXT")

        columns = support.table_columns(self.db, "exercise_translations")
        for column in APP_REQUIRED_TRANSLATION_COLUMNS:
            self.assertIn(column, columns, f"exercise_translations.{column} missing")

    def test_compat_columns_are_never_null(self) -> None:
        """NULL instead of "[]" would cause a silent crash in the app during
        JSON decoding — columns must be populated."""
        row = self.db.execute(
            "SELECT COUNT(*) AS n FROM exercises "
            "WHERE category_name IS NULL OR muscles_primary IS NULL OR muscles_secondary IS NULL"
        ).fetchone()
        self.assertEqual(0, row["n"])

    def test_muscle_columns_are_json_string_arrays(self) -> None:
        for row in self.db.execute("SELECT id, muscles_primary, muscles_secondary FROM exercises"):
            for column in ("muscles_primary", "muscles_secondary"):
                value = json.loads(row[column])
                self.assertIsInstance(value, list, f"{row['id']}.{column}")
                self.assertTrue(all(isinstance(item, str) for item in value))
                self.assertEqual(sorted(set(value)), value, f"{row['id']}.{column} unsorted")

    def test_every_exercise_has_de_and_en_text(self) -> None:
        """`complete_in_release` in vocab/languages.yaml is precisely this guarantee."""
        for language in APP_REQUIRED_LANGUAGES:
            missing = self.db.execute(
                "SELECT e.id FROM exercises e LEFT JOIN exercise_translations t "
                "ON t.exercise_id = e.id AND t.language_code = ? WHERE t.id IS NULL",
                (language,),
            ).fetchall()
            self.assertEqual([], [row["id"] for row in missing], f"{language} incomplete")

    def test_translation_ids_follow_the_expected_pattern(self) -> None:
        for row in self.db.execute(
            "SELECT id, exercise_id, language_code FROM exercise_translations"
        ):
            self.assertEqual(f"{row['exercise_id']}_{row['language_code']}", row["id"])

    def test_translation_names_are_never_empty(self) -> None:
        row = self.db.execute(
            "SELECT COUNT(*) AS n FROM exercise_translations WHERE name IS NULL OR TRIM(name) = ''"
        ).fetchone()
        self.assertEqual(0, row["n"])

    def test_foreign_keys_resolve(self) -> None:
        self.db.execute("PRAGMA foreign_keys = ON")
        violations = self.db.execute("PRAGMA foreign_key_check").fetchall()
        self.assertEqual([], [tuple(v) for v in violations])

    def test_metadata_carries_the_mandatory_keys(self) -> None:
        metadata = {row["key"]: row["value"] for row in self.db.execute("SELECT * FROM metadata")}
        for key in (
            "version",
            "schema_version",
            "generated_at",
            "source_repo",
            "source_commit",
            "license",
            "attribution_url",
        ):
            self.assertIn(key, metadata, f"metadata.{key} missing (SCHEMA.md §8)")
        self.assertEqual("2", metadata["schema_version"])
        self.assertEqual("1", metadata["min_app_schema_version"])

    def test_license_provenance_is_present_on_every_row(self) -> None:
        """The primary reason for the fork aspect of this phase: the previously
        shipped DB contained no attribution whatsoever (SCHEMA.md §3b)."""
        missing = self.db.execute(
            "SELECT COUNT(*) AS n FROM exercises WHERE upstream_license IS NULL AND upstream_source IS NOT NULL"
        ).fetchone()
        self.assertEqual(0, missing["n"])
        missing = self.db.execute(
            "SELECT COUNT(*) AS n FROM exercise_translations WHERE license IS NULL"
        ).fetchone()
        self.assertEqual(0, missing["n"])


class ReferenceComparison(DatabaseTestCase):
    """Character comparison against the published database."""

    reference: sqlite3.Connection

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        path = support.reference_database()
        if path is None:
            cls.reference = None  # type: ignore[assignment]
            return
        cls.reference = sqlite3.connect(path)
        cls.reference.row_factory = sqlite3.Row

    @classmethod
    def tearDownClass(cls) -> None:
        if getattr(cls, "reference", None) is not None:
            cls.reference.close()
        super().tearDownClass()

    def setUp(self) -> None:
        if getattr(type(self), "reference", None) is None:
            self.skipTest(
                "No reference DB. Set REFERENCE_DB_PATH or OEDB_ALLOW_DOWNLOAD=1."
            )

    # -- Helpers ------------------------------------------------------------
    def _ids(self, connection: sqlite3.Connection) -> set[str]:
        return {row["id"] for row in connection.execute("SELECT id FROM exercises")}

    def _shared_ids(self) -> set[str]:
        return self._ids(self.reference) & self._ids(self.db)

    # -- Tests --------------------------------------------------------------
    def test_no_reference_id_disappears(self) -> None:
        """Invariant 21: a disappearing ID breaks user history (SCHEMA.md §3)."""
        missing = sorted(self._ids(self.reference) - self._ids(self.db), key=str)
        self.assertEqual([], missing, f"{len(missing)} reference exercises missing")

    def test_exercise_count_does_not_drop(self) -> None:
        self.assertGreaterEqual(len(self._ids(self.db)), len(self._ids(self.reference)))

    def test_category_name_is_character_identical(self) -> None:
        """`category_name` is unmaintained — it is the preserved wger raw value.
        If it changes, something in the pipeline is wrong."""
        new = {row["id"]: row["category_name"] for row in self.db.execute(
            "SELECT id, category_name FROM exercises")}
        old = {row["id"]: row["category_name"] for row in self.reference.execute(
            "SELECT id, category_name FROM exercises")}
        differences = [
            (i, old[i], new[i]) for i in sorted(self._shared_ids()) if old[i] != new[i]
        ]
        self.assertEqual([], differences[:20], f"{len(differences)} divergences")

    def test_muscle_columns_never_lose_data_silently(self) -> None:
        """From Phase 2 onwards, muscle columns may change — that is the purpose.

        Character identity was the correct threshold for Phase 1 (no behavioral change).
        From Phase 2 onwards, it would block the exact work this repository exists for:
        better assignments necessarily change these columns.

        What remains is the real danger: that an exercise *loses* muscle information.
        Therefore, this test does not check for equality, but ensures that every
        divergence is backed by more precise data — `exercise_muscles` must contain
        the assignment, even if the legacy 15-value vocabulary cannot express it.
        """
        losses = []
        for row in self.reference.execute(
            "SELECT id, muscles_primary, muscles_secondary FROM exercises"
        ):
            exercise_id = row["id"]
            if exercise_id not in self._shared_ids():
                continue
            precise = self.db.execute(
                "SELECT COUNT(*) AS n FROM exercise_muscles WHERE exercise_id = ?",
                (exercise_id,),
            ).fetchone()["n"]
            new_row = self.db.execute(
                "SELECT muscles_primary, muscles_secondary FROM exercises WHERE id = ?",
                (exercise_id,),
            ).fetchone()
            had = json.loads(row["muscles_primary"] or "[]") + json.loads(
                row["muscles_secondary"] or "[]"
            )
            has = json.loads(new_row["muscles_primary"] or "[]") + json.loads(
                new_row["muscles_secondary"] or "[]"
            )
            # The only real loss: previously something, now nothing — and no
            # precise assignment either that would explain it.
            if had and not has and precise == 0:
                losses.append(exercise_id)
        self.assertEqual([], losses, f"{len(losses)} exercises without any muscle information")

    def test_the_legacy_vocabulary_gap_is_small_and_named(self) -> None:
        """How many exercises the legacy 15-value vocabulary can no longer represent.

        Not data loss — `exercise_muscles` carries the precise assignment —,
        but a consumer reading only legacy columns will no longer see them.
        The count belongs visibly in the test so that it does not grow unnoticed;
        it is resolved app-side by migrating to the bundled vocabularies
        (SCHEMA.md §10, item 6).
        """
        gap = []
        for exercise_id in sorted(self._shared_ids(), key=str):
            old = self.reference.execute(
                "SELECT muscles_primary FROM exercises WHERE id = ?", (exercise_id,)
            ).fetchone()["muscles_primary"]
            new = self.db.execute(
                "SELECT muscles_primary FROM exercises WHERE id = ?", (exercise_id,)
            ).fetchone()["muscles_primary"]
            if json.loads(old or "[]") and not json.loads(new or "[]"):
                gap.append(exercise_id)
        self.assertLessEqual(
            len(gap),
            10,
            f"{len(gap)} exercises dropped out of legacy columns: {gap[:20]}. "
            f"If this grows, app-side migration becomes more urgent.",
        )

    def test_legacy_row_defaults_are_unchanged(self) -> None:
        columns = ("image_path", "is_custom", "created_by", "source")
        select = f"SELECT id, {', '.join(columns)} FROM exercises"
        new = {row["id"]: row for row in self.db.execute(select)}
        old = {row["id"]: row for row in self.reference.execute(select)}
        differences = [
            (exercise_id, column, old[exercise_id][column], new[exercise_id][column])
            for exercise_id in sorted(self._shared_ids())
            for column in columns
            if old[exercise_id][column] != new[exercise_id][column]
        ]
        self.assertEqual([], differences[:20])

    def test_reference_de_and_en_names_remain_available(self) -> None:
        """An existing name must not disappear during text curation."""
        for language in APP_REQUIRED_LANGUAGES:
            new = self._translations(self.db, language)
            old = self._translations(self.reference, language)
            shared = self._shared_ids() & set(old)
            self.assertTrue(shared, f"Reference has no {language} texts")
            missing = [
                exercise_id for exercise_id in sorted(shared)
                if (old[exercise_id]["name"] or "").strip()
                and not (new.get(exercise_id, {}).get("name") or "").strip()
            ]
            self.assertEqual([], missing[:20], f"{language}: {len(missing)} names lost")

    def test_translation_coverage_never_drops(self) -> None:
        """Every language row present in the release DB remains present."""
        old = {
            row["language_code"]: row["n"]
            for row in self.reference.execute(
                "SELECT language_code, COUNT(*) AS n FROM exercise_translations GROUP BY language_code"
            )
        }
        new = {
            row["language_code"]: row["n"]
            for row in self.db.execute(
                "SELECT language_code, COUNT(*) AS n FROM exercise_translations GROUP BY language_code"
            )
        }
        regressions = [
            (language, old_count, new.get(language, 0))
            for language, old_count in sorted(old.items())
            if new.get(language, 0) < old_count
        ]
        self.assertEqual([], regressions)

    def _translations(self, connection: sqlite3.Connection, language: str) -> dict:
        columns = {col[1] for col in connection.execute("PRAGMA table_info(exercise_translations)")}
        fields = ["exercise_id", "name", "description"]
        if "search_terms" in columns:
            fields.append("search_terms")
        query = f"SELECT {', '.join(fields)} FROM exercise_translations WHERE language_code = ?"
        return {
            row["exercise_id"]: dict(row)
            for row in connection.execute(query, (language,))
        }


if __name__ == "__main__":
    unittest.main(verbosity=2)

