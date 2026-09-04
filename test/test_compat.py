#!/usr/bin/env python3
"""Abnahmetest: laedt die heutige App diese Datenbank noch?

Die Schwelle steht in `_bootstrap/HANDOFF.md`: der Importer der App
(`_mapExerciseBundle` in `lib/core/infrastructure/basis_data_manager.dart`) liest
genau vier Spalten aus `exercises` — `id`, `category_name`, `muscles_primary`,
`muscles_secondary` — plus `exercise_translations`.

**Was sich mit Phase 2 an diesem Test geaendert hat.** In Phase 1 war
Zeichengleichheit die richtige Schwelle: der Umbau der Pipeline sollte nachweislich
folgenlos sein. Ab Phase 2 waere sie falsch — bessere Muskelzuweisungen aendern
`muscles_primary` und `muscles_secondary` zwangslaeufig, das ist der Zweck des
ganzen Projekts. Ein Test, der darauf besteht, blockiert genau die Arbeit, fuer
die er da ist.

Geblieben ist die Zeichengleichheit dort, wo sie eine echte Aussage macht:
`category_name` (wird nicht gepflegt, ist der konservierte Rohwert). Texte
werden in Phase 2 bewusst kuratiert. Der Test schuetzt deshalb ihre
Verfuegbarkeit und Abdeckung, nicht mehr einen ueberholten Zeichengleichstand.
Fuer die Muskelspalten steht jetzt die eigentliche Gefahr im Test — dass eine
Uebung ihre Information *verliert* statt sie zu praezisieren.

Als Referenz dient bei Bedarf eine zuvor veroeffentlichte OpenExerciseDB-DB.
Ohne Referenz (kein lokaler Cache) ueberspringen sich die Tests, die eine
brauchen; die Struktur- und Vertragstests laufen immer.

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
        db_path = Path(cls.tmp.name) / "openexercisedb.db"
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

    def test_category_name_is_character_identical(self) -> None:
        """`category_name` wird nicht gepflegt — es ist der konservierte
        wger-Rohwert. Aendert es sich, stimmt etwas mit der Pipeline nicht."""
        new = {row["id"]: row["category_name"] for row in self.db.execute(
            "SELECT id, category_name FROM exercises")}
        old = {row["id"]: row["category_name"] for row in self.reference.execute(
            "SELECT id, category_name FROM exercises")}
        differences = [
            (i, old[i], new[i]) for i in sorted(self._shared_ids()) if old[i] != new[i]
        ]
        self.assertEqual([], differences[:20], f"{len(differences)} Abweichungen")

    def test_muscle_columns_never_lose_data_silently(self) -> None:
        """Ab Phase 2 duerfen sich die Muskelspalten aendern — das ist der Zweck.

        Zeichengleichheit war die richtige Schwelle fuer Phase 1 (keine
        Verhaltensaenderung). Ab Phase 2 wuerde sie genau die Arbeit blockieren,
        fuer die es dieses Repo gibt: bessere Zuweisungen aendern diese Spalten
        zwangslaeufig.

        Was bleibt, ist die eigentliche Gefahr: dass eine Uebung ihre
        Muskelinformation *verliert*. Deshalb wird hier nicht mehr auf Gleichheit
        geprueft, sondern darauf, dass jede Abweichung durch praezisere Daten
        gedeckt ist — `exercise_muscles` muss die Zuweisung enthalten, auch wenn
        das alte 15-Werte-Vokabular sie nicht ausdruecken kann.
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
            # Der einzige echte Verlust: vorher etwas, jetzt nichts — und auch
            # keine praezise Zuweisung, die das erklaeren wuerde.
            if had and not has and precise == 0:
                losses.append(exercise_id)
        self.assertEqual([], losses, f"{len(losses)} Uebungen ohne jede Muskelinformation")

    def test_the_legacy_vocabulary_gap_is_small_and_named(self) -> None:
        """Wie viele Uebungen das alte 15-Werte-Vokabular nicht mehr ausdruecken kann.

        Kein Datenverlust — `exercise_muscles` traegt die praezise Zuweisung —,
        aber ein Konsument, der nur die Legacy-Spalten liest, sieht sie nicht
        mehr. Die Zahl gehoert sichtbar in den Test, damit sie nicht unbemerkt
        waechst; behoben wird sie App-seitig durch den Umstieg auf die
        mitgelieferten Vokabulare (SCHEMA.md 10, Punkt 6).
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
            f"{len(gap)} Uebungen fallen aus den Legacy-Spalten heraus: {gap[:20]}. "
            f"Wenn das waechst, lohnt der App-seitige Umstieg dringender.",
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
        """Ein vorhandener Name darf durch die Textpflege nicht verschwinden."""
        for language in APP_REQUIRED_LANGUAGES:
            new = self._translations(self.db, language)
            old = self._translations(self.reference, language)
            shared = self._shared_ids() & set(old)
            self.assertTrue(shared, f"Referenz hat keine {language}-Texte")
            missing = [
                exercise_id for exercise_id in sorted(shared)
                if (old[exercise_id]["name"] or "").strip()
                and not (new.get(exercise_id, {}).get("name") or "").strip()
            ]
            self.assertEqual([], missing[:20], f"{language}: {len(missing)} Namen verloren")

    def test_translation_coverage_never_drops(self) -> None:
        """Jede in der Release-DB vorhandene Sprachzeile bleibt vorhanden."""
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
