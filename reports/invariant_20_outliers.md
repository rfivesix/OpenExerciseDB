# Outlier Report: Invariant 20 (movement_pattern <-> primary_muscle_group)

## 1. Methodology & Raw Data Measurement

1. **Statistical Raw Derivation**:
   The expectation table was initially derived strictly from the **818 non-golden exercises** (minimum frequency $\ge 5\ \%$, minimum count $\ge 2$ occurrences per pattern).
2. **Cross-Validation Against the Golden Set (50 hand-verified reference entries)**:
   - Against the unadjusted raw frequency table, **6 of 50 Golden Set exercises failed**.
   - **Measured false-alarm rate of the raw statistics: 12.0 %** (6 / 50).
   - All 6 Golden Set cases (`1100 Wall-Balls`, `1116 Farmer's Carry`, `1523 Sled Push`, `1684 Thruster`, `423 Muscle-Up`, `500 Reverse Plank`) are domain-wise **completely correctly annotated**.
3. **Explicit Golden Set Additions**:
   - To prevent distortion (e.g. Sled Push silently legitimizing quads/glutes for 91 regular bench press exercises), the legitimate muscle groups of these 6 cases were added **explicitly per pattern with anatomical rationale** in `vocab/pattern_muscle_expectations.yaml`.
4. **Exemptions from Invariant 20**:
   - **`movement_pattern: other`** (73 active exercises) is explicitly **exempt from Invariant 20**, as `other` by definition carries no directional or muscle-bound constraint.
5. **Semantics for Stretches (`SCHEMA.md §5`)**:
   - For stretches (`modality: stretch`), `role: primary` denotes the target muscle group being **stretched** (e.g. `hamstrings` in Sit & Reach or `abs` in Cobra Stretch), not the contracting antagonist. Many apparent outliers resolve naturally as completely factually accurate under this definition.

---

## 2. Overview of the Remaining 36 Outliers

Across the total active inventory (868 exercises), exactly **36 exercises** (~4.1% of the catalog) trigger a soft warning (Invariant 20). None of these 36 exercises were artificially manipulated.

Here are all 36 cases, grouped by movement pattern, with specific domain assessments:

### Pattern `anti_extension` (4 outliers)
*Expected muscle groups per table:* `abs, back, triceps`

| ID | Name (EN) | Name (DE) | Unexpected | Primary Muscle(s) | Assessment |
|---|---|---|---|---|---|
| `1010` | [Back Neck Stretch](../data/exercises/1010.yaml) | Nackendehnung (hinten) | **neck** | `neck_extensors, traps_upper` | **Legitimate stretch**: Stretches anatomical counterpart (neck) under joint angle `anti_extension` (per SCHEMA §5). |
| `1238` | [Frog Stand](../data/exercises/1238.yaml) | Froschstand (Frog Stand) | **shoulders** | `deltoid, triceps_brachii` | **Gymnastics / Calisthenics**: Isometric tension on shoulders for body tension. |
| `1410` | [Plank with Alternating Leg Lift](../data/exercises/1410.yaml) | Plank mit alternierendem Beinheben | **glutes** | `rectus_abdominis, gluteus_maximus` | **Dynamic plank**: Leg lift activates gluteus maximus as additional primary component. |
| `1911` | [Cat Plank](../data/exercises/1911.yaml) | Katzen-Plank | **quads** | `rectus_abdominis, quadriceps` | **Possible misannotation**: Quadriceps as primary muscle in plank is unusual (check if core is primary). |

### Pattern `anti_flexion` (1 outliers)
*Expected muscle groups per table:* `glutes, lower_back`

| ID | Name (EN) | Name (DE) | Unexpected | Primary Muscle(s) | Assessment |
|---|---|---|---|---|---|
| `1742` | [Back Lever](../data/exercises/1742.yaml) | Rückhangwaage (Back Lever) | **back** | `latissimus_dorsi, erector_spinae` | **Gymnastics / Calisthenics**: Isometric tension on back for body tension. |

### Pattern `elbow_flexion` (2 outliers)
*Expected muscle groups per table:* `biceps, forearms`

