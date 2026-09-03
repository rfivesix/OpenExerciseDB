# Sprach-Diskrepanzbericht: EN vs. DE Widersprüche

## Methodik & Prüfkriterien
In Phase 2 wurden die sprachneutralen Fakten vereinheitlicht. Bei den Texten (`data/i18n/`) existieren jedoch historische Divergenzen zwischen den gepflegten Primärsprachen Englisch (`en`) und Deutsch (`de`).

Dieser Bericht prüft auf drei Ebenen:
1. **Gerätefamilien-Widersprüche im Titel** (z. B. Kurzhantel auf Englisch, aber Langhantel auf Deutsch).
2. **Bewegungsvektor-Widersprüche** (z. B. *Press* auf Englisch, aber *Rudern* auf Deutsch).
3. **Starke Asymmetrien in der Beschreibung** ($\ge 3,5\times$ Längenunterschied oder völlig fehlende deutsche Beschreibung bei bestehendem englischen Fachtext).

Insgesamt wurden **31 Übungen** mit Diskrepanzen identifiziert:

| ID | Name (EN) | Name (DE) | Gefundene Diskrepanz(en) |
|---|---|---|---|
| `20` | [Arnold Shoulder Press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/20.yaml) | Arnold Press | Große Asymmetrie: DE (44 Wörter) deutlich ausführlicher als EN (7 Wörter) |
| `51` | [Barbell Wrist Curl](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/51.yaml) | Handgelenkstreckung | Große Asymmetrie: EN (61 Wörter) deutlich ausführlicher als DE (16 Wörter) |
| `71` | [Single Leg Extension](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/71.yaml) | Beinstrecker Einbeinig | Vollständige Text-Diskrepanz: DE hat 56 Wörter Beschreibung, EN ist leer |
| `75` | [Benchpress Dumbbells](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/75.yaml) | Bankdrücken KH | Große Asymmetrie: EN (185 Wörter) deutlich ausführlicher als DE (48 Wörter) |
| `152` | [Chin Up](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/152.yaml) | Chin-ups | Große Asymmetrie: EN (71 Wörter) deutlich ausführlicher als DE (6 Wörter) |
| `165` | [Ball crunches](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/165.yaml) | Crunch am TRX Oder Auf Ball | Vollständige Text-Diskrepanz: DE hat 26 Wörter Beschreibung, EN ist leer |
| `177` | [Cycling](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/177.yaml) | Fahrrad fahren | Vollständige Text-Diskrepanz: EN hat 47 Wörter Beschreibung, DE ist leer |
| `256` | [Front Raises](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/256.yaml) | Frontheben am Kabel | Große Asymmetrie: EN (192 Wörter) deutlich ausführlicher als DE (44 Wörter) |
| `312` | [Incline Plank With Alternate Floor Touch](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/312.yaml) | Negativ Plank Mit Abwechselnden Fuß-Kontakt | Geräte-Widerspruch im Titel: Schrägbank (EN) vs. Negativ/Flachbank (DE) |
| `323` | [Cable Cross-over](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/323.yaml) | Kabelcross | Vollständige Text-Diskrepanz: EN hat 57 Wörter Beschreibung, DE ist leer |
| `346` | [Landmine press](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/346.yaml) | Landmine-Press, Einarmig | Vollständige Text-Diskrepanz: DE hat 49 Wörter Beschreibung, EN ist leer |
| `367` | [Leg Curls (standing)](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/367.yaml) | Beinbeuger Stehend | Vollständige Text-Diskrepanz: DE hat 53 Wörter Beschreibung, EN ist leer |
| `375` | [Leg Press on Hackenschmidt Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/375.yaml) | Kniebeuge an Hackenschmidtmaschine | Vollständige Text-Diskrepanz: DE hat 63 Wörter Beschreibung, EN ist leer |
| `454` | [Pike Push Ups](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/454.yaml) | Hecht-Liegestütze | Große Asymmetrie: DE (85 Wörter) deutlich ausführlicher als EN (12 Wörter) |
| `516` | [Front Wood Chop](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/516.yaml) | Rückenstrecker im Stehen | Vollständige Text-Diskrepanz: DE hat 36 Wörter Beschreibung, EN ist leer |
| `530` | [Run - Treadmill](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/530.yaml) | Laufen an Laufband | Große Asymmetrie: DE (27 Wörter) deutlich ausführlicher als EN (4 Wörter) |
| `537` | [Incline Bench Press - Dumbbell](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/537.yaml) | Schrägbankdrücken KH | Große Asymmetrie: EN (238 Wörter) deutlich ausführlicher als DE (49 Wörter) |
| `538` | [Incline Bench Press - Barbell](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/538.yaml) | Schrägbankdrücken LH | Große Asymmetrie: DE (54 Wörter) deutlich ausführlicher als EN (6 Wörter) |
| `539` | [Incline Bench Press - MP](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/539.yaml) | Schrägbankdrücken MP | Vollständige Text-Diskrepanz: DE hat 67 Wörter Beschreibung, EN ist leer |
| `556` | [Side Bends on Machine](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/556.yaml) | Seitliches Oberkörperbeugen am Gerät | Vollständige Text-Diskrepanz: DE hat 42 Wörter Beschreibung, EN ist leer |
| `566` | [Shoulder Press, Barbell](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/566.yaml) | Schulterdrücken LH | Große Asymmetrie: EN (41 Wörter) deutlich ausführlicher als DE (6 Wörter) |
| `575` | [Shrugs on Multipress](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/575.yaml) | Shrugs an der MP | Vollständige Text-Diskrepanz: DE hat 65 Wörter Beschreibung, EN ist leer |
| `577` | [Side Dumbbell Trunk Flexion](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/577.yaml) | Seitliches Oberkörperbeugen Mit KH | Große Asymmetrie: EN (47 Wörter) deutlich ausführlicher als DE (7 Wörter) |
| `595` | [Skipping - Standard](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/595.yaml) | Seilspringen | Vollständige Text-Diskrepanz: EN hat 26 Wörter Beschreibung, DE ist leer |
| `614` | [Squat Jumps](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/614.yaml) | Tiefe Hocksprünge | Große Asymmetrie: DE (23 Wörter) deutlich ausführlicher als EN (4 Wörter) |
| `630` | [Sumo Deadlift](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/630.yaml) | Sumo Kreuzheben | Große Asymmetrie: EN (153 Wörter) deutlich ausführlicher als DE (14 Wörter) |
| `632` | [Sumo Squats](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/632.yaml) | Sumo Kniebeuge | Große Asymmetrie: EN (80 Wörter) deutlich ausführlicher als DE (18 Wörter) |
| `655` | [Tricep Dumbbell Kickback](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/655.yaml) | Kick-Backs | Große Asymmetrie: EN (208 Wörter) deutlich ausführlicher als DE (49 Wörter) |
| `1479` | [Sit Up Elbow Thrust](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1479.yaml) | Sit-Ups (Ellenbogen zum Knie) | Große Asymmetrie: EN (54 Wörter) deutlich ausführlicher als DE (13 Wörter) |
| `1889` | [Decline Bench Leg Raise](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1889.yaml) | Beinheben auf der Schrägbank | Geräte-Widerspruch im Titel: Negativbank (EN) vs. Schräg/Flachbank (DE) |
| `1922` | [Seated Cable chest fly](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/1922.yaml) | Butterfly am Kabelzug | Große Asymmetrie: EN (85 Wörter) deutlich ausführlicher als DE (14 Wörter) |