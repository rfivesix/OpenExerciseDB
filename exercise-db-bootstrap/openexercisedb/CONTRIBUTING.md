# Contributing

Thank you for helping. The most valuable contributions are corrections to
**muscle assignments** — that is the weakest part of the inherited data.

## Before you start

Read [SCHEMA.md](SCHEMA.md). It explains the data model and, importantly, why
identifiers can never be changed or reused.

## Making a change

1. Facts (muscles, equipment, classification) live in
   `data/exercises/<id>.yaml`. Text lives in `data/i18n/<lang>/<id>.yaml`.
   These are separate on purpose — you never need to touch both.
2. Every classifying value must come from the matching file in `vocab/`.
   CI rejects unknown values.
3. Annotate muscles at the depth you are actually confident about. A correct
   group is worth more than a guessed head. See "Muscles are a hierarchy" in
   the [README](README.md#whats-different).
4. Never change `id` or `slug`. Never delete an exercise — set
   `status: deprecated`, or `status: merged` with `merged_into`.

## Adding a language

Add an entry to `vocab/languages.yaml`, create `data/i18n/<code>/`, and start
translating. Nothing else needs to change. A partial language is fine; only
languages marked `tier: curated` block a release when incomplete.

## Machine-assisted contributions

They are welcome, and they must be declared. Set the `provenance` block on
every field you generated, including the model. Undeclared bulk-generated
content will be rejected — not because generated data is unwelcome, but because
a wrong value that looks plausible is worse than a missing one, and reviewers
need to know which is which.

## Review

CI runs the invariants in [schema/invariants.md](schema/invariants.md) plus the
golden-set evaluation. A green build is necessary but not sufficient: anatomy
changes get a human review.
