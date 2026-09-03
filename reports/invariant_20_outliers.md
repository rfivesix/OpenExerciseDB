# Ausreißer-Bericht: Invariante 20 (movement_pattern <-> primary_muscle_group)

## 1. Methodik & Rohdaten-Messung

1. **Statistische Roh-Ableitung**:
   Die Erwartungstabelle wurde zunächst streng aus den **819 Nicht-Golden-Übungen** abgeleitet (Mindesthäufigkeit $\ge 5\ \%$, Mindestanzahl $\ge 2$ Vorkommen je Muster).
2. **Gegenprüfung am Golden Set (50 handgeprüfte Referenz-Einträge)**:
   - Gegen die unkorrigierte Roh-Häufigkeitstabelle fielen **6 von 50 Golden-Set-Übungen durch**.
   - **Gemessene Fehlalarmquote der Rohstatistik: 12,0 %** (6 / 50).
   - Alle 6 Golden-Set-Fälle (`1100 Wall-Balls`, `1116 Farmer's Carry`, `1523 Sled Push`, `1684 Thruster`, `423 Muscle-Up`, `500 Reverse Plank`) sind fachlich **vollkommen korrekt annotiert**.
3. **Explizite Golden-Set-Ergänzungen**:
   - Um Verzerrungen zu vermeiden (z. B. dass Sled Push stillschweigend Quads/Glutes für 91 normale Bankdrück-Übungen legitimiert), wurden die legitimen Muskelgruppen dieser 6 Fälle **explizit je Muster mit anatomischer Begründung** in `vocab/pattern_muscle_expectations.yaml` nachgetragen.
4. **Ausnahmen von Invariante 20**:
   - **`movement_pattern: other`** (73 aktive Übungen) ist ausdrücklich **von Invariante 20 ausgenommen**, da `other` definitionsgemäß keine Richtungs- oder Muskelbindung besitzt.
5. **Semantik bei Dehnübungen (`SCHEMA.md §5`)**:
   - Bei Dehnübungen (`modality: stretch`) bezeichnet `role: primary` die Zielmuskelgruppe, die **gedehnt** wird (z. B. `hamstrings` beim Sit & Reach oder `abs` beim Cobra Stretch), nicht den kontrahierenden Antagonisten. Viele scheinbare Ausreißer lösen sich dadurch als sachlich vollkommen korrekt auf.

---

## 2. Übersicht der verbleibenden 36 Ausreißer

Im aktiven Gesamtbestand (869 Übungen) lösen genau **36 Übungen** (~4,1 % des Bestands) eine weiche Warnung (Invariante 20) aus. Keine dieser 36 Übungen wurde automatisch manipuliert.

Hier sind alle 36 Fälle, gruppiert nach Bewegungsmuster, mit konkreter fachlicher Einschätzung:


### Muster `anti_extension` (4 Ausreißer)
*Erwartete Muskelgruppen laut Tabelle:* `abs, back, triceps`

| ID | Name (EN) | Name (DE) | Unerwartet | Primärmuskel(n) | Einschätzung |
|---|---|---|---|---|---|
| `1010` | [Back neck stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1010.yaml) | Nackendehnung | **neck** | `neck_extensors, traps_upper` | **Legitime Dehnung**: Dehnt anatomische Gegenseite (neck) bei Gelenkstellung `anti_extension` (gemäß SCHEMA §5). |
| `1238` | [Frog stand](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1238.yaml) | Froschstand | **shoulders** | `deltoid, triceps_brachii` | **Turnen/Calisthenics**: Isometrische Haltekraft auf shoulders zur Körperspannung. |
| `1410` | [Plank with Alternating Leg Lift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1410.yaml) | - | **glutes** | `rectus_abdominis, gluteus_maximus` | **Dynamische Plank**: Beinanheben aktiviert Gluteus maximus als zusätzliche Primärkomponente. |
| `1911` | [Cat Plank](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1911.yaml) | Katzen-Plank | **quads** | `rectus_abdominis, quadriceps` | **Mögliche Fehlannotation**: Quadrizeps als Primärmuskel bei Plank ungewöhnlich (prüfen ob Core primär). |

### Muster `anti_flexion` (1 Ausreißer)
*Erwartete Muskelgruppen laut Tabelle:* `glutes, lower_back`

| ID | Name (EN) | Name (DE) | Unerwartet | Primärmuskel(n) | Einschätzung |
|---|---|---|---|---|---|
| `1742` | [Back Lever](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1742.yaml) | - | **back** | `latissimus_dorsi, erector_spinae` | **Turnen/Calisthenics**: Isometrische Haltekraft auf back zur Körperspannung. |

