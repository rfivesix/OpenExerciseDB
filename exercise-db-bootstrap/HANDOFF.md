# Handoff — Bootstrap für das neue Übungsdatenbank-Repo

Dieser Ordner ist **zum Herausnehmen gedacht**. Er enthält alles, was das neue,
öffentliche Repo braucht, damit dort in einem eigenen Chat ohne Zugriff auf
`train-libre` weitergearbeitet werden kann. Nach dem Umzug kann er hier
gelöscht werden — er gehört nicht dauerhaft ins App-Repo.

## Inhalt

```
SCHEMA.md                    # die Spezifikation. Zuerst lesen.
vocab/muscles.yaml           # 14 Gruppen / 32 Muskeln / 22 Köpfe + wger-Legacy-Mapping
vocab/equipment.yaml         # 17 primary_equipment, 19 setup
vocab/classification.yaml    # modality, usage_tags, tracking_type, movement_pattern, …
vocab/languages.yaml         # Sprach-Registry, beliebig erweiterbar
schema/exercise.schema.json  # CI-Validierung sprachneutrale Fakten
schema/translation.schema.json
schema/invariants.md         # 23 inhaltliche Regeln als CI-Gate
examples/                    # eine vollständig annotierte Beispielübung (475, Klimmzug)
from-train-libre/            # der bestehende Pipeline-Code, siehe unten
```

## Was aus `train-libre` mitkommt und was damit zu tun ist

| Datei | Rolle heute | Rolle im neuen Repo |
|---|---|---|
| `script/create_wger_exercise_db.py` (594 Z.) | zieht live von `wger.de/api/v2` und schreibt die `.db` | **aufspalten**: `import/wger_to_yaml.py` (Einmal-Import in Quelldateien) und `build/build_db.py` (YAML → `.db`). Der Live-Fetch verschwindet aus dem Build. |
| `script/wger_catalog_diff.py` (576 Z.) | Diff zweier Katalog-DBs, Breaking-Change-Erkennung | **übernehmen und erweitern** um die neuen Tabellen. Deckt Invarianten 21–22 ab. |
| `script/tests/test_wger_catalog_diff.py` | Tests dazu | übernehmen |
| `script/build_wger_catalog_manifest.py` | erzeugt das Manifest | übernehmen, `schema_version` + `min_app_schema_version` ergänzen (SCHEMA.md §9) |
| `script/build_wger_release_notes.py` | Release Notes | übernehmen |
| `script/publish_wger_run_summary.py` | GitHub-Step-Summary | übernehmen |
| `script/resolve_wger_reference_manifest.py` | löst das Referenz-Release für den Diff auf | übernehmen |
| `script/check_database.py` | Sanity-Check auf der erzeugten DB | übernehmen, um die neuen Tabellen erweitern |
| `.github/workflows/wger-catalog-refresh.yml` | wöchentlicher Cron + Release-Publish | **Vorlage** für den neuen Build-Workflow. Der Cron entfällt (kein Live-Fetch mehr); der Trigger wird Push auf `main` + `workflow_dispatch`. Der Release-Publish-Teil bleibt fast unverändert. |
| `assets/db/wger_catalog_manifest.json` | ausgeliefertes Manifest | Referenz für das neue Manifest-Format |

Die Umgebungsvariablen des Workflows (`RELEASE_TAG`, `RELEASE_CHANNEL`,
`WGER_FAIL_ON_REMOVED_THRESHOLD` = 30, `RELEASE_DOWNLOAD_BASE`, …) zeigen den
kompletten Release-Vertrag, den die App heute erwartet — die Datei ist die
beste Dokumentation davon.

## Fakten aus der App, die im neuen Repo gebraucht werden

Damit dort niemand raten muss:

