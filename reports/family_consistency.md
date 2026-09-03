# Familien-Konsistenzbericht: Abweichungen innerhalb gleicher Muster & Muskelgruppen

## Zweck & Methodik
Übungen, die dasselbe Bewegungsmuster (`movement_pattern`) teilen und dieselbe primäre Muskelgruppe adressieren, bilden eine funktionelle Familie (z. B. `horizontal_push` + `chest` = Bankdrück-Familie).

Dieser Bericht deckt Übungen auf, bei denen innerhalb derselben Familie abweichende Werte für:
- **`mechanic`** (`compound` vs. `isolation`)
- **`tracking_type`** (`weight_reps`, `bodyweight_reps`, `time`, etc.)
- **`load_mode`** (`external`, `bodyweight`, `assisted`, `variable`)

auftreten. Einige Abweichungen sind **strukturell legitim** (z. B. Klimmzug mit Körpergewicht vs. Latzug mit externem Gewicht), andere sind **echte Inkonsistenzen** (z. B. eine Kniebeugen-Variante fälschlich als `isolation` oder ein Curl als `compound`).


Insgesamt wurden **76 Familien** mit Werte-Varianzen identifiziert:


### Familie `anti_extension` + `abs` (32 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], tracking_type: ['bodyweight_reps', 'time']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `41` | [Barbell Ab Rollout](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/41.yaml) | `barbell` | `compound` | `bodyweight` | `bodyweight_reps` |
| `178` | [Deadbug](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/178.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `235` | [Flutter Kicks](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/235.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `297` | [Hollow Hold](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/297.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `312` | [Incline Plank With Alternate Floor Touch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/312.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `376` | [Leg Raise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/376.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `382` | [L Hold](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/382.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `458` | [Plank](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/458.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `545` | [Scissors](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/545.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1001` | [High plank](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1001.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1103` | [walking bridge](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1103.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1214` | [Front lever tuck](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1214.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1245` | [Front Lever](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1245.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1246` | [TRX roll out](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1246.yaml) | `suspension_trainer` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1307` | [Front Plank](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1307.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1406` | [Plank-to-Elbow Extension](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1406.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1409` | [Dragon-flag](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1409.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1410` | [Plank with Alternating Leg Lift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1410.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1425` | [Toe Taps](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1425.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1489` | [Plank Jacks](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1489.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1573` | [Ab wheel](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1573.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1704` | [Tuck L-sit](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1704.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1827` | [Double-Leg Abdominal Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1827.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1828` | [Abdominal Draw-In](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1828.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1847` | [Straddle L-Sit](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1847.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1852` | [L-sit](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1852.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1853` | [L-Sit (Foot Supported)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1853.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1909` | [Leg Wheel](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1909.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1911` | [Cat Plank](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1911.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2505` | [Dead Bug (Core L1)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2505.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2507` | [Forearm Plank (Core L1)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2507.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2510` | [Hollow Body Hold (Core L1)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2510.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Familie `anti_extension` + `back` (3 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1010` | [Back neck stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1010.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1214` | [Front lever tuck](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1214.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1245` | [Front Lever](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1245.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Familie `anti_extension` + `triceps` (2 Übungen)
*Varianzen:* tracking_type: ['bodyweight_reps', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1238` | [Frog stand](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1238.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1406` | [Plank-to-Elbow Extension](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1406.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Familie `anti_lateral_flexion` + `abs` (12 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'time_weight', 'weight_reps']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `556` | [Side Bends on Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/556.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `576` | [Side Crunch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/576.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `577` | [Side Dumbbell Trunk Flexion](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/577.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `580` | [Side Plank](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/580.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1019` | [Side plank right](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1019.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1099` | [Dynamic side hold](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1099.yaml) | `kettlebell` | `compound` | `external` | `time_weight` |
| `1188` | [Side bend](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1188.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1288` | [Dynamic side plank](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1288.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1411` | [Heel Touches](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1411.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1426` | [Standing Side Crunches](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1426.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1650` | [Dumbbell Side Bend](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1650.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `2509` | [Side Plank (Core L1)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2509.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Familie `anti_lateral_flexion` + `lower_back` (11 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'time_weight', 'weight_reps']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `556` | [Side Bends on Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/556.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `576` | [Side Crunch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/576.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `577` | [Side Dumbbell Trunk Flexion](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/577.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `580` | [Side Plank](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/580.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1019` | [Side plank right](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1019.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1099` | [Dynamic side hold](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1099.yaml) | `kettlebell` | `compound` | `external` | `time_weight` |
| `1188` | [Side bend](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1188.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1288` | [Dynamic side plank](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1288.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1426` | [Standing Side Crunches](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1426.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1650` | [Dumbbell Side Bend](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1650.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `2509` | [Side Plank (Core L1)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2509.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Familie `anti_rotation` + `abs` (5 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `56` | [Abdominal Stabilization](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/56.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1091` | [Plank Shoulder Taps](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1091.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1194` | [Pallof Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1194.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1687` | [Bear crawl pull through](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1687.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1766` | [Plank Reach](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1766.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Familie `anti_rotation` + `glutes` (4 Übungen)
*Varianzen:* tracking_type: ['bodyweight_reps', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `957` | [Quadriped Arm and Leg Raise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/957.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1572` | [Bird Dog](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1572.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1910` | [Kneeling Superman](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1910.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2508` | [Bird Dog (Core L1)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2508.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Familie `anti_rotation` + `lower_back` (4 Übungen)
*Varianzen:* tracking_type: ['bodyweight_reps', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `957` | [Quadriped Arm and Leg Raise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/957.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1572` | [Bird Dog](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1572.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1910` | [Kneeling Superman](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1910.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2508` | [Bird Dog (Core L1)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2508.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Familie `carry` + `forearms` (2 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], tracking_type: ['distance_time', 'time_weight']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1116` | [Dumbbell farmer's carry](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1116.yaml) | `dumbbell` | `compound` | `external` | `distance_time` |
| `1430` | [Plate Pinch Hold](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1430.yaml) | `weight_plate` | `isolation` | `external` | `time_weight` |

### Familie `dorsiflexion` + `calves` (3 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'variable']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1200` | [Tibialis raises](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1200.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1241` | [Exercise Band Dorsiflexion](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1241.yaml) | `resistance_band` | `isolation` | `variable` | `bodyweight_reps` |
| `1804` | [ankle dorsiflexion rocks](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1804.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |

### Familie `elbow_extension` + `triceps` (35 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'external', 'variable'], tracking_type: ['bodyweight_reps', 'time_weight', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `50` | [Barbell Triceps Extension](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/50.yaml) | `barbell` | `isolation` | `external` | `weight_reps` |
| `112` | [Body-Ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/112.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `211` | [Dumbbell Triceps Extension](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/211.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `245` | [Skullcrusher Dumbbells](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/245.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `246` | [Skullcrusher SZ-bar](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/246.yaml) | `ez_bar` | `isolation` | `external` | `weight_reps` |
| `549` | [Seated Triceps Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/549.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `655` | [Tricep Dumbbell Kickback](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/655.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `659` | [Triceps Extensions on Cable](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/659.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `660` | [Triceps Extensions on Cable With Bar](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/660.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `661` | [Triceps on Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/661.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `803` | [One Arm Triceps Extensions on Cable](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/803.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `805` | [Tricep Pushdown on Cable](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/805.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `911` | [Incline Skull Crush](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/911.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1185` | [Triceps Pushdown](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1185.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1266` | [TRX Tricep Extension](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1266.yaml) | `suspension_trainer` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1298` | [High-Cable Cross Tricep Extention - NB](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1298.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1336` | [Triceps Overhead (Dumbbell)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1336.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1468` | [Floor Skull Crusher](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1468.yaml) | `ez_bar` | `isolation` | `external` | `weight_reps` |
| `1480` | [Lying Triceps Extensions](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1480.yaml) | `barbell` | `isolation` | `external` | `weight_reps` |
| `1481` | [Drag Pushdown](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1481.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1485` | [Rocking Triceps Pushdown](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1485.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1490` | [Lying Triceps Kickback](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1490.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1509` | [Cable Tricep Kickback](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1509.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1513` | [Overhead Cable Tricep Extension](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1513.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1519` | [Overhead Triceps Extension](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1519.yaml) | `ez_bar` | `isolation` | `external` | `weight_reps` |
| `1661` | [Cable Triceps Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1661.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1662` | [Cable Tri Extension - Internal Rotation](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1662.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1668` | [One Arm Overhead Cable Tricep Extension](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1668.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1703` | [Patadas traseras](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1703.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1717` | [Neck extension](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1717.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1824` | [Dumbell Tate Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1824.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1900` | [Tricep Rope Pushdowns](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1900.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1969` | [Single-arm cable pushdown](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1969.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `2522` | [Tricep Pull-Down](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2522.yaml) | `resistance_band` | `isolation` | `variable` | `weight_reps` |
| `2541` | [Triceps Pushdown Isometric](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2541.yaml) | `cable` | `isolation` | `external` | `time_weight` |

### Familie `elbow_flexion` + `biceps` (51 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time_weight', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `91` | [Biceps Curls With Barbell](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/91.yaml) | `barbell` | `isolation` | `external` | `weight_reps` |
| `92` | [Biceps Curls With Dumbbell](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/92.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `94` | [Biceps Curls With SZ-bar](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/94.yaml) | `ez_bar` | `isolation` | `external` | `weight_reps` |
| `95` | [Biceps Curl With Cable](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/95.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `202` | [Dumbbell Concentration Curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/202.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `204` | [Dumbbell Incline Curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/204.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `208` | [Dumbbells on Scott Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/208.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `272` | [Hammer Curls](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/272.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `275` | [Hammercurls on Cable](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/275.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `439` | [Overhand Cable Curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/439.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `465` | [Preacher Curls](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/465.yaml) | `ez_bar` | `isolation` | `external` | `weight_reps` |
| `493` | [Reverse Bar Curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/493.yaml) | `ez_bar` | `isolation` | `external` | `weight_reps` |
| `495` | [Reverse Curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/495.yaml) | `barbell` | `isolation` | `external` | `weight_reps` |
| `584` | [Single-arm Preacher Curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/584.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `621` | [Standing Bicep Curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/621.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `912` | [Straight Bar Cable Curls](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/912.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `913` | [Reverse Preacher Curl (Close Grip)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/913.yaml) | `ez_bar` | `isolation` | `external` | `weight_reps` |
| `914` | [Reverse EZ Bar Cable Curls](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/914.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `958` | [Biceps with TRX](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/958.yaml) | `suspension_trainer` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `974` | [Curl with kettlebell two hands](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/974.yaml) | `kettlebell` | `isolation` | `external` | `weight_reps` |
| `975` | [one-handed kettlebell curls](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/975.yaml) | `kettlebell` | `isolation` | `external` | `weight_reps` |
| `1012` | [Alternating bicep curls](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1012.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1109` | [Cable Concentration Curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1109.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1192` | [Alternating Biceps Curls With Dumbbell](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1192.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1224` | [Dumbbell drag curls](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1224.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1225` | [Dumbbell wide bicep curls](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1225.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1260` | [TRX hammer curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1260.yaml) | `suspension_trainer` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1261` | [TRX gorilla biceps curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1261.yaml) | `suspension_trainer` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1262` | [Trx Single Arm Bicep Curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1262.yaml) | `suspension_trainer` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1289` | [Seated Dumbbell Curls](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1289.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1290` | [Reverse Grip Barbell Curls](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1290.yaml) | `barbell` | `isolation` | `external` | `weight_reps` |
| `1424` | [Biceps Curl Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1424.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1448` | [Seated W Curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1448.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1465` | [Spider Curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1465.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1482` | [Dumbbell Cheat Curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1482.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1483` | [Bizeps Curls Trifecta](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1483.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1493` | [Bayesian Curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1493.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1502` | [DB Cross Body Hammer Curls](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1502.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1511` | [Kong Curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1511.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1512` | [Drop Curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1512.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1530` | [Lying Dumbbell Curls](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1530.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1531` | [Cable Curls](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1531.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1567` | [Alternating dumbbell hammer curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1567.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1608` | [Bodyweight Biceps Curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1608.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1657` | [Preacher Curl - Internally Rotated](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1657.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1658` | [Preacher Curl - Externally Rotated](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1658.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1666` | [Curl  - With Shoulder Elevated](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1666.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1683` | [Zottman curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1683.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1931` | [Dumbbell Curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1931.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `2504` | [DB Hammer Curls (5kg)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2504.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `2539` | [Preacher Curl Isometric](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2539.yaml) | `dumbbell` | `isolation` | `external` | `time_weight` |

### Familie `gait` + `abs` (5 Übungen)
*Varianzen:* tracking_type: ['distance_time', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `57` | [Bear Walk 2](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/57.yaml) | `bodyweight` | `compound` | `bodyweight` | `distance_time` |
| `983` | [High knees](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/983.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1196` | [Wall Drills](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1196.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1318` | [High Knee Skips HD](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1318.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1965` | [Marching High Knees](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1965.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Familie `gait` + `calves` (10 Übungen)
*Varianzen:* tracking_type: ['distance_time', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `319` | [Jogging](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/319.yaml) | `bodyweight` | `compound` | `bodyweight` | `distance_time` |
| `527` | [Run](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/527.yaml) | `bodyweight` | `compound` | `bodyweight` | `distance_time` |
| `529` | [Run - Interval Training](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/529.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `530` | [Run - Treadmill](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/530.yaml) | `cardio_machine` | `compound` | `bodyweight` | `distance_time` |
| `908` | [Zone 2 Running](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/908.yaml) | `bodyweight` | `compound` | `bodyweight` | `distance_time` |
| `1104` | [Walking](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1104.yaml) | `bodyweight` | `compound` | `bodyweight` | `distance_time` |
| `1285` | [Talons fesses](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1285.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1579` | [Bronco](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1579.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1584` | [March or jog in place](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1584.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1615` | [Treadmill Cardio](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1615.yaml) | `cardio_machine` | `compound` | `bodyweight` | `distance_time` |

### Familie `gait` + `glutes` (6 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'external'], tracking_type: ['distance_time', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `177` | [Cycling](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/177.yaml) | `other` | `compound` | `external` | `distance_time` |
| `962` | [Elliptical](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/962.yaml) | `cardio_machine` | `compound` | `external` | `distance_time` |
| `1449` | [ClimbMill](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1449.yaml) | `cardio_machine` | `compound` | `bodyweight` | `time` |
| `1548` | [Stair Master](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1548.yaml) | `cardio_machine` | `compound` | `bodyweight` | `time` |
| `2481` | [Kick with Board](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2481.yaml) | `other` | `compound` | `bodyweight` | `distance_time` |
| `2484` | [Side-Kick Breathing (Kickboard)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2484.yaml) | `other` | `compound` | `bodyweight` | `distance_time` |

### Familie `gait` + `quads` (24 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'external'], tracking_type: ['distance_time', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `57` | [Bear Walk 2](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/57.yaml) | `bodyweight` | `compound` | `bodyweight` | `distance_time` |
| `177` | [Cycling](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/177.yaml) | `other` | `compound` | `external` | `distance_time` |
| `319` | [Jogging](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/319.yaml) | `bodyweight` | `compound` | `bodyweight` | `distance_time` |
| `527` | [Run](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/527.yaml) | `bodyweight` | `compound` | `bodyweight` | `distance_time` |
| `529` | [Run - Interval Training](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/529.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `530` | [Run - Treadmill](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/530.yaml) | `cardio_machine` | `compound` | `bodyweight` | `distance_time` |
| `624` | [Stationary Bike](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/624.yaml) | `cardio_machine` | `compound` | `external` | `distance_time` |
| `908` | [Zone 2 Running](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/908.yaml) | `bodyweight` | `compound` | `bodyweight` | `distance_time` |
| `962` | [Elliptical](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/962.yaml) | `cardio_machine` | `compound` | `external` | `distance_time` |
| `983` | [High knees](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/983.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1104` | [Walking](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1104.yaml) | `bodyweight` | `compound` | `bodyweight` | `distance_time` |
| `1196` | [Wall Drills](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1196.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1204` | [Cycling cardio session](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1204.yaml) | `cardio_machine` | `compound` | `external` | `distance_time` |
| `1318` | [High Knee Skips HD](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1318.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1376` | [Recumbent Bike](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1376.yaml) | `cardio_machine` | `compound` | `external` | `distance_time` |
| `1449` | [ClimbMill](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1449.yaml) | `cardio_machine` | `compound` | `bodyweight` | `time` |
| `1548` | [Stair Master](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1548.yaml) | `cardio_machine` | `compound` | `bodyweight` | `time` |
| `1579` | [Bronco](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1579.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1584` | [March or jog in place](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1584.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1615` | [Treadmill Cardio](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1615.yaml) | `cardio_machine` | `compound` | `bodyweight` | `distance_time` |
| `1618` | [Stationary bike cardio](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1618.yaml) | `cardio_machine` | `compound` | `external` | `distance_time` |
| `1965` | [Marching High Knees](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1965.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2481` | [Kick with Board](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2481.yaml) | `other` | `compound` | `bodyweight` | `distance_time` |
| `2484` | [Side-Kick Breathing (Kickboard)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2484.yaml) | `other` | `compound` | `bodyweight` | `distance_time` |

### Familie `hinge` + `adductors` (4 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1396` | [Standing Pancake](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1396.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1397` | [Standing Pancake Good Morning](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1397.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1612` | [kettlebell sumo deadlift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1612.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1845` | [Seated Pancake Good Morning](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1845.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Familie `hinge` + `glutes` (30 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `9` | [2 Handed Kettlebell Swing](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/9.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `184` | [Deadlifts](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/184.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `189` | [Deficit Deadlift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/189.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `331` | [Kettlebell Swings](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/331.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `484` | [Rack Deadlift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/484.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `507` | [Romanian Deadlift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/507.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `604` | [Speed Deadlift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/604.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `627` | [Stiff-legged Deadlifts](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/627.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `630` | [Sumo Deadlift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/630.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `683` | [Power Clean](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/683.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `960` | [Kettlebell Swing](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/960.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1003` | [Kettlebell deadlifts](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1003.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1087` | [Dumbbell Hang Power Cleans](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1087.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1088` | [Dumbbell sumo deadlift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1088.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1141` | [Arabesque](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1141.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1370` | [Dumbbell Deadlift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1370.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1388` | [Single Leg RDL](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1388.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1392` | [Good Morning](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1392.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1438` | [Clean](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1438.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1576` | [Snap Down](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1576.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1578` | [Hip hinge](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1578.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1612` | [kettlebell sumo deadlift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1612.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1641` | [Kettlebell One Legged Deadlift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1641.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1652` | [Dumbbell Romanian Deadlift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1652.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1688` | [Kickstand RDL](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1688.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1700` | [Barbell Romanian Deadlift (RDL)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1700.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1736` | [Single-Leg Deadlift with Dumbbell](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1736.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1947` | [dumbbell snatch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1947.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `2447` | [Hip Airplane](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2447.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2524` | [Straddle Stance Good Morning](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2524.yaml) | `barbell` | `compound` | `external` | `weight_reps` |

### Familie `hinge` + `hamstrings` (30 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `9` | [2 Handed Kettlebell Swing](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/9.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `184` | [Deadlifts](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/184.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `331` | [Kettlebell Swings](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/331.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `507` | [Romanian Deadlift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/507.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `604` | [Speed Deadlift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/604.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `627` | [Stiff-legged Deadlifts](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/627.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `630` | [Sumo Deadlift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/630.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `683` | [Power Clean](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/683.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `960` | [Kettlebell Swing](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/960.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1003` | [Kettlebell deadlifts](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1003.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1087` | [Dumbbell Hang Power Cleans](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1087.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1088` | [Dumbbell sumo deadlift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1088.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1141` | [Arabesque](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1141.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1370` | [Dumbbell Deadlift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1370.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1388` | [Single Leg RDL](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1388.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1390` | [Toe Touch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1390.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1392` | [Good Morning](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1392.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1393` | [Single Leg Hamstring Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1393.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1396` | [Standing Pancake](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1396.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1397` | [Standing Pancake Good Morning](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1397.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1400` | [Crossbody Hamstring Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1400.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1578` | [Hip hinge](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1578.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1641` | [Kettlebell One Legged Deadlift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1641.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1652` | [Dumbbell Romanian Deadlift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1652.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1688` | [Kickstand RDL](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1688.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1700` | [Barbell Romanian Deadlift (RDL)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1700.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1736` | [Single-Leg Deadlift with Dumbbell](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1736.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1845` | [Seated Pancake Good Morning](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1845.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1947` | [dumbbell snatch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1947.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `2524` | [Straddle Stance Good Morning](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2524.yaml) | `barbell` | `compound` | `external` | `weight_reps` |

### Familie `hinge` + `quads` (3 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `630` | [Sumo Deadlift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/630.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1438` | [Clean](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1438.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1576` | [Snap Down](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1576.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Familie `hip_abduction` + `adductors` (2 Übungen)
*Varianzen:* tracking_type: ['bodyweight_reps', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1395` | [Crossbody Leg Swings](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1395.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1844` | [Frog Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1844.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |

### Familie `hip_abduction` + `glutes` (11 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'external', 'variable'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1096` | [Abduction while standing](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1096.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1202` | [Side Lying Hip Abduction](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1202.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1395` | [Crossbody Leg Swings](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1395.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1514` | [Lateral Walk](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1514.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1672` | [Seated Hip Abduction](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1672.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1748` | [Machine Hip Abduction](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1748.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1823` | [Clamshell](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1823.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1842` | [Banded Clamshell](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1842.yaml) | `resistance_band` | `isolation` | `variable` | `bodyweight_reps` |
| `1886` | [Supine Hip Abduction](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1886.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1915` | [Quadruped Hip Abduction](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1915.yaml) | `resistance_band` | `isolation` | `variable` | `bodyweight_reps` |
| `2491` | [Abductors](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2491.yaml) | `machine` | `isolation` | `external` | `weight_reps` |

### Familie `hip_adduction` + `adductors` (5 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['time', 'weight_reps']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `12` | [Seated Hip Adduction](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/12.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1605` | [Copenhagen Adduction Exercise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1605.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1724` | [Standing Adduction (Cable)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1724.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `2492` | [Adductors](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2492.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `2493` | [Adductor Side Plank](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2493.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Familie `hip_extension` + `glutes` (19 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external', 'variable'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `265` | [Glute Bridge](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/265.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `292` | [Hip Raise, Lying](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/292.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `294` | [Hip Thrust](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/294.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `990` | [Kneeling kickbacks](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/990.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1131` | [Cable glute extension](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1131.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1132` | [Machine glute extension](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1132.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1234` | [Dumbbell Single-leg Hip Thrust](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1234.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1503` | [Dumbbell Frog Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1503.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1528` | [Glute Drive](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1528.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1613` | [rubber band glute kickback](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1613.yaml) | `resistance_band` | `isolation` | `variable` | `bodyweight_reps` |
| `1616` | [Dumbbell donkey kick](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1616.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1642` | [Dumbbell Hip Thrust](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1642.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1723` | [Glute Kickback (Machine)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1723.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1740` | [Single Leg Glute Bridge](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1740.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1751` | [Cable pull through](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1751.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1809` | [Reverse Hyperextension](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1809.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1906` | [Hip Bridge](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1906.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1913` | [Unilateral Hip Thrust](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1913.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2534` | [(D) Puente de glúteos](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2534.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Familie `hip_extension` + `hamstrings` (3 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1132` | [Machine glute extension](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1132.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1751` | [Cable pull through](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1751.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1809` | [Reverse Hyperextension](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1809.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Familie `horizontal_pull` + `abs` (4 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `490` | [Renegade Row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/490.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1022` | [Single Arm Plank to Row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1022.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1248` | [Ice cream maker](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1248.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1252` | [Front lever pull-up](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1252.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Familie `horizontal_pull` + `back` (68 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external', 'variable'], tracking_type: ['bodyweight_reps', 'distance_time', 'weight_reps']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `79` | [Bent High Pulls](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/79.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `81` | [Bent Over Dumbbell Rows](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/81.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `83` | [Bent Over Rowing](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/83.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `84` | [Bent Over Rowing Reverse](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/84.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `222` | [Facepull](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/222.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `310` | [Incline Dumbbell Row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/310.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `380` | [Leverage Machine Iso Row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/380.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `394` | [Long-Pulley (low Row)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/394.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `395` | [Long-Pulley, Narrow](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/395.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `448` | [Pendelay Rows](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/448.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `468` | [Prone Scapular Retraction - Arms at Side](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/468.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `490` | [Renegade Row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/490.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `508` | [Row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/508.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `510` | [Rowing, Lying on Bench](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/510.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `512` | [Rowing seated, narrow grip](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/512.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `513` | [Rowing, T-bar](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/513.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `562` | [Shotgun Row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/562.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `674` | [Rowing with TRX band](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/674.yaml) | `suspension_trainer` | `compound` | `bodyweight` | `bodyweight_reps` |
| `919` | [T-Bar row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/919.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `922` | [Seated Cable Mid Trap Shrug](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/922.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `923` | [Lying Dumbbell Row SS Seated Shrug](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/923.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `959` | [TRX Rows](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/959.yaml) | `suspension_trainer` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1022` | [Single Arm Plank to Row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1022.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1083` | [YWTs](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1083.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1093` | [Rowing Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1093.yaml) | `cardio_machine` | `compound` | `external` | `distance_time` |
| `1117` | [Seated Cable Row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1117.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1119` | [Remo maquina agarre estrecho](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1119.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1120` | [Remo maquina agarre estrecho supino](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1120.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1186` | [One Arm Bent Row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1186.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1198` | [Inverted Rows](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1198.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1215` | [Reverse Snow Angel](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1215.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1219` | [Australian pull-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1219.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1248` | [Ice cream maker](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1248.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1252` | [Front lever pull-up](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1252.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1283` | [Incline Chest-Supported Dumbbell Row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1283.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1303` | [Helms Row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1303.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1304` | [Meadows Row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1304.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1380` | [Band pull-aparts](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1380.yaml) | `resistance_band` | `compound` | `variable` | `bodyweight_reps` |
| `1381` | [Upper Back](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1381.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1434` | [Lat Pull DB](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1434.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1458` | [Cross-Body Cable Y-Raise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1458.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1463` | [Dumbbell Underhand Dead Row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1463.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1471` | [Kroc Row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1471.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1486` | [Alternating High Cable Row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1486.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1492` | [High Row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1492.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1501` | [Alternative DB Gorilla rows](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1501.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1580` | [Perpendicular Unilateral Landmine Row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1580.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1621` | [Unilateral Cable row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1621.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1634` | [Rope Pullover/row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1634.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1637` | [Single arm row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1637.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1639` | [Dumbbell Bent Over Face Pull](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1639.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1698` | [Barbell Row (Overhand)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1698.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1699` | [Barbell Row (Underhand)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1699.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1701` | [One-Arm Heavy Row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1701.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1718` | [Remo alto polea alta](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1718.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1725` | [Seated Row (Machine)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1725.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1732` | [Face pulls with yellow/green band](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1732.yaml) | `resistance_band` | `compound` | `variable` | `bodyweight_reps` |
| `1834` | [Trap-3 Raise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1834.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1877` | [Banded Scapular Retraction](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1877.yaml) | `resistance_band` | `isolation` | `variable` | `bodyweight_reps` |
| `1885` | [YTWL Exercise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1885.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1905` | [Pullback](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1905.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1928` | [Seated V-Grip Row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1928.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `2454` | [YTW Raises](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2454.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2489` | [Low row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2489.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `2490` | [Pulley (low, with triangle)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2490.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `2501` | [Table Bodyweight Rows (Vasco L1)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2501.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2502` | [DB Single-Arm Row (5kg)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2502.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `2503` | [Face Pulls (Bodyweight Doorframe/Towel)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2503.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Familie `horizontal_pull` + `biceps` (4 Übungen)
*Varianzen:* tracking_type: ['time_weight', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `84` | [Bent Over Rowing Reverse](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/84.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `284` | [Hercules Pillars](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/284.yaml) | `cable` | `compound` | `external` | `time_weight` |
| `1120` | [Remo maquina agarre estrecho supino](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1120.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1699` | [Barbell Row (Underhand)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1699.yaml) | `barbell` | `compound` | `external` | `weight_reps` |

### Familie `horizontal_pull` + `shoulders` (20 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external', 'variable'], tracking_type: ['bodyweight_reps', 'time_weight', 'weight_reps']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `79` | [Bent High Pulls](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/79.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `82` | [Bent-over Lateral Raises](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/82.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `139` | [Butterfly Reverse](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/139.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `222` | [Facepull](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/222.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `284` | [Hercules Pillars](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/284.yaml) | `cable` | `compound` | `external` | `time_weight` |
| `487` | [Rear Delt Raises](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/487.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `822` | [Cable Rear Delt Fly](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/822.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `828` | [Incline Bench Reverse Fly](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/828.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1098` | [Seated rear delt rise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1098.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1227` | [Dumbbell rear delt row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1227.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1380` | [Band pull-aparts](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1380.yaml) | `resistance_band` | `compound` | `variable` | `bodyweight_reps` |
| `1458` | [Cross-Body Cable Y-Raise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1458.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1473` | [Reverse Cable Flye](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1473.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1639` | [Dumbbell Bent Over Face Pull](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1639.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1709` | [Reverse Fly Standing](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1709.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1732` | [Face pulls with yellow/green band](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1732.yaml) | `resistance_band` | `compound` | `variable` | `bodyweight_reps` |
| `1775` | [Pec deck rear delt fly](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1775.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1825` | [Chest-Supported Rear Delt Raise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1825.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1936` | [Cable Rear-Delt Fly (single arm)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1936.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `2503` | [Face Pulls (Bodyweight Doorframe/Towel)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2503.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Familie `horizontal_push` + `chest` (87 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'time_weight', 'weight_reps']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `73` | [Bench Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/73.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `75` | [Benchpress Dumbbells](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/75.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `129` | [Chest Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/129.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `135` | [Butterfly](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/135.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `137` | [Butterfly Narrow Grip](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/137.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `185` | [Decline Bench Press Barbell](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/185.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `186` | [Decline Bench Press Dumbbell](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/186.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `237` | [Fly With Cable](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/237.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `238` | [Fly With Dumbbells](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/238.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `239` | [Fly With Dumbbells, Decline Bench](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/239.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `308` | [Incline Dumbbell Fly](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/308.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `314` | [Isometric Wipers](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/314.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `323` | [Cable Cross-over](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/323.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `379` | [Leverage Machine Chest Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/379.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `386` | [Diamond push ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/386.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `445` | [Pause Bench](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/445.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `498` | [Reverse Grip Bench Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/498.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `537` | [Incline Bench Press - Dumbbell](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/537.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `538` | [Incline Bench Press - Barbell](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/538.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `539` | [Incline Bench Press - MP](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/539.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `583` | [Side to Side Push Ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/583.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `598` | [Smith Machine Close-grip Bench Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/598.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `713` | [Wall Pushup](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/713.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `801` | [Dumbbell Push-Up](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/801.yaml) | `dumbbell` | `compound` | `bodyweight` | `bodyweight_reps` |
| `925` | [Smith Machine Slight Incline Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/925.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `926` | [Machine chest fly](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/926.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `927` | [Suspended crossess](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/927.yaml) | `suspension_trainer` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `985` | [Push-up rotations](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/985.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1080` | [Hindu Pushups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1080.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1084` | [Dumbbell Floor Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1084.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1086` | [Close-grip Press-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1086.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1092` | [Bag training](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1092.yaml) | `other` | `compound` | `bodyweight` | `time` |
| `1094` | [Seated Bench Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1094.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1111` | [Push-Ups | Incline](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1111.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1112` | [Push-Ups | Decline](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1112.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1113` | [Push-Ups | Parallettes](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1113.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1209` | [Shoulder width three-point push-up](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1209.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1217` | [Finger Pushup](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1217.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1218` | [knee push-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1218.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1228` | [Dumbbell close grip bench press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1228.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1270` | [Low Pulley Cable Fly](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1270.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1284` | [Pseudo Planche Push-up](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1284.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1293` | [One armed push-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1293.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1296` | [Low-Cable Cross-Over - NB](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1296.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1353` | [Dumbbell Hex Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1353.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1436` | [Pin Bench Press BB](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1436.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1457` | [Cable Press Around](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1457.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1461` | [No Leg Drive Dumbbell Chest Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1461.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1467` | [Incline Close Grip Barbell Bench Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1467.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1469` | [Bent over Cable Flye](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1469.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1484` | [Omni Cable Cross-over](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1484.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1496` | [DB Upper Chest Variation](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1496.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1497` | [DB Underhand bench press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1497.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1498` | [Elbows Tucked DB Bench Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1498.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1508` | [High-Incline Smith Machine Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1508.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `1546` | [Larsen Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1546.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1551` | [Push-Up](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1551.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1554` | [Clap Push-UP](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1554.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1581` | [Trap press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1581.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1583` | [Supine press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1583.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1656` | [Cable Chest Press - Decline](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1656.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1660` | [Cable Chest Press - Incline](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1660.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1686` | [Glute Bridge Single-Arm Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1686.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1689` | [Cable Fly Middle Chest](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1689.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1690` | [Cable Fly Upper Chest](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1690.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1691` | [Cable Fly Lower Chest](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1691.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1693` | [Incline Static Hold](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1693.yaml) | `dumbbell` | `compound` | `external` | `time_weight` |
| `1694` | [Flat Machine Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1694.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1716` | [Incline Shoulder Press Up](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1716.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1773` | [Legend Incline Bench Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1773.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1777` | [Deficit Push ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1777.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1778` | [Supino inclinado](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1778.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1831` | [Hammerstrength Decline Chest Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1831.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1902` | [Weighted push-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1902.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1904` | [Pec Deck](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1904.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1916` | [Tuck planche](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1916.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1918` | [Legend Chest Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1918.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1922` | [Seated Cable chest fly](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1922.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1964` | [Wide Push-Up](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1964.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2496` | [Wall Push-ups (Vasco L1)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2496.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2497` | [DB Floor Press (5kg Single Arm)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2497.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `2499` | [Incline Push-ups (Vasco L2)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2499.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2529` | [explosive push ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2529.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2530` | [Russian Push Ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2530.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2532` | [Planche Lean Hold](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2532.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2536` | [Bench Press Isometric](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2536.yaml) | `barbell` | `compound` | `external` | `time_weight` |
| `2542` | [Boxing](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2542.yaml) | `other` | `compound` | `bodyweight` | `time` |

### Familie `horizontal_push` + `glutes` (2 Übungen)
*Varianzen:* tracking_type: ['distance_time', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1523` | [Sled Push](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1523.yaml) | `sled` | `compound` | `external` | `distance_time` |
| `1686` | [Glute Bridge Single-Arm Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1686.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |

### Familie `horizontal_push` + `shoulders` (7 Übungen)
*Varianzen:* tracking_type: ['bodyweight_reps', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1080` | [Hindu Pushups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1080.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1092` | [Bag training](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1092.yaml) | `other` | `compound` | `bodyweight` | `time` |
| `1284` | [Pseudo Planche Push-up](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1284.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1462` | [punches](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1462.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1916` | [Tuck planche](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1916.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2532` | [Planche Lean Hold](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2532.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2542` | [Boxing](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2542.yaml) | `other` | `compound` | `bodyweight` | `time` |

### Familie `horizontal_push` + `triceps` (13 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `76` | [Bench Press Narrow Grip](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/76.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `386` | [Diamond push ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/386.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `498` | [Reverse Grip Bench Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/498.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `598` | [Smith Machine Close-grip Bench Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/598.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `1086` | [Close-grip Press-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1086.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1092` | [Bag training](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1092.yaml) | `other` | `compound` | `bodyweight` | `time` |
| `1228` | [Dumbbell close grip bench press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1228.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1293` | [One armed push-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1293.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1302` | [JM Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1302.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1467` | [Incline Close Grip Barbell Bench Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1467.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1498` | [Elbows Tucked DB Bench Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1498.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1583` | [Supine press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1583.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `2542` | [Boxing](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2542.yaml) | `other` | `compound` | `bodyweight` | `time` |

### Familie `knee_extension` + `quads` (5 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'external', 'variable'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `71` | [Single Leg Extension](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/71.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `369` | [Leg Extension](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/369.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `909` | [Reverse Nordic Curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/909.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `2494` | [Band Terminal Knee extension](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2494.yaml) | `resistance_band` | `isolation` | `variable` | `bodyweight_reps` |
| `2535` | [Leg Extension Isometric](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2535.yaml) | `machine` | `isolation` | `external` | `time` |

### Familie `knee_flexion` + `hamstrings` (11 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'external', 'variable'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `364` | [Leg Curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/364.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `365` | [Leg Curls (laying)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/365.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `366` | [Leg Curls (sitting)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/366.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `367` | [Leg Curls (standing)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/367.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `910` | [Nordic Curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/910.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1294` | [Single-leg hamstring curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1294.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1391` | [Elephant Walks](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1391.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1603` | [Leg curl with elastic](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1603.yaml) | `resistance_band` | `isolation` | `variable` | `bodyweight_reps` |
| `1833` | [Floor Glider Hamstring Curls](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1833.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `2478` | [Glute-Ham Raise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2478.yaml) | `machine` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `2495` | [Machine Leg Flexion](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2495.yaml) | `machine` | `isolation` | `external` | `weight_reps` |

### Familie `lunge` + `glutes` (26 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `46` | [Barbell Lunges Standing](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/46.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `205` | [Dumbbell Lunges Standing](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/205.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `206` | [Dumbbell Lunges Walking](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/206.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `722` | [Weighted Step-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/722.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `802` | [Barbell Lunges Walking](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/802.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `981` | [Step-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/981.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `984` | [Lunges](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/984.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `986` | [Side split squats left](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/986.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `987` | [Side split squats right](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/987.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `988` | [Bulgarian split squats left](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/988.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `989` | [Bulgarian split squats right](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/989.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `991` | [Split squats left](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/991.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `992` | [Split squats right](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/992.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `999` | [Reverse lunges](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/999.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1102` | [Alternate back lunges](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1102.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1115` | [3D lunge warmup](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1115.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1324` | [Bodyweight lunge HD](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1324.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1366` | [Dumbbell Split Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1366.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1593` | [Smith Machine Split Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1593.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `1604` | [Sliding Lateral Lunge](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1604.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1651` | [Dumbbell Rear Lunge](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1651.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1706` | [Bulgarian Squat with Dumbbells](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1706.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1734` | [Single-Leg Lunge with Kettlebell:](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1734.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1830` | [Barbell Step Back Lunge](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1830.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1907` | [Unilateral Lunges](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1907.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2526` | [Long Lunge Pulse Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2526.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Familie `lunge` + `quads` (25 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `46` | [Barbell Lunges Standing](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/46.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `205` | [Dumbbell Lunges Standing](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/205.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `206` | [Dumbbell Lunges Walking](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/206.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `722` | [Weighted Step-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/722.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `802` | [Barbell Lunges Walking](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/802.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `981` | [Step-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/981.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `984` | [Lunges](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/984.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `986` | [Side split squats left](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/986.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `987` | [Side split squats right](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/987.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `988` | [Bulgarian split squats left](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/988.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `989` | [Bulgarian split squats right](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/989.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `991` | [Split squats left](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/991.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `992` | [Split squats right](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/992.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `999` | [Reverse lunges](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/999.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1102` | [Alternate back lunges](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1102.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1115` | [3D lunge warmup](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1115.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1324` | [Bodyweight lunge HD](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1324.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1366` | [Dumbbell Split Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1366.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1593` | [Smith Machine Split Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1593.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `1604` | [Sliding Lateral Lunge](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1604.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1651` | [Dumbbell Rear Lunge](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1651.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1706` | [Bulgarian Squat with Dumbbells](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1706.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1734` | [Single-Leg Lunge with Kettlebell:](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1734.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1830` | [Barbell Step Back Lunge](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1830.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1907` | [Unilateral Lunges](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1907.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Familie `other` + `abs` (20 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `675` | [Turkish Get-Up](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/675.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `996` | [Mountain climbers](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/996.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `997` | [4-count burpees](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/997.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1244` | [Yoga exercise: Cow-cat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1244.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1524` | [Battle Ropes](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1524.yaml) | `other` | `compound` | `bodyweight` | `time` |
| `1525` | [Ball Slams](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1525.yaml) | `medicine_ball` | `compound` | `external` | `weight_reps` |
| `1591` | [Deep breathing (standing or seated)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1591.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1670` | [Leg Swings (Front–Back)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1670.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1839` | [Solo Hip Flexor Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1839.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1861` | [Side stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1861.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1867` | [Hip Flexor Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1867.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1874` | [Runners Lunge Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1874.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1938` | [Cat-Cow](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1938.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1940` | [Diaphragmatic Breathing](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1940.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1949` | [Limber 11](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1949.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1960` | [Rear-foot-elevated Hip Flexor Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1960.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `2482` | [Bobbing Exhale Drill](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2482.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2486` | [Recovery Bobbing](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2486.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2525` | [Couch Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2525.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `2527` | [Front Split Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2527.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Familie `other` + `adductors` (4 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], tracking_type: ['bodyweight_reps', 'time']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1843` | [Butterfly Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1843.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1860` | [Foam Roller Adductors](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1860.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1949` | [Limber 11](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1949.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1954` | [Roll-overs into V-sits](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1954.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Familie `other` + `back` (6 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['time', 'weight_reps']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1027` | [Elevated prayer stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1027.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1525` | [Ball Slams](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1525.yaml) | `medicine_ball` | `compound` | `external` | `weight_reps` |
| `1590` | [Arm and neck stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1590.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1710` | [Butchers Block Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1710.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1861` | [Side stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1861.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1921` | [Extreme Lat Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1921.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |

### Familie `other` + `calves` (14 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'variable'], tracking_type: ['bodyweight_reps', 'time']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `320` | [Jumping Jacks](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/320.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `595` | [Skipping - Standard](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/595.yaml) | `jump_rope` | `compound` | `bodyweight` | `time` |
| `993` | [Jump rope: basic jumps](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/993.yaml) | `jump_rope` | `compound` | `bodyweight` | `time` |
| `998` | [No push-up burpees](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/998.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1239` | [Standing Calf Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1239.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1240` | [Standing Soleus Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1240.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1274` | [Sitting Calf Stretch (Dorsiflexion)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1274.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1275` | [Plantarflexion Stretch with Band](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1275.yaml) | `resistance_band` | `isolation` | `variable` | `time` |
| `1314` | [Jumping Jack HD](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1314.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1854` | [Calves foam roller](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1854.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1856` | [Foam Roller Anterior tibialis](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1856.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1865` | [Banded Ankle Mobility](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1865.yaml) | `resistance_band` | `isolation` | `variable` | `bodyweight_reps` |
| `1876` | [Supported Calf Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1876.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1962` | [Step Jack](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1962.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Familie `other` + `chest` (5 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], tracking_type: ['bodyweight_reps', 'time']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `132` | [Burpees](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/132.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1712` | [Horizontal Shoulder Flexion Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1712.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1713` | [Doorway Pectoral Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1713.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1919` | [Extreme Pec Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1919.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `2523` | [Serratus Wall Slide Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2523.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |

### Familie `other` + `glutes` (16 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1325` | [Lateral Push Off](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1325.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1452` | [Knee to Chest Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1452.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1556` | [Devil’s Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1556.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1589` | [Leg and hip stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1589.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1630` | [Blaze](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1630.yaml) | `other` | `compound` | `external` | `time` |
| `1680` | [seated figure four](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1680.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1857` | [Foam Roller Iliotibial band](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1857.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1859` | [Foam Roller Gluteus](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1859.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1869` | [Lying Figure Four Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1869.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1872` | [Pigeon Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1872.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1874` | [Runners Lunge Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1874.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1875` | [Standing IT Band Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1875.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1949` | [Limber 11](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1949.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1950` | [Foam Roll IT Band](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1950.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1952` | [SMR Glutes (lax ball)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1952.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1959` | [Seated Piriformis Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1959.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |

### Familie `other` + `hamstrings` (9 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'variable'], tracking_type: ['bodyweight_reps', 'time']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1387` | [Hamstring Kicks](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1387.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1589` | [Leg and hip stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1589.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1670` | [Leg Swings (Front–Back)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1670.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1840` | [Bent-Leg Hamstring Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1840.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1855` | [Hamstring Foam roller](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1855.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1870` | [Lying Hamstring Stretch with Band](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1870.yaml) | `resistance_band` | `isolation` | `variable` | `time` |
| `1949` | [Limber 11](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1949.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1954` | [Roll-overs into V-sits](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1954.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2527` | [Front Split Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2527.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Familie `other` + `lower_back` (4 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], tracking_type: ['bodyweight_reps', 'time']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1244` | [Yoga exercise: Cow-cat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1244.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1363` | [Blackroll](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1363.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1592` | [Guided or free meditation](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1592.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1938` | [Cat-Cow](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1938.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Familie `other` + `neck` (3 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], tracking_type: ['bodyweight_reps', 'time']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1006` | [Chin tuck](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1006.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1018` | [Head tilts](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1018.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1590` | [Arm and neck stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1590.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Familie `other` + `quads` (14 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `132` | [Burpees](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/132.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `320` | [Jumping Jacks](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/320.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `595` | [Skipping - Standard](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/595.yaml) | `jump_rope` | `compound` | `bodyweight` | `time` |
| `993` | [Jump rope: basic jumps](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/993.yaml) | `jump_rope` | `compound` | `bodyweight` | `time` |
| `997` | [4-count burpees](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/997.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `998` | [No push-up burpees](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/998.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1314` | [Jumping Jack HD](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1314.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1325` | [Lateral Push Off](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1325.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1630` | [Blaze](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1630.yaml) | `other` | `compound` | `external` | `time` |
| `1858` | [Foam Roller quadriceps](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1858.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1873` | [Quad Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1873.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1960` | [Rear-foot-elevated Hip Flexor Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1960.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1962` | [Step Jack](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1962.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2525` | [Couch Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2525.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |

### Familie `other` + `shoulders` (7 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['time', 'weight_reps']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `675` | [Turkish Get-Up](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/675.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1524` | [Battle Ropes](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1524.yaml) | `other` | `compound` | `bodyweight` | `time` |
| `1536` | [Delt Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1536.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1556` | [Devil’s Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1556.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1630` | [Blaze](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1630.yaml) | `other` | `compound` | `external` | `time` |
| `1841` | [Seated Shoulder Extension Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1841.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1920` | [Extreme Shoulder Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1920.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |

### Familie `plantar_flexion` + `calves` (12 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'external', 'variable'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `146` | [Calf Press Using Leg Press Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/146.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `148` | [Calf Raises on Hackenschmitt Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/148.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `590` | [Sitting Calf Raises](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/590.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `622` | [Standing Calf Raises](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/622.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `702` | [Calf raises, one legged](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/702.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1021` | [Calf raises, right leg](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1021.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1203` | [Calf raises, left leg](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1203.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1242` | [Exercise Band Plantarflexion](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1242.yaml) | `resistance_band` | `isolation` | `variable` | `bodyweight_reps` |
| `1243` | [Double Leg Calf Raise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1243.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1466` | [Calf Raise using Hack Squat Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1466.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1515` | [Leg Press Toe Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1515.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1620` | [Seated Dumbbell Calf Raise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1620.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |

### Familie `rotation` + `abs` (26 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external', 'variable'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `145` | [Cable Woodchoppers](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/145.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `260` | [Full Sit Outs](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/260.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `607` | [Splinter Sit-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/607.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `672` | [Trunk Rotation With Cable](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/672.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1028` | [Quadruped thoracic rotation left](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1028.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1029` | [Quadruped thoracic rotation right](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1029.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1089` | [Medicine ball twist](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1089.yaml) | `medicine_ball` | `compound` | `external` | `weight_reps` |
| `1193` | [Russian Twist](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1193.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1259` | [TRX Obliques](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1259.yaml) | `suspension_trainer` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1374` | [Rotary Torso Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1374.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1377` | [Torso Twist](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1377.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1412` | [bicycle crunches](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1412.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1433` | [Reverse Wood Chops](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1433.yaml) | `resistance_band` | `compound` | `variable` | `bodyweight_reps` |
| `1451` | [Torso rotation stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1451.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1475` | [Black Widow Knee Slides](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1475.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1477` | [Seated Corkscrew](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1477.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1479` | [Sit Up Elbow Thrust](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1479.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1743` | [Windshield Wipers](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1743.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1779` | [Landmine Rotation](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1779.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1822` | [Open Book](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1822.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1868` | [Lunge with Twist Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1868.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1912` | [Core Rotation](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1912.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1953` | [Bent-knee Iron Cross](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1953.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1966` | [1/2 Kneeling Thoracic Rotation](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1966.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2483` | [Wall-Hold Rotation](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2483.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2528` | [Squat Sky Reach Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2528.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Familie `rotation` + `back` (5 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'variable']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1028` | [Quadruped thoracic rotation left](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1028.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1029` | [Quadruped thoracic rotation right](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1029.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1082` | [Bent over row to external rotation](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1082.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1822` | [Open Book](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1822.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1826` | [Band pull-apart with external rotation](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1826.yaml) | `resistance_band` | `compound` | `variable` | `bodyweight_reps` |

### Familie `rotation` + `glutes` (10 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], tracking_type: ['bodyweight_reps', 'time']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1207` | [Scorpion Kick](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1207.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1577` | [Bretzel stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1577.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1862` | [Hip Circles](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1862.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1863` | [Hip Crossover](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1863.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1868` | [Lunge with Twist Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1868.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1884` | [Shinbox IR Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1884.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1953` | [Bent-knee Iron Cross](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1953.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1956` | [Fire Hydrant Circles](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1956.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `2448` | [Reverse Clamshell](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2448.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `2449` | [Clamshell to Reverse Clamshell](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2449.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |

### Familie `rotation` + `neck` (5 Übungen)
*Varianzen:* tracking_type: ['bodyweight_reps', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1007` | [Head turns](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1007.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1015` | [Clockwise neck circles](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1015.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1016` | [Counterclockwise neck circles](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1016.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1017` | [Neck half circles](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1017.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1939` | [Neck CARs](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1939.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |

### Familie `rotation` + `shoulders` (20 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external', 'variable'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `142` | [Cable External Rotation](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/142.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `406` | [Lying Rotator Cuff Exercise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/406.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `578` | [Side-lying External Rotation](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/578.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `915` | [Bus Drivers](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/915.yaml) | `weight_plate` | `isolation` | `external` | `weight_reps` |
| `994` | [Forward arm circles](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/994.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `995` | [Backward arm circles](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/995.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1004` | [Forward shoulder rotation](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1004.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1005` | [Backward shoulder rotation](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1005.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1081` | [Shoulder dislocates](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1081.yaml) | `resistance_band` | `compound` | `variable` | `bodyweight_reps` |
| `1082` | [Bent over row to external rotation](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1082.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1429` | [Dumbbell Shoulder Rotations](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1429.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1582` | [Side-laying interior rotation](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1582.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1711` | [Sleeper Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1711.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1714` | [Shoulder Dumbbell Pendular Exercise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1714.yaml) | `dumbbell` | `isolation` | `external` | `time` |
| `1715` | [Shoulder External Rotation with Dumbbell](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1715.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1728` | [Shoulder Internal Rotation (Cable)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1728.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1729` | [Shoulder External Rotation (Cable)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1729.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1826` | [Band pull-apart with external rotation](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1826.yaml) | `resistance_band` | `compound` | `variable` | `bodyweight_reps` |
| `1835` | [External Rotation Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1835.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1838` | [Banded Shoulder Drills](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1838.yaml) | `resistance_band` | `compound` | `variable` | `bodyweight_reps` |

### Familie `scapular_elevation` + `back` (6 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `570` | [Shoulder Shrug](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/570.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `571` | [Shrugs, Barbells](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/571.yaml) | `barbell` | `isolation` | `external` | `weight_reps` |
| `572` | [Shrugs, Dumbbells](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/572.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `575` | [Shrugs on Multipress](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/575.yaml) | `smith_machine` | `isolation` | `external` | `weight_reps` |
| `1472` | [Cable Shrug-In](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1472.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1925` | [Barbell Silverback Shrug](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1925.yaml) | `barbell` | `isolation` | `external` | `weight_reps` |

### Familie `shoulder_abduction` + `back` (3 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1606` | [Arm Raises (T/Y/I)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1606.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1679` | [Wall Angels](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1679.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1879` | [Incline DB Y-Raise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1879.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |

### Familie `shoulder_abduction` + `shoulders` (19 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time_weight', 'weight_reps']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `31` | [Axe Hold](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/31.yaml) | `dumbbell` | `isolation` | `external` | `time_weight` |
| `348` | [Lateral Raises](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/348.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `349` | [Lateral Rows on Cable, One Armed](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/349.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `351` | [Lateral-to-Front Raises](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/351.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `918` | [Seated Dumbbell Side Lateral](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/918.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1378` | [Cable Lateral Raises (Single Arm)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1378.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1443` | [Shoulder Raise Side and Front DB](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1443.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1602` | [Dumbbell Scaption](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1602.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1606` | [Arm Raises (T/Y/I)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1606.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1654` | [Machine Lateral Raise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1654.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1707` | [Elevación lateral polea](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1707.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1730` | [Side Lateral Raise (Cable)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1730.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1752` | [Side lateral raise - Front (Cable)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1752.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1753` | [Side lateral raise - Back (Cable)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1753.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1754` | [45° lateral raises](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1754.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1807` | [Behind the Back Cable Lateral Raise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1807.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1879` | [Incline DB Y-Raise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1879.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1882` | [High-Cable Lateral Raise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1882.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `2538` | [Lateral Raise Isometric](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2538.yaml) | `cable` | `isolation` | `external` | `time_weight` |

### Familie `shoulder_flexion` + `shoulders` (7 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `254` | [Front Raises with Plates](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/254.yaml) | `weight_plate` | `isolation` | `external` | `weight_reps` |
| `256` | [Front Raises](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/256.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `917` | [Straight Bar Cable Front Raise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/917.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1223` | [Claps over the head](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1223.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1338` | [Shoulder Raise (Dumbbell)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1338.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1731` | [Front Raise (Cable)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1731.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1745` | [Cable Front Raise with a small bar](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1745.yaml) | `cable` | `isolation` | `external` | `weight_reps` |

### Familie `spinal_extension` + `back` (2 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1455` | [Towel Superman](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1455.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1487` | [Hyper Y W Combo](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1487.yaml) | `weight_plate` | `compound` | `external` | `weight_reps` |

### Familie `spinal_extension` + `glutes` (4 Übungen)
*Varianzen:* tracking_type: ['bodyweight_reps', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `636` | [Superman](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/636.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1210` | [Skydiver with arms in T-position](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1210.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1263` | [Back bridge](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1263.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1348` | [Lower Back Extensions](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1348.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Familie `spinal_extension` + `lower_back` (11 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `301` | [Hyperextensions](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/301.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `516` | [Front Wood Chop](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/516.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `636` | [Superman](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/636.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1143` | [Back extensión](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1143.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1210` | [Skydiver with arms in T-position](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1210.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1263` | [Back bridge](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1263.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1348` | [Lower Back Extensions](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1348.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1455` | [Towel Superman](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1455.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1487` | [Hyper Y W Combo](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1487.yaml) | `weight_plate` | `compound` | `external` | `weight_reps` |
| `1810` | [Sphinx](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1810.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1908` | [Butterfly Superman](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1908.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Familie `spinal_flexion` + `abs` (31 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `165` | [Ball crunches](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/165.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `167` | [Crunches](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/167.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `171` | [Incline Crunches](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/171.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `172` | [Crunches on Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/172.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `173` | [Crunches With Cable](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/173.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `174` | [Crunches With Legs Up](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/174.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `283` | [Hanging Leg Raises](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/283.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `377` | [Leg Raises, Lying](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/377.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `378` | [Leg Raises, Standing](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/378.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `427` | [Negative Crunches](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/427.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `505` | [Roman Chair Crunch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/505.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `591` | [Sit-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/591.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `688` | [Upper External Oblique](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/688.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `976` | [Medicine ball booklet crunch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/976.yaml) | `medicine_ball` | `compound` | `external` | `weight_reps` |
| `978` | [Knee Raises](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/978.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `979` | [Leg raises pull up bar](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/979.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1105` | [Seated Knee Tuck](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1105.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1286` | [Dynamic Planche](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1286.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1287` | [Reach ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1287.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1399` | [Roll Down](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1399.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1415` | [Dumbbell Crunches](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1415.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1474` | [W-Raise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1474.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1476` | [Butterfly Sit Up](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1476.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1478` | [Levitation Crunch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1478.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1529` | [Toes to bar](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1529.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1648` | [Weighted Crunch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1648.yaml) | `weight_plate` | `isolation` | `external` | `weight_reps` |
| `1772` | [Reverse crunch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1772.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1889` | [Decline Bench Leg Raise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1889.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1924` | [3008 Abdominal Crunch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1924.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1933` | [Abdominal Crunch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1933.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `2488` | [Posterior Pelvic Tilt](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2488.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |

### Familie `spinal_flexion` + `lower_back` (2 Übungen)
*Varianzen:* tracking_type: ['bodyweight_reps', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1002` | [Child's pose](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1002.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1399` | [Roll Down](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1399.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Familie `squat` + `adductors` (2 Übungen)
*Varianzen:* tracking_type: ['bodyweight_reps', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `632` | [Sumo Squats](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/632.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1846` | [Horse Stance (Side Splits)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1846.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Familie `squat` + `glutes` (43 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `43` | [Barbell Hack Squats](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/43.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `124` | [Braced Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/124.yaml) | `weight_plate` | `compound` | `external` | `weight_reps` |
| `203` | [Dumbbell Goblet Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/203.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `257` | [Front Squats](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/257.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `285` | [High Knee Jumps](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/285.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `341` | [Squats on Multipress](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/341.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `371` | [Leg Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/371.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `374` | [Leg Presses (wide)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/374.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `375` | [Leg Press on Hackenschmidt Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/375.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `397` | [Low Box Squat - Wide Stance](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/397.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `441` | [Overhead Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/441.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `456` | [Pistol Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/456.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `614` | [Squat Jumps](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/614.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `615` | [Squats](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/615.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `616` | [Squat Thrust](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/616.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `632` | [Sumo Squats](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/632.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `650` | [Thruster](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/650.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `977` | [Box squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/977.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1020` | [Pistol squats right](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1020.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1195` | [Side Slides + Squats](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1195.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1201` | [Dragon squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1201.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1208` | [Prisoner Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1208.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1312` | [Bodyweight Squat HD](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1312.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1361` | [Double Kettlebell Front Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1361.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1373` | [box jumps](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1373.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1407` | [Cossack squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1407.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1408` | [Wall-sit](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1408.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1414` | [Hack Squats](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1414.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1437` | [Pin Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1437.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1464` | [Pause Hack Squats](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1464.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1527` | [Pendulum Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1527.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1640` | [Dumbbell Front Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1640.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1653` | [Dumbbell Side Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1653.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1733` | [Isometric Squat to Failure](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1733.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1735` | [Single-leg side glute press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1735.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1739` | [Shrimp Squad](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1739.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1747` | [Smith machine squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1747.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `1801` | [Barbell Full Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1801.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1803` | [Trap Bar Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1803.yaml) | `trap_bar` | `compound` | `external` | `weight_reps` |
| `1829` | [Landmine Squat to Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1829.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1935` | [Belt Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1935.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1948` | [1 Leg Box Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1948.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1963` | [Slow Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1963.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Familie `squat` + `quads` (47 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `43` | [Barbell Hack Squats](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/43.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `124` | [Braced Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/124.yaml) | `weight_plate` | `compound` | `external` | `weight_reps` |
| `203` | [Dumbbell Goblet Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/203.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `257` | [Front Squats](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/257.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `285` | [High Knee Jumps](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/285.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `291` | [Hindu Squats](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/291.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `341` | [Squats on Multipress](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/341.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `371` | [Leg Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/371.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `373` | [Leg Presses (narrow)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/373.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `374` | [Leg Presses (wide)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/374.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `375` | [Leg Press on Hackenschmidt Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/375.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `397` | [Low Box Squat - Wide Stance](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/397.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `441` | [Overhead Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/441.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `456` | [Pistol Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/456.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `614` | [Squat Jumps](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/614.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `615` | [Squats](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/615.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `616` | [Squat Thrust](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/616.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `632` | [Sumo Squats](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/632.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `650` | [Thruster](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/650.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `718` | [Wall Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/718.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `977` | [Box squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/977.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1020` | [Pistol squats right](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1020.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1195` | [Side Slides + Squats](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1195.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1201` | [Dragon squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1201.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1208` | [Prisoner Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1208.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1312` | [Bodyweight Squat HD](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1312.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1361` | [Double Kettlebell Front Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1361.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1373` | [box jumps](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1373.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1407` | [Cossack squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1407.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1408` | [Wall-sit](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1408.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1414` | [Hack Squats](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1414.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1437` | [Pin Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1437.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1464` | [Pause Hack Squats](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1464.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1521` | [Pendular hack](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1521.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1527` | [Pendulum Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1527.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1640` | [Dumbbell Front Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1640.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1653` | [Dumbbell Side Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1653.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1733` | [Isometric Squat to Failure](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1733.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1739` | [Shrimp Squad](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1739.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1747` | [Smith machine squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1747.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `1801` | [Barbell Full Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1801.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1803` | [Trap Bar Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1803.yaml) | `trap_bar` | `compound` | `external` | `weight_reps` |
| `1829` | [Landmine Squat to Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1829.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1846` | [Horse Stance (Side Splits)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1846.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1935` | [Belt Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1935.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1948` | [1 Leg Box Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1948.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1963` | [Slow Squat](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1963.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Familie `vertical_pull` + `abs` (2 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'distance_time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1526` | [Ski Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1526.yaml) | `cardio_machine` | `compound` | `external` | `distance_time` |
| `1741` | [L-Sit Pull-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1741.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Familie `vertical_pull` + `back` (60 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['assisted', 'bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'distance_time', 'time', 'time_weight', 'weight_reps']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `152` | [Chin Up](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/152.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `158` | [Close-grip Lat Pull Down](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/158.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `161` | [Cross-Bench Dumbbell Pullovers](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/161.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `258` | [Front pull wide](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/258.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `259` | [Front Pull narrow](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/259.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `289` | [High Pull](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/289.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `354` | [Lat Pull Down (Leaning Back)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/354.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `355` | [Lat Pull Down (Straight Back)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/355.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `423` | [Muscle up](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/423.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `475` | [Pull-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/475.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `477` | [Pull Ups on Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/477.yaml) | `machine` | `compound` | `assisted` | `weight_reps` |
| `628` | [Straight-arm Pull Down (bar Attachment)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/628.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `629` | [Straight-arm Pull Down (rope Attachment)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/629.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `684` | [Underhand Lat Pull Down](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/684.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `691` | [Upright Row, on Multi Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/691.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `693` | [Upright Row, SZ-bar](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/693.yaml) | `ez_bar` | `compound` | `external` | `weight_reps` |
| `694` | [Upright Row w/ Dumbbells](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/694.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `695` | [V-Bar Pulldown](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/695.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `723` | [Wide-grip Pulldown](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/723.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `821` | [Pullup on fingerboard](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/821.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `980` | [commando pull-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/980.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1101` | [Horizontal traction isometry](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1101.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1125` | [Wide-grip supinated lat pulldown](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1125.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1127` | [Close-grip supinated lat pulldown](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1127.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1136` | [Neutral-grip chest pulldown](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1136.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1137` | [High-pulley pullover](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1137.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1138` | [Incline bench pulldown](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1138.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1216` | [Recruitment Pulls](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1216.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1273` | [Pullover](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1273.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1280` | [Biceps Close Grip Pull Down](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1280.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1282` | [Isometria trazioni impugnatura inversa](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1282.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1292` | [Reverse-grip pull-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1292.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1384` | [Pullover Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1384.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1435` | [Scapula Pulls](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1435.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1470` | [1-Arm Half-Kneeling Lat Pulldown](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1470.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1510` | [Neutral Grip Lat Pulldown](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1510.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1526` | [Ski Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1526.yaml) | `cardio_machine` | `compound` | `external` | `distance_time` |
| `1537` | [Pull-up Isometric Hold](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1537.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1545` | [Archer Pull Up](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1545.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1607` | [Typewriter Pull-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1607.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1635` | [Modified pulldown](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1635.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1659` | [Lat Pulldown - Cross Body Single Arm](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1659.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1695` | [Pull-Ups (Wide Grip)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1695.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1696` | [Pull-Ups (Neutral Grip)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1696.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1702` | [Jalón al pecho con agarre ancho](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1702.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1719` | [Jalon caballero unialteral](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1719.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1726` | [Straight-Arm Pulldown (Cable)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1726.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1727` | [Side Straight-Arm Pulldown (Cable)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1727.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1737` | [Assisted chin-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1737.yaml) | `machine` | `compound` | `assisted` | `bodyweight_reps` |
| `1738` | [Neutral-grip pull-ups or TRX rows](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1738.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1741` | [L-Sit Pull-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1741.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1755` | [Shoulder Y-pull cable](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1755.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1795` | [unilateral cross body cable pull down](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1795.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1927` | [Inverted Lat Pull Down](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1927.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1929` | [Assisted Pull-Up](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1929.yaml) | `resistance_band` | `compound` | `assisted` | `bodyweight_reps` |
| `1970` | [Kettlebell sumo high pull](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1970.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1971` | [Mentzer Pulldown](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1971.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1972` | [Single-Arm Lat Pulldown](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1972.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `2533` | [Arch Hang](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2533.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2540` | [Lat Pulldown Isometric](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2540.yaml) | `cable` | `compound` | `external` | `time_weight` |

### Familie `vertical_pull` + `biceps` (12 Übungen)
*Varianzen:* load_mode: ['assisted', 'bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `152` | [Chin Up](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/152.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `684` | [Underhand Lat Pull Down](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/684.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `980` | [commando pull-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/980.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1101` | [Horizontal traction isometry](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1101.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1127` | [Close-grip supinated lat pulldown](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1127.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1280` | [Biceps Close Grip Pull Down](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1280.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1282` | [Isometria trazioni impugnatura inversa](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1282.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1292` | [Reverse-grip pull-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1292.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1537` | [Pull-up Isometric Hold](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1537.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1737` | [Assisted chin-ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1737.yaml) | `machine` | `compound` | `assisted` | `bodyweight_reps` |
| `1927` | [Inverted Lat Pull Down](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1927.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1971` | [Mentzer Pulldown](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1971.yaml) | `cable` | `compound` | `external` | `weight_reps` |

### Familie `vertical_pull` + `chest` (3 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `161` | [Cross-Bench Dumbbell Pullovers](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/161.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `423` | [Muscle up](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/423.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1273` | [Pullover](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1273.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |

### Familie `vertical_pull` + `forearms` (5 Übungen)
*Varianzen:* mechanic: ['compound', 'isolation'], tracking_type: ['bodyweight_reps', 'time']

> [!WARNING]
> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `182` | [Deadhang](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/182.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `804` | [Sloper hanging](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/804.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `820` | [Fingerboard 20 mm edge](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/820.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `821` | [Pullup on fingerboard](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/821.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1216` | [Recruitment Pulls](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1216.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Familie `vertical_push` + `back` (2 Übungen)
*Varianzen:* tracking_type: ['bodyweight_reps', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `711` | [Wall Handstand](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/711.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `716` | [Wall Slides](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/716.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Familie `vertical_push` + `chest` (5 Übungen)
*Varianzen:* tracking_type: ['bodyweight_reps', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `194` | [Dips](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/194.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `501` | [Ring Dips](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/501.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `716` | [Wall Slides](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/716.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1832` | [Ring Support Hold](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1832.yaml) | `suspension_trainer` | `compound` | `bodyweight` | `time` |
| `1914` | [Isometria alle parallele](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1914.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Familie `vertical_push` + `shoulders` (35 Übungen)
*Varianzen:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'time_weight', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `20` | [Arnold Shoulder Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/20.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `193` | [Diagonal Shoulder Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/193.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `282` | [Handstand Pushup](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/282.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `346` | [Landmine press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/346.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `418` | [Military Press mit SZ-Bar](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/418.yaml) | `ez_bar` | `compound` | `external` | `weight_reps` |
| `454` | [Pike Push Ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/454.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `478` | [Push Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/478.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `543` | [Shoulder Press, on Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/543.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `566` | [Shoulder Press, Barbell](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/566.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `567` | [Shoulder Press, Dumbbells](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/567.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `569` | [Shoulder Press, on Multi Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/569.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `687` | [Overhead Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/687.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `711` | [Wall Handstand](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/711.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `916` | [Smith Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/916.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `1090` | [Vpushup](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1090.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1226` | [Dumbbell bicep curl to press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1226.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1360` | [Double Kettlebell Clean and Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1360.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1439` | [Pin OHP](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1439.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1440` | [Push OHP](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1440.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1441` | [Incline OHP DB](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1441.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1442` | [Kreis Press DB](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1442.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1445` | [Jerk OL](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1445.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1446` | [Clean and Jerk OL](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1446.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1504` | [Dumbbell Bradford press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1504.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1516` | [Handstand](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1516.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1575` | [Standing Dowel Shoulder press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1575.yaml) | `other` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1638` | [Barbell Clean and press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1638.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1684` | [Dumbbell Thruster](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1684.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1808` | [Parallel Bar Hold](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1808.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1893` | [Overhead Barbell Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1893.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1901` | [Clean and Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1901.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1967` | [lento avanti seduto](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1967.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1968` | [Single-arm dumbbell shoulder press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1968.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `2498` | [Pike Push-ups (Vasco L1)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2498.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2537` | [Overhead Press Isometric](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2537.yaml) | `cable` | `compound` | `external` | `time_weight` |

### Familie `vertical_push` + `triceps` (19 Übungen)
*Varianzen:* load_mode: ['assisted', 'bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'time_weight', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `194` | [Dips](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/194.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `197` | [Dips Between Two Benches](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/197.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `282` | [Handstand Pushup](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/282.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `418` | [Military Press mit SZ-Bar](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/418.yaml) | `ez_bar` | `compound` | `external` | `weight_reps` |
| `501` | [Ring Dips](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/501.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `566` | [Shoulder Press, Barbell](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/566.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1000` | [Floor dips](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1000.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1090` | [Vpushup](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1090.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1269` | [TRX dips](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1269.yaml) | `suspension_trainer` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1320` | [Bench Dips On Floor HD](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1320.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1372` | [Triceps Dips (Assisted)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1372.yaml) | `machine` | `compound` | `assisted` | `weight_reps` |
| `1439` | [Pin OHP](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1439.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1774` | [Chair dips](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1774.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1808` | [Parallel Bar Hold](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1808.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1832` | [Ring Support Hold](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1832.yaml) | `suspension_trainer` | `compound` | `bodyweight` | `time` |
| `1893` | [Overhead Barbell Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1893.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1914` | [Isometria alle parallele](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1914.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2498` | [Pike Push-ups (Vasco L1)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2498.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2537` | [Overhead Press Isometric](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2537.yaml) | `cable` | `compound` | `external` | `time_weight` |

### Familie `wrist_flexion` + `forearms` (7 Übungen)
*Varianzen:* load_mode: ['external', 'variable'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `51` | [Barbell Wrist Curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/51.yaml) | `barbell` | `isolation` | `external` | `weight_reps` |
| `279` | [Hand Grip](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/279.yaml) | `other` | `isolation` | `variable` | `bodyweight_reps` |
| `623` | [Standing Rope Forearm](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/623.yaml) | `other` | `isolation` | `external` | `weight_reps` |
| `1205` | [Wrist curl, dumbbells](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1205.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1333` | [Forearm Curls (underhand grip)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1333.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1771` | [Wrist curl, cable](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1771.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `2452` | [Curl De Muñeca Con Barra](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2452.yaml) | `barbell` | `isolation` | `external` | `weight_reps` |