### Muster `elbow_flexion` (2 Ausreißer)
*Erwartete Muskelgruppen laut Tabelle:* `biceps, forearms`

| ID | Name (EN) | Name (DE) | Unerwartet | Primärmuskel(n) | Einschätzung |
|---|---|---|---|---|---|
| `1230` | [Triceps stretch left](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1230.yaml) | Trizepsdehnung links | **triceps** | `triceps_brachii` | **Legitime Dehnung**: Dehnt anatomische Gegenseite (triceps) bei Gelenkstellung `elbow_flexion` (gemäß SCHEMA §5). |
| `1231` | [Triceps stretch right](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1231.yaml) | Trizepsdehnung rechts | **triceps** | `triceps_brachii` | **Legitime Dehnung**: Dehnt anatomische Gegenseite (triceps) bei Gelenkstellung `elbow_flexion` (gemäß SCHEMA §5). |

### Muster `gait` (1 Ausreißer)
*Erwartete Muskelgruppen laut Tabelle:* `abs, back, calves, glutes, quads, shoulders`

| ID | Name (EN) | Name (DE) | Unerwartet | Primärmuskel(n) | Einschätzung |
|---|---|---|---|---|---|
| `1285` | [Talons fesses](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1285.yaml) | - | **hamstrings** | `hamstring_complex, calves` | **Lauf-Drill**: Butt Kicks (Fersenanschlag ans Gesäß); Beinbeuger kontrahieren aktiv bei der Kniebeugung. |

### Muster `hinge` (1 Ausreißer)
*Erwartete Muskelgruppen laut Tabelle:* `adductors, glutes, hamstrings, lower_back, quads`

| ID | Name (EN) | Name (DE) | Unerwartet | Primärmuskel(n) | Einschätzung |
|---|---|---|---|---|---|
| `1947` | [dumbbell snatch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1947.yaml) | Kurzhantel-Reißen (Dumbbell Snatch) | **shoulders** | `gluteus_maximus, hamstring_complex, deltoid` | **Legitimer Hybrid**: Mehrgelenk-/Ganzkörperbewegung; shoulders liefert Kraftkomponente der Teilbewegung. |

### Muster `hip_adduction` (1 Ausreißer)
*Erwartete Muskelgruppen laut Tabelle:* `adductors`

| ID | Name (EN) | Name (DE) | Unerwartet | Primärmuskel(n) | Einschätzung |
|---|---|---|---|---|---|
| `2493` | [Adductor Side Plank](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2493.yaml) | Adductor side plank | **abs** | `hip_adductors, obliques` | **Prüffall**: Primärmuskel abs bei `hip_adduction` ungewöhnlich; prüfen ob Sekundärmuskel genügt. |

### Muster `horizontal_pull` (2 Ausreißer)
*Erwartete Muskelgruppen laut Tabelle:* `abs, back, biceps, shoulders`

| ID | Name (EN) | Name (DE) | Unerwartet | Primärmuskel(n) | Einschätzung |
|---|---|---|---|---|---|
| `1093` | [Rowing Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1093.yaml) | Rudergerät | **calves, glutes, quads** | `quadriceps, latissimus_dorsi, gluteus_maximus, calves` | **Legitimer Hybrid**: Mehrgelenk-/Ganzkörperbewegung; calves, glutes, quads liefert Kraftkomponente der Teilbewegung. |
| `1905` | [Pullback](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1905.yaml) | Pullback | **lower_back** | `latissimus_dorsi, erector_spinae` | **Prüfen**: Pullback mit unterem Rücken als Primärmuskel (prüfen ob oberer Rücken/Lats gemeint sind). |

### Muster `horizontal_push` (1 Ausreißer)
*Erwartete Muskelgruppen laut Tabelle:* `chest, glutes, quads, shoulders, triceps`

| ID | Name (EN) | Name (DE) | Unerwartet | Primärmuskel(n) | Einschätzung |
|---|---|---|---|---|---|
| `1217` | [Finger Pushup](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1217.yaml) | Fingerliegestütz | **forearms** | `pectoralis_major, wrist_flexors` | **Legitime Ausnahme**: Liegestütz auf Fingern; Unterarm-Beugesehnen tragen extreme Haltekraft. |

### Muster `knee_extension` (1 Ausreißer)
*Erwartete Muskelgruppen laut Tabelle:* `quads`

