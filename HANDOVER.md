# Handover — Stand 2026-09-03

Übergabeprotokoll für die Weiterarbeit mit Antigravity. Enthält den Stand, die
getroffenen Entscheidungen samt Begründung, die offenen Punkte und den fertigen
Prompt für den nächsten Schritt.

---

## 1. Stand

Stand 2026-09-04. Working Tree sauber, Validator 0 Fehler / 55 weiche
Warnungen (36 aus Invariante 20, 19 aus der Übersetzungsidentität — beide
dokumentiert, keine offenen Fehler).

| | |
|---|---|
| Übungen | 909 — **868 aktiv**, 15 `merged`, 26 `deprecated` |
| vollständig klassifiziert | **868 von 868 aktiven** |
| ohne primären Muskel | **0** |
| Text `en` / `de` | Namen und Beschreibungen **vollständig und kuratiert** |
| Text `fr` / `it` / `ja` | Namen vollständig, Beschreibungen offen (566 / 142 / 0) |
| Sprachen registriert | 23 |
| Phase 1 | **abgenommen**, in der App durchgeklickt |
| Phase 2 | Klassifikation und `en`/`de`-Text **fertig**, abgeleitete Sprachen offen |

Letzte Commits:

```
396d091 Complete German exercise description coverage
f2e29f4 Translate German arm and lower-body descriptions
f108218 Translate German upper-body and lower-body descriptions
aa754cc Translate German core and lower-body descriptions
3b573e3 Add German exercise descriptions and provenance metadata
d6ad58c Restore descriptive German exercise names
1ba2966 Document curated text changes and retire phase-one text checks
```

---|---|
| Übungen | 909 — 871 aktiv, 38 `deprecated` |
| vollständig klassifiziert | **50** von 909 |
| ohne primären Muskel | **131** |
| Sprachen | 22, `en`/`de` kuratiert |
| Phase 1 | **abgenommen**, in der App durchgeklickt |

Letzte Commits:

```
ea45449  Fix group-level muscle resolution; move the compat test to its phase 2 contract
bf62eb3  Carry the 50 annotated exercises over to the new schema
3369db5  Split the invariants into hard and soft, add an exceptions mechanism
e0ad8d6  Derive force_vector from movement_pattern instead of annotating it
ab16c0f  Add load_mode; drop supports_assistance and invariant 16
b13aee0  Vocabulary: four movement patterns and swiss_ball
cf0a8fc  Fix the ID ratchet: register every published ID, recover the 38 lost
```

---

## 2. Entscheidungen, die nicht neu verhandelt werden

Wer hier weiterarbeitet, muss diese fünf kennen — sie sind teuer erkauft.

**IDs sind ein Vertrag.** `exercises.id` ist Fremdschlüssel in den Workout-Logs
der App. Nichts wird je gelöscht; Zusammenlegungen laufen über
`exercise_aliases`. Invariante 21 prüft gegen `data/published_ids.yaml`, ein nur
wachsendes Register. Der Grund: eine Prüfung gegen das *vorige* Release hat eine
Ratsche — ein einmal durchgerutschter Verlust ist danach unsichtbar. Genau so
sind 38 Übungen verschwunden, darunter Klimmzüge und Hip Thrust.

**`load_mode` statt `supports_assistance`.** An einer Assistenzmaschine ist die
geloggte Zahl Entlastung, nicht Last. Als `weight_reps` gespeichert läse jede
Auswertung die Progression rückwärts. Werte: `external`, `bodyweight`,
`assisted`, `variable`.

**`force_vector` wird abgeleitet, nicht annotiert.** Er ist eine Funktion von
`movement_pattern`; die Tabelle steht in `vocab/classification.yaml`. Acht
Muster bilden bewusst auf `null` ab — Tragen ist weder Drücken noch Ziehen. Die
Spalte ist deshalb dauerhaft nullable.

**Harte und weiche Invarianten.** Weiche Regeln (11–15, 18, 20) blockieren nur,
solange der Verstoß nicht per `exceptions:`-Block begründet ist. Grund: eine zu
strenge Regel erzeugt keinen sichtbaren Fehler, sondern eine still verbogene
Annotation. Häufen sich die Ausnahmen, ist die Regel falsch, nicht die Daten.

