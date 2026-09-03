# Exercise Database — Schema

Version: **Entwurf 0.1** · Stand 2026-09-02 · Ziel-Schemaversion des Builds: **2**

Dieses Dokument definiert das Datenmodell der geforkten Übungsdatenbank: die
Quellformate im Repo, das erzeugte SQLite-Artefakt und den Vertrag zur
konsumierenden App.

---

## 1. Warum überhaupt ein neues Schema

Gemessen am Bestand zum Zeitpunkt der Analyse (852 Übungen aus `wger`). Der
Import am 2026-09-02 fand 871 Übungen und 129 statt 189 leere Muskelzuweisungen
vor — upstream hat nachgebessert, die Diagnose bleibt (§13):

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
7. **Lizenz und Autor reisen mit den Daten mit** (§3b).
8. **Herkunft ist pro Feld dokumentiert.** Ohne das ist "prüf nochmal alle
   KI-Muskelzuweisungen von Modell X" Archäologie statt Query.

---

## 3. Der ID-Vertrag — der Teil, der nicht nachrüstbar ist

In der App referenzieren `routine_exercises.exercise_id` und
`set_logs.exercise_id` direkt `exercises.id`
(`lib/data/drift_database.dart:111` und `:163`). **Die Nutzerdaten hängen also
an den IDs dieser Datenbank.** Jede Zusammenlegung, Umbenennung oder Löschung
ist potenziell Datenverlust auf Geräten da draußen.

**Format der IDs:** Der Bestand nutzt die numerischen wger-IDs als TEXT,
Wertebereich beim Import am 2026-09-02 **9–2543** bei 871 Übungen — *keine*
UUIDs, und *kein* zusammenhängender Block. (Die früher hier notierte Spanne
1000–1972 war eine Fehlmessung; sie stammt vermutlich aus einem Ausschnitt.
Wer Code schreibt, der einen Wertebereich annimmt, liegt in beiden Fällen
falsch — die IDs sind undurchsichtige Schlüssel.) Daraus folgt:

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

## 3b. Lizenz-Provenienz — pro Eintrag, nicht pro Repo

wger lizenziert Übungsdaten **nicht** pauschal. Das README des Projekts sagt
"Exercise/Ingredient Data: Creative Commons (see individual entries)", und die
API bestätigt das: die Lizenz hängt an der einzelnen *Übersetzung*.

Stand des Abrufs am 2026-09-02 (871 Übungen, 3.336 Übersetzungen):

| Lizenz | Übersetzungen |
|---|---|
| CC-BY-SA 4.0 | 2.918 |
| CC-BY-SA 3.0 | 333 |
| CC0 1.0 | 85 |

Dazu **251 verschiedene `license_author`-Werte** (häufigste: `wger.de` 1.531,
leer 511, `wgerjhn` 105). Attribution schuldet man also einzelnen Beitragenden,
nicht "wger".

Die heutige Pipeline (`create_wger_exercise_db.py`) verwirft `license` und
`license_author` vollständig — die ausgelieferte DB enthält keinerlei
Attribution. **Das ist vor der Veröffentlichung zu beheben**, und zwar auch für
die bestehende App, unabhängig von diesem Fork.

Konsequenzen für das Schema:

- Jede importierte Übung trägt einen `upstream`-Block (Quelle, Fremd-ID,
  Lizenz, Autor, Importdatum), jede importierte Übersetzung ebenfalls.
- `ATTRIBUTION.md` wird **aus den Daten generiert**, nicht von Hand gepflegt.
  Bei 251 Namen ist das die einzige Variante, die dauerhaft stimmt.
- Repo-Gesamtlizenz ist CC-BY-SA 4.0. CC-BY-SA 3.0 erlaubt die Weitergabe
  von Bearbeitungen unter einer späteren Version derselben Lizenz, CC0-Material
  ist ohnehin unbeschränkt einbindbar. Die Original-Lizenz bleibt pro Eintrag
  erhalten, damit die Herkunft prüfbar bleibt.
- Selbst erstellte Übungen (`x-`-IDs) tragen `upstream: null` und die
  Repo-Lizenz.
- KI-erzeugte Texte, die aus CC-BY-SA-Vorlagen abgeleitet sind, sind
  Bearbeitungen und bleiben CC-BY-SA. Deshalb ist die einheitliche
  Repo-Lizenz die einfachste korrekte Antwort.

> Die Einschätzung zur 3.0→4.0-Weitergabe stammt aus dem Lizenztext selbst und
> ist keine Rechtsberatung. Vor dem ersten öffentlichen Release einmal
> gegenprüfen lassen.

