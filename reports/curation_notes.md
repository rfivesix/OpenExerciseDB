# Curation notes

These durable points were retained from the former session handover. The main specification and contribution guide remain [SCHEMA.md](../SCHEMA.md) and [CONTRIBUTING.md](../CONTRIBUTING.md). Those files were excluded from the repository cleanup, so supplementary guidance is preserved here for a future documentation edit.

For the schema documentation: the ID contract is enforced against the append-only `data/published_ids.yaml` registry by invariant 21. Comparing only with the previous release can hide an ID lost in an earlier release. Precise muscle annotations should not be weakened to fit the legacy muscle vocabulary; `test/test_compat.py` allows at most ten exercises shared with the reference release to lose a previously populated legacy primary-muscle mapping.

For the contribution guide: select annotation batches across equipment classes, muscle groups and modalities rather than by numeric ID. Read both English and German text alongside the exercise facts; report conflicting descriptions explicitly. If the vocabulary cannot express the exercise, report the gap and leave the field unset rather than force an inaccurate value.

The other durable decisions are already documented: immutable IDs and merges in SCHEMA §3, `load_mode` in §6, derived `force_vector` in §8, and provenance, justified invariant exceptions and grouped review in §11. Session status, old counts, pending prompts and unverified individual data claims were not retained here.
