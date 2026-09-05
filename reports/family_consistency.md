# Family Consistency Report: Divergences Within Same Patterns & Muscle Groups

## Purpose & Methodology
Exercises that share the same movement pattern (`movement_pattern`) and target the same primary muscle group form a functional family (e.g., `horizontal_push` + `chest` = bench press family).

This report identifies exercises where divergent values occur within the same family for:
- **`mechanic`** (`compound` vs. `isolation`)
- **`tracking_type`** (`weight_reps`, `bodyweight_reps`, `time`, etc.)
- **`load_mode`** (`external`, `bodyweight`, `assisted`, `variable`)

Some divergences are **structurally legitimate** (e.g. bodyweight pull-up vs. lat pulldown with external weight), while others are **true inconsistencies** (e.g. a squat variant erroneously declared as `isolation` or a curl as `compound`).

A total of **76 families** with value variances were identified:


### Family `anti_extension` + `abs` (32 exercises)
*Variances:* mechanic: ['compound', 'isolation'], tracking_type: ['bodyweight_reps', 'time']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `41` | [Barbell Ab Rollout](../data/exercises/41.yaml) | `barbell` | `compound` | `bodyweight` | `bodyweight_reps` |
| `178` | [Deadbug](../data/exercises/178.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `235` | [Flutter Kicks](../data/exercises/235.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `297` | [Hollow Hold](../data/exercises/297.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `312` | [Decline Swiss Ball Plank with Alternating Toe Tap](../data/exercises/312.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `376` | [Lying Leg Raise](../data/exercises/376.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `382` | [Hanging L-Sit Hold](../data/exercises/382.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `458` | [Plank](../data/exercises/458.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `545` | [Scissors](../data/exercises/545.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1001` | [High Plank](../data/exercises/1001.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1103` | [Walking Bridge](../data/exercises/1103.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1214` | [Tuck Front Lever](../data/exercises/1214.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1245` | [Front Lever](../data/exercises/1245.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1246` | [TRX Rollout](../data/exercises/1246.yaml) | `suspension_trainer` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1307` | [Plank](../data/exercises/1307.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1406` | [Plank-to-Elbow Extension (Plank to Push-Up)](../data/exercises/1406.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1409` | [Dragon-flag](../data/exercises/1409.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1410` | [Plank with Alternating Leg Lift](../data/exercises/1410.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1425` | [Toe Taps](../data/exercises/1425.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1489` | [Plank Jacks](../data/exercises/1489.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1573` | [Ab Wheel Rollout](../data/exercises/1573.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1704` | [Tuck L-sit](../data/exercises/1704.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1827` | [Double-Leg Abdominal Press](../data/exercises/1827.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1828` | [Abdominal Draw-In Maneuver (ADIM)](../data/exercises/1828.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1847` | [Straddle L-Sit](../data/exercises/1847.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1852` | [L-sit](../data/exercises/1852.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1853` | [L-Sit (Foot Supported)](../data/exercises/1853.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1909` | [Lying Leg Circles](../data/exercises/1909.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1911` | [Cat Plank](../data/exercises/1911.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2505` | [Dead Bug](../data/exercises/2505.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2507` | [Forearm Plank](../data/exercises/2507.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2510` | [Hollow Body Hold](../data/exercises/2510.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Family `anti_extension` + `back` (3 exercises)
*Variances:* mechanic: ['compound', 'isolation']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1010` | [Back Neck Stretch](../data/exercises/1010.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1214` | [Tuck Front Lever](../data/exercises/1214.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1245` | [Front Lever](../data/exercises/1245.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Family `anti_extension` + `triceps` (2 exercises)
*Variances:* tracking_type: ['bodyweight_reps', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1238` | [Frog Stand](../data/exercises/1238.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1406` | [Plank-to-Elbow Extension (Plank to Push-Up)](../data/exercises/1406.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Family `anti_lateral_flexion` + `abs` (12 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'time_weight', 'weight_reps']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `556` | [Roman Chair Side Bends](../data/exercises/556.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `576` | [Side Crunch](../data/exercises/576.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `577` | [Side Dumbbell Trunk Flexion](../data/exercises/577.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `580` | [Side Plank](../data/exercises/580.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1019` | [Side Plank Right](../data/exercises/1019.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1099` | [Dynamic Single-Leg Side Hold with Kettlebell](../data/exercises/1099.yaml) | `kettlebell` | `compound` | `external` | `time_weight` |
| `1188` | [Dumbbell Side Bend](../data/exercises/1188.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1288` | [Dynamic Side Plank](../data/exercises/1288.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1411` | [Heel Touches](../data/exercises/1411.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1426` | [Standing Side Crunches](../data/exercises/1426.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1650` | [Dumbbell Side Bend](../data/exercises/1650.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `2509` | [Side Plank](../data/exercises/2509.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Family `anti_lateral_flexion` + `lower_back` (11 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'time_weight', 'weight_reps']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `556` | [Roman Chair Side Bends](../data/exercises/556.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `576` | [Side Crunch](../data/exercises/576.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `577` | [Side Dumbbell Trunk Flexion](../data/exercises/577.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `580` | [Side Plank](../data/exercises/580.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1019` | [Side Plank Right](../data/exercises/1019.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1099` | [Dynamic Single-Leg Side Hold with Kettlebell](../data/exercises/1099.yaml) | `kettlebell` | `compound` | `external` | `time_weight` |
| `1188` | [Dumbbell Side Bend](../data/exercises/1188.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1288` | [Dynamic Side Plank](../data/exercises/1288.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1426` | [Standing Side Crunches](../data/exercises/1426.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1650` | [Dumbbell Side Bend](../data/exercises/1650.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `2509` | [Side Plank](../data/exercises/2509.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Family `anti_rotation` + `abs` (5 exercises)
*Variances:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `56` | [Abdominal Stabilization](../data/exercises/56.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1091` | [Plank Shoulder Taps](../data/exercises/1091.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1194` | [Cable Pallof Press](../data/exercises/1194.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1687` | [Bear Crawl Pull-Through](../data/exercises/1687.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1766` | [Plank Reach](../data/exercises/1766.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Family `anti_rotation` + `glutes` (4 exercises)
*Variances:* tracking_type: ['bodyweight_reps', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `957` | [Quadruped Arm and Leg Raise (Bird Dog)](../data/exercises/957.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1572` | [Bird Dog](../data/exercises/1572.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1910` | [Kneeling Superman (Bird Dog)](../data/exercises/1910.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2508` | [Bird Dog](../data/exercises/2508.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Family `anti_rotation` + `lower_back` (4 exercises)
*Variances:* tracking_type: ['bodyweight_reps', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `957` | [Quadruped Arm and Leg Raise (Bird Dog)](../data/exercises/957.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1572` | [Bird Dog](../data/exercises/1572.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1910` | [Kneeling Superman (Bird Dog)](../data/exercises/1910.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2508` | [Bird Dog](../data/exercises/2508.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Family `carry` + `forearms` (2 exercises)
*Variances:* mechanic: ['compound', 'isolation'], tracking_type: ['distance_time', 'time_weight']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1116` | [Dumbbell Farmer's Carry](../data/exercises/1116.yaml) | `dumbbell` | `compound` | `external` | `distance_time` |
| `1430` | [Plate Pinch Hold](../data/exercises/1430.yaml) | `weight_plate` | `isolation` | `external` | `time_weight` |

### Family `dorsiflexion` + `calves` (3 exercises)
*Variances:* load_mode: ['bodyweight', 'variable']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1200` | [Tibialis Raises](../data/exercises/1200.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1241` | [Resistance Band Ankle Dorsiflexion](../data/exercises/1241.yaml) | `resistance_band` | `isolation` | `variable` | `bodyweight_reps` |
| `1804` | [Ankle Dorsiflexion Rocks](../data/exercises/1804.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |

### Family `elbow_extension` + `triceps` (35 exercises)
*Variances:* load_mode: ['bodyweight', 'external', 'variable'], tracking_type: ['bodyweight_reps', 'time_weight', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `50` | [Barbell Triceps Extension](../data/exercises/50.yaml) | `barbell` | `isolation` | `external` | `weight_reps` |
| `112` | [Body-Ups](../data/exercises/112.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `211` | [Dumbbell Triceps Extension](../data/exercises/211.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `245` | [Dumbbell Skull Crusher](../data/exercises/245.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `246` | [Skullcrusher EZ-Bar](../data/exercises/246.yaml) | `ez_bar` | `isolation` | `external` | `weight_reps` |
| `549` | [Seated Triceps Press](../data/exercises/549.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `655` | [Dumbbell Triceps Kickback](../data/exercises/655.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `659` | [Cable Rope Triceps Extension](../data/exercises/659.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `660` | [Cable Straight-Bar Triceps Extension](../data/exercises/660.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `661` | [Machine Triceps Extension](../data/exercises/661.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `803` | [One-Arm Cable Triceps Extension](../data/exercises/803.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `805` | [Cable Rope Triceps Pushdown](../data/exercises/805.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `911` | [Incline Dumbbell Skull Crusher](../data/exercises/911.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1185` | [Triceps Pushdown](../data/exercises/1185.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1266` | [TRX Tricep Extension](../data/exercises/1266.yaml) | `suspension_trainer` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1298` | [High-Cable Triceps Extension](../data/exercises/1298.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1336` | [Overhead Dumbbell Triceps Extension](../data/exercises/1336.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1468` | [EZ-Bar Floor Skull Crusher](../data/exercises/1468.yaml) | `ez_bar` | `isolation` | `external` | `weight_reps` |
| `1480` | [Lying Barbell Triceps Extension](../data/exercises/1480.yaml) | `barbell` | `isolation` | `external` | `weight_reps` |
| `1481` | [Cable Drag Pushdown](../data/exercises/1481.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1485` | [Rocking Triceps Pushdown](../data/exercises/1485.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1490` | [Incline Dumbbell Triceps Kickback](../data/exercises/1490.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1509` | [Cable Tricep Kickback](../data/exercises/1509.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1513` | [Overhead Cable Tricep Extension](../data/exercises/1513.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1519` | [EZ-Bar Overhead Triceps Extension](../data/exercises/1519.yaml) | `ez_bar` | `isolation` | `external` | `weight_reps` |
| `1661` | [Cable Triceps Press](../data/exercises/1661.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1662` | [Cable Tri Extension - Internal Rotation](../data/exercises/1662.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1668` | [One Arm Overhead Cable Tricep Extension](../data/exercises/1668.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1703` | [Dumbbell Kickback](../data/exercises/1703.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1717` | [One-Arm Overhead Cable Triceps Extension](../data/exercises/1717.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1824` | [Dumbbell Tate Press](../data/exercises/1824.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1900` | [Cable Rope Triceps Pushdown](../data/exercises/1900.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1969` | [Single-Arm Cable Triceps Pushdown](../data/exercises/1969.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `2522` | [Band Triceps Pushdown](../data/exercises/2522.yaml) | `resistance_band` | `isolation` | `variable` | `weight_reps` |
| `2541` | [Single-Arm Isometric Triceps Pushdown](../data/exercises/2541.yaml) | `cable` | `isolation` | `external` | `time_weight` |

### Family `elbow_flexion` + `biceps` (51 exercises)
*Variances:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time_weight', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `91` | [Barbell Biceps Curl](../data/exercises/91.yaml) | `barbell` | `isolation` | `external` | `weight_reps` |
| `92` | [Dumbbell Biceps Curl](../data/exercises/92.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `94` | [EZ-Bar Biceps Curl](../data/exercises/94.yaml) | `ez_bar` | `isolation` | `external` | `weight_reps` |
| `95` | [Cable Biceps Curl](../data/exercises/95.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `202` | [Dumbbell Concentration Curl](../data/exercises/202.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `204` | [Dumbbell Incline Curl](../data/exercises/204.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `208` | [Dumbbells on Scott Machine](../data/exercises/208.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `272` | [Hammer Curls](../data/exercises/272.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `275` | [Hammercurls on Cable](../data/exercises/275.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `439` | [Overhand Cable Curl](../data/exercises/439.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `465` | [EZ-Bar Preacher Curl](../data/exercises/465.yaml) | `ez_bar` | `isolation` | `external` | `weight_reps` |
| `493` | [EZ-Bar Reverse Curl](../data/exercises/493.yaml) | `ez_bar` | `isolation` | `external` | `weight_reps` |
| `495` | [Reverse Curl](../data/exercises/495.yaml) | `barbell` | `isolation` | `external` | `weight_reps` |
| `584` | [Single-arm Preacher Curl](../data/exercises/584.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `621` | [Standing Bicep Curl](../data/exercises/621.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `912` | [Straight-Bar Cable Curl](../data/exercises/912.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `913` | [Reverse Preacher Curl (Close Grip)](../data/exercises/913.yaml) | `ez_bar` | `isolation` | `external` | `weight_reps` |
| `914` | [Reverse EZ-Bar Cable Curl](../data/exercises/914.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `958` | [TRX Biceps Curl](../data/exercises/958.yaml) | `suspension_trainer` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `974` | [Two-Handed Kettlebell Curl](../data/exercises/974.yaml) | `kettlebell` | `isolation` | `external` | `weight_reps` |
| `975` | [One-Handed Kettlebell Curl](../data/exercises/975.yaml) | `kettlebell` | `isolation` | `external` | `weight_reps` |
| `1012` | [Alternating Dumbbell Bicep Curls](../data/exercises/1012.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1109` | [Cable Concentration Curl](../data/exercises/1109.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1192` | [Alternating Dumbbell Biceps Curl](../data/exercises/1192.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1224` | [Dumbbell Drag Curl](../data/exercises/1224.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1225` | [Dumbbell Wide Biceps Curl](../data/exercises/1225.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1260` | [TRX Hammer Curl](../data/exercises/1260.yaml) | `suspension_trainer` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1261` | [TRX Gorilla Biceps Curl](../data/exercises/1261.yaml) | `suspension_trainer` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1262` | [TRX Single-Arm Biceps Curl](../data/exercises/1262.yaml) | `suspension_trainer` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1289` | [Seated Dumbbell Curls](../data/exercises/1289.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1290` | [Reverse Grip Barbell Curls](../data/exercises/1290.yaml) | `barbell` | `isolation` | `external` | `weight_reps` |
| `1424` | [Biceps Curl Machine](../data/exercises/1424.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1448` | [Seated W-Curl with Dumbbells](../data/exercises/1448.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1465` | [Dumbbell Spider Curl](../data/exercises/1465.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1482` | [Dumbbell Cheat Curl](../data/exercises/1482.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1483` | [Biceps Curl Trifecta](../data/exercises/1483.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1493` | [Cable Bayesian Curl](../data/exercises/1493.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1502` | [DB Cross Body Hammer Curls](../data/exercises/1502.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1511` | [Kong Curl](../data/exercises/1511.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1512` | [Drop Curl](../data/exercises/1512.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1530` | [Lying Dumbbell Curl](../data/exercises/1530.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1531` | [Cable Biceps Curl](../data/exercises/1531.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1567` | [Alternating Dumbbell Hammer Curl](../data/exercises/1567.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1608` | [Bodyweight Biceps Curl](../data/exercises/1608.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1657` | [Preacher Curl - Internally Rotated](../data/exercises/1657.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1658` | [Preacher Curl - Externally Rotated](../data/exercises/1658.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1666` | [Curl with Shoulder Elevated](../data/exercises/1666.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1683` | [Zottman curl](../data/exercises/1683.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1931` | [Dumbbell Spider Curl](../data/exercises/1931.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `2504` | [Dumbbell Hammer Curls](../data/exercises/2504.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `2539` | [Isometric Dumbbell Preacher Curl](../data/exercises/2539.yaml) | `dumbbell` | `isolation` | `external` | `time_weight` |

### Family `gait` + `abs` (5 exercises)
*Variances:* tracking_type: ['distance_time', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `57` | [Bear Walk](../data/exercises/57.yaml) | `bodyweight` | `compound` | `bodyweight` | `distance_time` |
| `983` | [High Knees](../data/exercises/983.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1196` | [Wall Drills (Sprint Mechanics)](../data/exercises/1196.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1318` | [High Knee Skips](../data/exercises/1318.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1965` | [Standing Knee Raise](../data/exercises/1965.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Family `gait` + `calves` (10 exercises)
*Variances:* tracking_type: ['distance_time', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `319` | [Jogging](../data/exercises/319.yaml) | `bodyweight` | `compound` | `bodyweight` | `distance_time` |
| `527` | [Run](../data/exercises/527.yaml) | `bodyweight` | `compound` | `bodyweight` | `distance_time` |
| `529` | [Run - Interval Training](../data/exercises/529.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `530` | [Treadmill Running](../data/exercises/530.yaml) | `cardio_machine` | `compound` | `bodyweight` | `distance_time` |
| `908` | [Zone 2 Running](../data/exercises/908.yaml) | `bodyweight` | `compound` | `bodyweight` | `distance_time` |
| `1104` | [Walking](../data/exercises/1104.yaml) | `bodyweight` | `compound` | `bodyweight` | `distance_time` |
| `1285` | [Butt Kicks](../data/exercises/1285.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1579` | [Bronco Test](../data/exercises/1579.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1584` | [March or Jog in Place](../data/exercises/1584.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1615` | [Treadmill Cardio](../data/exercises/1615.yaml) | `cardio_machine` | `compound` | `bodyweight` | `distance_time` |

### Family `gait` + `glutes` (6 exercises)
*Variances:* load_mode: ['bodyweight', 'external'], tracking_type: ['distance_time', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `177` | [Cycling](../data/exercises/177.yaml) | `other` | `compound` | `external` | `distance_time` |
| `962` | [Elliptical Trainer](../data/exercises/962.yaml) | `cardio_machine` | `compound` | `external` | `distance_time` |
| `1449` | [Stair Climber (ClimbMill)](../data/exercises/1449.yaml) | `cardio_machine` | `compound` | `bodyweight` | `time` |
| `1548` | [StairMaster (Stair Climber)](../data/exercises/1548.yaml) | `cardio_machine` | `compound` | `bodyweight` | `time` |
| `2481` | [Kickboard Flutter Kick](../data/exercises/2481.yaml) | `other` | `compound` | `bodyweight` | `distance_time` |
| `2484` | [Side-Kick Breathing with Kickboard](../data/exercises/2484.yaml) | `other` | `compound` | `bodyweight` | `distance_time` |

### Family `gait` + `quads` (24 exercises)
*Variances:* load_mode: ['bodyweight', 'external'], tracking_type: ['distance_time', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `57` | [Bear Walk](../data/exercises/57.yaml) | `bodyweight` | `compound` | `bodyweight` | `distance_time` |
| `177` | [Cycling](../data/exercises/177.yaml) | `other` | `compound` | `external` | `distance_time` |
| `319` | [Jogging](../data/exercises/319.yaml) | `bodyweight` | `compound` | `bodyweight` | `distance_time` |
| `527` | [Run](../data/exercises/527.yaml) | `bodyweight` | `compound` | `bodyweight` | `distance_time` |
| `529` | [Run - Interval Training](../data/exercises/529.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `530` | [Treadmill Running](../data/exercises/530.yaml) | `cardio_machine` | `compound` | `bodyweight` | `distance_time` |
| `624` | [Stationary Bike](../data/exercises/624.yaml) | `cardio_machine` | `compound` | `external` | `distance_time` |
| `908` | [Zone 2 Running](../data/exercises/908.yaml) | `bodyweight` | `compound` | `bodyweight` | `distance_time` |
| `962` | [Elliptical Trainer](../data/exercises/962.yaml) | `cardio_machine` | `compound` | `external` | `distance_time` |
| `983` | [High Knees](../data/exercises/983.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1104` | [Walking](../data/exercises/1104.yaml) | `bodyweight` | `compound` | `bodyweight` | `distance_time` |
| `1196` | [Wall Drills (Sprint Mechanics)](../data/exercises/1196.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1204` | [Stationary Bike Cardio Session](../data/exercises/1204.yaml) | `cardio_machine` | `compound` | `external` | `distance_time` |
| `1318` | [High Knee Skips](../data/exercises/1318.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1376` | [Barbell Calf Raise](../data/exercises/1376.yaml) | `cardio_machine` | `compound` | `external` | `distance_time` |
| `1449` | [Stair Climber (ClimbMill)](../data/exercises/1449.yaml) | `cardio_machine` | `compound` | `bodyweight` | `time` |
| `1548` | [StairMaster (Stair Climber)](../data/exercises/1548.yaml) | `cardio_machine` | `compound` | `bodyweight` | `time` |
| `1579` | [Bronco Test](../data/exercises/1579.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1584` | [March or Jog in Place](../data/exercises/1584.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1615` | [Treadmill Cardio](../data/exercises/1615.yaml) | `cardio_machine` | `compound` | `bodyweight` | `distance_time` |
| `1618` | [Stationary bike cardio](../data/exercises/1618.yaml) | `cardio_machine` | `compound` | `external` | `distance_time` |
| `1965` | [Standing Knee Raise](../data/exercises/1965.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2481` | [Kickboard Flutter Kick](../data/exercises/2481.yaml) | `other` | `compound` | `bodyweight` | `distance_time` |
| `2484` | [Side-Kick Breathing with Kickboard](../data/exercises/2484.yaml) | `other` | `compound` | `bodyweight` | `distance_time` |

### Family `hinge` + `adductors` (4 exercises)
*Variances:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1396` | [Standing Pancake](../data/exercises/1396.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1397` | [Standing Pancake Good Morning](../data/exercises/1397.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1612` | [Kettlebell Sumo Deadlift](../data/exercises/1612.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1845` | [Seated Pancake Good Morning](../data/exercises/1845.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Family `hinge` + `glutes` (30 exercises)
*Variances:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `9` | [Two-Arm Kettlebell Swing](../data/exercises/9.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `184` | [Conventional Deadlift](../data/exercises/184.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `189` | [Deficit Deadlift](../data/exercises/189.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `331` | [Kettlebell Swings](../data/exercises/331.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `484` | [Rack Deadlift](../data/exercises/484.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `507` | [Romanian Deadlift](../data/exercises/507.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `604` | [Speed Deadlift](../data/exercises/604.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `627` | [Stiff-legged Deadlifts](../data/exercises/627.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `630` | [Sumo Deadlift](../data/exercises/630.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `683` | [Power Clean](../data/exercises/683.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `960` | [Kettlebell Swing](../data/exercises/960.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1003` | [Kettlebell Deadlift](../data/exercises/1003.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1087` | [Dumbbell Hang Power Cleans](../data/exercises/1087.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1088` | [Dumbbell Sumo Deadlift](../data/exercises/1088.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1141` | [Arabesque](../data/exercises/1141.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1370` | [Dumbbell Deadlift](../data/exercises/1370.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1388` | [Single Leg RDL](../data/exercises/1388.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1392` | [Bodyweight Good Morning](../data/exercises/1392.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1438` | [Barbell Clean](../data/exercises/1438.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1576` | [Snap Down](../data/exercises/1576.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1578` | [Hip Hinge](../data/exercises/1578.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1612` | [Kettlebell Sumo Deadlift](../data/exercises/1612.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1641` | [Kettlebell One Legged Deadlift](../data/exercises/1641.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1652` | [Dumbbell Romanian Deadlift](../data/exercises/1652.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1688` | [Kickstand RDL](../data/exercises/1688.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1700` | [Barbell Romanian Deadlift (RDL)](../data/exercises/1700.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1736` | [Single-Leg Deadlift with Dumbbell](../data/exercises/1736.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1947` | [Dumbbell Snatch](../data/exercises/1947.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `2447` | [Hip Airplane](../data/exercises/2447.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2524` | [Staggered-Stance Good Morning](../data/exercises/2524.yaml) | `barbell` | `compound` | `external` | `weight_reps` |

### Family `hinge` + `hamstrings` (30 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `9` | [Two-Arm Kettlebell Swing](../data/exercises/9.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `184` | [Conventional Deadlift](../data/exercises/184.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `331` | [Kettlebell Swings](../data/exercises/331.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `507` | [Romanian Deadlift](../data/exercises/507.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `604` | [Speed Deadlift](../data/exercises/604.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `627` | [Stiff-legged Deadlifts](../data/exercises/627.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `630` | [Sumo Deadlift](../data/exercises/630.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `683` | [Power Clean](../data/exercises/683.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `960` | [Kettlebell Swing](../data/exercises/960.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1003` | [Kettlebell Deadlift](../data/exercises/1003.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1087` | [Dumbbell Hang Power Cleans](../data/exercises/1087.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1088` | [Dumbbell Sumo Deadlift](../data/exercises/1088.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1141` | [Arabesque](../data/exercises/1141.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1370` | [Dumbbell Deadlift](../data/exercises/1370.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1388` | [Single Leg RDL](../data/exercises/1388.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1390` | [Toe Touch](../data/exercises/1390.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1392` | [Bodyweight Good Morning](../data/exercises/1392.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1393` | [Single Leg Hamstring Stretch](../data/exercises/1393.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1396` | [Standing Pancake](../data/exercises/1396.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1397` | [Standing Pancake Good Morning](../data/exercises/1397.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1400` | [Crossbody Hamstring Stretch](../data/exercises/1400.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1578` | [Hip Hinge](../data/exercises/1578.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1641` | [Kettlebell One Legged Deadlift](../data/exercises/1641.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1652` | [Dumbbell Romanian Deadlift](../data/exercises/1652.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1688` | [Kickstand RDL](../data/exercises/1688.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1700` | [Barbell Romanian Deadlift (RDL)](../data/exercises/1700.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1736` | [Single-Leg Deadlift with Dumbbell](../data/exercises/1736.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1845` | [Seated Pancake Good Morning](../data/exercises/1845.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1947` | [Dumbbell Snatch](../data/exercises/1947.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `2524` | [Staggered-Stance Good Morning](../data/exercises/2524.yaml) | `barbell` | `compound` | `external` | `weight_reps` |

### Family `hinge` + `quads` (3 exercises)
*Variances:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `630` | [Sumo Deadlift](../data/exercises/630.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1438` | [Barbell Clean](../data/exercises/1438.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1576` | [Snap Down](../data/exercises/1576.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Family `hip_abduction` + `adductors` (2 exercises)
*Variances:* tracking_type: ['bodyweight_reps', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1395` | [Crossbody Leg Swings](../data/exercises/1395.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1844` | [Frog Stretch](../data/exercises/1844.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |

### Family `hip_abduction` + `glutes` (11 exercises)
*Variances:* load_mode: ['bodyweight', 'external', 'variable'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1096` | [Standing Hip Abduction](../data/exercises/1096.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1202` | [Side-Lying Hip Abduction](../data/exercises/1202.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1395` | [Crossbody Leg Swings](../data/exercises/1395.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1514` | [Lateral Walk](../data/exercises/1514.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1672` | [Seated Hip Abduction](../data/exercises/1672.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1748` | [Seated Machine Hip Abduction](../data/exercises/1748.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1823` | [Clamshell](../data/exercises/1823.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1842` | [Banded Clamshell](../data/exercises/1842.yaml) | `resistance_band` | `isolation` | `variable` | `bodyweight_reps` |
| `1886` | [Supine Hip Abduction](../data/exercises/1886.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1915` | [Quadruped Hip Abduction (Fire Hydrant)](../data/exercises/1915.yaml) | `resistance_band` | `isolation` | `variable` | `bodyweight_reps` |
| `2491` | [Seated Hip Abduction Machine](../data/exercises/2491.yaml) | `machine` | `isolation` | `external` | `weight_reps` |

### Family `hip_adduction` + `adductors` (5 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['time', 'weight_reps']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `12` | [Seated Hip Adduction](../data/exercises/12.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1605` | [Copenhagen Adduction Exercise](../data/exercises/1605.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1724` | [Standing Adduction (Cable)](../data/exercises/1724.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `2492` | [Seated Hip Adduction Machine](../data/exercises/2492.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `2493` | [Adductor Side Plank (Copenhagen Plank)](../data/exercises/2493.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Family `hip_extension` + `glutes` (19 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external', 'variable'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `265` | [Glute Bridge](../data/exercises/265.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `292` | [Lying Hip Raise](../data/exercises/292.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `294` | [Hip Thrust](../data/exercises/294.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `990` | [Kneeling Glute Kickback](../data/exercises/990.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1131` | [Cable Glute Extension](../data/exercises/1131.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1132` | [GHD Glute Extension](../data/exercises/1132.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1234` | [Dumbbell Single-Leg Hip Thrust](../data/exercises/1234.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1503` | [Dumbbell Frog Press](../data/exercises/1503.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1528` | [Glute Drive](../data/exercises/1528.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1613` | [Rubber Band Glute Kickback](../data/exercises/1613.yaml) | `resistance_band` | `isolation` | `variable` | `bodyweight_reps` |
| `1616` | [Dumbbell donkey kick](../data/exercises/1616.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1642` | [Dumbbell Hip Thrust](../data/exercises/1642.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1723` | [Glute Kickback (Machine)](../data/exercises/1723.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1740` | [Single-Leg Glute Bridge](../data/exercises/1740.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1751` | [Cable Pull-Through](../data/exercises/1751.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1809` | [Reverse Hyperextension](../data/exercises/1809.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1906` | [Glute Bridge with Alternating Leg Extension](../data/exercises/1906.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1913` | [Single-Leg Glute Bridge (Unilateral Hip Thrust)](../data/exercises/1913.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2534` | [Glute Bridge](../data/exercises/2534.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Family `hip_extension` + `hamstrings` (3 exercises)
*Variances:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1132` | [GHD Glute Extension](../data/exercises/1132.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1751` | [Cable Pull-Through](../data/exercises/1751.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1809` | [Reverse Hyperextension](../data/exercises/1809.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Family `horizontal_pull` + `abs` (4 exercises)
*Variances:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `490` | [Renegade Row](../data/exercises/490.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1022` | [Single-Arm Plank to Row (Renegade Row)](../data/exercises/1022.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1248` | [Ice Cream Maker](../data/exercises/1248.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1252` | [Front Lever Pull-up](../data/exercises/1252.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Family `horizontal_pull` + `back` (67 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external', 'variable'], tracking_type: ['bodyweight_reps', 'distance_time', 'weight_reps']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `79` | [Bent High Pulls](../data/exercises/79.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `81` | [One-Arm Dumbbell Row](../data/exercises/81.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `83` | [Barbell Bent-Over Row](../data/exercises/83.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `84` | [Reverse-Grip Barbell Bent-Over Row](../data/exercises/84.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `222` | [Facepull](../data/exercises/222.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `310` | [Incline Dumbbell Row](../data/exercises/310.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `380` | [Leverage Machine Iso Row](../data/exercises/380.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `394` | [Seated Cable Row (Wide Grip)](../data/exercises/394.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `395` | [Seated Cable Row (Narrow Grip)](../data/exercises/395.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `448` | [Pendlay Row](../data/exercises/448.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `468` | [Prone Scapular Retraction - Arms at Side](../data/exercises/468.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `490` | [Renegade Row](../data/exercises/490.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `508` | [Row](../data/exercises/508.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `510` | [Chest-Supported Barbell Row on Bench](../data/exercises/510.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `513` | [T-Bar Row (Wide Grip)](../data/exercises/513.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `562` | [Shotgun Row](../data/exercises/562.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `674` | [TRX Row](../data/exercises/674.yaml) | `suspension_trainer` | `compound` | `bodyweight` | `bodyweight_reps` |
| `919` | [T-Bar Row](../data/exercises/919.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `922` | [Seated Cable Mid Trap Shrug](../data/exercises/922.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `923` | [Lying Dumbbell Row and Seated Shrug](../data/exercises/923.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `959` | [TRX Row](../data/exercises/959.yaml) | `suspension_trainer` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1022` | [Single-Arm Plank to Row (Renegade Row)](../data/exercises/1022.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1083` | [Prone Y-W-T Raises](../data/exercises/1083.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1093` | [Indoor Rowing Machine](../data/exercises/1093.yaml) | `cardio_machine` | `compound` | `external` | `distance_time` |
| `1117` | [Seated Cable Row](../data/exercises/1117.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1119` | [Seated Machine Row (Close Grip)](../data/exercises/1119.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1120` | [Seated Machine Row (Underhand Grip)](../data/exercises/1120.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1186` | [One-Arm Cable Bent-Over Row](../data/exercises/1186.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1198` | [Inverted Row](../data/exercises/1198.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1215` | [Reverse Snow Angel](../data/exercises/1215.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1219` | [Australian Pull-up](../data/exercises/1219.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1248` | [Ice Cream Maker](../data/exercises/1248.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1252` | [Front Lever Pull-up](../data/exercises/1252.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1283` | [Incline Chest-Supported Dumbbell Row](../data/exercises/1283.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1303` | [Helms Row](../data/exercises/1303.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1304` | [Meadows Row](../data/exercises/1304.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1380` | [Band Pull-Aparts](../data/exercises/1380.yaml) | `resistance_band` | `compound` | `variable` | `bodyweight_reps` |
| `1381` | [Machine Upper Back Row](../data/exercises/1381.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1434` | [Dumbbell Bent-Over Lat Pull](../data/exercises/1434.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1458` | [Cross-Body Cable Y-Raise](../data/exercises/1458.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1463` | [Dumbbell Underhand Dead Row](../data/exercises/1463.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1471` | [Kroc Row](../data/exercises/1471.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1486` | [Alternating High Cable Row](../data/exercises/1486.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1492` | [Half-Kneeling Cable High Row](../data/exercises/1492.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1501` | [Alternating Dumbbell Gorilla Row](../data/exercises/1501.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1580` | [Perpendicular Unilateral Landmine Row](../data/exercises/1580.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1621` | [Unilateral Cable Row](../data/exercises/1621.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1634` | [Cable Rope Pullover Row](../data/exercises/1634.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1637` | [Single arm row](../data/exercises/1637.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1639` | [Dumbbell Bent Over Face Pull](../data/exercises/1639.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1698` | [Barbell Row (Overhand)](../data/exercises/1698.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1699` | [Barbell Row (Underhand)](../data/exercises/1699.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1701` | [One-Arm Heavy Row](../data/exercises/1701.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1718` | [Single-Arm High Cable Row](../data/exercises/1718.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1725` | [Seated Row (Machine)](../data/exercises/1725.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1732` | [Resistance Band Face Pull](../data/exercises/1732.yaml) | `resistance_band` | `compound` | `variable` | `bodyweight_reps` |
| `1834` | [Trap-3 Raise](../data/exercises/1834.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1877` | [Banded Scapular Retraction](../data/exercises/1877.yaml) | `resistance_band` | `isolation` | `variable` | `bodyweight_reps` |
| `1885` | [YTWL Exercise](../data/exercises/1885.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1905` | [Cable Pullback with Back Extension](../data/exercises/1905.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1928` | [Seated Cable Row with V-Grip](../data/exercises/1928.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `2454` | [YTW Raises](../data/exercises/2454.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2489` | [Seated Machine Low Row](../data/exercises/2489.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `2490` | [Low Pulley Cable Row (Triangle Grip)](../data/exercises/2490.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `2501` | [Inverted Table Row](../data/exercises/2501.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2502` | [Single-Arm Dumbbell Row](../data/exercises/2502.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `2503` | [Doorframe Bodyweight Face Pull](../data/exercises/2503.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Family `horizontal_pull` + `biceps` (4 exercises)
*Variances:* tracking_type: ['time_weight', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `84` | [Reverse-Grip Barbell Bent-Over Row](../data/exercises/84.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `284` | [Hercules Pillars](../data/exercises/284.yaml) | `cable` | `compound` | `external` | `time_weight` |
| `1120` | [Seated Machine Row (Underhand Grip)](../data/exercises/1120.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1699` | [Barbell Row (Underhand)](../data/exercises/1699.yaml) | `barbell` | `compound` | `external` | `weight_reps` |

### Family `horizontal_pull` + `shoulders` (20 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external', 'variable'], tracking_type: ['bodyweight_reps', 'time_weight', 'weight_reps']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `79` | [Bent High Pulls](../data/exercises/79.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `82` | [Bent-Over Lateral Raise](../data/exercises/82.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `139` | [Reverse Pec Deck (Rear Delt Fly)](../data/exercises/139.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `222` | [Facepull](../data/exercises/222.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `284` | [Hercules Pillars](../data/exercises/284.yaml) | `cable` | `compound` | `external` | `time_weight` |
| `487` | [Seated Dumbbell Rear Delt Raise](../data/exercises/487.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `822` | [Cable Rear Delt Fly](../data/exercises/822.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `828` | [Incline Bench Reverse Fly](../data/exercises/828.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1098` | [Seated Rear Delt Raise](../data/exercises/1098.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1227` | [Dumbbell Rear Delt Row](../data/exercises/1227.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1380` | [Band Pull-Aparts](../data/exercises/1380.yaml) | `resistance_band` | `compound` | `variable` | `bodyweight_reps` |
| `1458` | [Cross-Body Cable Y-Raise](../data/exercises/1458.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1473` | [Reverse Cable Flye](../data/exercises/1473.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1639` | [Dumbbell Bent Over Face Pull](../data/exercises/1639.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1709` | [Reverse Fly Standing](../data/exercises/1709.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1732` | [Resistance Band Face Pull](../data/exercises/1732.yaml) | `resistance_band` | `compound` | `variable` | `bodyweight_reps` |
| `1775` | [Pec Deck Rear Delt Fly](../data/exercises/1775.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1825` | [Chest-Supported Rear Delt Raise](../data/exercises/1825.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1936` | [One-Arm Cable Rear Delt Fly](../data/exercises/1936.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `2503` | [Doorframe Bodyweight Face Pull](../data/exercises/2503.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Family `horizontal_push` + `chest` (87 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'time_weight', 'weight_reps']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `73` | [Bench Press](../data/exercises/73.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `75` | [Dumbbell Bench Press](../data/exercises/75.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `129` | [Chest Press](../data/exercises/129.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `135` | [Pec Deck Fly (Butterfly)](../data/exercises/135.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `137` | [Butterfly Narrow Grip](../data/exercises/137.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `185` | [Decline Bench Press Barbell](../data/exercises/185.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `186` | [Decline Bench Press Dumbbell](../data/exercises/186.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `237` | [Fly With Cable](../data/exercises/237.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `238` | [Fly With Dumbbells](../data/exercises/238.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `239` | [Decline Dumbbell Fly](../data/exercises/239.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `308` | [Incline Dumbbell Fly](../data/exercises/308.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `314` | [Isometric Wipers](../data/exercises/314.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `323` | [Cable Cross-over](../data/exercises/323.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `379` | [Leverage Machine Chest Press](../data/exercises/379.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `386` | [Diamond Push-Up](../data/exercises/386.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `445` | [Pause Bench](../data/exercises/445.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `498` | [Reverse Grip Bench Press](../data/exercises/498.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `537` | [Incline Bench Press - Dumbbell](../data/exercises/537.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `538` | [Incline Bench Press - Barbell](../data/exercises/538.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `539` | [Smith Machine Incline Bench Press](../data/exercises/539.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `583` | [Side to Side Push Ups](../data/exercises/583.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `598` | [Smith Machine Close-grip Bench Press](../data/exercises/598.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `713` | [Wall Pushup](../data/exercises/713.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `801` | [Dumbbell Push-Up](../data/exercises/801.yaml) | `dumbbell` | `compound` | `bodyweight` | `bodyweight_reps` |
| `925` | [Smith Machine Slight Incline Press](../data/exercises/925.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `926` | [Machine Chest Fly](../data/exercises/926.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `927` | [Suspension Chest Fly](../data/exercises/927.yaml) | `suspension_trainer` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `985` | [Push-up with Rotation](../data/exercises/985.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1080` | [Hindu Push-Ups](../data/exercises/1080.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1084` | [Dumbbell Floor Press](../data/exercises/1084.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1086` | [Close-Grip Push-Ups](../data/exercises/1086.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1092` | [Heavy Bag Training (Boxing)](../data/exercises/1092.yaml) | `other` | `compound` | `bodyweight` | `time` |
| `1094` | [Seated Chest Press Machine](../data/exercises/1094.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1111` | [Incline Push-Ups](../data/exercises/1111.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1112` | [Decline Push-Ups](../data/exercises/1112.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1113` | [Parallette Push-Ups](../data/exercises/1113.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1209` | [Three-Point Push-Up](../data/exercises/1209.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1217` | [Finger Push-Up](../data/exercises/1217.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1218` | [Knee Push-Up](../data/exercises/1218.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1228` | [Dumbbell Close-Grip Bench Press](../data/exercises/1228.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1270` | [Low Pulley Cable Fly](../data/exercises/1270.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1284` | [Pseudo Planche Push-up](../data/exercises/1284.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1293` | [One-Arm Push-Up](../data/exercises/1293.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1296` | [Low-Cable Crossover](../data/exercises/1296.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1353` | [Dumbbell Hex Press](../data/exercises/1353.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1436` | [Barbell Pin Bench Press](../data/exercises/1436.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1457` | [Cable Press Around](../data/exercises/1457.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1461` | [No Leg Drive Dumbbell Chest Press](../data/exercises/1461.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1467` | [Incline Close-Grip Barbell Bench Press](../data/exercises/1467.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1469` | [Bent-Over Cable Flye](../data/exercises/1469.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1484` | [Omni Cable Crossover](../data/exercises/1484.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1496` | [Supinated Dumbbell Upper Chest Raise](../data/exercises/1496.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1497` | [DB Underhand bench press](../data/exercises/1497.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1498` | [Elbows Tucked DB Bench Press](../data/exercises/1498.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1508` | [High-Incline Smith Machine Press](../data/exercises/1508.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `1546` | [Larsen Press](../data/exercises/1546.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1551` | [Push-Up](../data/exercises/1551.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1554` | [Clap Push-Up](../data/exercises/1554.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1581` | [Dumbbell Scapular Press (Trap Press)](../data/exercises/1581.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1583` | [Close-Grip Barbell Bench Press (Supine Press)](../data/exercises/1583.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1656` | [Cable Chest Press - Decline](../data/exercises/1656.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1660` | [Cable Chest Press - Incline](../data/exercises/1660.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1686` | [Glute Bridge Single-Arm Press](../data/exercises/1686.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1689` | [Cable Fly Middle Chest](../data/exercises/1689.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1690` | [Cable Fly Upper Chest](../data/exercises/1690.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1691` | [Cable Fly Lower Chest](../data/exercises/1691.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1693` | [Incline Dumbbell Static Hold](../data/exercises/1693.yaml) | `dumbbell` | `compound` | `external` | `time_weight` |
| `1694` | [Flat Machine Press](../data/exercises/1694.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1716` | [Incline Scapular Push-Up](../data/exercises/1716.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1773` | [Legend Incline Bench Press](../data/exercises/1773.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1777` | [Deficit Push-Ups](../data/exercises/1777.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1778` | [Barbell Incline Bench Press](../data/exercises/1778.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1831` | [Hammerstrength Decline Chest Press](../data/exercises/1831.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1902` | [Weighted push-ups](../data/exercises/1902.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1904` | [Pec Deck](../data/exercises/1904.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1916` | [Tuck Planche](../data/exercises/1916.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1918` | [Legend Plate-Loaded Chest Press](../data/exercises/1918.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1922` | [Seated Cable Chest Fly](../data/exercises/1922.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1964` | [Wide Push-Up](../data/exercises/1964.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2496` | [Wall Push-Ups](../data/exercises/2496.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2497` | [Single-Arm Dumbbell Floor Press](../data/exercises/2497.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `2499` | [Incline Push-Ups](../data/exercises/2499.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2529` | [Explosive Push-Ups](../data/exercises/2529.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2530` | [Russian Push-Ups](../data/exercises/2530.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2532` | [Planche Lean Hold](../data/exercises/2532.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2536` | [Isometric Bench Press](../data/exercises/2536.yaml) | `barbell` | `compound` | `external` | `time_weight` |
| `2542` | [Boxing Training](../data/exercises/2542.yaml) | `other` | `compound` | `bodyweight` | `time` |

### Family `horizontal_push` + `glutes` (2 exercises)
*Variances:* tracking_type: ['distance_time', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1523` | [Sled Push](../data/exercises/1523.yaml) | `sled` | `compound` | `external` | `distance_time` |
| `1686` | [Glute Bridge Single-Arm Press](../data/exercises/1686.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |

### Family `horizontal_push` + `shoulders` (7 exercises)
*Variances:* tracking_type: ['bodyweight_reps', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1080` | [Hindu Push-Ups](../data/exercises/1080.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1092` | [Heavy Bag Training (Boxing)](../data/exercises/1092.yaml) | `other` | `compound` | `bodyweight` | `time` |
| `1284` | [Pseudo Planche Push-up](../data/exercises/1284.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1462` | [Punches](../data/exercises/1462.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1916` | [Tuck Planche](../data/exercises/1916.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2532` | [Planche Lean Hold](../data/exercises/2532.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2542` | [Boxing Training](../data/exercises/2542.yaml) | `other` | `compound` | `bodyweight` | `time` |

### Family `horizontal_push` + `triceps` (13 exercises)
*Variances:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `76` | [Bench Press Narrow Grip](../data/exercises/76.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `386` | [Diamond Push-Up](../data/exercises/386.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `498` | [Reverse Grip Bench Press](../data/exercises/498.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `598` | [Smith Machine Close-grip Bench Press](../data/exercises/598.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `1086` | [Close-Grip Push-Ups](../data/exercises/1086.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1092` | [Heavy Bag Training (Boxing)](../data/exercises/1092.yaml) | `other` | `compound` | `bodyweight` | `time` |
| `1228` | [Dumbbell Close-Grip Bench Press](../data/exercises/1228.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1293` | [One-Arm Push-Up](../data/exercises/1293.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1302` | [JM Press](../data/exercises/1302.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1467` | [Incline Close-Grip Barbell Bench Press](../data/exercises/1467.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1498` | [Elbows Tucked DB Bench Press](../data/exercises/1498.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1583` | [Close-Grip Barbell Bench Press (Supine Press)](../data/exercises/1583.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `2542` | [Boxing Training](../data/exercises/2542.yaml) | `other` | `compound` | `bodyweight` | `time` |

### Family `knee_extension` + `quads` (5 exercises)
*Variances:* load_mode: ['bodyweight', 'external', 'variable'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `71` | [Single Leg Extension](../data/exercises/71.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `369` | [Leg Extension](../data/exercises/369.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `909` | [Reverse Nordic Curl](../data/exercises/909.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `2494` | [Band Terminal Knee Extension (TKE)](../data/exercises/2494.yaml) | `resistance_band` | `isolation` | `variable` | `bodyweight_reps` |
| `2535` | [Isometric Leg Extension](../data/exercises/2535.yaml) | `machine` | `isolation` | `external` | `time` |

### Family `knee_flexion` + `hamstrings` (11 exercises)
*Variances:* load_mode: ['bodyweight', 'external', 'variable'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `364` | [Leg Curl](../data/exercises/364.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `365` | [Leg Curls (laying)](../data/exercises/365.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `366` | [Leg Curls (sitting)](../data/exercises/366.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `367` | [Leg Curls (standing)](../data/exercises/367.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `910` | [Nordic Curl](../data/exercises/910.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1294` | [Single-Leg Hamstring Curl](../data/exercises/1294.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1391` | [Elephant Walks](../data/exercises/1391.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1603` | [Leg curl with elastic](../data/exercises/1603.yaml) | `resistance_band` | `isolation` | `variable` | `bodyweight_reps` |
| `1833` | [Floor Glider Hamstring Curls](../data/exercises/1833.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `2478` | [Glute-Ham Raise (GHR)](../data/exercises/2478.yaml) | `machine` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `2495` | [Seated Leg Curl Machine](../data/exercises/2495.yaml) | `machine` | `isolation` | `external` | `weight_reps` |

### Family `lunge` + `glutes` (26 exercises)
*Variances:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `46` | [Standing Barbell Lunge](../data/exercises/46.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `205` | [Dumbbell Lunges Standing](../data/exercises/205.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `206` | [Dumbbell Lunges Walking](../data/exercises/206.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `722` | [Weighted Step-Ups](../data/exercises/722.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `802` | [Walking Barbell Lunge](../data/exercises/802.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `981` | [Step-Up](../data/exercises/981.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `984` | [Bodyweight Lunge](../data/exercises/984.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `986` | [Side Lunge (Left)](../data/exercises/986.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `987` | [Side Lunge (Right)](../data/exercises/987.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `988` | [Bulgarian Split Squat (Left)](../data/exercises/988.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `989` | [Bulgarian Split Squat (Right)](../data/exercises/989.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `991` | [Split Squat (Left)](../data/exercises/991.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `992` | [Split Squat (Right)](../data/exercises/992.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `999` | [Reverse Lunge](../data/exercises/999.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1102` | [Alternating Reverse Lunges](../data/exercises/1102.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1115` | [3D Lunge Warmup](../data/exercises/1115.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1324` | [Bodyweight Lunge](../data/exercises/1324.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1366` | [Dumbbell Split Squat](../data/exercises/1366.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1593` | [Smith Machine Split Squat](../data/exercises/1593.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `1604` | [Sliding Lateral Lunge](../data/exercises/1604.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1651` | [Dumbbell Rear Lunge](../data/exercises/1651.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1706` | [Bulgarian Split Squat with Dumbbells](../data/exercises/1706.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1734` | [Single-Leg Lunge with Kettlebell](../data/exercises/1734.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1830` | [Barbell Reverse Lunge](../data/exercises/1830.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1907` | [Unilateral Lunges (Split Squats)](../data/exercises/1907.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2526` | [Long Lunge Pulse Stretch](../data/exercises/2526.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Family `lunge` + `quads` (25 exercises)
*Variances:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `46` | [Standing Barbell Lunge](../data/exercises/46.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `205` | [Dumbbell Lunges Standing](../data/exercises/205.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `206` | [Dumbbell Lunges Walking](../data/exercises/206.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `722` | [Weighted Step-Ups](../data/exercises/722.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `802` | [Walking Barbell Lunge](../data/exercises/802.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `981` | [Step-Up](../data/exercises/981.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `984` | [Bodyweight Lunge](../data/exercises/984.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `986` | [Side Lunge (Left)](../data/exercises/986.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `987` | [Side Lunge (Right)](../data/exercises/987.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `988` | [Bulgarian Split Squat (Left)](../data/exercises/988.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `989` | [Bulgarian Split Squat (Right)](../data/exercises/989.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `991` | [Split Squat (Left)](../data/exercises/991.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `992` | [Split Squat (Right)](../data/exercises/992.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `999` | [Reverse Lunge](../data/exercises/999.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1102` | [Alternating Reverse Lunges](../data/exercises/1102.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1115` | [3D Lunge Warmup](../data/exercises/1115.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1324` | [Bodyweight Lunge](../data/exercises/1324.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1366` | [Dumbbell Split Squat](../data/exercises/1366.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1593` | [Smith Machine Split Squat](../data/exercises/1593.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `1604` | [Sliding Lateral Lunge](../data/exercises/1604.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1651` | [Dumbbell Rear Lunge](../data/exercises/1651.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1706` | [Bulgarian Split Squat with Dumbbells](../data/exercises/1706.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1734` | [Single-Leg Lunge with Kettlebell](../data/exercises/1734.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1830` | [Barbell Reverse Lunge](../data/exercises/1830.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1907` | [Unilateral Lunges (Split Squats)](../data/exercises/1907.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Family `other` + `abs` (20 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `675` | [Turkish Get-Up](../data/exercises/675.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `996` | [Mountain Climbers](../data/exercises/996.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `997` | [4-Count Burpees](../data/exercises/997.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1244` | [Yoga exercise: Cow-cat](../data/exercises/1244.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1524` | [Battle Ropes](../data/exercises/1524.yaml) | `other` | `compound` | `bodyweight` | `time` |
| `1525` | [Medicine Ball Slams](../data/exercises/1525.yaml) | `medicine_ball` | `compound` | `external` | `weight_reps` |
| `1591` | [Deep breathing (standing or seated)](../data/exercises/1591.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1670` | [Leg Swings (Front–Back)](../data/exercises/1670.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1839` | [Solo Hip Flexor Stretch](../data/exercises/1839.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1861` | [Side stretch](../data/exercises/1861.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1867` | [Hip Flexor Stretch](../data/exercises/1867.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1874` | [Runners Lunge Stretch](../data/exercises/1874.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1938` | [Cat-Cow Stretch](../data/exercises/1938.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1940` | [Diaphragmatic Breathing (Belly Breathing)](../data/exercises/1940.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1949` | [Limber 11 Mobility Routine](../data/exercises/1949.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1960` | [Rear-Foot-Elevated Hip Flexor Stretch](../data/exercises/1960.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `2482` | [Bobbing Exhale Drill](../data/exercises/2482.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2486` | [Deep-Water Recovery Bobbing](../data/exercises/2486.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2525` | [Couch Stretch](../data/exercises/2525.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `2527` | [Front Split Stretch](../data/exercises/2527.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Family `other` + `adductors` (4 exercises)
*Variances:* mechanic: ['compound', 'isolation'], tracking_type: ['bodyweight_reps', 'time']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1843` | [Butterfly Stretch](../data/exercises/1843.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1860` | [Foam Roller Adductors](../data/exercises/1860.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1949` | [Limber 11 Mobility Routine](../data/exercises/1949.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1954` | [Roll-Overs into V-Sits](../data/exercises/1954.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Family `other` + `back` (6 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['time', 'weight_reps']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1027` | [Elevated Prayer Stretch](../data/exercises/1027.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1525` | [Medicine Ball Slams](../data/exercises/1525.yaml) | `medicine_ball` | `compound` | `external` | `weight_reps` |
| `1590` | [Arm and neck stretch](../data/exercises/1590.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1710` | [Butchers Block Stretch](../data/exercises/1710.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1861` | [Side stretch](../data/exercises/1861.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1921` | [Extreme Lat Stretch](../data/exercises/1921.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |

### Family `other` + `calves` (14 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'variable'], tracking_type: ['bodyweight_reps', 'time']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `320` | [Jumping Jacks](../data/exercises/320.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `595` | [Skipping - Standard](../data/exercises/595.yaml) | `jump_rope` | `compound` | `bodyweight` | `time` |
| `993` | [Jump Rope (Basic Jumps)](../data/exercises/993.yaml) | `jump_rope` | `compound` | `bodyweight` | `time` |
| `998` | [No-Push-Up Burpees](../data/exercises/998.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1239` | [Standing Calf Stretch](../data/exercises/1239.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1240` | [Standing Soleus Stretch](../data/exercises/1240.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1274` | [Sitting Calf Stretch (Dorsiflexion)](../data/exercises/1274.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1275` | [Plantarflexion Stretch with Band](../data/exercises/1275.yaml) | `resistance_band` | `isolation` | `variable` | `time` |
| `1314` | [Jumping Jack](../data/exercises/1314.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1854` | [Calves foam roller](../data/exercises/1854.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1856` | [Foam Roller Anterior Tibialis](../data/exercises/1856.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1865` | [Banded Ankle Mobility](../data/exercises/1865.yaml) | `resistance_band` | `isolation` | `variable` | `bodyweight_reps` |
| `1876` | [Supported Calf Stretch](../data/exercises/1876.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1962` | [Step Jack (Low-Impact Jumping Jack)](../data/exercises/1962.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Family `other` + `chest` (5 exercises)
*Variances:* mechanic: ['compound', 'isolation'], tracking_type: ['bodyweight_reps', 'time']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `132` | [Burpees](../data/exercises/132.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1712` | [Horizontal Shoulder Flexion Stretch](../data/exercises/1712.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1713` | [Doorway Pectoral Stretch](../data/exercises/1713.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1919` | [Extreme Chest Stretch](../data/exercises/1919.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `2523` | [Serratus Wall Slide](../data/exercises/2523.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |

### Family `other` + `glutes` (16 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1325` | [Lateral Push Off](../data/exercises/1325.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1452` | [Knee-to-Chest Stretch](../data/exercises/1452.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1556` | [Devil's Press](../data/exercises/1556.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1589` | [Leg and hip stretch](../data/exercises/1589.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1630` | [Blaze](../data/exercises/1630.yaml) | `other` | `compound` | `external` | `time` |
| `1680` | [Seated Figure Four](../data/exercises/1680.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1857` | [Foam Roller Iliotibial band](../data/exercises/1857.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1859` | [Foam Roller Gluteus](../data/exercises/1859.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1869` | [Lying Figure Four Stretch](../data/exercises/1869.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1872` | [Pigeon Stretch](../data/exercises/1872.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1874` | [Runners Lunge Stretch](../data/exercises/1874.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1875` | [Standing IT Band Stretch](../data/exercises/1875.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1949` | [Limber 11 Mobility Routine](../data/exercises/1949.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1950` | [Foam Roll IT Band](../data/exercises/1950.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1952` | [SMR Glutes with Lacrosse Ball](../data/exercises/1952.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1959` | [Seated Piriformis Stretch](../data/exercises/1959.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |

### Family `other` + `hamstrings` (9 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'variable'], tracking_type: ['bodyweight_reps', 'time']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1387` | [Hamstring Kicks](../data/exercises/1387.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1589` | [Leg and hip stretch](../data/exercises/1589.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1670` | [Leg Swings (Front–Back)](../data/exercises/1670.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1840` | [Bent-Leg Hamstring Stretch](../data/exercises/1840.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1855` | [Hamstring Foam roller](../data/exercises/1855.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1870` | [Lying Hamstring Stretch with Band](../data/exercises/1870.yaml) | `resistance_band` | `isolation` | `variable` | `time` |
| `1949` | [Limber 11 Mobility Routine](../data/exercises/1949.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1954` | [Roll-Overs into V-Sits](../data/exercises/1954.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2527` | [Front Split Stretch](../data/exercises/2527.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Family `other` + `lower_back` (4 exercises)
*Variances:* mechanic: ['compound', 'isolation'], tracking_type: ['bodyweight_reps', 'time']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1244` | [Yoga exercise: Cow-cat](../data/exercises/1244.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1363` | [Foam Rolling (Blackroll)](../data/exercises/1363.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1592` | [Guided or free meditation](../data/exercises/1592.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1938` | [Cat-Cow Stretch](../data/exercises/1938.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Family `other` + `neck` (3 exercises)
*Variances:* mechanic: ['compound', 'isolation'], tracking_type: ['bodyweight_reps', 'time']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1006` | [Chin Tuck](../data/exercises/1006.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1018` | [Head Tilts (Lateral Neck Stretch)](../data/exercises/1018.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1590` | [Arm and neck stretch](../data/exercises/1590.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Family `other` + `quads` (14 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `132` | [Burpees](../data/exercises/132.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `320` | [Jumping Jacks](../data/exercises/320.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `595` | [Skipping - Standard](../data/exercises/595.yaml) | `jump_rope` | `compound` | `bodyweight` | `time` |
| `993` | [Jump Rope (Basic Jumps)](../data/exercises/993.yaml) | `jump_rope` | `compound` | `bodyweight` | `time` |
| `997` | [4-Count Burpees](../data/exercises/997.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `998` | [No-Push-Up Burpees](../data/exercises/998.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1314` | [Jumping Jack](../data/exercises/1314.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1325` | [Lateral Push Off](../data/exercises/1325.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1630` | [Blaze](../data/exercises/1630.yaml) | `other` | `compound` | `external` | `time` |
| `1858` | [Foam Roller Quadriceps](../data/exercises/1858.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1873` | [Quad Stretch](../data/exercises/1873.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1960` | [Rear-Foot-Elevated Hip Flexor Stretch](../data/exercises/1960.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1962` | [Step Jack (Low-Impact Jumping Jack)](../data/exercises/1962.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2525` | [Couch Stretch](../data/exercises/2525.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |

### Family `other` + `shoulders` (7 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['time', 'weight_reps']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `675` | [Turkish Get-Up](../data/exercises/675.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1524` | [Battle Ropes](../data/exercises/1524.yaml) | `other` | `compound` | `bodyweight` | `time` |
| `1536` | [Cross-Body Shoulder Stretch](../data/exercises/1536.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1556` | [Devil's Press](../data/exercises/1556.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1630` | [Blaze](../data/exercises/1630.yaml) | `other` | `compound` | `external` | `time` |
| `1841` | [Seated Shoulder Extension Stretch](../data/exercises/1841.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1920` | [Extreme Shoulder Stretch](../data/exercises/1920.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |

### Family `plantar_flexion` + `calves` (12 exercises)
*Variances:* load_mode: ['bodyweight', 'external', 'variable'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `146` | [Calf Press Using Leg Press Machine](../data/exercises/146.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `148` | [Hack Squat Calf Raise](../data/exercises/148.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `590` | [Sitting Calf Raises](../data/exercises/590.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `622` | [Standing Calf Raises](../data/exercises/622.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `702` | [Single-Leg Calf Raise](../data/exercises/702.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1021` | [Right-Leg Calf Raise](../data/exercises/1021.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1203` | [Left-Leg Calf Raise](../data/exercises/1203.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1242` | [Exercise Band Plantarflexion](../data/exercises/1242.yaml) | `resistance_band` | `isolation` | `variable` | `bodyweight_reps` |
| `1243` | [Double Leg Calf Raise](../data/exercises/1243.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1466` | [Calf Raise on Hack Squat Machine](../data/exercises/1466.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1515` | [Leg Press Toe Press](../data/exercises/1515.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1620` | [Seated Dumbbell Calf Raise](../data/exercises/1620.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |

### Family `rotation` + `abs` (26 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external', 'variable'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `145` | [Cable Woodchopper](../data/exercises/145.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `260` | [Full Sit-Out](../data/exercises/260.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `607` | [Sprinter Sit-up](../data/exercises/607.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `672` | [Trunk Rotation With Cable](../data/exercises/672.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1028` | [Quadruped Thoracic Rotation Left](../data/exercises/1028.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1029` | [Quadruped Thoracic Rotation Right](../data/exercises/1029.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1089` | [Medicine Ball Russian Twist](../data/exercises/1089.yaml) | `medicine_ball` | `compound` | `external` | `weight_reps` |
| `1193` | [Dumbbell Russian Twist](../data/exercises/1193.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1259` | [TRX Knee Tuck to Elbow](../data/exercises/1259.yaml) | `suspension_trainer` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1374` | [Rotary Torso Machine](../data/exercises/1374.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1377` | [Standing Torso Twist](../data/exercises/1377.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1412` | [Bicycle Crunch](../data/exercises/1412.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1433` | [Band Reverse Wood Chops](../data/exercises/1433.yaml) | `resistance_band` | `compound` | `variable` | `bodyweight_reps` |
| `1451` | [Torso Rotation Stretch](../data/exercises/1451.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1475` | [Black Widow Knee Slides](../data/exercises/1475.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1477` | [Seated Corkscrew](../data/exercises/1477.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1479` | [Sit Up Elbow Thrust](../data/exercises/1479.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1743` | [Hanging Windshield Wipers](../data/exercises/1743.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1779` | [Landmine Rotation](../data/exercises/1779.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1822` | [Open Book Thoracic Mobility Stretch](../data/exercises/1822.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1868` | [Lunge with Twist Stretch](../data/exercises/1868.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1912` | [Seated Core Rotation (Russian Twist)](../data/exercises/1912.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1953` | [Bent-Knee Iron Cross](../data/exercises/1953.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1966` | [Half-Kneeling Thoracic Rotation](../data/exercises/1966.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2483` | [Wall-Hold Head Rotation Drill](../data/exercises/2483.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2528` | [Squat Sky Reach Stretch](../data/exercises/2528.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Family `rotation` + `back` (5 exercises)
*Variances:* load_mode: ['bodyweight', 'variable']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1028` | [Quadruped Thoracic Rotation Left](../data/exercises/1028.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1029` | [Quadruped Thoracic Rotation Right](../data/exercises/1029.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1082` | [Bent-Over Row to External Rotation](../data/exercises/1082.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1822` | [Open Book Thoracic Mobility Stretch](../data/exercises/1822.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1826` | [Band Pull-Apart with External Rotation](../data/exercises/1826.yaml) | `resistance_band` | `compound` | `variable` | `bodyweight_reps` |

### Family `rotation` + `glutes` (10 exercises)
*Variances:* mechanic: ['compound', 'isolation'], tracking_type: ['bodyweight_reps', 'time']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1207` | [Scorpion Kick](../data/exercises/1207.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1577` | [Bretzel Stretch](../data/exercises/1577.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1862` | [Hip Circles](../data/exercises/1862.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1863` | [Hip Crossover](../data/exercises/1863.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1868` | [Lunge with Twist Stretch](../data/exercises/1868.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1884` | [Shinbox IR Stretch](../data/exercises/1884.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1953` | [Bent-Knee Iron Cross](../data/exercises/1953.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1956` | [Fire Hydrant Circles](../data/exercises/1956.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `2448` | [Reverse Clamshell](../data/exercises/2448.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `2449` | [Clamshell to Reverse Clamshell](../data/exercises/2449.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |

### Family `rotation` + `neck` (5 exercises)
*Variances:* tracking_type: ['bodyweight_reps', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1007` | [Head Turns](../data/exercises/1007.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1015` | [Clockwise Neck Circles](../data/exercises/1015.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1016` | [Counterclockwise Neck Circles](../data/exercises/1016.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1017` | [Neck Half Circles](../data/exercises/1017.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1939` | [Controlled Articular Rotations for Neck (Neck CARs)](../data/exercises/1939.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |

### Family `rotation` + `shoulders` (20 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external', 'variable'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `142` | [Cable External Rotation](../data/exercises/142.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `406` | [Side-Lying External Shoulder Rotation](../data/exercises/406.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `578` | [Side-lying External Rotation](../data/exercises/578.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `915` | [Bus Drivers](../data/exercises/915.yaml) | `weight_plate` | `isolation` | `external` | `weight_reps` |
| `994` | [Forward Arm Circles](../data/exercises/994.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `995` | [Backward Arm Circles](../data/exercises/995.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1004` | [Forward Shoulder Rotation](../data/exercises/1004.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1005` | [Backward Shoulder Rotation](../data/exercises/1005.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1081` | [Shoulder Dislocates (with Band or Stick)](../data/exercises/1081.yaml) | `resistance_band` | `compound` | `variable` | `bodyweight_reps` |
| `1082` | [Bent-Over Row to External Rotation](../data/exercises/1082.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1429` | [Dumbbell Shoulder Rotations](../data/exercises/1429.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1582` | [Side-Lying Internal Rotation](../data/exercises/1582.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1711` | [Sleeper Stretch](../data/exercises/1711.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1714` | [Shoulder Dumbbell Pendular Exercise](../data/exercises/1714.yaml) | `dumbbell` | `isolation` | `external` | `time` |
| `1715` | [Shoulder External Rotation with Dumbbell](../data/exercises/1715.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1728` | [Shoulder Internal Rotation (Cable)](../data/exercises/1728.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1729` | [Shoulder External Rotation (Cable)](../data/exercises/1729.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1826` | [Band Pull-Apart with External Rotation](../data/exercises/1826.yaml) | `resistance_band` | `compound` | `variable` | `bodyweight_reps` |
| `1835` | [Seated Dumbbell External Rotation](../data/exercises/1835.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1838` | [Banded Shoulder Drills](../data/exercises/1838.yaml) | `resistance_band` | `compound` | `variable` | `bodyweight_reps` |

### Family `scapular_elevation` + `back` (6 exercises)
*Variances:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `570` | [Shoulder Shrug](../data/exercises/570.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `571` | [Barbell Shrug](../data/exercises/571.yaml) | `barbell` | `isolation` | `external` | `weight_reps` |
| `572` | [Dumbbell Shrug](../data/exercises/572.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `575` | [Smith Machine Shrug](../data/exercises/575.yaml) | `smith_machine` | `isolation` | `external` | `weight_reps` |
| `1472` | [Cable Shrug-In](../data/exercises/1472.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1925` | [Barbell Silverback Shrug](../data/exercises/1925.yaml) | `barbell` | `isolation` | `external` | `weight_reps` |

### Family `shoulder_abduction` + `back` (3 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1606` | [Arm Raises (T/Y/I)](../data/exercises/1606.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1679` | [Wall Angels](../data/exercises/1679.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1879` | [Incline DB Y-Raise](../data/exercises/1879.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |

### Family `shoulder_abduction` + `shoulders` (19 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time_weight', 'weight_reps']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `31` | [Axe Hold](../data/exercises/31.yaml) | `dumbbell` | `isolation` | `external` | `time_weight` |
| `348` | [Dumbbell Lateral Raise](../data/exercises/348.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `349` | [Single-Arm Cable Lateral Raise](../data/exercises/349.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `351` | [Lateral-to-Front Raises](../data/exercises/351.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `918` | [Seated Dumbbell Lateral Raise](../data/exercises/918.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1378` | [Single-Arm Cable Lateral Raise](../data/exercises/1378.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1443` | [Dumbbell Lateral and Front Raise](../data/exercises/1443.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1602` | [Dumbbell Scaption](../data/exercises/1602.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1606` | [Arm Raises (T/Y/I)](../data/exercises/1606.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1654` | [Machine Lateral Raise](../data/exercises/1654.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1707` | [Cable Lateral Raise](../data/exercises/1707.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1730` | [Side Lateral Raise (Cable)](../data/exercises/1730.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1752` | [Front-Crossing Cable Lateral Raise](../data/exercises/1752.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1753` | [Behind-the-Back Cable Lateral Raise](../data/exercises/1753.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1754` | [45° Scapular Lateral Raise](../data/exercises/1754.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1807` | [Behind-the-Back Cable Lateral Raise](../data/exercises/1807.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1879` | [Incline DB Y-Raise](../data/exercises/1879.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1882` | [Cable Lateral Raise from Waist Height](../data/exercises/1882.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `2538` | [Isometric Cable Lateral Raise](../data/exercises/2538.yaml) | `cable` | `isolation` | `external` | `time_weight` |

### Family `shoulder_flexion` + `shoulders` (7 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `254` | [Front Raises with Plates](../data/exercises/254.yaml) | `weight_plate` | `isolation` | `external` | `weight_reps` |
| `256` | [Front Raises](../data/exercises/256.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `917` | [Straight Bar Cable Front Raise](../data/exercises/917.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1223` | [Claps Over the Head](../data/exercises/1223.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1338` | [Dumbbell Front Raise](../data/exercises/1338.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1731` | [Front Raise (Cable)](../data/exercises/1731.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1745` | [Cable Front Raise with Short Bar](../data/exercises/1745.yaml) | `cable` | `isolation` | `external` | `weight_reps` |

### Family `spinal_extension` + `back` (2 exercises)
*Variances:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1455` | [Towel Superman](../data/exercises/1455.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1487` | [Hyper Y-W Combo with Weight Plates](../data/exercises/1487.yaml) | `weight_plate` | `compound` | `external` | `weight_reps` |

### Family `spinal_extension` + `glutes` (4 exercises)
*Variances:* tracking_type: ['bodyweight_reps', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `636` | [Superman](../data/exercises/636.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1210` | [Skydiver with Arms in T-Position](../data/exercises/1210.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1263` | [Back Bridge](../data/exercises/1263.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1348` | [Back Extension](../data/exercises/1348.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Family `spinal_extension` + `lower_back` (11 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `301` | [Hyperextensions](../data/exercises/301.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `516` | [Front Wood Chop](../data/exercises/516.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `636` | [Superman](../data/exercises/636.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1143` | [Machine Back Extension](../data/exercises/1143.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1210` | [Skydiver with Arms in T-Position](../data/exercises/1210.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1263` | [Back Bridge](../data/exercises/1263.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1348` | [Back Extension](../data/exercises/1348.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1455` | [Towel Superman](../data/exercises/1455.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1487` | [Hyper Y-W Combo with Weight Plates](../data/exercises/1487.yaml) | `weight_plate` | `compound` | `external` | `weight_reps` |
| `1810` | [Sphinx Pose](../data/exercises/1810.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `1908` | [Butterfly Superman](../data/exercises/1908.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Family `spinal_flexion` + `abs` (31 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `165` | [Swiss Ball Knee Tuck](../data/exercises/165.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `167` | [Crunch](../data/exercises/167.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `171` | [Decline Crunch](../data/exercises/171.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `172` | [Machine Crunch](../data/exercises/172.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `173` | [Cable Kneeling Crunch](../data/exercises/173.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `174` | [Vertical Leg Crunch](../data/exercises/174.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `283` | [Hanging Leg Raise](../data/exercises/283.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `377` | [Lying Leg Raise](../data/exercises/377.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `378` | [Dip Station Leg Raise](../data/exercises/378.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `427` | [Decline Crunch](../data/exercises/427.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `505` | [Roman Chair Crunch](../data/exercises/505.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `591` | [Bench-Elevated Sit-up](../data/exercises/591.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `688` | [Upper External Oblique](../data/exercises/688.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `976` | [Medicine Ball V-Up Crunch](../data/exercises/976.yaml) | `medicine_ball` | `compound` | `external` | `weight_reps` |
| `978` | [Hanging Knee Raise](../data/exercises/978.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `979` | [Hanging Leg Raise](../data/exercises/979.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1105` | [Seated Knee Tuck](../data/exercises/1105.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1286` | [Plank Tuck Jump](../data/exercises/1286.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1287` | [Reach-up](../data/exercises/1287.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1399` | [Roll Down](../data/exercises/1399.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1415` | [Dumbbell Crunch](../data/exercises/1415.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1474` | [W-Raise](../data/exercises/1474.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1476` | [Butterfly Sit-up](../data/exercises/1476.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1478` | [Levitation Crunch](../data/exercises/1478.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1529` | [Toes-to-Bar](../data/exercises/1529.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1648` | [Weight Plate Crunch](../data/exercises/1648.yaml) | `weight_plate` | `isolation` | `external` | `weight_reps` |
| `1772` | [Reverse Crunch](../data/exercises/1772.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1889` | [Decline Bench Leg Raise](../data/exercises/1889.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1924` | [gym80 3008 Abdominal Crunch Machine](../data/exercises/1924.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1933` | [Reverse Crunch](../data/exercises/1933.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `2488` | [Posterior Pelvic Tilt](../data/exercises/2488.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |

### Family `spinal_flexion` + `lower_back` (2 exercises)
*Variances:* tracking_type: ['bodyweight_reps', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1002` | [Child's Pose](../data/exercises/1002.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1399` | [Roll Down](../data/exercises/1399.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Family `squat` + `adductors` (2 exercises)
*Variances:* tracking_type: ['bodyweight_reps', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `632` | [Sumo Squats](../data/exercises/632.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1846` | [Horse Stance (Side Splits)](../data/exercises/1846.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Family `squat` + `glutes` (43 exercises)
*Variances:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `43` | [Barbell Hack Squat](../data/exercises/43.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `124` | [Braced Squat](../data/exercises/124.yaml) | `weight_plate` | `compound` | `external` | `weight_reps` |
| `203` | [Dumbbell Goblet Squat](../data/exercises/203.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `257` | [Front Squats](../data/exercises/257.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `285` | [High Knee Jumps](../data/exercises/285.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `341` | [Squats on Multipress](../data/exercises/341.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `371` | [Leg Press](../data/exercises/371.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `374` | [Wide Stance Leg Press](../data/exercises/374.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `375` | [Leg Press on Hackenschmidt Machine](../data/exercises/375.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `397` | [Low Box Squat - Wide Stance](../data/exercises/397.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `441` | [Overhead Squat](../data/exercises/441.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `456` | [Pistol Squat](../data/exercises/456.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `614` | [Squat Jumps](../data/exercises/614.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `615` | [Squats](../data/exercises/615.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `616` | [Squat Thrust](../data/exercises/616.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `632` | [Sumo Squats](../data/exercises/632.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `650` | [Thruster](../data/exercises/650.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `977` | [Box Squat](../data/exercises/977.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1020` | [Pistol Squats Right](../data/exercises/1020.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1195` | [Side Slides to Squats](../data/exercises/1195.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1201` | [Dragon Squat](../data/exercises/1201.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1208` | [Prisoner Squat](../data/exercises/1208.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1312` | [Bodyweight Squat](../data/exercises/1312.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1361` | [Double Kettlebell Front Squat](../data/exercises/1361.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1373` | [Box Jump](../data/exercises/1373.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1407` | [Cossack squat](../data/exercises/1407.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1408` | [Wall-sit](../data/exercises/1408.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1414` | [Machine Hack Squat](../data/exercises/1414.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1437` | [Barbell Pin Squat](../data/exercises/1437.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1464` | [Pause Hack Squats](../data/exercises/1464.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1527` | [Pendulum Squat](../data/exercises/1527.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1640` | [Dumbbell Front Squat](../data/exercises/1640.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1653` | [Dumbbell Side Squat](../data/exercises/1653.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1733` | [Isometric Squat to Failure](../data/exercises/1733.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1735` | [Single-leg side glute press](../data/exercises/1735.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1739` | [Shrimp Squat](../data/exercises/1739.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1747` | [Smith Machine Squat](../data/exercises/1747.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `1801` | [Barbell Full Squat](../data/exercises/1801.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1803` | [Trap Bar Squat](../data/exercises/1803.yaml) | `trap_bar` | `compound` | `external` | `weight_reps` |
| `1829` | [Landmine Squat to Press](../data/exercises/1829.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1935` | [Belt Squat Machine](../data/exercises/1935.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1948` | [Cossack Squat](../data/exercises/1948.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1963` | [Slow Squat](../data/exercises/1963.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Family `squat` + `quads` (47 exercises)
*Variances:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `43` | [Barbell Hack Squat](../data/exercises/43.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `124` | [Braced Squat](../data/exercises/124.yaml) | `weight_plate` | `compound` | `external` | `weight_reps` |
| `203` | [Dumbbell Goblet Squat](../data/exercises/203.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `257` | [Front Squats](../data/exercises/257.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `285` | [High Knee Jumps](../data/exercises/285.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `291` | [Hindu Squats](../data/exercises/291.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `341` | [Squats on Multipress](../data/exercises/341.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `371` | [Leg Press](../data/exercises/371.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `373` | [Narrow Stance Leg Press](../data/exercises/373.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `374` | [Wide Stance Leg Press](../data/exercises/374.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `375` | [Leg Press on Hackenschmidt Machine](../data/exercises/375.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `397` | [Low Box Squat - Wide Stance](../data/exercises/397.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `441` | [Overhead Squat](../data/exercises/441.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `456` | [Pistol Squat](../data/exercises/456.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `614` | [Squat Jumps](../data/exercises/614.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `615` | [Squats](../data/exercises/615.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `616` | [Squat Thrust](../data/exercises/616.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `632` | [Sumo Squats](../data/exercises/632.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `650` | [Thruster](../data/exercises/650.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `718` | [Wall Sit](../data/exercises/718.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `977` | [Box Squat](../data/exercises/977.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1020` | [Pistol Squats Right](../data/exercises/1020.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1195` | [Side Slides to Squats](../data/exercises/1195.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1201` | [Dragon Squat](../data/exercises/1201.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1208` | [Prisoner Squat](../data/exercises/1208.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1312` | [Bodyweight Squat](../data/exercises/1312.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1361` | [Double Kettlebell Front Squat](../data/exercises/1361.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1373` | [Box Jump](../data/exercises/1373.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1407` | [Cossack squat](../data/exercises/1407.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1408` | [Wall-sit](../data/exercises/1408.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1414` | [Machine Hack Squat](../data/exercises/1414.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1437` | [Barbell Pin Squat](../data/exercises/1437.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1464` | [Pause Hack Squats](../data/exercises/1464.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1521` | [Pendulum Hack Squat](../data/exercises/1521.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1527` | [Pendulum Squat](../data/exercises/1527.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1640` | [Dumbbell Front Squat](../data/exercises/1640.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1653` | [Dumbbell Side Squat](../data/exercises/1653.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1733` | [Isometric Squat to Failure](../data/exercises/1733.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1739` | [Shrimp Squat](../data/exercises/1739.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1747` | [Smith Machine Squat](../data/exercises/1747.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `1801` | [Barbell Full Squat](../data/exercises/1801.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1803` | [Trap Bar Squat](../data/exercises/1803.yaml) | `trap_bar` | `compound` | `external` | `weight_reps` |
| `1829` | [Landmine Squat to Press](../data/exercises/1829.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1846` | [Horse Stance (Side Splits)](../data/exercises/1846.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1935` | [Belt Squat Machine](../data/exercises/1935.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `1948` | [Cossack Squat](../data/exercises/1948.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1963` | [Slow Squat](../data/exercises/1963.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Family `vertical_pull` + `abs` (2 exercises)
*Variances:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'distance_time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `1526` | [SkiErg (Ski Machine)](../data/exercises/1526.yaml) | `cardio_machine` | `compound` | `external` | `distance_time` |
| `1741` | [L-Sit Pull-Ups](../data/exercises/1741.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Family `vertical_pull` + `back` (60 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['assisted', 'bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'distance_time', 'time', 'time_weight', 'weight_reps']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `152` | [Chin Up](../data/exercises/152.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `158` | [Close-Grip Lat Pulldown](../data/exercises/158.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `161` | [Cross-Bench Dumbbell Pullovers](../data/exercises/161.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `258` | [Front pull wide](../data/exercises/258.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `259` | [Front Pull narrow](../data/exercises/259.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `289` | [High Pull](../data/exercises/289.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `354` | [Lat Pull Down (Leaning Back)](../data/exercises/354.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `355` | [Lat Pulldown (Straight Back)](../data/exercises/355.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `423` | [Muscle-Up](../data/exercises/423.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `475` | [Pull-Up](../data/exercises/475.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `477` | [Assisted Machine Pull-Up](../data/exercises/477.yaml) | `machine` | `compound` | `assisted` | `weight_reps` |
| `628` | [Cable Straight-Arm Pulldown with Straight Bar](../data/exercises/628.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `629` | [Cable Straight-Arm Pulldown with Rope](../data/exercises/629.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `684` | [Underhand Lat Pulldown](../data/exercises/684.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `691` | [Smith Machine Upright Row](../data/exercises/691.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `693` | [EZ-Bar Upright Row](../data/exercises/693.yaml) | `ez_bar` | `compound` | `external` | `weight_reps` |
| `694` | [Dumbbell Upright Row](../data/exercises/694.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `695` | [V-Bar Lat Pulldown](../data/exercises/695.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `723` | [Wide-Grip Lat Pulldown](../data/exercises/723.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `821` | [Fingerboard Pull-Up](../data/exercises/821.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `980` | [Commando Pull-Up](../data/exercises/980.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1101` | [Isometric Pull-Up / Row Hold](../data/exercises/1101.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1125` | [Wide-Grip Supinated Lat Pulldown](../data/exercises/1125.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1127` | [Close-Grip Supinated Lat Pulldown](../data/exercises/1127.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1136` | [Neutral-Grip Lat Pulldown](../data/exercises/1136.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1137` | [High-Pulley Cable Pullover](../data/exercises/1137.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1138` | [Incline Bench Cable Pulldown](../data/exercises/1138.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1216` | [Hangboard Recruitment Pulls](../data/exercises/1216.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1273` | [Dumbbell Pullover](../data/exercises/1273.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1280` | [Biceps Close Grip Pull Down](../data/exercises/1280.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1282` | [Isometric Reverse-Grip Chin-Up Hold](../data/exercises/1282.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1292` | [Reverse-Grip Pull-Up](../data/exercises/1292.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1384` | [Pullover Machine](../data/exercises/1384.yaml) | `machine` | `isolation` | `external` | `weight_reps` |
| `1435` | [Scapular Pull-Ups](../data/exercises/1435.yaml) | `bodyweight` | `isolation` | `bodyweight` | `bodyweight_reps` |
| `1470` | [One-Arm Half-Kneeling Lat Pulldown](../data/exercises/1470.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1510` | [Neutral Grip Lat Pulldown](../data/exercises/1510.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1526` | [SkiErg (Ski Machine)](../data/exercises/1526.yaml) | `cardio_machine` | `compound` | `external` | `distance_time` |
| `1537` | [Pull-Up Isometric Hold](../data/exercises/1537.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1545` | [Archer Pull-Up](../data/exercises/1545.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1607` | [Typewriter Pull-Up](../data/exercises/1607.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1635` | [Modified pulldown](../data/exercises/1635.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1659` | [Single-Arm Cross-Body Lat Pulldown](../data/exercises/1659.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1695` | [Wide-Grip Pull-Up](../data/exercises/1695.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1696` | [Neutral-Grip Pull-Up](../data/exercises/1696.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1702` | [Wide-Grip Lat Pulldown](../data/exercises/1702.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1719` | [Half-Kneeling One-Arm Lat Pulldown](../data/exercises/1719.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1726` | [Cable Straight-Arm Pulldown](../data/exercises/1726.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1727` | [Cable Standing Lateral Straight-Arm Pulldown](../data/exercises/1727.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1737` | [Assisted chin-ups](../data/exercises/1737.yaml) | `machine` | `compound` | `assisted` | `bodyweight_reps` |
| `1738` | [Neutral-grip pull-ups or TRX rows](../data/exercises/1738.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1741` | [L-Sit Pull-Ups](../data/exercises/1741.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1755` | [Cable Shoulder Y-Raise](../data/exercises/1755.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1795` | [Unilateral Cross-Body Cable Pulldown](../data/exercises/1795.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `1927` | [Reverse-Grip Lat Pulldown (Inverted Lat Pulldown)](../data/exercises/1927.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1929` | [Straight-Arm Band Pulldown](../data/exercises/1929.yaml) | `resistance_band` | `compound` | `assisted` | `bodyweight_reps` |
| `1970` | [Kettlebell Sumo High Pull](../data/exercises/1970.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1971` | [Mentzer Pulldown](../data/exercises/1971.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1972` | [Single-Arm Lat Pulldown](../data/exercises/1972.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `2533` | [Arch Hang](../data/exercises/2533.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2540` | [Isometric Lat Pulldown](../data/exercises/2540.yaml) | `cable` | `compound` | `external` | `time_weight` |

### Family `vertical_pull` + `biceps` (12 exercises)
*Variances:* load_mode: ['assisted', 'bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `152` | [Chin Up](../data/exercises/152.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `684` | [Underhand Lat Pulldown](../data/exercises/684.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `980` | [Commando Pull-Up](../data/exercises/980.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1101` | [Isometric Pull-Up / Row Hold](../data/exercises/1101.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1127` | [Close-Grip Supinated Lat Pulldown](../data/exercises/1127.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1280` | [Biceps Close Grip Pull Down](../data/exercises/1280.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1282` | [Isometric Reverse-Grip Chin-Up Hold](../data/exercises/1282.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1292` | [Reverse-Grip Pull-Up](../data/exercises/1292.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1537` | [Pull-Up Isometric Hold](../data/exercises/1537.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1737` | [Assisted chin-ups](../data/exercises/1737.yaml) | `machine` | `compound` | `assisted` | `bodyweight_reps` |
| `1927` | [Reverse-Grip Lat Pulldown (Inverted Lat Pulldown)](../data/exercises/1927.yaml) | `cable` | `compound` | `external` | `weight_reps` |
| `1971` | [Mentzer Pulldown](../data/exercises/1971.yaml) | `cable` | `compound` | `external` | `weight_reps` |

### Family `vertical_pull` + `chest` (3 exercises)
*Variances:* mechanic: ['compound', 'isolation'], load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'weight_reps']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `161` | [Cross-Bench Dumbbell Pullovers](../data/exercises/161.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `423` | [Muscle-Up](../data/exercises/423.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1273` | [Dumbbell Pullover](../data/exercises/1273.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |

### Family `vertical_pull` + `forearms` (5 exercises)
*Variances:* mechanic: ['compound', 'isolation'], tracking_type: ['bodyweight_reps', 'time']

> [!WARNING]
> **Mechanic Inconsistency**: This family contains both `compound` and `isolation`! Please check whether isolation exercises were accidentally declared as compound.

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `182` | [Deadhang](../data/exercises/182.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `804` | [Fingerboard Sloper Hang](../data/exercises/804.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `820` | [Fingerboard 20 mm Edge Hang](../data/exercises/820.yaml) | `bodyweight` | `isolation` | `bodyweight` | `time` |
| `821` | [Fingerboard Pull-Up](../data/exercises/821.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1216` | [Hangboard Recruitment Pulls](../data/exercises/1216.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Family `vertical_push` + `back` (2 exercises)
*Variances:* tracking_type: ['bodyweight_reps', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `711` | [Wall Handstand](../data/exercises/711.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `716` | [Wall Slides](../data/exercises/716.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |

### Family `vertical_push` + `chest` (5 exercises)
*Variances:* tracking_type: ['bodyweight_reps', 'time']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `194` | [Dips](../data/exercises/194.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `501` | [Ring Dips](../data/exercises/501.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `716` | [Wall Slides](../data/exercises/716.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1832` | [Ring Support Hold](../data/exercises/1832.yaml) | `suspension_trainer` | `compound` | `bodyweight` | `time` |
| `1914` | [Parallel Bar Support Hold](../data/exercises/1914.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |

### Family `vertical_push` + `shoulders` (35 exercises)
*Variances:* load_mode: ['bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'time_weight', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `20` | [Arnold Shoulder Press](../data/exercises/20.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `193` | [Diagonal Shoulder Press](../data/exercises/193.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `282` | [Handstand Pushup](../data/exercises/282.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `346` | [Landmine press](../data/exercises/346.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `418` | [EZ-Bar Military Press](../data/exercises/418.yaml) | `ez_bar` | `compound` | `external` | `weight_reps` |
| `454` | [Pike Push-Up](../data/exercises/454.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `478` | [Dumbbell Push Press](../data/exercises/478.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `543` | [Machine Shoulder Press](../data/exercises/543.yaml) | `machine` | `compound` | `external` | `weight_reps` |
| `566` | [Barbell Shoulder Press](../data/exercises/566.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `567` | [Dumbbell Shoulder Press](../data/exercises/567.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `569` | [Smith Machine Shoulder Press](../data/exercises/569.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `687` | [Overhead Press](../data/exercises/687.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `711` | [Wall Handstand](../data/exercises/711.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `916` | [Smith Machine Overhead Press](../data/exercises/916.yaml) | `smith_machine` | `compound` | `external` | `weight_reps` |
| `1090` | [Pike Push-Up (V-Push-Up)](../data/exercises/1090.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1226` | [Dumbbell Biceps Curl to Overhead Press](../data/exercises/1226.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1360` | [Double Kettlebell Clean and Press](../data/exercises/1360.yaml) | `kettlebell` | `compound` | `external` | `weight_reps` |
| `1439` | [Barbell Pin Overhead Press](../data/exercises/1439.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1440` | [Push Press](../data/exercises/1440.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1441` | [Incline Dumbbell Overhead Press](../data/exercises/1441.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1442` | [Kreis Press with Dumbbells](../data/exercises/1442.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1445` | [Olympic Jerk](../data/exercises/1445.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1446` | [Olympic Clean and Jerk](../data/exercises/1446.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1504` | [Dumbbell Bradford Press](../data/exercises/1504.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1516` | [Handstand](../data/exercises/1516.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1575` | [Standing Dowel Shoulder Press](../data/exercises/1575.yaml) | `other` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1638` | [Barbell Clean and press](../data/exercises/1638.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1684` | [Dumbbell Thruster](../data/exercises/1684.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1808` | [Parallel Bar Support Hold](../data/exercises/1808.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1893` | [Overhead Barbell Press](../data/exercises/1893.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1901` | [Clean and Press](../data/exercises/1901.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1967` | [Seated Dumbbell Overhead Press](../data/exercises/1967.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `1968` | [Single-Arm Dumbbell Shoulder Press](../data/exercises/1968.yaml) | `dumbbell` | `compound` | `external` | `weight_reps` |
| `2498` | [Pike Push-Ups](../data/exercises/2498.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2537` | [Isometric Cable Overhead Press](../data/exercises/2537.yaml) | `cable` | `compound` | `external` | `time_weight` |

### Family `vertical_push` + `triceps` (19 exercises)
*Variances:* load_mode: ['assisted', 'bodyweight', 'external'], tracking_type: ['bodyweight_reps', 'time', 'time_weight', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `194` | [Dips](../data/exercises/194.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `197` | [Dips Between Two Benches](../data/exercises/197.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `282` | [Handstand Pushup](../data/exercises/282.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `418` | [EZ-Bar Military Press](../data/exercises/418.yaml) | `ez_bar` | `compound` | `external` | `weight_reps` |
| `501` | [Ring Dips](../data/exercises/501.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `566` | [Barbell Shoulder Press](../data/exercises/566.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1000` | [Floor Dips](../data/exercises/1000.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1090` | [Pike Push-Up (V-Push-Up)](../data/exercises/1090.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1269` | [TRX Dips](../data/exercises/1269.yaml) | `suspension_trainer` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1320` | [Bench Dips On Floor](../data/exercises/1320.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1372` | [Assisted Triceps Dips (Machine)](../data/exercises/1372.yaml) | `machine` | `compound` | `assisted` | `weight_reps` |
| `1439` | [Barbell Pin Overhead Press](../data/exercises/1439.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1774` | [Chair Dips](../data/exercises/1774.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `1808` | [Parallel Bar Support Hold](../data/exercises/1808.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `1832` | [Ring Support Hold](../data/exercises/1832.yaml) | `suspension_trainer` | `compound` | `bodyweight` | `time` |
| `1893` | [Overhead Barbell Press](../data/exercises/1893.yaml) | `barbell` | `compound` | `external` | `weight_reps` |
| `1914` | [Parallel Bar Support Hold](../data/exercises/1914.yaml) | `bodyweight` | `compound` | `bodyweight` | `time` |
| `2498` | [Pike Push-Ups](../data/exercises/2498.yaml) | `bodyweight` | `compound` | `bodyweight` | `bodyweight_reps` |
| `2537` | [Isometric Cable Overhead Press](../data/exercises/2537.yaml) | `cable` | `compound` | `external` | `time_weight` |

### Family `wrist_flexion` + `forearms` (7 exercises)
*Variances:* load_mode: ['external', 'variable'], tracking_type: ['bodyweight_reps', 'weight_reps']

| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |
|---|---|---|---|---|---|
| `51` | [Barbell Wrist Curl](../data/exercises/51.yaml) | `barbell` | `isolation` | `external` | `weight_reps` |
| `279` | [Hand Grip](../data/exercises/279.yaml) | `other` | `isolation` | `variable` | `bodyweight_reps` |
| `623` | [Standing Wrist Roller](../data/exercises/623.yaml) | `other` | `isolation` | `external` | `weight_reps` |
| `1205` | [Dumbbell Wrist Curl](../data/exercises/1205.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1333` | [Underhand Dumbbell Wrist Curl](../data/exercises/1333.yaml) | `dumbbell` | `isolation` | `external` | `weight_reps` |
| `1771` | [Cable Wrist Curl](../data/exercises/1771.yaml) | `cable` | `isolation` | `external` | `weight_reps` |
| `2452` | [Barbell Wrist Curl](../data/exercises/2452.yaml) | `barbell` | `isolation` | `external` | `weight_reps` |
