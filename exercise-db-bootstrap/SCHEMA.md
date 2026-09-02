# Exercise Database — Schema

Version: **Entwurf 0.1** · Stand 2026-09-02 · Ziel-Schemaversion des Builds: **2**

Dieses Dokument definiert das Datenmodell der geforkten Übungsdatenbank: die
Quellformate im Repo, das erzeugte SQLite-Artefakt und den Vertrag zur
konsumierenden App.

---

## 1. Warum überhaupt ein neues Schema

Gemessen am aktuellen Bestand (852 Übungen aus `wger`):

| Befund | Zahl |
|---|---|
| Übungen **ohne jede** Muskelzuweisung | **189** (22 %) |
| Übungen ohne *primäre* Muskelzuweisung | 194 (23 %) |
| Distinkte Muskelwerte im gesamten Bestand | **15** |
| Beschreibungen leer (de/en) | je 12 |
| Beschreibungen < 40 Zeichen | 32 (de) / 35 (en) |

Die 15 Werte sind: `Chest`, `Lats`, `Trapezius`, `Serratus anterior`,
`Shoulders`, `Biceps`, `Brachialis`, `Triceps`, `Abs`,
`Obliquus externus abdominis`, `Glutes`, `Quads`, `Hamstrings`, `Calves`,
`Soleus`. Das Vokabular mischt grobe Gruppen mit anatomischen Einzelnamen, hat
keine Delt-Aufteilung, und kennt Unterarme, Adduktoren, Rückenstrecker,
Rotatorenmanschette und Rhomboiden überhaupt nicht — die App-seitige
Alias-Map in `recovery_domain_service.dart` hat Einträge dafür, aber die Daten
liefern sie nie.

Dazu die eigentliche Kostenstelle: `majorMuscleGroupFor()` gibt bei unbekannten
Muskeln stillschweigend `null` zurück, und die Übung fällt aus Recovery und
Volumenstatistik heraus. Zusammen mit den 189 leeren Zuweisungen heißt das:
**ein signifikanter Teil des geloggten Trainingsvolumens landet heute nirgends.**

Zweites Strukturproblem: `category_name` ist gleichzeitig Körperregion
(`Legs`, `Back`, `Arms`, …) *und* Trainingsart (`Cardio`). Deshalb ist
`Exercise.isCardio` heute ein String-Vergleich auf einem Feld, das eigentlich
eine Körperregion beschreibt — und die Log-Maske hängt daran.

---

## 2. Grundprinzipien

1. **Source of Truth sind Textdateien, nicht die `.db`.** Eine Datei je Übung,
   in git, diffbar, per PR beitragbar. Die SQLite-Datei ist reines
   Build-Artefakt und liegt ausschließlich im Release.
2. **Geschlossene Vokabulare.** Jedes klassifizierende Feld referenziert eine
   `vocab/*.yaml`. Freitext gibt es nur in Übersetzungen.
3. **Orthogonale Achsen.** Was eine Übung *ist*, *wofür* sie eingesetzt wird,
   *womit* sie ausgeführt wird und *wie* sie geloggt wird, sind vier
   verschiedene Felder.
4. **Sprachneutrale Fakten und Texte sind getrennt.** Übersetzer fassen nie
   Muskeldaten an, Datenpflege fasst nie Texte an.
5. **Beliebig viele Sprachen ohne Schema-Änderung.** Eine neue Sprache ist ein
   Eintrag in `vocab/languages.yaml` plus ein Verzeichnis.
6. **Nichts wird hart gelöscht.** IDs sind ein Vertrag mit Nutzerdaten
   (siehe §3).
7. **Herkunft ist pro Feld dokumentiert.** Ohne das ist "prüf nochmal alle
   KI-Muskelzuweisungen von Modell X" Archäologie statt Query.

---

## 3. Der ID-Vertrag — der Teil, der nicht nachrüstbar ist

In der App referenzieren `routine_exercises.exercise_id` und
`set_logs.exercise_id` direkt `exercises.id`
(`lib/data/drift_database.dart:111` und `:163`). **Die Nutzerdaten hängen also
an den IDs dieser Datenbank.** Jede Zusammenlegung, Umbenennung oder Löschung
ist potenziell Datenverlust auf Geräten da draußen.

**Format der IDs:** Der Bestand nutzt die numerischen wger-IDs als TEXT,
Wertebereich aktuell 1000–1972 — *keine* UUIDs. Daraus folgt:

