# Exercise Database — Schema

Version: **Draft 0.2** · Date: 2026-09-05 · Target Build Schema Version: **2**

This document defines the data model of the forked exercise database: source
formats in the repository, the generated SQLite artifact, and the contract
with consuming applications.

---

## 1. Why a New Schema

Measured against the catalog state at the time of initial analysis (852 exercises from `wger`).
The import on 2026-09-02 contained 871 exercises and 129 instead of 189 empty muscle assignments —
upstream made minor improvements, but the fundamental diagnosis remains (§13):

| Finding | Count |
|---|---|
| Exercises with **no muscle assignment at all** | **189** (22%) |
| Exercises without a *primary* muscle assignment | 194 (23%) |
| Distinct muscle values across the entire catalog | **15** |
| Empty descriptions (de/en) | 12 each |
| Descriptions < 40 characters | 32 (de) / 35 (en) |

The 15 legacy values were: `Chest`, `Lats`, `Trapezius`, `Serratus anterior`,
`Shoulders`, `Biceps`, `Brachialis`, `Triceps`, `Abs`,
`Obliquus externus abdominis`, `Glutes`, `Quads`, `Hamstrings`, `Calves`,
`Soleus`. The vocabulary mixed coarse groups with specific anatomical names, lacked
deltoid subdivision, and completely omitted forearms, adductors, spinal erectors,
rotator cuff, and rhomboids — the app's internal alias map in
`recovery_domain_service.dart` had keys for them, but the dataset never delivered them.

Additionally, the actual defect in consuming applications: `majorMuscleGroupFor()`
silently returned `null` for unrecognized muscles, causing the exercise to fall out
of recovery tracking and volume statistics. Together with the 189 empty assignments, this meant:
**a significant portion of logged workout volume was lost in statistics.**

> **Current status.** The findings in this section describe the baseline at fork inception,
> not today's status. No active exercise lacks muscle assignments, the vocabulary
> comprises 69 nodes (51 actively used in the catalog), and English, German, French,
> Italian, and Japanese texts are complete and verified against attributes. This section
> remains to explain the architectural rationale behind the schema design.

A second structural defect: `category_name` simultaneously represented body region
(`Legs`, `Back`, `Arms`, …) *and* training modality (`Cardio`). As a result,
`Exercise.isCardio` was evaluated via a string comparison against a field that ostensibly
described an anatomical region — which determined the workout logging UI.

---

## 2. Core Principles

1. **Text files are the source of truth, not the `.db`.** One file per exercise,
   version-controlled in Git, diffable, and editable via pull requests. The SQLite file
   is purely a build artifact published in releases.
2. **Closed vocabularies.** Every classifying attribute references a file under
   `vocab/*.yaml`. Freeform text exists exclusively in translations.
3. **Orthogonal axes.** What an exercise *is*, *what purpose* it serves, *what equipment*
   creates the load, and *how* it is logged are four separate, independent fields.
4. **Language-neutral facts and text are decoupled.** Translators never touch muscle
   annotations, and data curators never touch localized prose.
5. **Arbitrary number of languages without schema changes.** Adding a language requires
   only an entry in `vocab/languages.yaml` and a subdirectory.
6. **Hard deletions are forbidden.** IDs represent an immutable contract with user data
   (see §3).
7. **License and authorship travel with the data** (§3b).
8. **Provenance is documented per field.** Without granular provenance, auditing
   machine-assisted assignments is archaeology rather than a query.

---

## 3. The ID Contract — The Non-Negotiable Foundation

In consuming applications, `routine_exercises.exercise_id` and
`set_logs.exercise_id` directly reference `exercises.id`
(`lib/data/drift_database.dart:111` and `:163`). **User workout history depends
directly on database IDs.** Any deletion, unmapped ID change, or inadvertent drop
causes permanent data loss or broken foreign keys on client devices.

