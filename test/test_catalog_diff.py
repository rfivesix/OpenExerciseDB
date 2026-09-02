"""Tests fuer build/catalog_diff.py.

Uebernommen aus `train-libre`. Die Schwellwert-Tests sind unveraendert in ihrer
Absicht, aber ihre Fixtures haben jetzt Aliase: unter Invariante 21 ist eine
verschwundene ID ohne Nachfolger fuer sich genommen schon ein Abbruchgrund, und
ohne Alias wuerden die Tests nicht mehr die Schwelle pruefen, sondern die neue
Invariante. Beide Regeln bekommen eigene Tests.
"""

import argparse
import importlib.util
import sqlite3
import tempfile
import unittest
from pathlib import Path
from typing import Any, Dict, Iterable, Optional, Set

MODULE_PATH = Path(__file__).resolve().parents[1] / "build" / "catalog_diff.py"
SPEC = importlib.util.spec_from_file_location("catalog_diff", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def _create_catalog(
    path: Path,
    ids: Iterable[str],
    overrides: Optional[Dict[str, Dict[str, Any]]] = None,
    relational: bool = False,
    aliases: Optional[Dict[str, str]] = None,
    schema_version: Optional[int] = None,
) -> None:
    overrides = overrides or {}
    conn = sqlite3.connect(path)
    try:
        conn.execute("CREATE TABLE metadata (key TEXT, value TEXT)")
        conn.execute(
            "INSERT INTO metadata(key, value) VALUES ('version', 'test-version')"
        )
        if schema_version is not None:
            conn.execute(
                "INSERT INTO metadata(key, value) VALUES ('schema_version', ?)",
                (str(schema_version),),
            )
        if aliases is not None:
            conn.execute(
                """
                CREATE TABLE exercise_aliases (
                    old_id TEXT PRIMARY KEY,
                    new_id TEXT NOT NULL,
                    reason TEXT,
                    since_version TEXT NOT NULL
                )
                """
            )
            for old_id, new_id in aliases.items():
                conn.execute(
                    "INSERT INTO exercise_aliases VALUES (?, ?, 'merged', 'test-version')",
                    (str(old_id), str(new_id)),
                )
        if relational:
            conn.execute(
                """
                CREATE TABLE exercises (
                    id TEXT PRIMARY KEY,
                    category_name TEXT,
                    muscles_primary TEXT,
                    muscles_secondary TEXT
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE exercise_translations (
                    id TEXT PRIMARY KEY,
                    exercise_id TEXT,
                    language_code TEXT,
                    name TEXT,
                    description TEXT,
                    FOREIGN KEY(exercise_id) REFERENCES exercises(id) ON DELETE CASCADE
                )
                """
            )
            for raw_id in ids:
                exercise_id = str(raw_id)
                override = overrides.get(exercise_id, {})
                conn.execute(
                    """
                    INSERT INTO exercises(
                        id,
                        category_name,
                        muscles_primary,
                        muscles_secondary
                    ) VALUES (?, ?, ?, ?)
                    """,
                    (
                        exercise_id,
                        override.get("category_name", "cat"),
                        override.get("muscles_primary", "[]"),
                        override.get("muscles_secondary", "[]"),
                    ),
                )
                name_de = override.get("name_de", f"DE {exercise_id}")
                if name_de is not None:
                    conn.execute(
                        "INSERT INTO exercise_translations(id, exercise_id, language_code, name, description) VALUES (?, ?, ?, ?, ?)",
                        (f"{exercise_id}_de", exercise_id, "de", name_de, override.get("description_de", "desc de")),
                    )
                name_en = override.get("name_en", f"EN {exercise_id}")
                if name_en is not None:
                    conn.execute(
                        "INSERT INTO exercise_translations(id, exercise_id, language_code, name, description) VALUES (?, ?, ?, ?, ?)",
                        (f"{exercise_id}_en", exercise_id, "en", name_en, override.get("description_en", "desc en")),
                    )
        else:
            conn.execute(
                """
                CREATE TABLE exercises (
                    id TEXT PRIMARY KEY,
                    name_de TEXT,
                    name_en TEXT,
                    description_de TEXT,
                    description_en TEXT,
                    category_name TEXT,
                    muscles_primary TEXT,
                    muscles_secondary TEXT
                )
                """
            )
            for raw_id in ids:
                exercise_id = str(raw_id)
                override = overrides.get(exercise_id, {})
                conn.execute(
                    """
                    INSERT INTO exercises(
                        id,
                        name_de,
                        name_en,
                        description_de,
                        description_en,
                        category_name,
                        muscles_primary,
                        muscles_secondary
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        exercise_id,
                        override.get("name_de", f"DE {exercise_id}"),
                        override.get("name_en", f"EN {exercise_id}"),
                        override.get("description_de", "desc de"),
                        override.get("description_en", "desc en"),
                        override.get("category_name", "cat"),
                        override.get("muscles_primary", "[]"),
                        override.get("muscles_secondary", "[]"),
                    ),
                )
        conn.commit()
    finally:
        conn.close()


class WgerCatalogDiffThresholdTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        base = Path(self.tmp.name)
        self.old_db = base / "old.db"
        self.new_db = base / "new.db"

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _args(self) -> argparse.Namespace:
        return argparse.Namespace(
            examples=10,
            removed_severe_threshold=25,
            row_drop_warn_percent=1000.0,
            row_drop_severe_percent=1000.0,
            category_regression_threshold=1,
            muscle_regression_threshold=1,
            de_fallback_shift_threshold=10,
            fail_on_removed_threshold=30,
        )

    def _report(
        self,
        old_ids: Set[str],
        new_ids: Set[str],
        *,
        new_overrides: Optional[Dict[str, Dict[str, Any]]] = None,
        fail_on_removed_threshold: Optional[int] = None,
        map_removals: bool = True,
        new_aliases: Optional[Dict[str, str]] = None,
    ):
        """`map_removals` gibt jeder verschwundenen ID einen Nachfolger.

        Das ist der Normalfall im neuen Schema: geloescht wird nie, es wird
        umgeleitet (SCHEMA.md 3). Ohne das wuerde jeder dieser Tests an
        Invariante 21 haengenbleiben, statt die Schwelle zu pruefen, um die es
        ihm geht.
        """
        if new_aliases is None and map_removals:
            successor = sorted(new_ids)[0] if new_ids else "1"
            new_aliases = {removed: successor for removed in sorted(old_ids - new_ids)}

        _create_catalog(self.old_db, old_ids)
        _create_catalog(self.new_db, new_ids, overrides=new_overrides, aliases=new_aliases)

        old_catalog = MODULE.load_catalog(str(self.old_db))
        new_catalog = MODULE.load_catalog(str(self.new_db))

        args = self._args()
        if fail_on_removed_threshold is not None:
            args.fail_on_removed_threshold = fail_on_removed_threshold

        return MODULE.compare_catalogs(
            old_catalog,
            new_catalog,
            args,
        )

    def test_removed_count_below_threshold_does_not_fail(self):
        old_ids = {str(i) for i in range(1, 901)}
        new_ids = {str(i) for i in range(1, 876)}
        report = self._report(
            old_ids,
            new_ids,
            fail_on_removed_threshold=30,
        )
        should_fail, reasons = MODULE.should_fail(
            report,
            argparse.Namespace(fail_on_removed_threshold=30),
        )
        self.assertEqual(25, report["summary"]["removed_count"])
        self.assertFalse(report["summary"]["removed_threshold_exceeded"])
        self.assertFalse(should_fail)
        self.assertEqual([], reasons)

    def test_removed_count_above_removed_severe_warning_but_below_fail_threshold_does_not_fail(self):
        old_ids = {str(i) for i in range(1, 901)}
        new_ids = {str(i) for i in range(1, 875)}
        report = self._report(
            old_ids,
            new_ids,
            fail_on_removed_threshold=30,
        )
        should_fail, reasons = MODULE.should_fail(
            report,
            argparse.Namespace(fail_on_removed_threshold=30),
        )
        self.assertEqual(26, report["summary"]["removed_count"])
        self.assertFalse(report["summary"]["removed_threshold_exceeded"])
        self.assertFalse(should_fail)
        self.assertEqual([], reasons)

    def test_removed_count_equal_threshold_does_not_fail(self):
        old_ids = {str(i) for i in range(1, 901)}
        new_ids = {str(i) for i in range(1, 871)}
        report = self._report(
            old_ids,
            new_ids,
            fail_on_removed_threshold=30,
        )
        should_fail, reasons = MODULE.should_fail(
            report,
            argparse.Namespace(fail_on_removed_threshold=30),
        )
        self.assertEqual(30, report["summary"]["removed_count"])
        self.assertFalse(report["summary"]["removed_threshold_exceeded"])
        self.assertFalse(should_fail)
        self.assertEqual([], reasons)

    def test_removed_count_above_threshold_fails(self):
        old_ids = {str(i) for i in range(1, 901)}
        new_ids = {str(i) for i in range(1, 870)}
        report = self._report(
            old_ids,
            new_ids,
            fail_on_removed_threshold=30,
        )
        should_fail, reasons = MODULE.should_fail(
            report,
            argparse.Namespace(fail_on_removed_threshold=30),
        )
        self.assertTrue(should_fail)
        self.assertTrue(report["summary"]["removed_threshold_exceeded"])
        self.assertTrue(any("removed_count=" in r for r in reasons))

    def test_severe_regressions_fail_even_when_removed_below_threshold(self):
        report = self._report(
            {str(i) for i in range(1, 101)},
            {str(i) for i in range(1, 100)},
            new_overrides={
                "1": {"name_de": ""},
                "2": {"category_name": ""},
                "3": {"muscles_primary": ""},
            },
            fail_on_removed_threshold=30,
        )
        should_fail, reasons = MODULE.should_fail(
            report,
            argparse.Namespace(fail_on_removed_threshold=30),
        )
        self.assertEqual(1, report["summary"]["removed_count"])
        self.assertFalse(report["summary"]["removed_threshold_exceeded"])
        self.assertTrue(should_fail)
        self.assertTrue(
            any(
                "name regression detected" in reason
                or "severe warning present" in reason
                for reason in reasons
            )
        )

    def test_relational_schema_comparison(self):
        old_ids = {"1", "2", "3"}
        new_ids = {"1", "2", "4"}
        
        _create_catalog(self.old_db, old_ids, relational=True)
        _create_catalog(self.new_db, new_ids, overrides={
            "2": {"category_name": "new_cat"}
        }, relational=True)
        
        old_catalog = MODULE.load_catalog(str(self.old_db))
        new_catalog = MODULE.load_catalog(str(self.new_db))
        
        report = MODULE.compare_catalogs(
            old_catalog,
            new_catalog,
            self._args()
        )
        
        self.assertEqual(1, report["summary"]["removed_count"])
        self.assertEqual(1, report["summary"]["added_count"])
        self.assertEqual(["3"], report["removed_ids"])
        self.assertEqual(["4"], report["added_ids"])
        self.assertEqual("new_cat", report["changed_fields_by_id"]["2"]["category_name"]["new"])

    def test_relational_to_flat_comparison(self):
        old_ids = {"1", "2"}
        new_ids = {"1", "2"}
        
        _create_catalog(self.old_db, old_ids, relational=False)
        _create_catalog(self.new_db, new_ids, overrides={
            "2": {"name_de": "New DE 2"}
        }, relational=True)
        
        old_catalog = MODULE.load_catalog(str(self.old_db))
        new_catalog = MODULE.load_catalog(str(self.new_db))
        
        report = MODULE.compare_catalogs(
            old_catalog,
            new_catalog,
            self._args()
        )
        self.assertEqual("New DE 2", report["changed_fields_by_id"]["2"]["name_de"]["new"])


if __name__ == "__main__":
    unittest.main()


class SchemaV2DiffTests(unittest.TestCase):
    """Die Regeln, die mit SCHEMA.md 8 dazugekommen sind."""

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        base = Path(self.tmp.name)
        self.old_db = base / "old.db"
        self.new_db = base / "new.db"

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def _args(self) -> argparse.Namespace:
        return argparse.Namespace(
            examples=10,
            removed_severe_threshold=25,
            row_drop_warn_percent=1000.0,
            row_drop_severe_percent=1000.0,
            category_regression_threshold=1,
            muscle_regression_threshold=1,
            de_fallback_shift_threshold=10,
            fail_on_removed_threshold=30,
        )

    def _compare(self, **kwargs):
        old = MODULE.load_catalog(str(self.old_db))
        new = MODULE.load_catalog(str(self.new_db))
        report = MODULE.compare_catalogs(old, new, self._args())
        should_fail, reasons = MODULE.should_fail(
            report, argparse.Namespace(fail_on_removed_threshold=30)
        )
        return report, should_fail, reasons

    def _codes(self, report) -> Set[str]:
        return {warning["code"] for warning in report["warning_flags"]}

    # -- Invariante 21 ------------------------------------------------------
    def test_invariant_21_a_single_unmapped_removal_is_breaking(self):
        """Eine ID ohne Nachfolger macht die Logs auf ihr unaufloesbar. Das ist
        kein Schwellwertthema — eine reicht."""
        _create_catalog(self.old_db, {str(i) for i in range(1, 901)})
        _create_catalog(self.new_db, {str(i) for i in range(2, 901)}, aliases={})
        report, should_fail, reasons = self._compare()
        self.assertEqual(1, report["summary"]["unmapped_removed_count"])
        self.assertEqual(["1"], report["unmapped_removed_ids"])
        self.assertIn("INVARIANT_21_UNMAPPED_REMOVAL", self._codes(report))
        self.assertTrue(should_fail)
        self.assertTrue(any("invariant 21" in reason for reason in reasons))

    def test_invariant_21_is_satisfied_by_an_alias(self):
        _create_catalog(self.old_db, {str(i) for i in range(1, 901)})
        _create_catalog(self.new_db, {str(i) for i in range(2, 901)}, aliases={"1": "2"})
        report, should_fail, _ = self._compare()
        self.assertEqual(0, report["summary"]["unmapped_removed_count"])
        self.assertNotIn("INVARIANT_21_UNMAPPED_REMOVAL", self._codes(report))
        self.assertFalse(should_fail)

    # -- Invariante 22 ------------------------------------------------------
    def test_invariant_22_active_count_drop_above_five_percent_is_breaking(self):
        old_ids = {str(i) for i in range(1, 101)}
        new_ids = {str(i) for i in range(1, 94)}  # -7 %
        _create_catalog(self.old_db, old_ids)
        _create_catalog(self.new_db, new_ids, aliases={i: "1" for i in old_ids - new_ids})
        report, should_fail, _ = self._compare()
        self.assertIn("INVARIANT_22_ACTIVE_COUNT_DROP", self._codes(report))
        self.assertTrue(should_fail)

    def test_invariant_22_tolerates_a_small_drop(self):
        old_ids = {str(i) for i in range(1, 101)}
        new_ids = {str(i) for i in range(1, 98)}  # -3 %
        _create_catalog(self.old_db, old_ids)
        _create_catalog(self.new_db, new_ids, aliases={i: "1" for i in old_ids - new_ids})
        report, should_fail, _ = self._compare()
        self.assertNotIn("INVARIANT_22_ACTIVE_COUNT_DROP", self._codes(report))
        self.assertFalse(should_fail)

    # -- Versionsvertrag ----------------------------------------------------
    def test_schema_version_must_not_go_backwards(self):
        ids = {"1", "2", "3"}
        _create_catalog(self.old_db, ids, schema_version=2)
        _create_catalog(self.new_db, ids, schema_version=1)
        report, should_fail, _ = self._compare()
        self.assertIn("SCHEMA_VERSION_REGRESSION", self._codes(report))
        self.assertTrue(should_fail)

    def test_schema_version_may_go_forwards(self):
        ids = {"1", "2", "3"}
        _create_catalog(self.old_db, ids, schema_version=1)
        _create_catalog(self.new_db, ids, schema_version=2)
        report, should_fail, _ = self._compare()
        self.assertNotIn("SCHEMA_VERSION_REGRESSION", self._codes(report))
        self.assertFalse(should_fail)

    def test_a_missing_schema_version_on_one_side_is_not_a_regression(self):
        """Der Vergleich v1-Release gegen v2-Build ist der Normalfall beim
        Umstieg und darf nicht rot sein."""
        ids = {"1", "2", "3"}
        _create_catalog(self.old_db, ids)
        _create_catalog(self.new_db, ids, schema_version=2)
        report, should_fail, _ = self._compare()
        self.assertNotIn("SCHEMA_VERSION_REGRESSION", self._codes(report))
        self.assertFalse(should_fail)


if __name__ == "__main__":
    unittest.main(verbosity=2)