- **Übernommene Übungen behalten ihre numerische ID unverändert.** Nie neu
  vergeben, nie normalisieren, nie auf UUID umstellen.
- **Neue eigene Übungen** bekommen `x-` + 12 Hexzeichen (gekürzte UUIDv5 über
  den Slug). Das Präfix garantiert, dass sie nie mit einer künftigen
  wger-ID kollidieren, und ist deterministisch reproduzierbar.
- **Löschen ist verboten.** Stattdessen `status: deprecated` — die Zeile bleibt
  in der DB, verschwindet nur aus Suche und Katalog. Bestehende Logs bleiben
  auflösbar.
- **Zusammenlegen** läuft über `status: merged` + `merged_into`. Der Build
  erzeugt daraus eine `exercise_aliases`-Tabelle, die mit ausgeliefert wird;
  die App wendet sie beim Import auf `routine_exercises` und `set_logs` an.
  Erst das macht Dedupe — den größten Aufräumgewinn — gefahrlos.
- **Alias-Ketten sind verboten** (Invariante 7). Wird B nach C gemerged und war
  A schon auf B gemerged, zeigen danach beide direkt auf C.

---

## 4. Repo-Layout

```
data/exercises/<id>.yaml           # sprachneutrale Fakten, eine Datei je Übung
data/i18n/<lang>/<id>.yaml         # Texte, eine Datei je Übung je Sprache
vocab/muscles.yaml                 # hierarchisches Muskel-Vokabular
vocab/equipment.yaml               # primary_equipment + setup
vocab/classification.yaml          # modality, usage_tags, tracking_type, …
vocab/languages.yaml               # Sprach-Registry
schema/exercise.schema.json        # CI-Validierung Fakten
schema/translation.schema.json     # CI-Validierung Texte
schema/invariants.md               # inhaltliche Regeln, CI-Gate
test/golden/*.yaml                 # ~50 handgeprüfte Übungen als Eval-Set
build/                             # YAML -> .db + manifest + reports
import/                            # Einmal-Importer wger -> YAML
```

---

## 5. Muskelmodell

Hierarchisch, drei Ebenen: **group → muscle → head**. Aktuell 14 Gruppen,
32 Muskeln, 22 Köpfe = 68 Knoten (`vocab/muscles.yaml`).

**Eine Übung darf auf jeder Ebene referenzieren.** Wer sich beim Kopf nicht
sicher ist, annotiert den Muskel; wer sich beim Muskel nicht sicher ist, die
Gruppe. Das löst das Review-Kostenproblem der feinen Granularität, ohne
Genauigkeit vorzutäuschen, die nicht da ist: eine Angabe auf Gruppenebene ist
eine ehrliche Angabe, eine geratene Kopfebene wäre eine Lüge.

Auflösung nach oben ist immer definiert. Statistik und Recovery rechnen auf
`group`, Filter und Body-Highlighter dürfen feiner gehen. Abfragen wie
„welche Übungen haben noch keine Kopf-Genauigkeit?" sind damit trivial und
steuern den Review.

`role` ist `primary` oder `secondary`. Das optionale Feld `contribution`
(0…1) ist im Schema vorgesehen, wird in v1 aber **bewusst nicht befüllt** —
solange 189 Übungen gar keine Muskeln haben, wäre eine Diskussion über
Nachkommastellen die falsche Arbeit.

Zwei Zuordnungen weichen bewusst von der heutigen App-Map ab und sind in
`vocab/muscles.yaml` als `legacy_group` vermerkt: `serratus_anterior`
(App: `back`) und `hip_flexors` (App: `glutes`). Der Build schreibt für die
Kompatibilitätsspalten weiterhin die Legacy-Gruppe.

---

## 6. Klassifikation

| Feld | Kardinalität | Zweck |
|---|---|---|
| `modality` | genau 1 | Was die Übung *ist*: strength, cardio, plyometric, mobility, stretch, balance |
| `usage_tags` | ≥ 1 | Wofür sie *eingesetzt* wird: warmup, activation, main_lift, accessory, conditioning, finisher, cooldown, prehab |
| `mechanic` | genau 1 | compound / isolation |
| `force_vector` | genau 1 | push / pull / static |
| `movement_pattern` | genau 1 | 24 Muster, von `vertical_pull` bis `anti_rotation` |
| `laterality` | genau 1 | bilateral / unilateral / alternating |
| `difficulty` | optional | beginner / intermediate / advanced |
| `tracking_type` | genau 1 | bestimmt die Log-Maske |
| `primary_equipment` | genau 1 | das lasterzeugende Gerät |
| `setup` | 0…n | was außerdem dastehen muss |

