# Exercise Naming Conventions (NAMING.md)

This document establishes the official English naming conventions for exercises in OpenExerciseDB.
These rules are derived from the majority patterns observed across the 868 active exercises in the corpus, standardizing inconsistent and conflicting entries.

---

## 1. Core Principles

1. **Clarity & Predictability**: A lifter or developer searching the catalog should immediately predict how an exercise is named.
2. **Grammar & Word Order**: English standard descriptive modifier order: `[Equipment / Setup] [Position / Modifier] [Movement]`. Inverted catalog commas (e.g. `"Shrugs, Barbells"`) are prohibited.
3. **Immutability of Identifiers**: `id` and `slug` **never change**, even when an English name is standardized or cleaned up ([SCHEMA.md §3](SCHEMA.md#3-the-id-contract--the-non-negotiable-foundation)).

---

## 2. Naming Structure & Word Order

### Standard Formula
$$\text{[Equipment / Setup]} + \text{[Stance / Grip / Angle]} + \text{[Movement / Exercise Name]}$$

- **Equipment Placement**: Equipment comes **first** when specifying the implement:
  - *Correct*: `Barbell Shrug`, `Dumbbell Bench Press`, `Cable Lateral Raise`
  - *Incorrect*: `Shrugs, Barbells`, `Benchpress Dumbbells`, `Lateral Rows on Cable`
- **Bodyweight & Setup**: When the exercise is primarily bodyweight with a setup implement, the implement or stance qualifies the movement:
  - *Examples*: `Incline Push-up`, `Decline Push-up`, `Parallel Bar Dip`, `Floor Glider Hamstring Curl`
- **No Comma Inversion**: Comma-inverted phrasing like `"Leg Raises, Lying"` or `"Rowing, T-bar"` is replaced with standard natural phrasing:
  - `Leg Raises, Lying` $\to$ `Lying Leg Raise`
  - `Leg Raises, Standing` $\to$ `Standing Leg Raise`
  - `Hip Raise, Lying` $\to$ `Lying Hip Raise`
  - `Rowing, T-bar` $\to$ `T-Bar Row`
  - `Shoulder Press, on Machine` $\to$ `Machine Shoulder Press`

---

## 3. Singular vs. Plural

### Rule: Singular by Default
Movement and exercise nouns are **singular**, representing a single completed execution of the movement pattern:
- *Singular*: `Curl`, `Shrug`, `Raise`, `Row`, `Press`, `Extension`, `Squat`, `Fly`, `Lunge`, `Crunch`
- *Exceptions (Inherent Plurals)*: Exercises where plural forms are conventional compound nouns or inherently two-legged/two-armed movements:
  - `Jumping Jacks`
  - `Dips`
  - `Mountain Climbers`
  - `Burpees`
  - `Pullovers` (when referring to the clothing-derived name, though `Dumbbell Pullover` is singular)

---

## 4. Capitalization & Typography

1. **Title Case**: All exercise names use standard Title Case.
   - Capitalize nouns, verbs, adjectives, adverbs.
   - Lowercase short prepositions and conjunctions (`with`, `on`, `to`, `and`, `of`) unless they begin the title.
   - *Example*: `Overhead Triceps Extension with Rope`, `Biceps Curl with Barbell`
2. **Acronyms & Implement Brands**:
   - `EZ` (not `SZ` in English names): `EZ-Bar Curl`
   - `TRX` (all caps): `TRX Push-up`, `TRX Row`
   - `DB` expanded to `Dumbbell`, `BB` expanded to `Barbell` where space permits.
3. **Hyphenation**:
   - Standard hyphenated compound modifiers: `Bent-Over Row`, `Close-Grip Bench Press`, `Single-Leg Deadlift`, `Chest-Supported Row`.
   - Nouns with established hyphens: `Pull-up`, `Chin-up`, `Push-up`.

---

## 5. Cleaning Artifacts and Noise Tags

1. **Arbitrary Suffixes**: Suffixes from scraping batches or video resolutions (e.g. ` - NB`, ` HD`, duplicate numbers like ` 2`) must be removed:
   - `Low-Cable Cross-Over - NB` $\to$ `Low-Cable Crossover`
   - `High-Cable Cross Tricep Extention - NB` $\to$ `High-Cable Triceps Extension`
   - `Bodyweight Squat HD` $\to$ `Bodyweight Squat`
   - `Jumping Jack HD` $\to$ `Jumping Jack`
   - `Crunches HD` $\to$ `Crunch`
2. **Supersets & Composite Tags**:
   - Composite tags like `SS` (Superset) in single exercise entries (e.g. `923 Lying Dumbbell Row SS Seated Shrug`) must be clarified or reviewed.
3. **Language Leakage in English Catalog**:
   - Untranslated foreign names in `data/i18n/en/` (e.g. Italian `lento avanti seduto`, French `Talons fesses`) must be rendered into proper English:
     - `Talons fesses` $\to$ `Butt Kicks`
     - `Isometria trazioni impugnatura inversa` $\to$ `Isometric Reverse-Grip Chin-up Hold`