**ID Format:** The catalog uses legacy numeric wger IDs stored as TEXT.
The value range at import on 2026-09-02 was **9–2543** across 871 exercises — *not*
UUIDs, and *not* a contiguous range. (An earlier draft incorrectly noted 1000–1972 due to
a sampled subset. Code assuming any contiguous numeric range is erroneous — IDs are opaque keys.)
Therefore:

- **Inherited exercises retain their numeric ID unchanged.** Never reassign,
  never normalize, never convert to UUID.
- **New custom exercises** receive `x-` + 12 hex characters (truncated UUIDv5
  derived from the slug). The prefix guarantees they never collide with future
  wger IDs, and generation is deterministic and reproducible.
- **Hard deletions are forbidden.** When an exercise is retired, set `status: deprecated`.
  The row remains in the database so existing logs remain resolvable, but is excluded
  from search and the active catalog.
- **Deduplication and merges** use `status: merged` together with `merged_into: <target_id>`.
  The build generates an `exercise_aliases` table distributed with the SQLite release;
  the app applies these aliases during catalog refresh to migrate `routine_exercises`
  and `set_logs` safely.
- **Alias chains are forbidden** (Invariant 7). If B merges into C, and A was previously
  merged into B, both A and B must directly point to C.
- **Invariant 21 against `data/published_ids.yaml`:** Comparing only against the *previous*
  release creates a ratchet effect: if an ID drops unnoticed in one release, the subsequent
  release sees zero diff removals and green CI. Invariant 21 prevents this by checking the
  repository against `data/published_ids.yaml` — an append-only registry of every exercise ID
  ever published to users. Once an ID is recorded in the registry, it can never disappear
  from `data/exercises/`.

---

## 3b. License Provenance — Per Entry, Not Globally

wger does **not** license exercise data globally under a single umbrella license. The upstream
project README states: *"Exercise/Ingredient Data: Creative Commons (see individual entries)"*,
and the API reflects this: licenses are attached to individual *translations*.

Snapshot breakdown on 2026-09-02 (871 exercises, 3,336 translations):

| License | Translations |
|---|---|
| CC-BY-SA 4.0 | 2,918 |
| CC-BY-SA 3.0 | 333 |
| CC0 1.0 | 85 |

In addition, there were **251 distinct `license_author` values** (most frequent: `wger.de` 1,531,
empty 511, `wgerjhn` 105). Attribution is owed to individual contributors, not to "wger" generically.

Legacy export pipelines discarded `license` and `license_author` completely — shipping a
database without attribution. OpenExerciseDB restores full attribution compliance:

- Every imported exercise carries an `upstream` block (source, remote ID, license, author,
  import date), and every imported translation does as well.
- `ATTRIBUTION.md` is **generated programmatically from data** (`build/build_attribution.py`),
  not maintained manually. With 251 contributors, automated generation is the only way to ensure accuracy.
- The overall repository dataset license is CC-BY-SA 4.0. CC-BY-SA 3.0 permits distribution of
  adaptations under later versions of the same license, and CC0 material is universally compatible.
  Original per-entry licenses are preserved to keep legal lineage verifiable.
- Custom exercises (`x-` IDs) carry `upstream: null` and fall under the repository dataset license.
- Machine-assisted descriptions derived from CC-BY-SA originals are derivative works and remain
  under CC-BY-SA.

> The assessment regarding CC-BY-SA 3.0 to 4.0 forward-compatibility is derived directly from
> the license terms and does not c## 4. Repository Layout

```
data/exercises/<id>.yaml           # Language-neutral facts, one file per exercise
data/i18n/<lang>/<id>.yaml         # Text, one file per exercise per language
vocab/muscles.yaml                 # Hierarchical muscle vocabulary
vocab/equipment.yaml               # primary_equipment + setup
vocab/classification.yaml          # modality, usage_tags, tracking_type, …
vocab/languages.yaml               # Language registry
vocab/licenses.yaml                # SPDX identifiers + wger license IDs
schema/exercise.schema.json        # CI validation for exercise facts
schema/translation.schema.json     # CI validation for localized texts
schema/invariants.md               # Domain rules, CI safety gate
test/golden/*.yaml                 # ~50 human-verified exercises as eval set
test/test_*.py                     # Acceptance and rule tests
snapshot/wger-<date>.json.gz       # Frozen raw upstream source snapshot
build/                             # YAML -> .db + manifest + reports
import/                            # Upstream importer scripts
oedb/                              # Shared Python library for tooling
```