`usage_tags` ist mehrwertig, weil ein leichtes Band-Pull-Apart legitim
Warm-up *und* Accessory ist. Ein einwertiges Feld würde hier zu willkürlichen
Entscheidungen zwingen.

Die Trennung `primary_equipment` / `setup` ist der Grund, warum „Was kann ich
im Hotelzimmer machen?" filterbar wird: `primary_equipment == bodyweight`
**und** `setup == []`.

`tracking_type` (`weight_reps`, `bodyweight_reps`, `time`, `time_weight`,
`distance_time`, `distance_only`) plus die Flags `supports_added_weight` und
`supports_assistance` ersetzen `Exercise.isCardio`. Damit bekommen Plank
(Zeit), Klimmzug (Wiederholungen, optional Zusatzgewicht *oder* Unterstützung)
und Laufband (Distanz + Zeit) endlich die richtige Eingabemaske.

`body_region` wird aus den Primärmuskeln **abgeleitet** und nicht von Hand
gepflegt — dann kann sie auch nicht mehr widersprüchlich werden.

---

## 7. Übersetzungen

Eine Datei je Übung je Sprache unter `data/i18n/<lang>/<id>.yaml`. Felder:
`name`, `description`, `instructions[]`, `cues[]`, `common_mistakes[]`,
`search_terms[]`.

- `instructions` ist bewusst eine Schrittliste, getrennt vom Fließtext — die
  App kann sie dann als Schritte rendern statt als Absatz.
- `search_terms` sind Synonyme und gängige Falschschreibungen. Gehen in den
  Suchindex, werden nie angezeigt.
- `status` je Dokument: `human` | `ai_reviewed` | `ai_raw`. Damit lässt sich
  später gezielt nachbessern, statt pauschal zu misstrauen.

**Beliebig viele Sprachen:** `vocab/languages.yaml` ist die Registry. Eine
neue Sprache = ein Eintrag + ein Verzeichnis. Kein Schema-Change, kein
App-Change, kein Build-Change. Sprachen tragen ein `tier`
(`curated` / `assisted` / `machine`); nur `curated` blockiert den Release bei
Lücken. Der Build rechnet je Sprache die `completeness` aus und schreibt sie in
die `languages`-Tabelle, damit die App nicht selbst zählen muss.

Nirgends im Schema existiert eine Spalte `name_de` oder `name_en`. Das ist die
Bedingung dafür, dass „beliebig viele" wirklich stimmt — und zugleich die
größte App-seitige Änderung (§10).

---

## 8. Erzeugtes SQLite-Artefakt (Schema-Version 2)