| ID | Name (EN) | Name (DE) | Unexpected | Primary Muscle(s) | Assessment |
|---|---|---|---|---|---|
| `1230` | [Overhead Triceps Stretch (Left)](../data/exercises/1230.yaml) | Trizepsdehnung links | **triceps** | `triceps_brachii` | **Legitimate stretch**: Stretches anatomical counterpart (triceps) under joint angle `elbow_flexion` (per SCHEMA §5). |
| `1231` | [Overhead Triceps Stretch (Right)](../data/exercises/1231.yaml) | Trizepsdehnung rechts | **triceps** | `triceps_brachii` | **Legitimate stretch**: Stretches anatomical counterpart (triceps) under joint angle `elbow_flexion` (per SCHEMA §5). |

### Pattern `gait` (1 outliers)
*Expected muscle groups per table:* `abs, back, calves, glutes, quads, shoulders`

| ID | Name (EN) | Name (DE) | Unexpected | Primary Muscle(s) | Assessment |
|---|---|---|---|---|---|
| `1285` | [Butt Kicks](../data/exercises/1285.yaml) | Anfersen | **hamstrings** | `hamstring_complex, calves` | **Running drill**: Butt Kicks (heels to buttocks); hamstrings contract actively during knee flexion. |

### Pattern `hinge` (1 outliers)
*Expected muscle groups per table:* `adductors, glutes, hamstrings, lower_back, quads`

| ID | Name (EN) | Name (DE) | Unexpected | Primary Muscle(s) | Assessment |
|---|---|---|---|---|---|
| `1947` | [Dumbbell Snatch](../data/exercises/1947.yaml) | Kurzhantel-Reißen (Dumbbell Snatch) | **shoulders** | `gluteus_maximus, hamstring_complex, deltoid` | **Legitimate hybrid**: Multi-joint / full-body movement; shoulders provides force component for sub-movement. |

### Pattern `hip_adduction` (1 outliers)
*Expected muscle groups per table:* `adductors`

| ID | Name (EN) | Name (DE) | Unexpected | Primary Muscle(s) | Assessment |
|---|---|---|---|---|---|
| `2493` | [Adductor Side Plank (Copenhagen Plank)](../data/exercises/2493.yaml) | Adduktoren-Seitstütz (Copenhagen Plank) | **abs** | `hip_adductors, obliques` | **Case for review**: Primary muscle abs in `hip_adduction` is unusual; check if secondary muscle suffices. |

### Pattern `horizontal_pull` (2 outliers)
*Expected muscle groups per table:* `abs, back, biceps, shoulders`

| ID | Name (EN) | Name (DE) | Unexpected | Primary Muscle(s) | Assessment |
|---|---|---|---|---|---|
| `1093` | [Indoor Rowing Machine](../data/exercises/1093.yaml) | Rudergerät (Indoor-Ruderergometer) | **calves, glutes, quads** | `quadriceps, latissimus_dorsi, gluteus_maximus, calves` | **Legitimate hybrid**: Multi-joint / full-body movement; calves, glutes, quads provides force component for sub-movement. |
| `1905` | [Cable Pullback with Back Extension](../data/exercises/1905.yaml) | Pullback am Kabelzug | **lower_back** | `latissimus_dorsi, erector_spinae` | **Review required**: Pullback with lower back as primary muscle (check if upper back/lats intended). |

### Pattern `horizontal_push` (1 outliers)
*Expected muscle groups per table:* `chest, glutes, quads, shoulders, triceps`

| ID | Name (EN) | Name (DE) | Unexpected | Primary Muscle(s) | Assessment |
|---|---|---|---|---|---|
| `1217` | [Finger Push-Up](../data/exercises/1217.yaml) | Finger-Liegestütze | **forearms** | `pectoralis_major, wrist_flexors` | **Legitimate exception**: Push-up on fingers; forearm flexor tendons bear extreme holding force. |

### Pattern `knee_extension` (1 outliers)
*Expected muscle groups per table:* `quads`

| ID | Name (EN) | Name (DE) | Unexpected | Primary Muscle(s) | Assessment |
|---|---|---|---|---|---|
| `1398` | [Seated Hamstring Choke Stretch](../data/exercises/1398.yaml) | Hamstring Chokes (Aktive Kniebeugerdehnung) | **hamstrings** | `hamstring_complex` | **Legitimate stretch**: Stretches anatomical counterpart (hamstrings) under joint angle `knee_extension` (per SCHEMA §5). |

