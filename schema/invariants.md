# Invariants (CI Gate)

These rules run on every push. They serve as the primary quality mechanism —
catching the majority of AI hallucinations or invalid annotations automatically,
so that human review focuses on what machines cannot decide.

## Hard and Soft

The rules are not all equal, and treating them as such previously caused harm.

**HARD** (1, 2, 3, 3b, 4, 5, 6, 7, 8, 9, 10, 17, 21, 22, 23, 24, 25) are
structural and referential: an ID points to nothing, a vocabulary value does not
exist, a muscle is listed twice. There are no legitimate exceptions for these,
and any violation blocks the build.

**SOFT** (11, 12, 13, 14, 15, 20) are plausibility heuristics. They state
correlations, not laws. "Cardio is not logged in reps" is usually true — but
burpees exist. "A compound movement has at least two muscles" is usually true —
but edge cases exist.

**The danger of an overly strict rule is not the false alarm.** A false alarm is
visible. The danger is the silent bending of annotations to pass the gate: the
result would be green CI with incorrect data — precisely the type of defect
these rules are designed to prevent.

A soft invariant can therefore be excepted on a per-exercise basis:

```yaml
exceptions:
  invariant_12: "Squat Thrust / Burpee is a cardio / full-body exercise, but logged by repetitions."
```

The following policies apply:

- An exception on a **hard** invariant is itself an error.
- An exception **without a justification text** is an error.
- An exception that **does not trigger at all** is a warning. Otherwise stale
  exceptions accumulate that no one can associate anymore.
- `build/validate.py` summarizes at the end how often each soft invariant fired
  and how often it was excepted. **A high frequency is a signal that the rule is
  flawed, not the data.**

## Structure

1. Every file under `data/exercises/` validates against `exercise.schema.json`.
2. Every vocabulary value exists in the corresponding `vocab/*.yaml`.
3. `slug` is globally unique; `id` is globally unique.
3b. **IDs within `vocab/muscles.yaml` are unique across all hierarchy levels.**
    Group, muscle, and head share a single table with a primary key in the build
    — therefore, a group `hamstrings` and a muscle `hamstrings` cannot both
    exist. The same rule applies in `equipment.yaml` across `primary_equipment`
    and `setup`.
4. Every language marked as `curated` in `vocab/languages.yaml` has a file under
   `data/i18n/<lang>/` for every exercise with `status: active`.
5. Every `data/i18n/<lang>/<id>.yaml` has a corresponding `data/exercises/<id>.yaml`.
6. `status: merged` ⇒ `merged_into` is set, target exists, target is `active`.
7. No alias points to an ID that is itself an alias (no chains).

## Content Plausibility

Everything here is **soft** unless stated otherwise: excusable via `exceptions`
with justification.

8. **(hard)** At least one muscle with `role: primary`.
9. **(hard)** No duplicate muscle; no muscle simultaneously primary and secondary.
10. **(hard)** No muscle node alongside one of its ancestors or descendants
    (`latissimus_dorsi` + `back` is redundant, `trapezius` + `traps_upper` as well).
11. `primary_equipment: bodyweight` ⇒ no heavy barbell/cable setup in `setup`
    (`squat_rack`, `power_rack`, `cable_tower`, `landmine` prohibited).
12. `modality: cardio` ⇒ `tracking_type` ∈ {`time`, `distance_time`, `distance_only`}.
13. `modality: strength` ⇒ `tracking_type` ∉ {`distance_only`}.
14. `mechanic: isolation` ⇒ at most 2 primary muscles.
15. `mechanic: compound` ⇒ at least 2 participating muscles in total.
16. *(deprecated/deleted)* The rule used to be `supports_assistance: true ⇒
    primary_equipment: bodyweight` — which caused the exact defect it was meant
    to prevent. It restricted "is assisted" exclusively to bodyweight exercises,
    forcing an incorrect answer for assisted weight machines.
    `supports_assistance` was removed without replacement; the intended concept
    is now represented by `load_mode: assisted` (Invariant 25).
17. **(hard)** `supports_added_weight: true` ⇒ `tracking_type` ∈
    {`bodyweight_reps`, `time`}.
18. *(deprecated/deleted)* The rule used to be `movement_pattern anti_* ⇒
    tracking_type ∈ {time, time_weight}`. Because `anti_*` describes what is
    being resisted (not whether the movement is static or dynamic), predicting
    the logging type is fundamentally impossible (rollouts, Pallof press,
    walkouts etc. are dynamic). The information is already captured in
    `tracking_type`.
19. *(structurally satisfied)* The rule used to be "`movement_pattern` matches
    `force_vector`". `force_vector` is no longer annotated; it is derived by the
    build from `force_vector_by_pattern` in `vocab/classification.yaml` — a
    violation can no longer be formulated. The rule was not abolished, but
    moved into the data structure itself — a superior kind of invariant: one
    that cannot be broken, rather than one checked after the fact.
20. Primary muscle group must match `movement_pattern` — table in
    `vocab/pattern_muscle_expectations.yaml`. Every primary muscle group of an
    exercise is checked against expected groups for that pattern.
    `movement_pattern: other` is exempt from this check. A violation is a
    **warning**, not an error: exceptions exist, but each warrants review.

## Load Mode Invariants

24. **(hard)** `supports_added_weight: true` ⇒ `load_mode: bodyweight`. Adding
    external load presumes the base movement is bodyweight.
25. **(hard)** `load_mode: assisted` ⇒ `primary_equipment` ∈ {`machine`,
    `resistance_band`}. Assistance is provided by either a machine or a band.

Nothing more. The remaining conceivable rules around `load_mode` are mere
correlations, and turning correlations into laws was the mistake that made this
separation necessary.

## Regression

21. No `status: active` exercise disappears between two releases without an alias
    or `merged_into` pointing to a successor.
22. Total count of active exercises never drops by more than 5% compared to the
    previous release (threshold analogous to `WGER_FAIL_ON_REMOVED_THRESHOLD`).
23. The golden set (`test/golden/*.yaml`, ~50 hand-reviewed exercises) matches
    field-for-field. Runs before every AI batch as an evaluation for prompt
    changes.