```sql
-- Kern
CREATE TABLE exercises (
  id                    TEXT PRIMARY KEY,
  slug                  TEXT NOT NULL UNIQUE,
  status                TEXT NOT NULL,          -- active | deprecated | merged
  merged_into           TEXT REFERENCES exercises(id),
  modality              TEXT NOT NULL,
  mechanic              TEXT NOT NULL,
  force_vector          TEXT NOT NULL,
  movement_pattern      TEXT NOT NULL,
  laterality            TEXT NOT NULL,
  difficulty            TEXT,
  tracking_type         TEXT NOT NULL,
  supports_added_weight INTEGER NOT NULL DEFAULT 0,
  supports_assistance   INTEGER NOT NULL DEFAULT 0,
  primary_equipment     TEXT NOT NULL,
  body_region           TEXT,                   -- abgeleitet aus Primärmuskeln

  -- Kompatibilitätsspalten für Schema-v1-Konsumenten (heutige App).
  -- Der Importer in basis_data_manager.dart liest GENAU diese vier Felder
  -- plus die Übersetzungen. Solange sie befüllt sind, läuft die heutige App
  -- unverändert auf einer v2-Datenbank.
  category_name         TEXT,
  muscles_primary       TEXT,                   -- JSON-Array, Legacy-Namen
  muscles_secondary     TEXT,                   -- JSON-Array, Legacy-Namen
  image_path            TEXT,                   -- immer NULL, es gibt keine Medien
  is_custom             INTEGER NOT NULL DEFAULT 0,
  created_by            TEXT DEFAULT 'system',
  source                TEXT DEFAULT 'base'
);

CREATE TABLE exercise_muscles (
  exercise_id  TEXT NOT NULL REFERENCES exercises(id) ON DELETE CASCADE,
  muscle_id    TEXT NOT NULL REFERENCES muscles(id),
  role         TEXT NOT NULL,                   -- primary | secondary
  contribution REAL,                            -- v1: NULL
  PRIMARY KEY (exercise_id, muscle_id)
);

CREATE TABLE exercise_equipment (
  exercise_id  TEXT NOT NULL REFERENCES exercises(id) ON DELETE CASCADE,
  equipment_id TEXT NOT NULL REFERENCES equipment(id),
  kind         TEXT NOT NULL,                   -- primary | setup
  PRIMARY KEY (exercise_id, equipment_id, kind)
);

CREATE TABLE exercise_tags (
  exercise_id TEXT NOT NULL REFERENCES exercises(id) ON DELETE CASCADE,
  tag         TEXT NOT NULL,                    -- aus usage_tags
  PRIMARY KEY (exercise_id, tag)
);

-- Übersetzungen: Struktur wie heute, additiv erweitert.
CREATE TABLE exercise_translations (
  id              TEXT PRIMARY KEY,             -- "<exercise_id>_<lang>"
  exercise_id     TEXT NOT NULL REFERENCES exercises(id) ON DELETE CASCADE,
  language_code   TEXT NOT NULL,
  name            TEXT NOT NULL,
  description     TEXT,
  instructions    TEXT,                         -- JSON-Array
  cues            TEXT,                         -- JSON-Array
  common_mistakes TEXT,                         -- JSON-Array
  search_terms    TEXT,                         -- JSON-Array
  status          TEXT,                         -- human | ai_reviewed | ai_raw
  source_lang     TEXT
);
CREATE INDEX idx_tr_exercise_lang ON exercise_translations(exercise_id, language_code);

-- Vokabulare, mitgeliefert statt in der App hartkodiert
CREATE TABLE muscles (
  id          TEXT PRIMARY KEY,
  parent_id   TEXT REFERENCES muscles(id),
  level       TEXT NOT NULL,                    -- group | muscle | head
  group_id    TEXT NOT NULL REFERENCES muscles(id),
  legacy_group TEXT,
  body_slugs  TEXT                              -- JSON-Array
);
CREATE TABLE muscle_translations   (muscle_id TEXT, language_code TEXT, name TEXT, PRIMARY KEY (muscle_id, language_code));
CREATE TABLE equipment             (id TEXT PRIMARY KEY, kind TEXT NOT NULL);
CREATE TABLE equipment_translations(equipment_id TEXT, language_code TEXT, name TEXT, PRIMARY KEY (equipment_id, language_code));

CREATE TABLE languages (
  code         TEXT PRIMARY KEY,
  tier         TEXT NOT NULL,
  completeness REAL NOT NULL,
  displayable  INTEGER NOT NULL
);

-- Der Migrationspfad für Nutzerdaten
CREATE TABLE exercise_aliases (
  old_id        TEXT PRIMARY KEY,
  new_id        TEXT NOT NULL REFERENCES exercises(id),
  reason        TEXT,                           -- merged | renamed_id | split
  since_version TEXT NOT NULL
);

CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT);
-- Pflichtschlüssel: version, schema_version, generated_at, source_repo,
--                   source_commit, license, attribution
```

Die Vokabulare wandern damit **aus der App in die Daten**. `body_slug_mapper.dart`
und die 70-Einträge-Alias-Map in `recovery_domain_service.dart` werden zu einem
Legacy-Fallback für Altdaten und selbst angelegte Übungen — sie sind dann nicht
mehr der Ort, an dem Anatomie definiert wird.

---

## 9. Manifest- und Versionsvertrag

Das heutige Manifest (`assets/db/wger_catalog_manifest.json`) kennt nur eine
Inhalts-`version` (Zeitstempel). Dazu kommt ein **unabhängiges**
`schema_version` (ganzzahlig, monoton):

```jsonc
{
  "version": "202609021047",     // Inhalt
  "schema_version": 2,           // Struktur  <-- neu
  "min_app_schema_version": 1,   // ältester Konsument, der das lesen kann
  // … db_url, db_sha256, expected_exercise_count, min_exercise_count, safety …
}
```

Die App deklariert, welche `schema_version` sie unterstützt, und
`exercise_catalog_refresh_service.dart` lehnt ein zu neues Release sauber ab,
statt es zu laden und daran zu scheitern. Alte Installationen bleiben auf dem
letzten kompatiblen Release stehen — genau das gewünschte Verhalten.

