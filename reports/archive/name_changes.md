# Proposed English Name Standardizations (reports/name_changes.md)

This report catalogs all proposed English exercise name standardizations according to [NAMING.md](../../NAMING.md).

**Invariants & Scope**:
- Restricted strictly to `status: active` exercises (deprecated entries `1319`, `1768`, `1769` excluded).
- `id` and `slug` remain strictly immutable ([SCHEMA.md §3](../../SCHEMA.md#3-der-id-vertrag--der-teil-der-nicht-nachrüstbar-ist)).
- When applied, original English names will be preserved in `search_terms` so existing user logs and queries resolve seamlessly.
- Frozen cases `1717`, `1967`, and `1833` remain strictly untouched.
- As instructed, these changes remain in the working tree for user review.

Total proposed active exercise modifications: **59 exercises** (plus 1 duplicate merge: `512` merged into `395`).

---

## 1. Duplicate Resolution (`merged` + Alias)

| Target ID | Retained Name | Merged ID | Original Name | Action / Rationale |
|---|---|---|---|---|
| `395` | **Seated Cable Row (Narrow Grip)** | `512` | Rowing seated, narrow grip | Both exercises represent `horizontal_pull` with `cable` in a seated, narrow-grip position. `512` will be merged into `395` with an alias pointing from `512` to `395`, preventing duplicate identical catalog entries. |

---

## 2. Standardizing Comma-Inverted Names (20 exercises)

| ID | Original Name | Proposed Standardized Name | Category / Rationale |
|---|---|---|---|
| `239` | Fly With Dumbbells, Decline Bench | **Decline Dumbbell Fly** | Removed comma inversion |
| `292` | Hip Raise, Lying | **Lying Hip Raise** | Removed comma inversion |
| `349` | Lateral Rows on Cable, One Armed | **One-Arm Cable Lateral Row** | Removed comma inversion |
| `377` | Leg Raises, Lying | **Lying Leg Raise** | Removed comma inversion (target of merged `1313`) |
| `378` | Leg Raises, Standing | **Standing Leg Raise** | Removed comma inversion |
| `395` | Long-Pulley, Narrow | **Seated Cable Row (Narrow Grip)** | Removed comma inversion and clarified setup |
| `513` | Rowing, T-bar | **T-Bar Row** | Removed comma inversion |
| `543` | Shoulder Press, on Machine | **Machine Shoulder Press** | Removed comma inversion |
| `566` | Shoulder Press, Barbell | **Barbell Shoulder Press** | Removed comma inversion |
| `567` | Shoulder Press, Dumbbells | **Dumbbell Shoulder Press** | Removed comma inversion |
| `569` | Shoulder Press, on Multi Press | **Smith Machine Shoulder Press** | Removed comma inversion |
| `571` | Shrugs, Barbells | **Barbell Shrug** | Removed comma inversion |
| `572` | Shrugs, Dumbbells | **Dumbbell Shrug** | Removed comma inversion (target of merged `1645`) |
| `691` | Upright Row, on Multi Press | **Smith Machine Upright Row** | Removed comma inversion |
| `693` | Upright Row, SZ-bar | **EZ-Bar Upright Row** | Removed comma inversion |
| `702` | Calf raises, one legged | **Single-Leg Calf Raise** | Removed comma inversion |
| `1021` | Calf raises, right leg | **Right-Leg Calf Raise** | Removed comma inversion |
| `1203` | Calf raises, left leg | **Left-Leg Calf Raise** | Removed comma inversion |
| `1205` | Wrist curl, dumbbells | **Dumbbell Wrist Curl** | Removed comma inversion |
| `1771` | Wrist curl, cable | **Cable Wrist Curl** | Removed comma inversion |
| `2490` | Pulley (low, with triangle) | **Low Pulley Cable Row (Triangle Grip)** | Removed comma inversion |

---

## 3. Title Case Standardization (15 exercises)

| ID | Original Name | Proposed Standardized Name | Category / Rationale |
|---|---|---|---|
| `975` | one-handed kettlebell curls | **One-Handed Kettlebell Curl** | Strict Title Case & singular noun |
| `980` | commando pull-ups | **Commando Pull-Up** | Strict Title Case & singular noun |
| `1103` | walking bridge | **Walking Bridge** | Strict Title Case |
| `1218` | knee push-ups | **Knee Push-Up** | Strict Title Case & singular noun |
| `1373` | box jumps | **Box Jump** | Strict Title Case & singular noun |
| `1412` | bicycle crunches | **Bicycle Crunch** | Strict Title Case & singular noun |
| `1462` | punches | **Punches** | Strict Title Case (inherent plural) |
| `1612` | kettlebell sumo deadlift | **Kettlebell Sumo Deadlift** | Strict Title Case |
| `1613` | rubber band glute kickback | **Rubber Band Glute Kickback** | Strict Title Case |
| `1680` | seated figure four | **Seated Figure Four** | Strict Title Case |
| `1795` | unilateral cross body cable pull down | **Unilateral Cross-Body Cable Pulldown** | Strict Title Case & hyphenation |
| `1804` | ankle dorsiflexion rocks | **Ankle Dorsiflexion Rocks** | Strict Title Case |
| `1947` | dumbbell snatch | **Dumbbell Snatch** | Strict Title Case |
| `2529` | explosive push ups | **Explosive Push-Up** | Strict Title Case & singular noun |
| `2531` | elbow lever | **Elbow Lever** | Strict Title Case |

---

## 4. Family Consistency: Biceps Curls & EZ-Bar (5 exercises)

| ID | Original Name | Proposed Standardized Name | Category / Rationale |
|---|---|---|---|
| `91` | Biceps Curls With Barbell | **Barbell Biceps Curl** | Unified Biceps family (`vocab/muscles.yaml`), singular |
| `92` | Biceps Curls With Dumbbell | **Dumbbell Biceps Curl** | Unified Biceps family (`vocab/muscles.yaml`), singular |
| `94` | Biceps Curls With SZ-bar | **EZ-Bar Biceps Curl** | Unified Biceps family, EZ-Bar standardization, singular |
| `246` | Skullcrusher SZ-bar | **Skullcrusher EZ-Bar** | Standardized SZ-bar to EZ-Bar for English |
| `418` | Military Press mit SZ-Bar | **EZ-Bar Military Press** | Standardized EZ-Bar, eliminated German preposition "mit" |

---

## 5. Singular Noun & Word Order Standardization (7 exercises)

| ID | Original Name | Proposed Standardized Name | Category / Rationale |
|---|---|---|---|
| `43` | Barbell Hack Squats | **Barbell Hack Squat** | Standardized plural noun to singular |
| `46` | Barbell Lunges Standing | **Standing Barbell Lunge** | Standardized equipment-first word order |
| `75` | Benchpress Dumbbells | **Dumbbell Bench Press** | Standardized equipment-first word order |
| `81` | Bent Over Dumbbell Rows | **Bent-Over Dumbbell Row** | Standardized plural noun to singular |
| `82` | Bent-over Lateral Raises | **Bent-Over Lateral Raise** | Standardized plural noun to singular |
| `95` | Biceps Curl With Cable | **Cable Biceps Curl** | Standardized equipment-first word order |
| `575` | Shrugs on Multipress | **Smith Machine Shrug** | Standardized equipment-first word order |

---

## 6. Language Leakage in English Catalog (2 exercises)

| ID | Original Name | Proposed Standardized Name | Category / Rationale |
|---|---|---|---|
| `1282` | Isometria trazioni impugnatura inversa | **Isometric Reverse-Grip Chin-Up Hold** | Translated Italian upstream name into English |
| `1285` | Talons fesses | **Butt Kicks** | Translated French upstream name into English |

---

## 7. Stripping Scraper & Video Resolution Artifacts (7 exercises)

| ID | Original Name | Proposed Standardized Name | Category / Rationale |
|---|---|---|---|
| `1296` | Low-Cable Cross-Over - NB | **Low-Cable Crossover** | Removed scrape tag `- NB`, standardized Crossover |
| `1298` | High-Cable Cross Tricep Extention - NB | **High-Cable Triceps Extension** | Removed scrape tag `- NB`, fixed typo "Extention" |
| `1312` | Bodyweight Squat HD | **Bodyweight Squat** | Removed resolution tag `HD` |
| `1314` | Jumping Jack HD | **Jumping Jack** | Removed resolution tag `HD` |
| `1318` | High Knee Skips HD | **High Knee Skips** | Removed resolution tag `HD` |
| `1320` | Bench Dips On Floor HD | **Bench Dips On Floor** | Removed resolution tag `HD` |
| `1324` | Bodyweight lunge HD | **Bodyweight Lunge** | Removed resolution tag `HD`, Title Case |

---

## 8. Explicit Review Required: Device / Semantic Refinements (2 exercises)

> [!IMPORTANT]
> These two exercises modify more than surface formatting or word order and require explicit review:

| ID | Original Name | Proposed Standardized Name | Category / Rationale |
|---|---|---|---|
| `148` | Calf Raises on Hackenschmitt Machine | **Hack Squat Calf Raise** | **Device reclassification**: Replaces the German eponym *"Hackenschmitt Machine"* with the standard international gym term *"Hack Squat Calf Raise"*. |
| `510` | Rowing, Lying on Bench | **Chest-Supported Dumbbell Row on Bench** | **Elaborated description**: The original title *"Rowing, Lying on Bench"* is vague; the exercise uses dumbbells with chest supported on a flat bench. |