Two directories added during architecture refinement:

- **`snapshot/`** — The raw dump from the wger API, pinned with a SHA-256 checksum
  in Git. Without this, build reproducibility depends on third-party API availability
  at any given moment. It also serves as an audit trail: the exact upstream origin
  remains inspectable forever.
- **`oedb/`** — Unified vocabulary, snapshot, and YAML access shared across the importer,
  builder, and validator. Implemented as a separate package because `import` is a
  reserved keyword in Python, preventing `import/` from exporting modules.

---

## 5. Muscle Model

Hierarchical, three levels: **group → muscle → head**. Currently 14 groups,
33 muscles, 22 heads = 69 nodes (`vocab/muscles.yaml`).

**An exercise may annotate at any level of the hierarchy.** If uncertain about the specific head,
annotate the muscle; if uncertain about the muscle, annotate the group. This resolves the
maintenance bottleneck of granular anatomies without pretending false precision: annotating
a muscle group is an honest assessment; guessing an anatomical head is a falsehood.

Upward resolution is strictly defined. Recovery and volume tracking aggregate at `group`,
while filters and anatomical visualizers can operate at fine-grained leaf nodes. Queries such as
"which exercises still lack head-level precision?" are trivial and guide curation priorities.

`role` is either `primary` or `secondary`. The optional `contribution` field
(0.0–1.0) is reserved in the schema, but is **intentionally left unpopulated** in v1 —
while exercises still required foundational classification, debating fractional percentages
was premature optimization.

Two assignments deliberately diverge from the legacy app mapping and are recorded in
`vocab/muscles.yaml` under `legacy_group`: `serratus_anterior` (legacy app: `back`)
and `hip_flexors` (legacy app: `glutes`). The build continues to populate legacy compatibility
columns using these inverse mappings.

### Semantics of `role: primary` in Stretching Exercises (`modality: stretch`)

