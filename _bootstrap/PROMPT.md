# Startprompt für den neuen Chat im openexercisedb-Ordner

Im neuen Ordner `claude` starten und Folgendes eingeben:

---

Das hier ist openexercisedb, ein neues öffentliches Repo: ein Fork der
wger-Übungsdaten, der die Datenqualität deutlich verbessern soll. Repo und
Spezifikation sind vorbereitet, aber es gibt noch keine Daten und keinen Code.

Lies zuerst `SCHEMA.md` (die Spezifikation), dann `_bootstrap/HANDOFF.md`
(was aus dem App-Repo mitkommt und welche Zwänge die konsumierende App setzt)
und `schema/invariants.md`. Die geschlossenen Vokabulare liegen in `vocab/`,
eine vollständig annotierte Beispielübung in `examples/`.

Deine Aufgabe ist **Phase 1: der Import**. Ziel ist ausdrücklich noch keine
inhaltliche Verbesserung, sondern ein sauberer Umbau der Pipeline ohne
Verhaltensänderung:

1. `_bootstrap/legacy-pipeline/script/create_wger_exercise_db.py` in zwei
   Teile zerlegen:
   - `import/wger_to_yaml.py` — holt die wger-API einmalig ab und schreibt
     `data/exercises/<id>.yaml` plus `data/i18n/<lang>/<id>.yaml`. Die
     bestehenden Muskelwerte werden über `legacy_wger_mapping` in
     `vocab/muscles.yaml` auf das neue Vokabular abgebildet. `license` und
     `license_author` sind **pro Übersetzung** zu übernehmen (SCHEMA.md §3b) —
     das verwirft das alte Skript heute, und genau das ist zu beheben.
     Felder, die wger nicht liefert (`primary_equipment`, `tracking_type`,
     `modality`, …), bleiben leer bzw. bekommen einen dokumentierten
     Default; sie sind Phase 2.
   - `build/build_db.py` — baut aus den YAML-Dateien die SQLite-Datei nach dem
     Schema in SCHEMA.md §8, inklusive der vier Kompatibilitätsspalten.
2. Einen Validator schreiben, der die Invarianten aus `schema/invariants.md`
   prüft, soweit sie mit den in Phase 1 vorhandenen Daten prüfbar sind, und
   ihn als GitHub-Workflow einhängen. `_bootstrap/legacy-pipeline/workflows/`
   ist die Vorlage für den Release-Teil; der wöchentliche Cron entfällt, weil
   der Build nicht mehr live von wger zieht.
3. `_bootstrap/legacy-pipeline/script/wger_catalog_diff.py` und
   `check_database.py` übernehmen und auf das neue Schema erweitern.

**Abnahmekriterium:** Die erzeugte `.db` enthält dieselben Übungs-IDs wie die
Referenz-DB, und die Kompatibilitätsspalten `id`, `category_name`,
`muscles_primary`, `muscles_secondary` plus `exercise_translations` sind so
befüllt, dass eine bestehende konsumierende App sie ohne Codeänderung laden würde.
Baue dafür einen Test, der genau das prüft.

Bevor du anfängst: Sag mir, was dir an der Spezifikation unklar oder
widersprüchlich ist. Danach leg einen Plan vor, bevor du Code schreibst.

---

## Was danach kommt (nicht Teil des ersten Chats)

- **Phase 2 — Inhalt.** Golden Set aufbauen, dann die KI-Pipeline. Reihenfolge:
  die 189 leeren Muskelzuweisungen, dann Equipment und `tracking_type`, dann
  `modality`/`usage_tags`, dann Muskel-Feinschliff, zuletzt Texte.
- **Phase 3 — Schema v2 in der App.** Die Änderungsliste steht in SCHEMA.md §10.
- **Phase 4 — Erstes öffentliches Release.**

## Noch offen, bevor das Repo public geht

- Der GitHub-Handle im `ATTRIBUTION.md`-Beispiel und in der README-URL ist auf
  `rfivesix/openexercisedb` geraten — anpassen, falls das Repo woanders liegt.
- `LICENSE.md` einmal rechtlich gegenprüfen lassen (CC-BY-SA 3.0 → 4.0).
- Eigenes Ticket im App-Repo: die heute ausgelieferte DB enthält keinerlei
  Lizenz- und Autorenangaben. Das ist unabhängig von diesem Fork zu beheben.