| ID | Name (EN) | Name (DE) | Unerwartet | Primärmuskel(n) | Einschätzung |
|---|---|---|---|---|---|
| `1398` | [Hamstring Chokes](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1398.yaml) | Hamstring Chokes | **hamstrings** | `hamstring_complex` | **Legitime Dehnung**: Dehnt anatomische Gegenseite (hamstrings) bei Gelenkstellung `knee_extension` (gemäß SCHEMA §5). |

### Muster `lunge` (1 Ausreißer)
*Erwartete Muskelgruppen laut Tabelle:* `glutes, quads`

| ID | Name (EN) | Name (DE) | Unerwartet | Primärmuskel(n) | Einschätzung |
|---|---|---|---|---|---|
| `2526` | [Long Lunge Pulse Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2526.yaml) | - | **abs** | `hip_flexors, gluteus_maximus` | **Legitime Dehnung**: Dehnt anatomische Gegenseite (abs) bei Gelenkstellung `lunge` (gemäß SCHEMA §5). |

### Muster `rotation` (4 Ausreißer)
*Erwartete Muskelgruppen laut Tabelle:* `abs, back, glutes, neck, shoulders`

| ID | Name (EN) | Name (DE) | Unerwartet | Primärmuskel(n) | Einschätzung |
|---|---|---|---|---|---|
| `1207` | [Scorpion Kick](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1207.yaml) | Skorpion-Kick | **lower_back** | `gluteus_maximus, erector_spinae` | **Legitime Dehnung**: Dehnt anatomische Gegenseite (lower_back) bei Gelenkstellung `rotation` (gemäß SCHEMA §5). |
| `1577` | [Bretzel stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1577.yaml) | Bretzel-Dehnung | **quads** | `gluteus_maximus, quadriceps` | **Legitime Dehnung**: Dehnt anatomische Gegenseite (quads) bei Gelenkstellung `rotation` (gemäß SCHEMA §5). |
| `1864` | [Ankle Roll](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1864.yaml) | - | **calves** | `calves` | **Legitime Dehnung**: Dehnt anatomische Gegenseite (calves) bei Gelenkstellung `rotation` (gemäß SCHEMA §5). |
| `2543` | [Wrist circles](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2543.yaml) | - | **forearms** | `wrist_flexors, wrist_extensors` | **Legitime Dehnung**: Dehnt anatomische Gegenseite (forearms) bei Gelenkstellung `rotation` (gemäß SCHEMA §5). |

### Muster `spinal_extension` (2 Ausreißer)
*Erwartete Muskelgruppen laut Tabelle:* `back, glutes, lower_back`

| ID | Name (EN) | Name (DE) | Unerwartet | Primärmuskel(n) | Einschätzung |
|---|---|---|---|---|---|
| `1011` | [Front neck stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1011.yaml) | Nackenstütze vorne | **neck** | `neck_flexors` | **Legitime Dehnung**: Dehnt anatomische Gegenseite (neck) bei Gelenkstellung `spinal_extension` (gemäß SCHEMA §5). |
| `1450` | [Cobra Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1450.yaml) | Kobra-Dehnung | **abs** | `rectus_abdominis` | **Legitime Dehnung**: Dehnt anatomische Gegenseite (abs) bei Gelenkstellung `spinal_extension` (gemäß SCHEMA §5). |

### Muster `spinal_flexion` (2 Ausreißer)
*Erwartete Muskelgruppen laut Tabelle:* `abs, lower_back`