Der `beta`-Channel, den das Manifest schon vorsieht, wird damit nützlich:
Schema-Änderungen gehen zuerst nach `beta`, die unterstützende App-Version geht
ins Store-Review, erst danach wandert das Release nach `stable`.

Als Vertrag zwischen den Repos werden zwei Artefakte gepflegt: das JSON-Schema
des Manifests und eine kleine Fixture-DB, die das App-Repo in seinen Tests
gegen den Importer laufen lässt. Dann bricht ein Schema-Fehler in der CI und
nicht auf dem Gerät.

---

## 10. Was sich App-seitig ändern muss

In grober Reihenfolge:

1. **Übersetzungen locale-generisch.** `Exercise.nameDe` / `nameEn` /
   `descriptionDe` / `descriptionEn` weichen einer Map `locale -> Texte` mit
   Fallback-Kette. Das ist die Voraussetzung für „beliebig viele Sprachen" und
   betrifft `exercise.dart`, `exercises_queries.dart` und alle Aufrufer von
   `getLocalizedName`.
2. Drift-Schema um die neuen Spalten und Tabellen erweitern + Migration.
3. Importer in `basis_data_manager.dart` (`_mapExerciseBundle`) auf die neuen
   Tabellen erweitern; die vier Legacy-Felder bleiben als Fallback.
4. `exercise_aliases` beim Import auf `routine_exercises` und `set_logs`
   anwenden.
5. `Exercise.isCardio` → `trackingType`, und die davon abhängige Log-Maske.
6. `_majorGroupMap` und `BodySlugMapper` auf die mitgelieferten Vokabulare
   umstellen, Hartkodierung zum Legacy-Fallback degradieren.
7. Equipment-Filter im Katalog-Screen (neu).
8. `usage_tags` in der Routinen-Erstellung nutzen.
9. `schema_version`-Prüfung im Refresh-Service.

Punkte 1–5 sind Pflicht für Schema v2. 6–8 sind der eigentliche Produktgewinn
und können nachziehen.

---

## 11. Arbeitsweise für die KI-gestützte Inhaltsarbeit

Bei 852 Übungen × ~10 Feldern werden ~8.500 Behauptungen über Anatomie
erzeugt. Bei 5 % Fehlerquote sind das 400 falsche Muskelzuweisungen — und die
sind **schlimmer als die heutigen 189 Lücken**, weil eine Lücke sichtbar ist
und eine falsche Zuweisung plausibel aussieht. Deshalb:

- **Provenance pro Feld**, wie im Beispiel `examples/exercises/475.yaml`.
- **Invarianten als CI-Gate** (`schema/invariants.md`), nicht als
  Review-Aufgabe. Sie fangen den mechanischen Anteil der Fehler ab.
- **Golden Set**: ~50 handgeprüfte Übungen quer über alle Muskelgruppen und
  Equipment-Typen. Jeder Prompt-Durchlauf wird zuerst dagegen evaluiert.
  Ohne das optimiert man blind.
- **Review gruppenweise, nicht alphabetisch.** Fehler clustern nach
  Muskelgruppe und Equipment — 40 Rudervarianten am Stück zu prüfen geht
  schnell, weil der Vergleich direkt danebensteht. Alphabetisch dauert es ein
  Vielfaches.
- **Reihenfolge**: zuerst die 189 Übungen ganz ohne Muskeln. Größter messbarer
  Effekt bei kleinstem Risiko — und man sieht früh, wie gut die Pipeline
  überhaupt ist.
- **Die KI fasst `id` und `slug` nie an.**

---

## 12. Offene Punkte

- **Lizenz.** wger-Übungsdaten stehen unter CC-BY-SA. Der Fork erbt
  Attribution und Share-Alike. `LICENSE` + `ATTRIBUTION.md` müssen im ersten
  Commit stehen, weil das Repo von Anfang an öffentlich ist.
- **Repo-Name** und ob die App-Releases (`wger-catalog-stable`) mit
  umziehen oder das neue Repo eigene Release-Tags bekommt. Empfehlung: eigene
  Tags im neuen Repo, Manifest-URL in der App umbiegen, der bestehende
  Legacy-Fallback in `exercise_catalog_refresh_service.dart` deckt den
  Übergang ab.
- **`contribution`-Gewichte**: Zeitpunkt der Einführung, frühestens nach
  stabilen Zuweisungen.
- **Kategorie-Ableitung**: exakte Regel für `body_region` aus den
  Primärmuskeln bei Übungen mit Primärmuskeln aus mehreren Gruppen.