**Präzision wird nicht auf das Legacy-Vokabular zurechtgebogen.** Die App kennt
heute 15 grobe Muskelnamen. Übungen, die das nicht mehr ausdrücken kann
(aktuell 2: `301 Hyperextensions`, `2492 Adductors`), verlieren die
Legacy-Spalte, nicht die Präzision. Die genaue Zuweisung liegt in
`exercise_muscles`, die App zieht mit SCHEMA §10.6 nach. Der
Kompatibilitätstest deckelt diese Zahl auf ≤ 10, damit sie nicht unbemerkt
wächst.

---

## 3. Wie der nächste Batch aussehen sollte

Die erste Runde hat gezeigt, wo es klemmt. Vier Dinge übernehmen:

1. **Auswahl nach Abdeckung, nicht nach ID.** ID-Nähe bedeutet in wger nichts;
   alphabetisch oder numerisch bekommt man zwanzig Bizeps-Curls am Stück.
   Stratifizieren nach Equipment-Klasse, Muskelgruppe und Modalität.
2. **Gruppenweise reviewen, nicht alphabetisch.** Fehler clustern nach
   Muskelgruppe und Gerät. Vierzig Rudervarianten am Stück prüfen geht schnell,
   weil der Vergleich danebensteht.
3. **Melden statt biegen.** Die erste Runde hat vier von fünf Vokabularlücken
   korrekt gemeldet statt einen Wert zu verbiegen — genau das ist das
   gewünschte Verhalten, und es hat drei echte Modellfehler aufgedeckt.
4. **Beide Sprachen lesen.** Der Name allein ist oft mehrdeutig, und es gibt
   Einträge, deren EN- und DE-Text verschiedene Übungen beschreiben (siehe §5).

---

## 4. Offene Punkte

### Erledigt seit der ersten Fassung

Golden Set (50 handgeprüfte Einträge in `test/golden/`) · Invariante 20 samt
Erwartungstabelle · `shoulder_raise` in `shoulder_flexion` und
`scapular_elevation` aufgeteilt · `hip_extension` eingeführt · EN/DE-Konsistenz
über alle 603 Paare geprüft · Alias-Tabelle mit 15 Einträgen · `512` nach `395`
gemerged · englische Namen vereinheitlicht · `en`/`de`-Beschreibungen
vollständig.

### Offen

| Punkt | Wo |
|---|---|
| **Abgeleitete Sprachen** — `fr` 302, `it` 726, `ja` 868 Beschreibungen | die nächste große Runde |
| **Dünne Quellen zuerst** — 119 englische Beschreibungen unter 12 Wörtern | vor der Ableitung, sonst werden daraus 357 dünne Texte |
| **Vorhandene `fr`/`it` prüfen** — 566 + 142 ungeprüfte Alttexte | die zwei mechanischen Prüfungen genügen |
| **3 aktiv-aktiv-Dubletten** dedupen: `382/1852`, `478/1440`, `805/1661` | `1654/1744` ist über den Merge-Mechanismus erledigt |
| **`languages.displayable`** steht für `it`/`ja` auf 0 | wird mit Paket 2 (Vollständigkeit ≥95 %) automatisch 1 |
| **`languages.completeness`** lieferte Werte über 1 | Behoben in `build/build_db.py` (nur aktive Übungen zählen) |
| **`exercises.body_region`** war in allen Zeilen NULL | Behoben in `build/build_db.py` (aus Primärmuskeln abgeleitet) |
| **`delt_lateral`** trug beide Delta-Slugs | Behoben in `vocab/muscles.yaml` (nur `frontDeltoids`; `rotator_cuff` leer) |
| **Attribution in der Train-Libre-App** — die ausgelieferte DB hat keine Lizenzangaben | eigenes Ticket im App-Repo |

### Einzelfälle, die noch niemand entschieden hat

- `320 Jumping Jacks` — `calves` als einziger Primärmuskel, Quads sekundär.
  Vermutlich falsch gewichtet.
- `76 Bench Press Narrow Grip` — Trizeps allein primär, Brust sekundär.
  Vertretbar, aber aggressiv.
- `529` vs `908` — beide Laufen, unterschiedlicher `tracking_type`
  (`time` vs `distance_time`). Begründbar, muss aber bewusst sein: das Paar
  entscheidet später über alle Läufe.
- `1083 YWTs` — `time`, obwohl üblicherweise in Wiederholungen.
- `312` — `laterality: alternating` plus `tracking_type: time`; die
  abwechselnden Bodenberührungen *sind* Wiederholungen.
