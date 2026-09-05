# Cross-Language Discrepancy Report: EN vs. DE Conflicts

## Methodology & Verification Criteria
In Phase 2, language-neutral facts were unified. However, within texts (`data/i18n/`), historical divergences exist between the maintained primary languages English (`en`) and German (`de`).

This report checks three levels:
1. **Equipment family conflicts in titles** (e.g. dumbbell in English, but barbell in German).
2. **Movement vector conflicts** (e.g. *Press* in English, but *Row* in German).
3. **Substantial description asymmetry** ($\ge 3.5\times$ length disparity or completely missing German description when English text exists).

A total of **15 exercises** with discrepancies were identified:
| ID | Name (EN) | Name (DE) | Identified Discrepancy / Discrepancies |
|---|---|---|---|
| `75` | [Dumbbell Bench Press](../data/exercises/75.yaml) | Kurzhantel-Bankdrücken | Large asymmetry: EN (180 words) significantly more detailed than DE (48 words) |
| `79` | [Bent High Pulls](../data/exercises/79.yaml) | Vorgebeugtes High Pull | Large asymmetry: EN (103 words) significantly more detailed than DE (25 words) |
| `205` | [Dumbbell Lunges Standing](../data/exercises/205.yaml) | Ausfallschritte mit Kurzhanteln im Stehen | Large asymmetry: DE (84 words) significantly more detailed than EN (12 words) |
| `237` | [Fly With Cable](../data/exercises/237.yaml) | Kabelzug-Fliegende | Large asymmetry: DE (85 words) significantly more detailed than EN (7 words) |
| `256` | [Front Raises](../data/exercises/256.yaml) | Frontheben mit Kurzhanteln | Large asymmetry: EN (192 words) significantly more detailed than DE (43 words) |
| `279` | [Hand Grip](../data/exercises/279.yaml) | Unterarm-Gripper | Large asymmetry: DE (63 words) significantly more detailed than EN (9 words) |
| `284` | [Hercules Pillars](../data/exercises/284.yaml) | Herkulessäulen am Kabelzug | Large asymmetry: DE (74 words) significantly more detailed than EN (13 words) |
| `537` | [Incline Bench Press - Dumbbell](../data/exercises/537.yaml) | Kurzhantel-Schrägbankdrücken | Large asymmetry: EN (238 words) significantly more detailed than DE (49 words) |
| `683` | [Power Clean](../data/exercises/683.yaml) | Umsetzen | Large asymmetry: EN (89 words) significantly more detailed than DE (19 words) |
| `711` | [Wall Handstand](../data/exercises/711.yaml) | Handstand gegen die Wand | Large asymmetry: EN (61 words) significantly more detailed than DE (10 words) |
| `1119` | [Seated Machine Row (Close Grip)](../data/exercises/1119.yaml) | Maschinenrudern im engen Griff | Large asymmetry: DE (106 words) significantly more detailed than EN (8 words) |
| `1120` | [Seated Machine Row (Underhand Grip)](../data/exercises/1120.yaml) | Maschinenrudern im engen Untergriff | Large asymmetry: DE (91 words) significantly more detailed than EN (12 words) |
| `1143` | [Machine Back Extension](../data/exercises/1143.yaml) | Rückenstrecken an der Maschine | Large asymmetry: DE (75 words) significantly more detailed than EN (13 words) |
| `1527` | [Pendulum Squat](../data/exercises/1527.yaml) | Pendelkniebeuge | Large asymmetry: EN (111 words) significantly more detailed than DE (22 words) |
| `1567` | [Alternating Dumbbell Hammer Curl](../data/exercises/1567.yaml) | Hammercurl mit Kurzhanteln, abwechselnd | Large asymmetry: EN (99 words) significantly more detailed than DE (24 words) |