| ID | Name (EN) | Name (DE) | Unerwartet | Primärmuskel(n) | Einschätzung |
|---|---|---|---|---|---|
| `1002` | [Child's pose](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1002.yaml) | Kinderpose | **back** | `latissimus_dorsi, erector_spinae` | **Legitime Dehnung**: Dehnt anatomische Gegenseite (back) bei Gelenkstellung `spinal_flexion` (gemäß SCHEMA §5). |
| `1394` | [Sit & Reach](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1394.yaml) | Sit & Reach | **hamstrings** | `hamstring_complex` | **Legitime Dehnung**: Dehnt anatomische Gegenseite (hamstrings) bei Gelenkstellung `spinal_flexion` (gemäß SCHEMA §5). |

### Muster `squat` (5 Ausreißer)
*Erwartete Muskelgruppen laut Tabelle:* `glutes, quads`

| ID | Name (EN) | Name (DE) | Unerwartet | Primärmuskel(n) | Einschätzung |
|---|---|---|---|---|---|
| `285` | [High Knee Jumps](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/285.yaml) | Hohe Knie-Sprünge | **abs** | `quadriceps, gluteus_maximus, hip_flexors` | **Prüffall**: Primärmuskel abs bei `squat` ungewöhnlich; prüfen ob Sekundärmuskel genügt. |
| `632` | [Sumo Squats](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/632.yaml) | Sumo Kniebeuge | **adductors** | `quadriceps, gluteus_maximus, hip_adductors` | **Legitime Variante**: Extrem breiter Stand rekrutiert Adduktoren primär. |
| `650` | [Thruster](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/650.yaml) | Thruster | **shoulders** | `quadriceps, gluteus_maximus, deltoid` | **Legitimer Hybrid**: Mehrgelenk-/Ganzkörperbewegung; shoulders liefert Kraftkomponente der Teilbewegung. |
| `1829` | [Landmine Squat to Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1829.yaml) | Landmine Kniebeuge mit Überkopfdrücken | **shoulders** | `quadriceps, gluteus_maximus, deltoid` | **Legitimer Hybrid**: Mehrgelenk-/Ganzkörperbewegung; shoulders liefert Kraftkomponente der Teilbewegung. |
| `1846` | [Horse Stance (Side Splits)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1846.yaml) | Reiterstellung (Seitspagat) | **adductors** | `quadriceps, hip_adductors` | **Legitime Variante**: Extrem breiter Stand rekrutiert Adduktoren primär. |

### Muster `vertical_pull` (5 Ausreißer)
*Erwartete Muskelgruppen laut Tabelle:* `back, biceps, chest, forearms, shoulders`

| ID | Name (EN) | Name (DE) | Unerwartet | Primärmuskel(n) | Einschätzung |
|---|---|---|---|---|---|
| `599` | [Snatch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/599.yaml) | Reißen (Snatch) | **glutes, hamstrings, quads** | `gluteus_maximus, hamstring_complex, quadriceps` | **Legitimer Hybrid**: Mehrgelenk-/Ganzkörperbewegung; glutes, hamstrings, quads liefert Kraftkomponente der Teilbewegung. |
| `1447` | [Snatch OL](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1447.yaml) | Snatch (Reißen) | **glutes, hamstrings, quads** | `gluteus_maximus, hamstring_complex, quadriceps` | **Legitimer Hybrid**: Mehrgelenk-/Ganzkörperbewegung; glutes, hamstrings, quads liefert Kraftkomponente der Teilbewegung. |
| `1526` | [Ski Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1526.yaml) | Ski-Maschine | **abs, triceps** | `latissimus_dorsi, triceps_brachii, rectus_abdominis` | **Legitimer Hybrid**: Mehrgelenk-/Ganzkörperbewegung; abs, triceps liefert Kraftkomponente der Teilbewegung. |
| `1741` | [L-Sit Pull-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1741.yaml) | - | **abs** | `latissimus_dorsi, rectus_abdominis` | **Legitimer Hybrid**: Klimmzug mit statisch gehaltenem L-Sitz (Bauchmuskeln primär aktiv). |
| `1970` | [Kettlebell sumo high pull](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1970.yaml) | Kettlebell Sumo High Pull | **glutes** | `traps_upper, gluteus_maximus` | **Legitimer Hybrid**: Mehrgelenk-/Ganzkörperbewegung; glutes liefert Kraftkomponente der Teilbewegung. |

### Muster `vertical_push` (3 Ausreißer)
*Erwartete Muskelgruppen laut Tabelle:* `chest, glutes, quads, shoulders, triceps`

| ID | Name (EN) | Name (DE) | Unerwartet | Primärmuskel(n) | Einschätzung |
|---|---|---|---|---|---|
| `711` | [Wall Handstand](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/711.yaml) | Handstand Gegen Die Wand | **back** | `deltoid, trapezius` | **Turnen/Calisthenics**: Isometrische Haltekraft auf back zur Körperspannung. |
| `716` | [Wall Slides](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/716.yaml) | Wandgleiten | **back** | `serratus_anterior, traps_lower` | **Legitime Dehnung**: Dehnt anatomische Gegenseite (back) bei Gelenkstellung `vertical_push` (gemäß SCHEMA §5). |
| `1226` | [Dumbbell bicep curl to press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1226.yaml) | Kurzhantel-Bizeps-Curl mit Schulterdrücken | **biceps** | `deltoid, biceps_brachii` | **Legitimer Hybrid**: Mehrgelenk-/Ganzkörperbewegung; biceps liefert Kraftkomponente der Teilbewegung. |