---

## 4. Repo-Layout

```
data/exercises/<id>.yaml           # sprachneutrale Fakten, eine Datei je Übung
data/i18n/<lang>/<id>.yaml         # Texte, eine Datei je Übung je Sprache
vocab/muscles.yaml                 # hierarchisches Muskel-Vokabular
vocab/equipment.yaml               # primary_equipment + setup
vocab/classification.yaml          # modality, usage_tags, tracking_type, …
vocab/languages.yaml               # Sprach-Registry
vocab/licenses.yaml                # SPDX-Bezeichner + wger-Lizenz-IDs
schema/exercise.schema.json        # CI-Validierung Fakten
schema/translation.schema.json     # CI-Validierung Texte
schema/invariants.md               # inhaltliche Regeln, CI-Gate
test/golden/*.yaml                 # ~50 handgeprüfte Übungen als Eval-Set
test/test_*.py                     # Abnahme- und Regeltests
snapshot/wger-<datum>.json.gz      # eingefrorener Rohstand der Quelle
build/                             # YAML -> .db + manifest + reports
import/                            # Einmal-Importer wger -> YAML
oedb/                              # gemeinsame Bibliothek der Skripte
```

Zwei Verzeichnisse, die in der ursprünglichen Fassung fehlten und beim Umbau
dazukamen:

- **`snapshot/`** — der Rohstand der wger-API, einmal abgerufen, mit SHA-256
  gepinnt und im Repo. Ohne ihn hängt das Ergebnis des Builds vom Tagesstand
  einer fremden API ab und ist weder reproduzierbar noch testbar. Er ist auch
  die Antwort auf „warum sieht diese Zeile so aus": der Ursprung ist nachlesbar
  statt weg.
- **`oedb/`** — Vokabular-, Snapshot- und Dateizugriff, den Importer, Build und
  Validator gemeinsam brauchen. Ein eigenes Paket, weil `import` ein
  Python-Schlüsselwort ist und `import/` deshalb nichts exportieren kann.

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
| `load_mode` | genau 1 | was die eingegebene Zahl *bedeutet* |
| `primary_equipment` | genau 1 | das lasterzeugende Gerät |
| `setup` | 0…n | was außerdem dastehen muss |

`usage_tags` ist mehrwertig, weil ein leichtes Band-Pull-Apart legitim
Warm-up *und* Accessory ist. Ein einwertiges Feld würde hier zu willkürlichen
Entscheidungen zwingen.

Die Trennung `primary_equipment` / `setup` ist der Grund, warum „Was kann ich
im Hotelzimmer machen?" filterbar wird: `primary_equipment == bodyweight`
**und** `setup == []`.

`tracking_type` (`weight_reps`, `bodyweight_reps`, `time`, `time_weight`,
`distance_time`, `distance_only`) plus das Flag `supports_added_weight`
ersetzen `Exercise.isCardio`. Damit bekommen Plank (Zeit), Klimmzug
(Wiederholungen, optional Zusatzgewicht) und Laufband (Distanz + Zeit) endlich
die richtige Eingabemaske.

`tracking_type` sagt aber nur, welche **Form** die Log-Maske hat — nicht, was
die eingegebene Zahl *bedeutet*. Das ist ein Unterschied mit Folgen: an einer
Assistenzmaschine ist die Zahl Entlastung und nicht Last. Mehr Kilo heißt
leichter. Als `weight_reps` geloggt lesen e1RM, Volumenrechnung und
Progressionserkennung die Entwicklung exakt rückwärts — und zwar ohne dass
irgendwo ein Fehler sichtbar würde.

Deshalb `load_mode`, genau ein Wert:

| Wert | Die Zahl ist … | Beispiele |
|---|---|---|
| `external` | der Widerstand | Langhantel, Maschine, Kabel |
| `bodyweight` | optionales Zusatzgewicht | Klimmzug, Dip, Liegestütz |
| `assisted` | eine **Verringerung** des Widerstands | Assistenzmaschine |
| `variable` | kein Kilogramm | Widerstandsband |

`supports_added_weight` bleibt daneben bestehen — „Klimmzug geht mit Gürtel"
ist eine echte optionale Fähigkeit und keine Aussage über die Grundform.