### Pattern `lunge` (1 outliers)
*Expected muscle groups per table:* `glutes, quads`

| ID | Name (EN) | Name (DE) | Unexpected | Primary Muscle(s) | Assessment |
|---|---|---|---|---|---|
| `2526` | [Long Lunge Pulse Stretch](../data/exercises/2526.yaml) | Tiefer Ausfallschritt mit Federn | **abs** | `hip_flexors, gluteus_maximus` | **Legitimate stretch**: Stretches anatomical counterpart (abs) under joint angle `lunge` (per SCHEMA §5). |

### Pattern `rotation` (4 outliers)
*Expected muscle groups per table:* `abs, back, glutes, neck, shoulders`

| ID | Name (EN) | Name (DE) | Unexpected | Primary Muscle(s) | Assessment |
|---|---|---|---|---|---|
| `1207` | [Scorpion Kick](../data/exercises/1207.yaml) | Skorpion-Kick | **lower_back** | `gluteus_maximus, erector_spinae` | **Legitimate stretch**: Stretches anatomical counterpart (lower_back) under joint angle `rotation` (per SCHEMA §5). |
| `1577` | [Bretzel Stretch](../data/exercises/1577.yaml) | Bretzel-Dehnung | **quads** | `gluteus_maximus, quadriceps` | **Legitimate stretch**: Stretches anatomical counterpart (quads) under joint angle `rotation` (per SCHEMA §5). |
| `1864` | [Ankle Roll](../data/exercises/1864.yaml) | Sprunggelenkkreisen | **calves** | `calves` | **Legitimate stretch**: Stretches anatomical counterpart (calves) under joint angle `rotation` (per SCHEMA §5). |
| `2543` | [Wrist Circles](../data/exercises/2543.yaml) | Handgelenkkreisen | **forearms** | `wrist_flexors, wrist_extensors` | **Legitimate stretch**: Stretches anatomical counterpart (forearms) under joint angle `rotation` (per SCHEMA §5). |

### Pattern `spinal_extension` (2 outliers)
*Expected muscle groups per table:* `back, glutes, lower_back`

| ID | Name (EN) | Name (DE) | Unexpected | Primary Muscle(s) | Assessment |
|---|---|---|---|---|---|
| `1011` | [Front Neck Stretch](../data/exercises/1011.yaml) | Vordere Halsdehnung | **neck** | `neck_flexors` | **Legitimate stretch**: Stretches anatomical counterpart (neck) under joint angle `spinal_extension` (per SCHEMA §5). |
| `1450` | [Cobra Stretch](../data/exercises/1450.yaml) | Kobra-Dehnung (Cobra Stretch) | **abs** | `rectus_abdominis` | **Legitimate stretch**: Stretches anatomical counterpart (abs) under joint angle `spinal_extension` (per SCHEMA §5). |

### Pattern `spinal_flexion` (2 outliers)
*Expected muscle groups per table:* `abs, lower_back`

| ID | Name (EN) | Name (DE) | Unexpected | Primary Muscle(s) | Assessment |
|---|---|---|---|---|---|
| `1002` | [Child's Pose](../data/exercises/1002.yaml) | Kindhaltung (Child's Pose) | **back** | `latissimus_dorsi, erector_spinae` | **Legitimate stretch**: Stretches anatomical counterpart (back) under joint angle `spinal_flexion` (per SCHEMA §5). |
| `1394` | [Sit & Reach](../data/exercises/1394.yaml) | Sit & Reach | **hamstrings** | `hamstring_complex` | **Legitimate stretch**: Stretches anatomical counterpart (hamstrings) under joint angle `spinal_flexion` (per SCHEMA §5). |

### Pattern `squat` (5 outliers)
*Expected muscle groups per table:* `glutes, quads`