For stretches (`modality: stretch`), `role: primary` denotes the anatomical target muscle group
being **stretched** (e.g., `hamstring_complex` in Sit & Reach, `rectus_abdominis` in Cobra Stretch,
`triceps_brachii` in Overhead Triceps Stretch, `latissimus_dorsi` in Child's Pose). It does
**not** denote the contracting antagonist muscle.

Rationale:
1. Stretches are frequently passive (gravity, wall, straps) without meaningful agonist muscle activation.
2. In training apps, users search for stretches by target area ("I want to stretch my hamstrings"),
   not by joint lever kinematics.
3. During plausibility validation (Invariant 20), stretches often appear at odds with joint mechanics
   (e.g., `spinal_extension` targeting `abs` in Cobra Stretch, or `elbow_flexion` targeting `triceps`
   in an overhead stretch) because they stretch the antagonistic muscle.

---

## 6. Classification

| Field | Cardinality | Purpose |
|---|---|---|
| `modality` | exactly 1 | What the exercise *is*: strength, cardio, plyometric, mobility, stretch, balance |
| `usage_tags` | ≥ 1 | What purpose it *serves*: warmup, activation, main_lift, accessory, conditioning, finisher, cooldown, prehab |
| `mechanic` | exactly 1 | compound / isolation |
| `force_vector` | *derived* | push / pull / static — derived from `movement_pattern` |
| `movement_pattern` | exactly 1 | 24 patterns, from `vertical_pull` to `anti_rotation` |
| `laterality` | exactly 1 | bilateral / unilateral / alternating |
| `difficulty` | optional | beginner / intermediate / advanced |
| `tracking_type` | exactly 1 | Determines the logging UI input form |
| `load_mode` | exactly 1 | What the logged numerical value *signifies* |
| `primary_equipment` | exactly 1 | The load-generating equipment |
| `setup` | 0…n | Auxiliary equipment required |

`usage_tags` is multi-valued because a light resistance band pull-apart is legitimately
both a warmup *and* an accessory movement. A single-valued field would force arbitrary compromises.

The separation between `primary_equipment` and `setup` is what enables queries like:
"What can I perform in a hotel room?" Answer: `primary_equipment == bodyweight`
**and** `setup == []`.

`tracking_type` (`weight_reps`, `bodyweight_reps`, `time`, `time_weight`,
`distance_time`, `distance_only`) alongside `supports_added_weight` replaces the legacy
`Exercise.isCardio` heuristic. This provides planks (time), pull-ups (reps, optional added weight),
and treadmills (distance + time) with appropriate input controls.

However, `tracking_type` specifies only the **format** of the logging UI — not what the entered number
*means*. This distinction has serious consequences: on an assisted pull-up machine, the entered weight
is assistance, not load. Increasing weight makes the exercise easier. When logged as generic `weight_reps`,
e1RM estimations, volume accumulation, and progression algorithms calculate progress completely backwards —
without any obvious system errors.

Hence `load_mode` (exactly one value):

| Value | The entered number represents … | Examples |
|---|---|---|
| `external` | Added resistance | Barbell, dumbbell, cable stack |
| `bodyweight` | Optional added load | Pull-up, dip, push-up |
| `assisted` | **Reduction** of bodyweight load | Assisted pull-up/dip machine |
| `variable` | Non-standardized tension | Resistance band |

`supports_added_weight` remains alongside `load_mode` — "pull-ups can be weighted with a dip belt"
is an optional user capability rather than a change to the fundamental base exercise.

`body_region` in the SQLite artifact is **derived** from primary muscles (`upper_body`, `lower_body`,
`core`, or `full_body` when primary muscles span multiple regions) rather than manually annotated:
- `upper_body`: chest, back, shoulders, biceps, triceps, forearms, neck
- `lower_body`: glutes, quads, hamstrings, adductors, calves
- `core`: abs, lower_back
- `full_body`: primary muscles span multiple regions

---

## 7. Translations

One file per exercise per language under `data/i18n/<lang>/<id>.yaml`. Fields:
`name`, `description`, `instructions[]`, `cues[]`, `common_mistakes[]`, `search_terms[]`.

- `instructions` is structured as an ordered list of steps separated from prose descriptions,
  enabling client apps to render structured workout guides.
- `search_terms` contains synonyms, alternative names, and common misspellings for search indexing;
  they are never rendered directly in the UI.
- `status` per document: `human` | `ai_reviewed` | `ai_authored` | `ai_raw` | `upstream_unreviewed`.
  This allows targeted future improvements rather than broad distrust:
  - `upstream_unreviewed`: Inherited from upstream, written by humans but never audited by this project.
  - `ai_raw`: Generated by an AI model without individual human review.
  - `ai_reviewed`: Generated by an AI model and verified by a human reviewer.
  - `ai_authored`: Fundamentally rewritten or newly authored descriptions produced with AI assistance where the original upstream text was missing, unintelligible, or factually misleading, followed by human review.
  - `human`: Directly authored or translated by a human contributor.

**Arbitrary Number of Languages:** `vocab/languages.yaml` serves as the central registry.
Adding a language requires only an entry in the vocabulary file and a new directory. No schema migrations,
no app code changes, and no build modifications are necessary. Languages specify a `tier`
(`curated` / `assisted` / `machine`); only `curated` languages block release builds on coverage gaps.
The build calculates coverage `completeness` per language and writes it into the SQLite `languages` table.

Nowhere in the schema does a column like `name_de` or `name_en` exist. This architectural separation
is the prerequisite for true multilingual scale (§10).

---

## 8. Generated SQLite Artifact (Schema Version 2)

```sql
-- Core
CREATE TABLE exercises (
  id                    TEXT PRIMARY KEY,
  slug                  TEXT NOT NULL UNIQUE,
  status                TEXT NOT NULL,          -- active | deprecated | merged
  merged_into           TEXT REFERENCES exercises(id),
  modality              TEXT NOT NULL,
  mechanic              TEXT NOT NULL,
  force_vector          TEXT,                   -- derived, see below
  movement_pattern      TEXT NOT NULL,
  laterality            TEXT NOT NULL,
  difficulty            TEXT,
  tracking_type         TEXT NOT NULL,
  load_mode             TEXT NOT NULL,          -- what the logged numerical value signifies
  supports_added_weight INTEGER NOT NULL DEFAULT 0,
  primary_equipment     TEXT NOT NULL,
  body_region           TEXT,                   -- derived from primary muscles

  -- Compatibility columns for schema v1 consumers (legacy app).
  -- The importer in basis_data_manager.dart reads EXACTLY these four fields
  -- plus translations. As long as they are populated, legacy apps run
  -- unchanged on a v2 database.
  category_name         TEXT,
  muscles_primary       TEXT,                   -- JSON array, legacy names
  muscles_secondary     TEXT,                   -- JSON array, legacy names
  image_path            TEXT,                   -- always "", no media assets exist
  is_custom             INTEGER NOT NULL DEFAULT 0,
  created_by            TEXT DEFAULT 'system',
  source                TEXT DEFAULT 'base',

  -- License provenance, see §3b. NULL only for custom exercises.
  upstream_source         TEXT,                 -- 'wger' | NULL
  upstream_id             TEXT,
  upstream_license        TEXT,                 -- SPDX identifier, e.g. CC-BY-SA-4.0
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
  tag         TEXT NOT NULL,                    -- from usage_tags
  PRIMARY KEY (exercise_id, tag)
);

-- Translations: structure matches legacy schema, additively extended.
CREATE TABLE exercise_translations (
  id              TEXT PRIMARY KEY,             -- "<exercise_id>_<lang>"
  exercise_id     TEXT NOT NULL REFERENCES exercises(id) ON DELETE CASCADE,
  language_code   TEXT NOT NULL,
  name            TEXT NOT NULL,
  description     TEXT,
  instructions    TEXT,                         -- JSON array
  cues            TEXT,                         -- JSON array
  common_mistakes TEXT,                         -- JSON array
  search_terms    TEXT,                         -- JSON array
  status          TEXT,                         -- human | ai_reviewed | ai_authored | ai_raw
  source_lang     TEXT,
  license         TEXT,                         -- per translation, see §3b
  license_author  TEXT
);
CREATE INDEX idx_tr_exercise_lang ON exercise_translations(exercise_id, language_code);

-- Vocabularies, distributed with the database rather than hardcoded in the app
CREATE TABLE muscles (
  id          TEXT PRIMARY KEY,
  parent_id   TEXT REFERENCES muscles(id),
  level       TEXT NOT NULL,                    -- group | muscle | head
  group_id    TEXT NOT NULL REFERENCES muscles(id),
  legacy_group TEXT,
  body_slugs  TEXT                              -- JSON array
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

-- Migration path for user data
CREATE TABLE exercise_aliases (
  old_id        TEXT PRIMARY KEY,
  new_id        TEXT NOT NULL REFERENCES exercises(id),
  reason        TEXT,                           -- merged | renamed_id | split
  since_version TEXT NOT NULL
);

CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT);
-- Mandatory keys: version, schema_version, generated_at, source_repo,
--                 source_commit, license, attribution_url
```

Two architectural nuances implemented in the generator:

- **`NOT NULL` constraints are data-dependent.** Classification columns are verified
  during build. The builder applies `NOT NULL` constraints dynamically once all active
  records possess values, and records any pending nullable columns in `metadata.nullable_columns`.
  This allows the schema to tighten itself progressively as curation finishes without
  risking runtime crashes or resorting to synthetic sentinel defaults.
- **`force_vector` is computed by the build rather than annotated directly.** It is a pure
  function of `movement_pattern` defined in `vocab/classification.yaml` under `force_vector_by_pattern`.
  Having two separate manual annotations that assert the same mechanical reality inevitably creates
  contradictions. Patterns without directional force vectors map intentionally to `NULL` (e.g. running
  is neither push nor pull; assigning `push` just because an LLM guessed it would be false precision).
  Therefore, this column is nullable and is omitted from `metadata.nullable_columns`.
- **`category_name` is populated from `upstream.source_fields.category`.** This column is legacy
  and is no longer maintained, but legacy apps still read it. The build does not access external
  snapshots directly, so raw values travel within each exercise file.

Vocabularies thereby move **out of application code and into the data package**. Application-side
mappers become simple legacy fallbacks for user-created custom exercises rather than the definitive
location where anatomy is defined.

---

## 9. Manifest and Versioning Contract

The release manifest (`catalog_manifest.json`) pairs a content `version` (timestamp)
with an **independent** integer `schema_version`:

```jsonc
{
  "version": "202609050000",     // Content version
  "schema_version": 2,           // Structural schema version
  "min_app_schema_version": 1,   // Earliest client version capable of reading this
  // … db_url, db_sha256, expected_exercise_count, min_exercise_count, safety …
}
```

Consuming apps declare which `schema_version` they support. Client refresh services gracefully
reject releases with incompatible structural versions rather than downloading and failing at runtime.
Existing installations remain pinned to their last compatible release.

The `beta` channel enables staged rollouts: schema updates publish to `beta` first, the supporting
app update passes app store review, and only then is the release promoted to `stable`.

---

## 10. Client Application Migration Requirements

In approximate implementation order:

1. **Locale-generic translations.** `Exercise.nameDe` / `nameEn` / `descriptionDe` /
   `descriptionEn` are replaced by a map `locale -> localized_texts` with an orderly fallback chain.
   This is the prerequisite for arbitrary language support, impacting `exercise.dart`,
   `exercises_queries.dart`, and callers of `getLocalizedName`.
2. Extend the Drift database schema with new columns/tables and add a schema migration.
3. Update the SQLite importer in `basis_data_manager.dart` (`_mapExerciseBundle`) to populate
   the new relational tables while retaining the four legacy fields as backwards-compatibility fallbacks.
4. Apply `exercise_aliases` during catalog updates to safely migrate foreign keys in
   `routine_exercises` and `set_logs`.
5. Replace `Exercise.isCardio` with `tracking_type` and adapt logging form controls accordingly.
6. Switch `_majorGroupMap` and `BodySlugMapper` to consume bundled database vocabularies,
   relegating hardcoded Dart definitions to legacy fallbacks.
7. Implement equipment-based catalog filtering in UI.
8. Utilize `usage_tags` in workout routine builders.
9. Enforce `schema_version` validation in the catalog refresh service.

Steps 1–5 are required for Schema v2 compatibility. Steps 6–8 deliver end-user product features
and can follow incrementally.

---

## 11. Methodology for Machine-Assisted Content Curation

Across ~900 exercises with ~10 classification attributes each, approximately 9,000 anatomical
and mechanical assertions are maintained. Even a low 5% error rate would mean 450 erroneous
muscle assignments — which are **worse than empty gaps**, because an empty field is obvious,
whereas an incorrect assignment looks deceptively plausible. Therefore:

- **Granular provenance per field**, as illustrated in `examples/exercises/475.yaml`.
- **Invariants enforced as automated CI gates** (`schema/invariants.md`), not manual checklists.
  They catch mechanical inconsistencies systematically.
- **Strict distinction between hard and soft invariants.** Structural violations (IDs, vocabularies,
  dangling references) block unconditionally. Plausibility checks (`anti_*` movement patterns are static,
  cardio is not logged in reps) block only if the anomaly is unexplained — resolved via an explicit
  `exceptions` entry in the exercise file containing a written justification.

  This design reflects an essential lesson from early curation passes: the true danger of an overly rigid
  rule is not a false alarm, but a quietly distorted annotation introduced solely to satisfy CI.
  For example, exercise 1103 originally had `anti_extension` swapped to `other` just to pass a brittle rule,
  resulting in green CI with incorrect anatomical data. Tracking fired versus excused counts ensures that
  systemic rule friction indicates an inaccurate rule rather than broken data.
- **Golden evaluation set**: ~50 human-audited exercises spanning diverse muscle groups and equipment types.
  Prompt engineering and batch modifications are evaluated against this set first.
- **Thematic batch review**: Reviewing in batches grouped by movement pattern and equipment (e.g. reviewing
  40 rowing variations together) enables direct comparative auditing and is significantly faster and more
  accurate than alphabetical reviews.
- **AI models never modify `id` or `slug`.**

---

## 12. Current Status and Open Items

- **Attribution in client applications.** OpenExerciseDB distributes complete licensing data in SQLite
  and generates `ATTRIBUTION.md`. Consuming applications can present contributor acknowledgments directly
  in app settings.
- **Release channels.** Releases are published to the `catalog-stable` channel (with schema changes
  staged in `catalog-beta`).
- **Contribution weighting.** The `contribution` column remains available for future quantitative modeling
  once foundational muscle classifications are fully established.
- **German curation level.** German text coverage is complete across all 868 active exercises and is
  classified as `tier: curated`, ensuring any future text regression triggers CI failure.

---

## 13. Implementation Notes (Historical Findings from Phase 1)

During the initial import from the upstream snapshot on 2026-09-02, several discrepancies were identified
and resolved:

**Legacy pipeline language IDs were miswired.** The legacy `create_wger_exercise_db.py` hardcoded
language IDs as `4:fr, 5:it, 8:ja`. In reality, the wger API defined `4=es, 5=ru, 8=el`; French was `12`,
Italian was `13`, and Japanese was not present upstream. Consequently, the legacy distributed database
shipped **646 Spanish descriptions mislabeled as French, 48 Greek texts mislabeled as Japanese, and
10 Russian texts mislabeled as Italian** (e.g. exercise 132 had Greek text in its `ja` translation).
True French and Italian translations were missing entirely. This mapping was corrected in
`vocab/languages.yaml` and is validated against snapshots automatically.

**Baseline inventory metrics.** At import on 2026-09-02, the catalog contained 871 exercises,
**129 of which lacked muscle assignments entirely** (down from 189 in older snapshots), and 135 lacked
primary muscle assignments. All 868 active exercises are now fully classified.

**Staged schema profiles.** `exercise.schema.json` defines required attributes that upstream wger data
originally lacked. Rather than polluting data with arbitrary dummy values, fields were populated
iteratively. The validator uses two profiles: `phase1` (verifies existing annotations without requiring
all Phase 2 fields) and `full` (enforces strict completeness across all attributes).

**Subset compatibility verification.** The legacy reference database contained 862 exercises.
Compatibility testing in `test/test_compat.py` strictly verifies that no previously published ID
is missing, and that legacy columns (`category_name`, `muscles_primary`, `muscles_secondary`, and
core translation texts) maintain exact character-level parity.

**Elimination of cross-language bleeding.** The legacy pipeline filled missing descriptions by copying
text from the opposing language (causing German text in English rows and vice versa across 17 exercises).
In OpenExerciseDB, untranslated descriptions remain clean `null` values or utilize explicit fallback chains
annotated with `source_lang: en`.

**SPDX license mapping.** Upstream integer license IDs are mapped to standard SPDX identifiers via
`vocab/licenses.yaml`. Unrecognized license IDs abort the import rather than silently dropping attribution.