- **IDs sind numerische Strings**, Wertebereich 1000–1972, 852 Stück. Keine UUIDs.
- **`exercises.id` ist ein Fremdschlüssel in Nutzerdaten**:
  `routine_exercises.exercise_id` und `set_logs.exercise_id`
  (`lib/data/drift_database.dart:111` / `:163`). Deshalb §3 in SCHEMA.md.
- **Der App-Importer liest exakt vier Spalten** aus `exercises`: `id`,
  `category_name`, `muscles_primary`, `muscles_secondary` — plus die
  `exercise_translations` (`_mapExerciseBundle` in
  `lib/core/infrastructure/basis_data_manager.dart:1877`). Solange diese
  befüllt bleiben, läuft die heutige App unverändert auf einer v2-Datenbank.
  **Das ist die Abnahmeschwelle für Phase 1.**
- **Unbekannte Muskelnamen werden still verworfen**
  (`majorMuscleGroupFor` → `null`, `recovery_domain_service.dart:368`).
  Kein Fehler, keine Warnung — die Übung fällt einfach aus der Statistik.
- **Die 13 kanonischen Gruppen der App** stehen in `_majorGroupMap`
  (`recovery_domain_service.dart:156`). `vocab/muscles.yaml` bildet sie ab und
  ergänzt `neck` als 14. Gruppe.
- **Body-Highlighter-Slugs** kommen aus `flutter_body_highlighter`, gepinnt auf
  `rfivesix/flutter_body_highlighter@a8503b0a`. 21 Muskel-Slugs; `lats`,
  `rhomboids`, `serratus` und `rotator_cuff` haben dort keine eigene Fläche.
  Deshalb ist `body_slugs` in `vocab/muscles.yaml` eine Liste und darf leer sein.
- **Ausgangslage inhaltlich**: 189 Übungen ohne jede Muskelzuweisung, 194 ohne
  primäre, 15 distinkte Muskelwerte insgesamt, 12 leere Beschreibungen je
  Sprache. Übersetzungen: en 852, de 852, fr 264, ja 48, it 10.

## Vorgehen im neuen Repo

1. **Phase 0 — Setup.** Repo anlegen, `LICENSE` (CC-BY-SA, geerbt) +
   `ATTRIBUTION.md`, diesen Ordner hineinkopieren, `SCHEMA.md` als Spec
   verabschieden.
2. **Phase 1 — Import ohne Verhaltensänderung.** `create_wger_exercise_db.py`
   zu `import/wger_to_yaml.py` umbauen, 852 YAML-Dateien + i18n-Dateien
   erzeugen, `build/build_db.py` schreiben. **Abnahme: die erzeugte `.db` hat
   dieselben 852 IDs und lädt in der heutigen App ohne eine Zeile
   Codeänderung.** Ab hier ist alles Weitere gefahrlos.
3. **Phase 2 — Inhalt.** Invarianten + Golden Set aufsetzen, dann die
   KI-Pipeline. Reihenfolge: die 189 leeren Zuweisungen, dann Equipment und
   `tracking_type`, dann `modality`/`usage_tags`, dann Muskel-Feinschliff,
   zuletzt Texte. Schema bleibt v1-kompatibel, App unangetastet.
4. **Phase 3 — Schema v2.** Neue Tabellen im Build, App-Änderungen aus
   SCHEMA.md §10, Ausrollen über den `beta`-Channel.
5. **Phase 4 — Umschalten.** Manifest-URL in der App umbiegen. Der
   Legacy-Fallback in `exercise_catalog_refresh_service.dart` deckt alte
   Clients ab.

Phase 2 und 3 sind zeitlich entkoppelt — das ist der Grund für das eigene Repo.

## Vor Phase 1 zu klären

- Repo-Name und ob die Release-Tags mit umziehen oder neu vergeben werden.
- Lizenztext und Formulierung der wger-Attribution.
- Ob `fr`/`ja`/`it` aus dem Bestand übernommen oder verworfen und neu erzeugt
  werden. Die 10 italienischen Einträge sind aktuell eher Ballast.
