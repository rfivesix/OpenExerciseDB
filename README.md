# openexercisedb

An open, structured, machine-readable strength-training exercise database.

Every exercise is a plain text file you can read, diff, and send a pull request
against. Every release ships a single SQLite file you can drop into an app.

> **Status: pre-release.** The import has run — 871 exercises and 3,336
> translations in 22 languages are in `data/`, and the build produces a database
> that today's consumer loads unchanged. The content work has not started and
> there is no published release yet. See [Roadmap](#roadmap).

---

## Why this exists

The best freely licensed exercise dataset available today is the one from the
[wger project](https://wger.de). It is a genuine public good and this project
is a fork of it. It is also, measured against what a training app needs,
incomplete in specific and fixable ways.

At the time of the import (2026-09-02, 871 exercises):

| | |
|---|---|
| Exercises with **no muscle assignment at all** | **129** (15%) |
| Exercises with no *primary* muscle | 135 (16%) |
| Distinct muscle values in the entire dataset | **15** |
| Exercises with no German text | 243 (28%) |

Fifteen values, mixing coarse groups (`Chest`, `Shoulders`) with single
anatomical muscles (`Obliquus externus abdominis`, `Soleus`, `Brachialis`).
No front/side/rear deltoid split. No forearms, adductors, spinal erectors,
rhomboids, or rotator cuff at all.

There is also no structured way to express things a training app needs on every
screen: what equipment an exercise requires, whether it is a warm-up or a main
lift, whether it is logged in reps, seconds, or kilometres. In the upstream
schema `category` is simultaneously a body region (`Legs`, `Back`) *and* a
training type (`Cardio`), so "is this a cardio exercise?" ends up being a string
comparison against a body part.

openexercisedb keeps the upstream identifiers and attribution intact, and fixes
the model.

## What's different

**Muscles are a hierarchy, and you may annotate at any depth.**
14 groups → 32 muscles → 22 heads. If you are confident an exercise hits the
long head of the triceps, say so. If you are only confident it is triceps, say
that. If you are only confident it is arms, say that. Every level resolves
upward, so statistics always work — and "which entries still lack head-level
precision?" is a query, not a guess.

**Orthogonal axes instead of one overloaded category.**
`modality` (what it is) · `usage_tags` (what it is used for, multi-valued)
· `mechanic` · `force_vector` · `movement_pattern` · `laterality`
· `tracking_type` (how it is logged) — each from a closed vocabulary.

**Equipment split into two questions.**
`primary_equipment` is the one thing that creates the load. `setup` is
everything else that has to be standing there. That split is what makes
"what can I do in a hotel room?" answerable: `primary_equipment: bodyweight`
**and** `setup: []`.

**Text is separate from facts, in any number of languages.**
No `name_en` column exists anywhere. A new language is one entry in
`vocab/languages.yaml` plus a directory — no schema change, no build change.
Translators never touch anatomy; data curators never touch prose.

**Identifiers are a contract.**
Consuming apps store exercise IDs in user workout logs. Nothing is ever hard
deleted; merges go through a shipped alias table so downstream apps can migrate
user data safely. See [SCHEMA.md §3](SCHEMA.md).

**Provenance is recorded per field.**
Whether a value came from upstream, from a human, or from a model — with which
model and reviewed by whom. Machine assistance is used heavily and said out
loud, and every generated value is gated by CI invariants and human review.

## Repository layout

```
data/exercises/<id>.yaml      Language-neutral facts, one file per exercise
data/i18n/<lang>/<id>.yaml    Text, one file per exercise per language
vocab/                        Closed vocabularies: muscles, equipment, classification, languages, licenses
schema/                       JSON Schemas + the CI invariants
snapshot/                     The frozen upstream snapshot the import was built from
oedb/                         Shared library used by the import, build and validator
build/                        YAML -> SQLite + manifest + reports
import/                       One-time upstream importer
test/                         Acceptance and rule tests; test/golden/ is the phase 2 eval set
```

## Building it yourself

```bash
pip install -r requirements.txt
python3 build/validate.py                 # the invariants from schema/invariants.md
python3 build/build_db.py --db-out artifacts/catalog.db
python3 build/check_database.py artifacts/catalog.db
```

Nothing there touches the network. Refreshing from upstream is a separate,
deliberate step that lands in the repository as a reviewable snapshot commit:

```bash
python3 import/fetch_wger_snapshot.py
python3 import/wger_to_yaml.py
```

**[SCHEMA.md](SCHEMA.md) is the specification.** Read it before contributing.

## Using the database

Each release publishes a SQLite file, a JSON manifest with a SHA-256 checksum,
and a diff report against the previous release. Point your app at the manifest,
verify the checksum, and read the database directly.

Releases carry two independent version numbers: `version` for content and
`schema_version` for structure. Check `schema_version` before consuming a
release so a structural change can never break an older client.

## Contributing

Corrections are welcome, especially to muscle assignments — that is the weakest
part of the inherited data and the main reason this fork exists.

1. Edit the relevant `data/exercises/<id>.yaml` or `data/i18n/<lang>/<id>.yaml`.
2. Use only values from `vocab/`. CI rejects anything else.
3. Open a pull request. The invariants in [schema/invariants.md](schema/invariants.md)
   run automatically.

Do not edit `id` or `slug` — see [SCHEMA.md §3](SCHEMA.md) for why.

## Roadmap

- [x] **Phase 1 — Import.** Upstream data into source files; the generated
      database is a drop-in replacement for the current one, asserted against
      the published release in `test/test_compat.py`.
- [ ] **Phase 2 — Content.** Fill the 129 empty muscle assignments, then
      equipment and tracking types, then classification, then muscle detail,
      then text.
- [ ] **Phase 3 — Schema v2.** Ship the new tables and the alias mechanism.
- [ ] **Phase 4 — First public release.**

## License

Data is [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), the
build tooling is MIT. Upstream records keep their original per-entry license and
author. See [LICENSE.md](LICENSE.md) and [ATTRIBUTION.md](ATTRIBUTION.md).