- Sieben Klassifikationsverdachtsfälle aus Job A, in
  `reports/job_a_review_report.md` dokumentiert und bewusst nicht geändert:
  `1660`, `1637`, `1885`, `508`, `142`, `1738`, `1929`.

---

## 5. Bekannte Datenfehler

**`456`: zwei verschiedene Übungen unter einer ID.** EN beschreibt einen Pistol
Squat, DE einen bulgarischen Split Squat. Kein Übersetzungsfehler — die
Annotation folgt EN und ist damit für deutsche Nutzer falsch.

**`51`: doppelter Widerspruch.** EN „palms facing up" mit Langhantel, DE
„Handrücken nach oben (Obergriff)" mit Kurzhanteln. Anderer Muskel, anderes
Gerät.

Eine grobe Suche nach Geräte-Widersprüchen fand vier weitere (`1193`, `50`,
`51`, `75`). `456` fällt durch dieses Raster — die echte Zahl liegt höher.

---

## 6. Prompt für Antigravity (nächster Batch)

Erst ausführen, wenn der Review der 50 durch ist und `test/golden/` steht.

```
Phase 2, round 2: annotate the next batch of exercises.

Read SCHEMA.md (§5, §6, §11), vocab/muscles.yaml, vocab/equipment.yaml,
vocab/classification.yaml, schema/exercise.schema.json and
schema/invariants.md. Then read HANDOVER.md §2 — those five decisions are
settled and must not be re-litigated.

The reviewed golden set is in test/golden/. Study it before you write anything:
it is the reference for how these fields are meant to be filled, and every
batch is measured against it. Where your judgement differs from a golden entry,
the golden entry wins.

Pick the batch by COVERAGE, not by ID order: stratify across equipment class,
muscle group and modality, and prioritise the 131 exercises that still have no
primary muscle at all. Tell me which IDs you picked and why before you start.

For each exercise, edit data/exercises/<id>.yaml and fill in:
  modality, mechanic, movement_pattern, laterality, difficulty, usage_tags,
  tracking_type, load_mode, supports_added_weight, primary_equipment, setup
and correct or complete the `muscles` list.

Do NOT write force_vector — it is derived from movement_pattern by the build.
Do NOT touch id, slug, status, upstream, or anything under data/i18n/.

Rules:
1. Only values from vocab/*.yaml. If nothing fits, do NOT bend an existing
   value — report it and leave the field out. Four of five vocabulary gaps
   reported in round 1 were accepted and led to real schema fixes.
2. upstream.source_fields carries wger's own category and equipment strings.
   Use them as evidence, but note that wger mixes implements with furniture
   ("Bench", "Gym mat" are `setup` here, not `primary_equipment`) and that 228
   entries have no equipment upstream at all.
3. Annotate muscles at the depth you are actually confident about. A correct
   group beats a guessed head — SCHEMA §5 exists so you can be honest about
   this, and group-level annotation is fully supported end to end.
4. Read data/i18n/en/<id>.yaml AND data/i18n/de/<id>.yaml before deciding. The
   name alone is often ambiguous. Some entries contradict each other across
   languages — see HANDOVER.md §5. Report any new ones you find rather than
   silently picking a side.
5. Set a provenance entry for every field you write: source: ai, the model
   name, today's date.
6. If a soft invariant fires on a value you believe is correct, do NOT change
   the data to please it. Add an exceptions: entry with a reason, or say that
   the rule itself looks wrong. Round 1 lost a correct annotation exactly this
   way.

Run python3 build/validate.py and make it pass. Then report:
  - a table of what you set,
  - every entry you were NOT confident about, with the specific question,
  - anything the vocabulary could not express,
  - any cross-language contradictions you found.

The last three lists are the most valuable output. Flag rather than fill.

Do not commit anything — leave it in the working tree so I can read the diffs.
```

---

## 7. Wo was liegt

- `SCHEMA.md` — die Spezifikation. §3 ID-Vertrag, §5 Muskelmodell,
  §6 Klassifikation, §8 DDL, §10 App-Änderungen, §12 offene Punkte
- `schema/invariants.md` — 25 Regeln, hart/weich getrennt
- `_bootstrap/HANDOFF.md` — die Fakten aus der Train-Libre-App
- `test/golden/CANDIDATES.md` — die 50 der ersten Runde
- App-Repo: `~/Projekte/train-libre`. Katalog-Asset nur **offline** testbar,
  sonst zieht der Force-Update das GitHub-Release statt der lokalen Datei.
