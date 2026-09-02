#!/usr/bin/env python3
"""Abnahmetest fuer Phase 1: laedt die heutige App diese Datenbank unveraendert?

Die Schwelle steht in `_bootstrap/HANDOFF.md`: der Importer der App
(`_mapExerciseBundle` in `lib/core/infrastructure/basis_data_manager.dart`) liest
genau vier Spalten aus `exercises` — `id`, `category_name`, `muscles_primary`,
`muscles_secondary` — plus `exercise_translations`. Solange die zeichengleich
zur veroeffentlichten Referenz sind, ist der Umbau der Pipeline nachweislich
folgenlos fuer Nutzer.

Als Referenz dient die DB aus dem `wger-catalog-stable`-Release — das, was auf
Geraeten tatsaechlich liegt. Ohne Referenz (kein Netz, kein Cache) ueberspringen
sich die Tests, die eine brauchen; die Struktur- und Vertragstests laufen immer.

Warum "Referenz-IDs sind eine Teilmenge" und nicht "gleiche Menge": das Release
ist vom 31.08. und kennt 862 Uebungen, der eingefrorene Snapshot vom 02.09. kennt
871. Neun sind seither dazugekommen, keine verschwunden. Ein Test auf
Mengengleichheit wuerde nicht die Pipeline pruefen, sondern das Alter des
Releases.
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
    """Baut die DB einmal fuer alle Tests dieser Datei."""

    tmp: tempfile.TemporaryDirectory
    db: sqlite3.Connection
    report: dict

    @classmethod
    def setUpClass(cls) -> None:
        cls.tmp = tempfile.TemporaryDirectory()
        db_path = Path(cls.tmp.name) / "train_libre_training.db"
        cls.report = support.build_database(db_path)
        cls.db = sqlite3.connect(db_path)
        cls.db.row_factory = sqlite3.Row

    @classmethod
    def tearDownClass(cls) -> None:
        cls.db.close()
        cls.tmp.cleanup()


class AppImporterContract(DatabaseTestCase):
    """Was die heutige App braucht — pruefbar ohne die Referenz-DB."""

    def test_required_tables_exist(self) -> None:
        tables = support.table_names(self.db)
        self.assertIn("exercises", tables)
        self.assertIn("exercise_translations", tables)
        self.assertIn("metadata", tables)

    def test_required_columns_exist(self) -> None:
        columns = support.table_columns(self.db, "exercises")
        for column in APP_REQUIRED_EXERCISE_COLUMNS:
            self.assertIn(column, columns, f"exercises.{column} fehlt")
            self.assertEqual("TEXT", columns[column], f"exercises.{column} ist kein TEXT")

        columns = support.table_columns(self.db, "exercise_translations")
        for column in APP_REQUIRED_TRANSLATION_COLUMNS:
            self.assertIn(column, columns, f"exercise_translations.{column} fehlt")

    def test_compat_columns_are_never_null(self) -> None:
        """NULL statt "[]" wuerde in der App zu einem stillen Absturz beim
        JSON-Dekodieren fuehren — die Spalten muessen belegt sein."""
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
                self.assertEqual(sorted(set(value)), value, f"{row['id']}.{column} unsortiert")

    def test_every_exercise_has_de_and_en_text(self) -> None:
        """`complete_in_release` in vocab/languages.yaml ist genau diese Zusage."""
        for language in APP_REQUIRED_LANGUAGES:
            missing = self.db.execute(
                "SELECT e.id FROM exercises e LEFT JOIN exercise_translations t "
                "ON t.exercise_id = e.id AND t.language_code = ? WHERE t.id IS NULL",
                (language,),
            ).fetchall()
            self.assertEqual([], [row["id"] for row in missing], f"{language} unvollstaendig")

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
            self.assertIn(key, metadata, f"metadata.{key} fehlt (SCHEMA.md 8)")
        self.assertEqual("2", metadata["schema_version"])
        self.assertEqual("1", metadata["min_app_schema_version"])

    def test_license_provenance_is_present_on_every_row(self) -> None:
        """Der eigentliche Grund fuer den Fork-Teil dieser Phase: die heute
        ausgelieferte DB enthaelt keinerlei Attribution (SCHEMA.md 3b)."""
        missing = self.db.execute(
            "SELECT COUNT(*) AS n FROM exercises WHERE upstream_license IS NULL AND upstream_source IS NOT NULL"
        ).fetchone()
        self.assertEqual(0, missing["n"])
        missing = self.db.execute(
            "SELECT COUNT(*) AS n FROM exercise_translations WHERE license IS NULL"
        ).fetchone()
        self.assertEqual(0, missing["n"])


class ReferenceComparison(DatabaseTestCase):
    """Zeichenvergleich gegen die veroeffentlichte Datenbank."""

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
                "Keine Referenz-DB. REFERENCE_DB_PATH setzen oder OEDB_ALLOW_DOWNLOAD=1."
            )

    # -- Helfer -------------------------------------------------------------
    def _ids(self, connection: sqlite3.Connection) -> set[str]:
        return {row["id"] for row in connection.execute("SELECT id FROM exercises")}

    def _shared_ids(self) -> set[str]:
        return self._ids(self.reference) & self._ids(self.db)

    # -- Tests --------------------------------------------------------------
    def test_no_reference_id_disappears(self) -> None:
        """Invariante 21: eine ID, die verschwindet, macht Nutzerdaten
        unaufloesbar (SCHEMA.md 3)."""
        missing = sorted(self._ids(self.reference) - self._ids(self.db), key=str)
        self.assertEqual([], missing, f"{len(missing)} Uebungen der Referenz fehlen")

    def test_exercise_count_does_not_drop(self) -> None:
        self.assertGreaterEqual(len(self._ids(self.db)), len(self._ids(self.reference)))

    def test_compat_columns_are_character_identical(self) -> None:
        columns = ("category_name", "muscles_primary", "muscles_secondary")
        select = f"SELECT id, {', '.join(columns)} FROM exercises"
        new = {row["id"]: row for row in self.db.execute(select)}
        old = {row["id"]: row for row in self.reference.execute(select)}
        differences = [
            (exercise_id, column, old[exercise_id][column], new[exercise_id][column])
            for exercise_id in sorted(self._shared_ids())
            for column in columns
            if old[exercise_id][column] != new[exercise_id][column]
        ]
        self.assertEqual([], differences[:20], f"{len(differences)} Abweichungen")

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

    def test_translation_names_are_character_identical(self) -> None:
        """Nur `de` und `en`.

        Fuer die uebrigen Sprachen ist ein Vergleich sinnlos: die alte Pipeline
        hatte die wger-Sprach-IDs falsch verdrahtet und fuehrt in der Referenz
        646 spanische Texte als `fr`, 48 griechische als `ja` und 10 russische
        als `it`. Das ist hier absichtlich korrigiert, nicht reproduziert.
        """
        for language in APP_REQUIRED_LANGUAGES:
            new = self._translations(self.db, language)
            old = self._translations(self.reference, language)
            shared = self._shared_ids() & set(old)
            self.assertTrue(shared, f"Referenz hat keine {language}-Texte")
            differences = [
                (exercise_id, old[exercise_id]["name"], new.get(exercise_id, {}).get("name"))
                for exercise_id in sorted(shared)
                if new.get(exercise_id, {}).get("name") != old[exercise_id]["name"]
            ]
            self.assertEqual([], differences[:20], f"{language}: {len(differences)} Abweichungen")

    def test_translation_descriptions_differ_only_where_the_old_script_mixed_languages(
        self,
    ) -> None:
        """Die einzige zugelassene Abweichung — und sie ist eine Korrektur.

        Das Altskript fuellte eine fehlende *Beschreibung* aus der jeweils
        anderen Sprache auf, auch wenn der Name in der Zielsprache existierte
        (`create_wger_exercise_db.py`, `description_de = orig_de or orig_en`).
        Dadurch steht in der ausgelieferten DB bei 17 Eintraegen deutscher Text
        in der englischen Zeile und umgekehrt. Hier bleibt die Beschreibung
        stattdessen leer.

        Der Test laesst genau diesen Fall zu und nichts sonst: die neue
        Beschreibung muss leer sein, und die alte muss zeichengleich mit der
        Beschreibung der anderen Sprache gewesen sein. Jede andere Abweichung
        ist ein Fehler.
        """
        new = {language: self._translations(self.db, language) for language in APP_REQUIRED_LANGUAGES}
        old = {
            language: self._translations(self.reference, language)
            for language in APP_REQUIRED_LANGUAGES
        }
        unexplained = []
        explained = 0
        for language, other in (("en", "de"), ("de", "en")):
            for exercise_id in sorted(self._shared_ids() & set(old[language])):
                was = old[language][exercise_id]["description"]
                now = new.get(language, {}).get(exercise_id, {}).get("description")
                if now == was:
                    continue
                borrowed = old[other].get(exercise_id, {}).get("description")
                if now == "" and was == borrowed:
                    explained += 1
                    continue
                unexplained.append((language, exercise_id, was, now))
        self.assertEqual([], unexplained[:20], f"{len(unexplained)} unerklaerte Abweichungen")
        self.assertLess(
            explained,
            50,
            "Deutlich mehr sprachvermischte Beschreibungen als erwartet — bitte ansehen.",
        )

    def _translations(self, connection: sqlite3.Connection, language: str) -> dict:
        return {
            row["exercise_id"]: dict(row)
            for row in connection.execute(
                "SELECT exercise_id, name, description FROM exercise_translations "
                "WHERE language_code = ?",
                (language,),
            )
        }


if __name__ == "__main__":
    unittest.main(verbosity=2)