| ID | Name (EN) | Name (DE) | Unexpected | Primary Muscle(s) | Assessment |
|---|---|---|---|---|---|
| `285` | [High Knee Jumps](../data/exercises/285.yaml) | Hohe Knie-Sprünge | **abs** | `quadriceps, gluteus_maximus, hip_flexors` | **Case for review**: Primary muscle abs in `squat` is unusual; check if secondary muscle suffices. |
| `632` | [Sumo Squats](../data/exercises/632.yaml) | Sumo-Kniebeugen | **adductors** | `quadriceps, gluteus_maximus, hip_adductors` | **Legitimate variation**: Extremely wide stance recruits adductors primarily. |
| `650` | [Thruster](../data/exercises/650.yaml) | Thruster | **shoulders** | `quadriceps, gluteus_maximus, deltoid` | **Legitimate hybrid**: Multi-joint / full-body movement; shoulders provides force component for sub-movement. |
| `1829` | [Landmine Squat to Press](../data/exercises/1829.yaml) | Landmine Kniebeuge mit Überkopfdrücken | **shoulders** | `quadriceps, gluteus_maximus, deltoid` | **Legitimate hybrid**: Multi-joint / full-body movement; shoulders provides force component for sub-movement. |
| `1846` | [Horse Stance (Side Splits)](../data/exercises/1846.yaml) | Reiterstellung (Seitspagat) | **adductors** | `quadriceps, hip_adductors` | **Legitimate variation**: Extremely wide stance recruits adductors primarily. |

### Pattern `vertical_pull` (5 outliers)
*Expected muscle groups per table:* `back, biceps, chest, forearms, shoulders`

| ID | Name (EN) | Name (DE) | Unexpected | Primary Muscle(s) | Assessment |
|---|---|---|---|---|---|
| `599` | [Snatch](../data/exercises/599.yaml) | Reißen (Snatch) | **glutes, hamstrings, quads** | `gluteus_maximus, hamstring_complex, quadriceps` | **Legitimate hybrid**: Multi-joint / full-body movement; glutes, hamstrings, quads provides force component for sub-movement. |
| `1447` | [Olympic Snatch](../data/exercises/1447.yaml) | Reißen (Snatch) | **glutes, hamstrings, quads** | `gluteus_maximus, hamstring_complex, quadriceps` | **Legitimate hybrid**: Multi-joint / full-body movement; glutes, hamstrings, quads provides force component for sub-movement. |
| `1526` | [SkiErg (Ski Machine)](../data/exercises/1526.yaml) | Skilanglauf-Ergometer (SkiErg) | **abs, triceps** | `latissimus_dorsi, triceps_brachii, rectus_abdominis` | **Legitimate hybrid**: Multi-joint / full-body movement; abs, triceps provides force component for sub-movement. |
| `1741` | [L-Sit Pull-Ups](../data/exercises/1741.yaml) | L-Sit-Klimmzüge | **abs** | `latissimus_dorsi, rectus_abdominis` | **Legitimate hybrid**: Pull-up with static L-sit hold (abdominals primarily active). |
| `1970` | [Kettlebell Sumo High Pull](../data/exercises/1970.yaml) | Kettlebell Sumo High Pull | **glutes** | `traps_upper, gluteus_maximus` | **Legitimate hybrid**: Multi-joint / full-body movement; glutes provides force component for sub-movement. |

### Pattern `vertical_push` (3 outliers)
*Expected muscle groups per table:* `chest, glutes, quads, shoulders, triceps`

| ID | Name (EN) | Name (DE) | Unexpected | Primary Muscle(s) | Assessment |
|---|---|---|---|---|---|
| `711` | [Wall Handstand](../data/exercises/711.yaml) | Handstand gegen die Wand | **back** | `deltoid, trapezius` | **Gymnastics / Calisthenics**: Isometric tension on back for body tension. |
| `716` | [Wall Slides](../data/exercises/716.yaml) | Wandgleiten | **back** | `serratus_anterior, traps_lower` | **Legitimate stretch**: Stretches anatomical counterpart (back) under joint angle `vertical_push` (per SCHEMA §5). |
| `1226` | [Dumbbell Biceps Curl to Overhead Press](../data/exercises/1226.yaml) | Kurzhantel-Bizeps-Curl mit Schulterdrücken | **biceps** | `deltoid, biceps_brachii` | **Legitimate hybrid**: Multi-joint / full-body movement; biceps provides force component for sub-movement. |
