# Report: Check of Existing French and Italian Descriptions (Paket 1)

## Summary

Mechanical check of the legacy wger descriptions in French and Italian before starting derivations:

- Total existing active French descriptions checked: **566**
- Total existing active Italian descriptions checked: **142**

## Check 1: Identical to English Text (Silent Fallbacks)

- French descriptions identical to English: **0**
- Italian descriptions identical to English: **0**

None of the existing descriptions are silent copies of the English text.

## Check 2: Equipment Contradictions

Contradictions detected where the translated text refers to equipment conflicting with `primary_equipment`:

### French (1 finding)

- **1426** (Crunchs latéraux debout):
  - `primary_equipment: bodyweight`
  - Text fragment: "...ou un haltère dans une main..."
  - Nature: Legacy text describes an optional weighted dumbbell variation for a bodyweight exercise. Recorded as technical debt.

### Italian (4 findings)

- **171** (Addominali su panca inclinata):
  - `primary_equipment: bodyweight`
  - Text fragment: "...utilizzate un altro aiuto (bilanciere, ecc.) per tenerli fissi..."
  - Nature: Barbell mentioned only as an anchor to hold feet down, not as primary resistance.

- **256** (Distensione lento avanti Bilanciere):
  - `primary_equipment: dumbbell`
  - Text: "Distensione lento avanti BilanciereDistensione lento avanti Bilanciere"
  - Nature: Corrupted duplicated string describing a barbell press, while exercise 256 is annotated as dumbbell front raises. Recorded as technical debt.

- **308** (Distensione Panca Inclinata Bilanciere):
  - `primary_equipment: dumbbell`
  - Text: "DistDistensione Panca Inclinata con BilanciereDistensione Panca Inclinata con Bilanciere"
  - Nature: Corrupted duplicated string describing an incline barbell bench press, while exercise 308 is annotated as dumbbell incline press. Recorded as technical debt.

- **1111** (Distensione Panca Inclinata Bilanciere):
  - `primary_equipment: bodyweight`
  - Text: "Distensione Panca Inclinata con BilanciereDistensione Panca Inclinata con Bilanciere"
  - Nature: Corrupted duplicated string describing an incline barbell bench press, while exercise 1111 is annotated as bodyweight decline pushup. Recorded as technical debt.

## Conclusion

Per specification, these discrepancies are documented as legacy technical debt without invasive in-place re-authoring in this round, as both checks delivered clear diagnostic results.
