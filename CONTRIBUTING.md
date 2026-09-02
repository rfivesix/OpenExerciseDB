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

## Checking your change before you push

```bash
pip install -r requirements.txt
python3 build/validate.py
```

That runs the invariants in [schema/invariants.md](schema/invariants.md) against
your working copy — the same gate CI uses.

Two profiles exist. `--profile phase1` is the default and the one CI enforces:
structure and vocabulary are strict, while the content rules apply only where a
field is actually filled in. `--profile full` turns everything on and shows the
work that is still outstanding; it is expected to report errors until phase 2 is
finished, so do not treat its output as a failure.

If you add a field to an exercise, the rules for that field start applying to it
immediately. That is deliberate: partial data is welcome, wrong data is not.

## Review

A green build is necessary but not sufficient: anatomy changes get a human
review. Machine-checkable mistakes are caught by CI so that reviewers can spend
their attention on the ones a machine cannot decide.
