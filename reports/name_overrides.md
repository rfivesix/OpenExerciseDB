# Name-Override-Bericht: Widersprüche zwischen Übungsname und Primärmuskel

## Zweck & Heuristik
In älteren wger-Datensätzen und bei automatisierten Annotationen treten gelegentlich fundamentale Diskrepanzen auf: Eine Übung heißt dem Namen nach eindeutig nach Muskelgruppe A (z. B. *Neck Extension*, *Hamstring Curl*, *Front Raise*), die Primärmuskelannotation weist jedoch eine völlig andere Muskelgruppe B zu.

Dieser Bericht gleicht standardisierte Namensbestandteile (Reguläre Ausdrücke auf EN/DE-Titel) mit den annotierten Primärmuskeln ab.

Gefundene Treffer: **29 Übungen**.

| ID | Name (EN) | Name (DE) | Suchbegriff | Name impliziert | Annotierte Gruppe(n) | Primärmuskel(n) |
|---|---|---|---|---|---|---|
| `500` | [Reverse Plank](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/500.yaml) | Reverse Plank | `Plank` | **`abs`** | `glutes, lower_back` | `erector_spinae, gluteus_maximus` |
| `349` | [Lateral Rows on Cable, One Armed](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/349.yaml) | Seitheben am Kabel, Einarmig | `Rows` | **`back`** | `shoulders` | `delt_lateral` |
| `1227` | [Dumbbell rear delt row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1227.yaml) | Kurzhantel-Rudern für die hintere Schulter | `row` | **`back`** | `shoulders` | `delt_posterior` |
| `76` | [Bench Press Narrow Grip](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/76.yaml) | Bankdrücken Eng | `Bench Press` | **`chest`** | `triceps` | `triceps_brachii` |
| `1136` | [Neutral-grip chest pulldown](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1136.yaml) | Latzug zur Brust mit neutralem Griff | `chest` | **`chest`** | `back` | `latissimus_dorsi, teres_major` |
| `1283` | [Incline Chest-Supported Dumbbell Row](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1283.yaml) | Schrägbank-Kurzhantelrudern mit Brustauflage | `Chest` | **`chest`** | `back` | `latissimus_dorsi, rhomboids` |
| `1452` | [Knee to Chest Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1452.yaml) | Knie-zur-Brust-Dehnung | `Chest` | **`chest`** | `glutes` | `gluteus_maximus` |
| `1775` | [Pec deck rear delt fly](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1775.yaml) | Reverse Butterfly für die hintere Schulter | `Pec` | **`chest`** | `shoulders` | `delt_posterior` |
| `1825` | [Chest-Supported Rear Delt Raise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1825.yaml) | Reverse Flys für die hintere Schulter mit Brustauflage | `Chest` | **`chest`** | `shoulders` | `delt_posterior` |
| `2478` | [Glute-Ham Raise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2478.yaml) | - | `Glute` | **`glutes`** | `hamstrings` | `hamstring_complex` |
| `189` | [Deficit Deadlift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/189.yaml) | Defizit Kreuzheben | `Deadlift` | **`hamstrings`** | `glutes, lower_back` | `gluteus_maximus, erector_spinae` |
| `484` | [Rack Deadlift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/484.yaml) | Rack Deadlift | `Deadlift` | **`hamstrings`** | `glutes, lower_back` | `gluteus_maximus, erector_spinae` |
| `1612` | [kettlebell sumo deadlift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1612.yaml) | Sumo-Kreuzheben mit Kettlebell | `deadlift` | **`hamstrings`** | `adductors, glutes` | `gluteus_maximus, hip_adductors` |
| `1717` | [Neck extension](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1717.yaml) | - | `Neck` | **`neck`** | `triceps` | `triceps_brachii` |
| `146` | [Calf Press Using Leg Press Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/146.yaml) | Wadendrücken an Beinpresse | `Leg Press` | **`quads`** | `calves` | `gastrocnemius` |
| `1466` | [Calf Raise using Hack Squat Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1466.yaml) | - | `Squat` | **`quads`** | `calves` | `gastrocnemius` |
| `1515` | [Leg Press Toe Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1515.yaml) | - | `Leg Press` | **`quads`** | `calves` | `gastrocnemius` |
| `2528` | [Squat Sky Reach Stretch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/2528.yaml) | - | `Squat` | **`quads`** | `abs` | `obliques` |
| `570` | [Shoulder Shrug](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/570.yaml) | Schulterzucken | `Shrug` | **`shoulders`** | `back` | `traps_upper` |
| `571` | [Shrugs, Barbells](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/571.yaml) | Shrugs LH | `Shrugs` | **`shoulders`** | `back` | `traps_upper` |
| `572` | [Shrugs, Dumbbells](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/572.yaml) | Shrugs KH | `Shrugs` | **`shoulders`** | `back` | `traps_upper` |
| `575` | [Shrugs on Multipress](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/575.yaml) | Shrugs an der MP | `Shrugs` | **`shoulders`** | `back` | `traps_upper` |
| `922` | [Seated Cable Mid Trap Shrug](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/922.yaml) | - | `Shrug` | **`shoulders`** | `back` | `traps_middle, rhomboids` |
| `923` | [Lying Dumbbell Row SS Seated Shrug](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/923.yaml) | - | `Shrug` | **`shoulders`** | `back` | `latissimus_dorsi, traps_middle` |
| `1472` | [Cable Shrug-In](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1472.yaml) | - | `Shrug` | **`shoulders`** | `back` | `traps_upper` |
| `1925` | [Barbell Silverback Shrug](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1925.yaml) | Langhantel-Silverback-Shrug | `Shrug` | **`shoulders`** | `back` | `traps_upper` |
| `990` | [Kneeling kickbacks](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/990.yaml) | Kniende Rückschläge | `kickbacks` | **`triceps`** | `glutes` | `gluteus_maximus` |
| `1613` | [rubber band glute kickback](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1613.yaml) | Glute Kickback mit Widerstandsband | `kickback` | **`triceps`** | `glutes` | `gluteus_maximus` |
| `1723` | [Glute Kickback (Machine)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1723.yaml) | - | `Kickback` | **`triceps`** | `glutes` | `gluteus_maximus` |