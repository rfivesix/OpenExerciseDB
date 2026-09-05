# Name Override Report: Conflicts Between Exercise Name and Primary Muscle

## Purpose & Heuristics
In legacy wger datasets and automated annotations, fundamental discrepancies occasionally occur: an exercise by name clearly targets muscle group A (e.g. *Neck Extension*, *Hamstring Curl*, *Front Raise*), but primary muscle annotation assigns a completely different muscle group B.

This report compares standardized naming patterns (regular expressions on EN/DE titles) with the annotated primary muscles.

Matches found: **36 exercises**.
| ID | Name (EN) | Name (DE) | Search Term | Implied by Name | Annotated Group(s) | Primary Muscle(s) |
|---|---|---|---|---|---|---|
| `500` | [Reverse Plank](../data/exercises/500.yaml) | Reverse Plank | `Plank` | **`abs`** | `glutes, lower_back` | `erector_spinae, gluteus_maximus` |
| `349` | [Single-Arm Cable Lateral Raise](../data/exercises/349.yaml) | Einarmiges Seitheben am Kabelzug | `rows` | **`back`** | `shoulders` | `delt_lateral` |
| `1227` | [Dumbbell Rear Delt Row](../data/exercises/1227.yaml) | Vorgebeugtes Kurzhantelrudern für die hintere Schulter | `Row` | **`back`** | `shoulders` | `delt_posterior` |
| `1376` | [Barbell Calf Raise](../data/exercises/1376.yaml) | Wadenheben mit der Langhantel | `Calf` | **`calves`** | `quads` | `quadriceps` |
| `76` | [Bench Press Narrow Grip](../data/exercises/76.yaml) | Enges Bankdrücken | `Bench Press` | **`chest`** | `triceps` | `triceps_brachii` |
| `139` | [Reverse Pec Deck (Rear Delt Fly)](../data/exercises/139.yaml) | Reverse Butterfly | `Pec` | **`chest`** | `shoulders` | `delt_posterior` |
| `510` | [Chest-Supported Barbell Row on Bench](../data/exercises/510.yaml) | Brustgestütztes Langhantelrudern auf der Bank | `Chest` | **`chest`** | `back` | `latissimus_dorsi, rhomboids` |
| `1136` | [Neutral-Grip Lat Pulldown](../data/exercises/1136.yaml) | Latzug zur Brust mit neutralem Griff | `chest` | **`chest`** | `back` | `latissimus_dorsi, teres_major` |
| `1283` | [Incline Chest-Supported Dumbbell Row](../data/exercises/1283.yaml) | Schrägbank-Kurzhantelrudern mit Brustauflage | `Chest` | **`chest`** | `back` | `latissimus_dorsi, rhomboids` |
| `1452` | [Knee-to-Chest Stretch](../data/exercises/1452.yaml) | Knie-zur-Brust-Dehnung | `Chest` | **`chest`** | `glutes` | `gluteus_maximus` |
| `1775` | [Pec Deck Rear Delt Fly](../data/exercises/1775.yaml) | Reverse Butterfly am Pec Deck | `Pec` | **`chest`** | `shoulders` | `delt_posterior` |
| `1825` | [Chest-Supported Rear Delt Raise](../data/exercises/1825.yaml) | Reverse Flys auf Schrägbank mit Brustauflage | `Chest` | **`chest`** | `shoulders` | `delt_posterior` |
| `2478` | [Glute-Ham Raise (GHR)](../data/exercises/2478.yaml) | Glute-Ham-Raise (GHR) | `Glute` | **`glutes`** | `hamstrings` | `hamstring_complex` |
| `189` | [Deficit Deadlift](../data/exercises/189.yaml) | Defizit Kreuzheben | `Deadlift` | **`hamstrings`** | `glutes, lower_back` | `gluteus_maximus, erector_spinae` |
| `484` | [Rack Deadlift](../data/exercises/484.yaml) | Rack-Pull | `Deadlift` | **`hamstrings`** | `glutes, lower_back` | `gluteus_maximus, erector_spinae` |
| `1612` | [Kettlebell Sumo Deadlift](../data/exercises/1612.yaml) | Sumo-Kreuzheben mit Kettlebell | `Deadlift` | **`hamstrings`** | `adductors, glutes` | `gluteus_maximus, hip_adductors` |
| `1717` | [One-Arm Overhead Cable Triceps Extension](../data/exercises/1717.yaml) | Einarmiges Überkopf-Trizepsdrücken am Kabelzug | `neck` | **`neck`** | `triceps` | `triceps_brachii` |
| `146` | [Calf Press Using Leg Press Machine](../data/exercises/146.yaml) | Wadendrücken an der Beinpresse | `Leg Press` | **`quads`** | `calves` | `gastrocnemius` |
| `148` | [Hack Squat Calf Raise](../data/exercises/148.yaml) | Wadenheben an der Hackenschmidt-Maschine | `Squat` | **`quads`** | `calves` | `gastrocnemius` |
| `1466` | [Calf Raise on Hack Squat Machine](../data/exercises/1466.yaml) | Wadenheben an der Hackenschmidt-Maschine | `Squat` | **`quads`** | `calves` | `gastrocnemius` |
| `1515` | [Leg Press Toe Press](../data/exercises/1515.yaml) | Wadenheben an der Beinpresse | `Leg Press` | **`quads`** | `calves` | `gastrocnemius` |
| `1735` | [Single-leg side glute press](../data/exercises/1735.yaml) | Einbeinige Beinpresse seitlich für das Gesäß | `Beinpresse` | **`quads`** | `glutes` | `gluteus_medius, gluteus_maximus` |
| `1906` | [Glute Bridge with Alternating Leg Extension](../data/exercises/1906.yaml) | Beckenheben mit abwechselnder Beinstreckung | `Leg Extension` | **`quads`** | `glutes` | `gluteus_maximus` |
| `2528` | [Squat Sky Reach Stretch](../data/exercises/2528.yaml) | Tiefe Kniebeuge mit Rotation (Sky Reach) | `Squat` | **`quads`** | `abs` | `obliques` |
| `570` | [Shoulder Shrug](../data/exercises/570.yaml) | Schulterzucken | `Shrug` | **`shoulders`** | `back` | `traps_upper` |
| `571` | [Barbell Shrug](../data/exercises/571.yaml) | Shrugs mit Langhantel | `Shrug` | **`shoulders`** | `back` | `traps_upper` |
| `572` | [Dumbbell Shrug](../data/exercises/572.yaml) | Shrugs mit Kurzhanteln | `Shrug` | **`shoulders`** | `back` | `traps_upper` |
| `575` | [Smith Machine Shrug](../data/exercises/575.yaml) | Shrugs an der Multipresse | `Shrug` | **`shoulders`** | `back` | `traps_upper` |
| `922` | [Seated Cable Mid Trap Shrug](../data/exercises/922.yaml) | Kabelzug-Shrugs sitzend (mittlerer Trapez) | `Shrug` | **`shoulders`** | `back` | `traps_middle, rhomboids` |
| `923` | [Lying Dumbbell Row and Seated Shrug](../data/exercises/923.yaml) | Kurzhantelrudern liegend & Shrugs sitzend | `Shrug` | **`shoulders`** | `back` | `latissimus_dorsi, traps_middle` |
| `1472` | [Cable Shrug-In](../data/exercises/1472.yaml) | Kabelzug-Shrugs eingedreht | `Shrug` | **`shoulders`** | `back` | `traps_upper` |
| `1496` | [Supinated Dumbbell Upper Chest Raise](../data/exercises/1496.yaml) | Kurzhantel-Frontheben supiniert für die obere Brust | `Frontheben` | **`shoulders`** | `chest` | `pecs_clavicular` |
| `1925` | [Barbell Silverback Shrug](../data/exercises/1925.yaml) | Silverback-Shrugs mit der Langhantel | `Shrug` | **`shoulders`** | `back` | `traps_upper` |
| `990` | [Kneeling Glute Kickback](../data/exercises/990.yaml) | Glute Kickback im Vierfüßlerstand | `Kickback` | **`triceps`** | `glutes` | `gluteus_maximus` |
| `1613` | [Rubber Band Glute Kickback](../data/exercises/1613.yaml) | Glute Kickback mit Widerstandsband | `Kickback` | **`triceps`** | `glutes` | `gluteus_maximus` |
| `1723` | [Glute Kickback (Machine)](../data/exercises/1723.yaml) | Glute Kickback an der Maschine | `Kickback` | **`triceps`** | `glutes` | `gluteus_maximus` |