Ein früheres Gegenstück `supports_assistance` ist ersatzlos entfallen. Es war
ein Flag an der falschen Achse: die dazugehörige Invariante sperrte es auf
`primary_equipment: bodyweight` und erzwang damit ausgerechnet für die
Assistenzmaschine — den Fall, um den es geht — die sachlich falsche Antwort.

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
- `status` je Dokument: `human` | `ai_reviewed` | `ai_raw` |
  `upstream_unreviewed`. Damit lässt sich später gezielt nachbessern, statt
  pauschal zu misstrauen. Alles, was der Import gebracht hat, ist
  `upstream_unreviewed`: von Menschen geschrieben, von diesem Projekt nie
  abgenommen. `human` heißt, dass jemand hier hingesehen hat — die beiden zu
  vermischen wäre eine Information, die sich später nicht mehr herstellen lässt.

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
  load_mode             TEXT NOT NULL,          -- was die geloggte Zahl bedeutet
  supports_added_weight INTEGER NOT NULL DEFAULT 0,
  primary_equipment     TEXT NOT NULL,
  body_region           TEXT,                   -- abgeleitet aus Primärmuskeln

  -- Kompatibilitätsspalten für Schema-v1-Konsumenten (heutige App).
  -- Der Importer in basis_data_manager.dart liest GENAU diese vier Felder
  -- plus die Übersetzungen. Solange sie befüllt sind, läuft die heutige App
  -- unverändert auf einer v2-Datenbank.
  category_name         TEXT,
  muscles_primary       TEXT,                   -- JSON-Array, Legacy-Namen
  muscles_secondary     TEXT,                   -- JSON-Array, Legacy-Namen
  image_path            TEXT,                   -- immer "", es gibt keine Medien
  is_custom             INTEGER NOT NULL DEFAULT 0,
  created_by            TEXT DEFAULT 'system',
  source                TEXT DEFAULT 'base',

  -- Lizenz-Provenienz, siehe §3b. NULL nur bei selbst erstellten Übungen.
  upstream_source         TEXT,                 -- 'wger' | NULL
  upstream_id             TEXT,
  upstream_license        TEXT,                 -- SPDX-artig, z. B. CC-BY-SA-4.0
  upstream_license_author TEXT
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
  source_lang     TEXT,
  license         TEXT,                         -- pro Übersetzung, siehe §3b
  license_author  TEXT
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
--                   source_commit, license, attribution_url
```

Zwei Punkte, die beim Bau des Generators konkret wurden:

- **`NOT NULL` ist datenabhängig.** Die Klassifikationsspalten oben sind
  in Phase 1 noch nicht befüllt (wger liefert sie nicht). Der Build setzt die
  Bedingung deshalb genau dann, wenn der Bestand sie trägt, und schreibt in
  `metadata.nullable_columns`, welche noch offen sind. Damit zieht sich das
  Schema mit dem Fortschritt von Phase 2 von selbst fest, statt auf jemanden zu
  warten, der daran denkt — und `nullable_columns == []` ist die Antwort auf
  „ist v2 inhaltlich erreicht?". Ein Platzhalterwert wäre die Alternative
  gewesen; der wäre von einem echten Wert nicht zu unterscheiden.
- **`category_name` speist sich aus `upstream.source_fields.category`.** Die
  Spalte ist Legacy und wird nicht gepflegt, aber die App liest sie. Der Build
  darf nicht selbst in den Snapshot greifen, also reist der Rohwert in der
  Übungsdatei mit. Dasselbe gilt für die rohe wger-Equipment-Liste, aus der
  Phase 2 `primary_equipment` und `setup` ableitet.

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

- **Attribution in der bestehenden App.** Unabhängig vom Fork: die heute
  ausgelieferte DB enthält keine Lizenz- und Autorenangaben (§3b). Das ist ein
  eigenes Ticket im App-Repo, nicht Teil dieser Migration — aber es ist offen.
- **Repo-Name** und ob die App-Releases (`wger-catalog-stable`) mit
  umziehen oder das neue Repo eigene Release-Tags bekommt. Empfehlung: eigene
  Tags im neuen Repo, Manifest-URL in der App umbiegen, der bestehende
  Legacy-Fallback in `exercise_catalog_refresh_service.dart` deckt den
  Übergang ab.
- **`contribution`-Gewichte**: Zeitpunkt der Einführung, frühestens nach
  stabilen Zuweisungen.
- **Kategorie-Ableitung**: exakte Regel für `body_region` aus den
  Primärmuskeln bei Übungen mit Primärmuskeln aus mehreren Gruppen.
- **`de` zurück auf `tier: curated`.** Deutsch ist beim Import auf `upstream`
  gesetzt, weil es nur 628 von 871 Übungen abdeckt und Invariante 4 sonst ab
  Tag eins rot stünde. Sobald die Lücke geschlossen ist, gehört es zurück auf
  `curated` — sonst blockiert eine Lücke im Deutschen den Release nicht mehr,
  und genau dafür ist die Stufe da.

---

## 13. Stand der Umsetzung (Phase 1, 2026-09-02)

Der Import ist gelaufen. Was dabei anders kam als in der Spezifikation
angenommen — jeweils mit der Entscheidung, die getroffen wurde:

**Die Sprach-IDs der alten Pipeline waren falsch.** `create_wger_exercise_db.py`
hatte sie fest verdrahtet: `4:fr, 5:it, 8:ja`. Die wger-API sagt `4=es, 5=ru,
8=el`; Französisch ist `12`, Italienisch `13`, Japanisch gibt es dort gar nicht.
Die heute ausgelieferte Datenbank führt deshalb **646 spanische Texte als
Französisch, 48 griechische als Japanisch und 10 russische als Italienisch** —
nachweisbar an Übung 132, deren `language_code='ja'`-Zeile „Βατραχάκια με
κάμψεις" enthält. Echtes Französisch (582) und Italienisch (142) fehlten
komplett. Korrigiert: die Zuordnung steht jetzt in `vocab/languages.yaml` und
wird bei jedem Import gegen den Snapshot geprüft. Importiert werden alle 22
Sprachen, die die Quelle führt.

> **App-seitig zu beachten:** wer im neuen Release `fr` liest, bekommt
> Französisch statt Spanisch, und `ja` gibt es nicht mehr. Für `de` und `en`
> ändert sich nichts. Falls irgendwo eine Sprachliste hartkodiert ist, gehört
> sie auf `vocab/languages.yaml` umgestellt.

**Zahlen aus §1 sind der Stand von damals.** Beim Import am 2026-09-02: 871
Übungen (nicht 852), **129 ohne jede Muskelzuweisung** (nicht 189), 135 ohne
primäre, weiterhin 15 distinkte Muskelwerte. Upstream hat also nachgebessert;
die Diagnose bleibt dieselbe, nur die Größenordnung ist kleiner geworden.

**Pflichtfelder, die es noch nicht geben kann.** `exercise.schema.json` führt
neun Felder als `required`, die wger nicht liefert. Sie werden nicht mit
Defaults gefüllt, sondern **weggelassen** — ein Platzhalter wäre von einem
echten Wert nicht zu unterscheiden, und das ist genau der Fehler aus §11. Der
Validator kennt dafür zwei Profile: `phase1` nimmt diese Felder aus `required`
heraus und prüft die inhaltlichen Regeln nur dort, wo die Felder existieren;
`full` schaltet alles scharf und beziffert damit jederzeit den Rückstand.

**Das Abnahmekriterium ist „Teilmenge", nicht „Mengengleichheit".** Das
Referenz-Release ist vom 31.08. und kennt 862 Übungen, der Snapshot vom 02.09.
kennt 871 — neun sind dazugekommen, keine verschwunden. Geprüft wird deshalb:
keine Referenz-ID fehlt, und `category_name`, `muscles_primary`,
`muscles_secondary` sowie die `de`/`en`-Texte sind für jede gemeinsame ID
zeichengleich (`test/test_compat.py`).

**Eine bewusste Abweichung von der Referenz.** Das Altskript füllte eine
fehlende *Beschreibung* aus der jeweils anderen Sprache auf, auch wenn der Name
in der Zielsprache vorhanden war. In der ausgelieferten Datenbank steht deshalb
bei 17 Einträgen deutscher Text in der englischen Zeile und umgekehrt. Hier
bleibt die Beschreibung stattdessen leer. Der Abnahmetest lässt genau diesen
Fall zu und nichts sonst.

**Fehlende `de`-Texte werden im Build ergänzt, nicht in den Quelldateien.**
`data/i18n/de/` enthält die 628 echten Übersetzungen; die restlichen 243 Zeilen
entstehen beim Build aus der `fallback_chain` und tragen `source_lang: en`.
Damit bleibt das Repo ehrlich und die Datenbank verhaltensgleich — und man kann
zum ersten Mal abfragen, welche der deutschen Zeilen tatsächlich deutsch sind.
Gesteuert wird das über `complete_in_release` in `vocab/languages.yaml`.

**`license` ist in der wger-API eine Zahl.** Die Abbildung auf die
SPDX-Bezeichner des Schemas steht in `vocab/licenses.yaml`. Eine unbekannte
Lizenz-ID bricht den Import ab, statt den Eintrag ohne Lizenzangabe zu
übernehmen.
