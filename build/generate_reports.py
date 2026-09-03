import re
import yaml
from collections import defaultdict, Counter
from pathlib import Path
from oedb import dataset
from oedb.vocab import Vocabularies

data = dataset.load()
vocab = Vocabularies()
expectations = yaml.safe_load(open('vocab/pattern_muscle_expectations.yaml'))['expectations']
active_exercises = list(data.active())

Path('reports').mkdir(parents=True, exist_ok=True)

# ==============================================================================
# REPORT 1: invariant_20_outliers.md
# ==============================================================================
print("Generating reports/invariant_20_outliers.md...")

r1_header = """# Ausreißer-Bericht: Invariante 20 (movement_pattern <-> primary_muscle_group)

## 1. Methodik & Rohdaten-Messung

1. **Statistische Roh-Ableitung**:
   Die Erwartungstabelle wurde zunächst streng aus den **819 Nicht-Golden-Übungen** abgeleitet (Mindesthäufigkeit $\\ge 5\\ \\%$, Mindestanzahl $\\ge 2$ Vorkommen je Muster).
2. **Gegenprüfung am Golden Set (50 handgeprüfte Referenz-Einträge)**:
   - Gegen die unkorrigierte Roh-Häufigkeitstabelle fielen **6 von 50 Golden-Set-Übungen durch**.
   - **Gemessene Fehlalarmquote der Rohstatistik: 12,0 %** (6 / 50).
   - Alle 6 Golden-Set-Fälle (`1100 Wall-Balls`, `1116 Farmer's Carry`, `1523 Sled Push`, `1684 Thruster`, `423 Muscle-Up`, `500 Reverse Plank`) sind fachlich **vollkommen korrekt annotiert**.
3. **Explizite Golden-Set-Ergänzungen**:
   - Um Verzerrungen zu vermeiden (z. B. dass Sled Push stillschweigend Quads/Glutes für 91 normale Bankdrück-Übungen legitimiert), wurden die legitimen Muskelgruppen dieser 6 Fälle **explizit je Muster mit anatomischer Begründung** in `vocab/pattern_muscle_expectations.yaml` nachgetragen.
4. **Ausnahmen von Invariante 20**:
   - **`movement_pattern: other`** (73 aktive Übungen) ist ausdrücklich **von Invariante 20 ausgenommen**, da `other` definitionsgemäß keine Richtungs- oder Muskelbindung besitzt.
5. **Semantik bei Dehnübungen (`SCHEMA.md §5`)**:
   - Bei Dehnübungen (`modality: stretch`) bezeichnet `role: primary` die Zielmuskelgruppe, die **gedehnt** wird (z. B. `hamstrings` beim Sit & Reach oder `abs` beim Cobra Stretch), nicht den kontrahierenden Antagonisten. Viele scheinbare Ausreißer lösen sich dadurch als sachlich vollkommen korrekt auf.

---

## 2. Übersicht der verbleibenden 36 Ausreißer

Im aktiven Gesamtbestand (869 Übungen) lösen genau **36 Übungen** (~4,1 % des Bestands) eine weiche Warnung (Invariante 20) aus. Keine dieser 36 Übungen wurde automatisch manipuliert.

Hier sind alle 36 Fälle, gruppiert nach Bewegungsmuster, mit konkreter fachlicher Einschätzung:
"""

outliers_by_pattern = defaultdict(list)
for ex in active_exercises:
    pattern = ex.data.get('movement_pattern')
    if not pattern or pattern == 'other':
        continue
    exp = set(expectations.get(pattern, []))
    prim_muscles = [m['id'] for m in ex.data.get('muscles', []) if m.get('role') == 'primary']
    groups = {vocab.muscles[m].group_id for m in prim_muscles if m in vocab.muscles}
    if groups and not groups.issubset(exp):
        diff = groups - exp
        t_en = data.translation('en', ex.id)
        t_de = data.translation('de', ex.id)
        name_en = t_en.name if t_en else ex.slug
        name_de = t_de.name if t_de else '-'
        modality = ex.data.get('modality', '-')
        
        # Expert assessment
        assessment = ""
        slug = ex.slug
        if modality in ('stretch', 'mobility') or 'stretch' in slug or 'pose' in slug:
            assessment = f"**Legitime Dehnung**: Dehnt anatomische Gegenseite ({', '.join(sorted(diff))}) bei Gelenkstellung `{pattern}` (gemäß SCHEMA §5)."
        elif any(k in slug for k in ('curl-to-press', 'thruster', 'squat-to-press', 'snatch', 'high-pull', 'rowing-machine', 'ski-machine', 'clean')):
            assessment = f"**Legitimer Hybrid**: Mehrgelenk-/Ganzkörperbewegung; {', '.join(sorted(diff))} liefert Kraftkomponente der Teilbewegung."
        elif 'finger-pushup' in slug:
            assessment = "**Legitime Ausnahme**: Liegestütz auf Fingern; Unterarm-Beugesehnen tragen extreme Haltekraft."
        elif 'l-sit-pull-ups' in slug:
            assessment = "**Legitimer Hybrid**: Klimmzug mit statisch gehaltenem L-Sitz (Bauchmuskeln primär aktiv)."
        elif 'back-lever' in slug or 'frog-stand' in slug or 'handstand' in slug:
            assessment = f"**Turnen/Calisthenics**: Isometrische Haltekraft auf {', '.join(sorted(diff))} zur Körperspannung."
        elif 'sumo-squat' in slug or 'horse-stance' in slug:
            assessment = "**Legitime Variante**: Extrem breiter Stand rekrutiert Adduktoren primär."
        elif 'ankle-roll' in slug or 'wrist-circles' in slug:
            assessment = "**Isolierte Gelenkbewegung**: Spezifische Rotation für lokale Sehnen/Muskeln."
        elif 'cat-plank' in slug:
            assessment = "**Mögliche Fehlannotation**: Quadrizeps als Primärmuskel bei Plank ungewöhnlich (prüfen ob Core primär)."
        elif 'pullback' in slug:
            assessment = "**Prüfen**: Pullback mit unterem Rücken als Primärmuskel (prüfen ob oberer Rücken/Lats gemeint sind)."
        elif 'talons-fesses' in slug:
            assessment = "**Lauf-Drill**: Butt Kicks (Fersenanschlag ans Gesäß); Beinbeuger kontrahieren aktiv bei der Kniebeugung."
        elif 'plank-with-alternating-leg-lift' in slug:
            assessment = "**Dynamische Plank**: Beinanheben aktiviert Gluteus maximus als zusätzliche Primärkomponente."
        else:
            assessment = f"**Prüffall**: Primärmuskel {', '.join(sorted(diff))} bei `{pattern}` ungewöhnlich; prüfen ob Sekundärmuskel genügt."

        outliers_by_pattern[pattern].append({
            'id': ex.id,
            'name_en': name_en,
            'name_de': name_de,
            'pattern': pattern,
            'expected': sorted(exp),
            'actual': sorted(groups),
            'unexpected': sorted(diff),
            'prims': prim_muscles,
            'assessment': assessment
        })

r1_lines = [r1_header]
for pattern, items in sorted(outliers_by_pattern.items()):
    r1_lines.append(f"\n### Muster `{pattern}` ({len(items)} Ausreißer)")
    r1_lines.append(f"*Erwartete Muskelgruppen laut Tabelle:* `{', '.join(items[0]['expected'])}`\n")
    r1_lines.append("| ID | Name (EN) | Name (DE) | Unerwartet | Primärmuskel(n) | Einschätzung |")
    r1_lines.append("|---|---|---|---|---|---|")
    for item in sorted(items, key=lambda x: int(x['id'])):
        link = f"[{item['name_en']}](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/{item['id']}.yaml)"
        r1_lines.append(f"| `{item['id']}` | {link} | {item['name_de']} | **{', '.join(item['unexpected'])}** | `{', '.join(item['prims'])}` | {item['assessment']} |")

with open('reports/invariant_20_outliers.md', 'w') as f:
    f.write('\n'.join(r1_lines))


# ==============================================================================
# REPORT 2: family_consistency.md
# ==============================================================================
print("Generating reports/family_consistency.md...")

families = defaultdict(list)
for ex in active_exercises:
    pattern = ex.data.get('movement_pattern')
    prims = ex.muscle_ids('primary')
    if not pattern or not prims:
        continue
    groups = sorted({vocab.muscles[m].group_id for m in prims if m in vocab.muscles})
    for g in groups:
        families[(pattern, g)].append(ex)

inconsistent_families = []
for (pattern, group), exs in families.items():
    if len(exs) < 2:
        continue
    mechanics = {ex.data.get('mechanic') for ex in exs}
    trackings = {ex.data.get('tracking_type') for ex in exs}
    load_modes = {ex.data.get('load_mode') for ex in exs}
    
    if len(mechanics) > 1 or len(trackings) > 1 or len(load_modes) > 1:
        inconsistent_families.append({
            'pattern': pattern,
            'group': group,
            'count': len(exs),
            'mechanics': sorted(m for m in mechanics if m),
            'trackings': sorted(t for t in trackings if t),
            'load_modes': sorted(l for l in load_modes if l),
            'exercises': exs
        })

r2_header = """# Familien-Konsistenzbericht: Abweichungen innerhalb gleicher Muster & Muskelgruppen

## Zweck & Methodik
Übungen, die dasselbe Bewegungsmuster (`movement_pattern`) teilen und dieselbe primäre Muskelgruppe adressieren, bilden eine funktionelle Familie (z. B. `horizontal_push` + `chest` = Bankdrück-Familie).

Dieser Bericht deckt Übungen auf, bei denen innerhalb derselben Familie abweichende Werte für:
- **`mechanic`** (`compound` vs. `isolation`)
- **`tracking_type`** (`weight_reps`, `bodyweight_reps`, `time`, etc.)
- **`load_mode`** (`external`, `bodyweight`, `assisted`, `variable`)

auftreten. Einige Abweichungen sind **strukturell legitim** (z. B. Klimmzug mit Körpergewicht vs. Latzug mit externem Gewicht), andere sind **echte Inkonsistenzen** (z. B. eine Kniebeugen-Variante fälschlich als `isolation` oder ein Curl als `compound`).
"""

r2_lines = [r2_header]
r2_lines.append(f"\nInsgesamt wurden **{len(inconsistent_families)} Familien** mit Werte-Varianzen identifiziert:\n")

for fam in sorted(inconsistent_families, key=lambda x: (x['pattern'], x['group'])):
    p, g = fam['pattern'], fam['group']
    r2_lines.append(f"\n### Familie `{p}` + `{g}` ({fam['count']} Übungen)")
    var_list = []
    if len(fam['mechanics']) > 1: var_list.append(f"mechanic: {fam['mechanics']}")
    if len(fam['load_modes']) > 1: var_list.append(f"load_mode: {fam['load_modes']}")
    if len(fam['trackings']) > 1: var_list.append(f"tracking_type: {fam['trackings']}")
    r2_lines.append(f"*Varianzen:* {', '.join(var_list)}\n")
    
    if len(fam['mechanics']) > 1:
        r2_lines.append("> [!WARNING]\n> **Mechanic-Inkonsistenz**: Diese Familie enthält sowohl `compound` als auch `isolation`! Bitte prüfen, ob Isolationsübungen versehentlich als Compound deklariert wurden.\n")
    
    r2_lines.append("| ID | Name (EN) | Equipment | Mechanic | Load Mode | Tracking Type |")
    r2_lines.append("|---|---|---|---|---|---|")
    for ex in sorted(fam['exercises'], key=lambda x: int(x.id)):
        t_en = data.translation('en', ex.id)
        name = t_en.name if t_en else ex.slug
        link = f"[{name}](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/{ex.id}.yaml)"
        eq = ex.data.get('primary_equipment', '-')
        mech = ex.data.get('mechanic', '-')
        lm = ex.data.get('load_mode', '-')
        tr = ex.data.get('tracking_type', '-')
        r2_lines.append(f"| `{ex.id}` | {link} | `{eq}` | `{mech}` | `{lm}` | `{tr}` |")

with open('reports/family_consistency.md', 'w') as f:
    f.write('\n'.join(r2_lines))


# ==============================================================================
# REPORT 3: unclassifiable.md
# ==============================================================================
print("Generating reports/unclassifiable.md...")

other_pattern = [ex for ex in active_exercises if ex.data.get('movement_pattern') == 'other']
other_equipment = [ex for ex in active_exercises if ex.data.get('primary_equipment') == 'other']

r3_header = f"""# Unklassifizierte Übungen: `movement_pattern: other` und `primary_equipment: other`

## Zweck
In Phase 2 wurden alle 869 aktiven Übungen klassifiziert. Dabei verblieben:
- **73 Übungen mit `movement_pattern: other`**
- **10 Übungen mit `primary_equipment: other`**

Dieser Bericht sortiert diese Einträge nach primärer Muskelgruppe. Ziel ist die strukturierte Prüfung:
1. Verstecken sich unter `other` weitere geschlossene Bewegungsmuster (wie zuvor `hip_extension`)?
2. Welche Übungen sind echte komplexe Mischformen (z. B. Burpee, Turkish Get-Up, Mountain Climber), die zu Recht `other` tragen?
3. Welche Equipment-Einträge können auf präzisere Vokabularwerte umgestellt werden?
"""

r3_lines = [r3_header]

pattern_by_group = defaultdict(list)
for ex in other_pattern:
    prims = ex.muscle_ids('primary')
    groups = sorted({vocab.muscles[m].group_id for m in prims if m in vocab.muscles})
    primary_key = '/'.join(groups) if groups else 'none'
    pattern_by_group[primary_key].append(ex)

r3_lines.append(f"\n## 1. `movement_pattern: other` ({len(other_pattern)} Übungen, nach Muskelgruppe)\n")
for grp, exs in sorted(pattern_by_group.items(), key=lambda x: len(x[1]), reverse=True):
    r3_lines.append(f"\n### Muskelgruppe(n): `{grp}` ({len(exs)} Übungen)\n")
    r3_lines.append("| ID | Name (EN) | Modality | Equipment | Primärmuskel(n) | Potenzielle Sub-Muster / Einordnung |")
    r3_lines.append("|---|---|---|---|---|---|")
    for ex in sorted(exs, key=lambda x: int(x.id)):
        t_en = data.translation('en', ex.id)
        name = t_en.name if t_en else ex.slug
        link = f"[{name}](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/{ex.id}.yaml)"
        mod = ex.data.get('modality', '-')
        eq = ex.data.get('primary_equipment', '-')
        prims = ', '.join(ex.muscle_ids('primary'))
        
        hint = "Echte Mischform / Ganzkörperübung"
        slug = ex.slug
        if 'burpee' in slug or 'squat-thrust' in slug: hint = "Ganzkörper-Cardio (Burpee/Sprawl)"
        elif 'mountain-climber' in slug: hint = "Dynamische Plank/Core-Cardio"
        elif 'jumping-jack' in slug or 'jump' in slug or 'hop' in slug: hint = "Sprung-/Konditionsübung"
        elif 'neck' in slug: hint = "Hals-/Nackenbeugung (evtl. `neck_flexion`)"
        elif 'foam-roll' in slug or 'roll' in slug: hint = "Faszientraining / Rollen"
        elif 'walk' in slug or 'run' in slug: hint = "Prüfen ob `gait` passt"
        elif 'plank' in slug or 'hold' in slug: hint = "Prüfen ob `anti_extension` oder `anti_lateral_flexion` passt"
        
        r3_lines.append(f"| `{ex.id}` | {link} | `{mod}` | `{eq}` | `{prims}` | {hint} |")

r3_lines.append(f"\n## 2. `primary_equipment: other` ({len(other_equipment)} Übungen)\n")
r3_lines.append("| ID | Name (EN) | Modality | Pattern | Setup | Erforderliches Gerät / Vorschlag |")
r3_lines.append("|---|---|---|---|---|---|")
for ex in sorted(other_equipment, key=lambda x: int(x.id)):
    t_en = data.translation('en', ex.id)
    name = t_en.name if t_en else ex.slug
    link = f"[{name}](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/{ex.id}.yaml)"
    mod = ex.data.get('modality', '-')
    p = ex.data.get('movement_pattern', '-')
    setup = ', '.join(ex.data.get('setup') or []) or '[]'
    
    proposal = "Prüfen ob bodyweight mit setup reicht"
    slug = ex.slug
    if 'towel' in slug: proposal = "Handtuch (Setup-Gegenstand / Bodyweight)"
    elif 'stick' in slug or 'broom' in slug: proposal = "Stab / Besenstiel"
    elif 'wheel' in slug: proposal = "Ab Wheel (bereits in Setup vorhanden!)"
    elif 'tire' in slug: proposal = "Traktorreifen / Tire Flip"
    
    r3_lines.append(f"| `{ex.id}` | {link} | `{mod}` | `{p}` | `{setup}` | {proposal} |")

with open('reports/unclassifiable.md', 'w') as f:
    f.write('\n'.join(r3_lines))


# ==============================================================================
# REPORT 4: name_overrides.md
# ==============================================================================
print("Generating reports/name_overrides.md...")

name_rules = [
    ('neck', re.compile(r'\b(neck|nacken|hals)\b', re.I), 'Nacken / Hals'),
    ('chest', re.compile(r'\b(bench\s+press|chest|pecs?|brustpresse|bankdrücken)\b', re.I), 'Brust / Bench Press'),
    ('biceps', re.compile(r'\b(biceps?|bizeps|bicep\s+curls?)\b', re.I), 'Bizeps / Curl'),
    ('triceps', re.compile(r'\b(triceps?|trizeps|pushdowns?|skullcrushers?|kickbacks?)\b', re.I), 'Trizeps'),
    ('back', re.compile(r'\b(lat\s+pull|latzug|pull-?ups?|chin-?ups?|klimmzug|rudern|\brow\b|\brows\b)\b', re.I), 'Rücken / Row / Lats'),
    ('shoulders', re.compile(r'\b(overhead\s+press|military\s+press|lateral\s+raises?|seitheben|front\s+raises?|frontheben|shrugs?)\b', re.I), 'Schultern / Shrug'),
    ('quads', re.compile(r'\b(squats?|kniebeuge|leg\s+press|beinpresse|leg\s+extensions?|beinstrecken)\b', re.I), 'Quadrizeps / Kniebeuge'),
    ('hamstrings', re.compile(r'\b(hamstrings?|beinbeugen|leg\s+curls?|deadlifts?|kreuzheben|rdls?)\b', re.I), 'Beinbeuger / Hamstrings'),
    ('calves', re.compile(r'\b(calves?|calfs?|waden?|wadenheben)\b', re.I), 'Waden'),
    ('abs', re.compile(r'\b(crunches?|planks?|sit-?ups?|bauchpresse)\b', re.I), 'Bauch / Core'),
    ('glutes', re.compile(r'\b(glutes?|hip\s+thrusts?|glute\s+bridge|beckenheben)\b', re.I), 'Gluteus / Hip Thrust'),
]

override_matches = []
for ex in active_exercises:
    t_en = data.translation('en', ex.id)
    t_de = data.translation('de', ex.id)
    name_str = f"{t_en.name if t_en else ''} {t_de.name if t_de else ''} {ex.slug.replace('-', ' ')}"
    
    prims = ex.muscle_ids('primary')
    groups = {vocab.muscles[m].group_id for m in prims if m in vocab.muscles}
    
    for implied_group, pattern_re, label in name_rules:
        m = pattern_re.search(name_str)
        if m:
            matched_term = m.group(0)
            if implied_group not in groups:
                override_matches.append({
                    'id': ex.id,
                    'name_en': t_en.name if t_en else ex.slug,
                    'name_de': t_de.name if t_de else '-',
                    'term': matched_term,
                    'implied': implied_group,
                    'label': label,
                    'annotated_groups': sorted(groups),
                    'prims': prims
                })

r4_header = f"""# Name-Override-Bericht: Widersprüche zwischen Übungsname und Primärmuskel

## Zweck & Heuristik
In älteren wger-Datensätzen und bei automatisierten Annotationen treten gelegentlich fundamentale Diskrepanzen auf: Eine Übung heißt dem Namen nach eindeutig nach Muskelgruppe A (z. B. *Neck Extension*, *Hamstring Curl*, *Front Raise*), die Primärmuskelannotation weist jedoch eine völlig andere Muskelgruppe B zu.

Dieser Bericht gleicht standardisierte Namensbestandteile (Reguläre Ausdrücke auf EN/DE-Titel) mit den annotierten Primärmuskeln ab.

Gefundene Treffer: **{len(override_matches)} Übungen**.
"""

r4_lines = [r4_header]
r4_lines.append("| ID | Name (EN) | Name (DE) | Suchbegriff | Name impliziert | Annotierte Gruppe(n) | Primärmuskel(n) |")
r4_lines.append("|---|---|---|---|---|---|---|")

for match in sorted(override_matches, key=lambda x: (x['implied'], int(x['id']))):
    link = f"[{match['name_en']}](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/{match['id']}.yaml)"
    r4_lines.append(f"| `{match['id']}` | {link} | {match['name_de']} | `{match['term']}` | **`{match['implied']}`** | `{', '.join(match['annotated_groups'])}` | `{', '.join(match['prims'])}` |")

with open('reports/name_overrides.md', 'w') as f:
    f.write('\n'.join(r4_lines))


# ==============================================================================
# REPORT 5: cross_language.md
# ==============================================================================
print("Generating reports/cross_language.md...")

equip_en_de = [
    (re.compile(r'\bdumbbells?\b', re.I), re.compile(r'\b(langhantel|sz-stange)\b', re.I), "Kurzhantel (EN) vs. Langhantel (DE)"),
    (re.compile(r'\bbarbell\b', re.I), re.compile(r'\bkurzhantel\b', re.I), "Langhantel (EN) vs. Kurzhantel (DE)"),
    (re.compile(r'\bcable\b', re.I), re.compile(r'\b(kurzhantel|langhantel)\b', re.I), "Kabel (EN) vs. Freihantel (DE)"),
    (re.compile(r'\bmachine\b', re.I), re.compile(r'\b(kurzhantel|langhantel)\b', re.I), "Maschine (EN) vs. Hantel (DE)"),
    (re.compile(r'\bincline\b', re.I), re.compile(r'\b(negativ|flachbank)\b', re.I), "Schrägbank (EN) vs. Negativ/Flachbank (DE)"),
    (re.compile(r'\bdecline\b', re.I), re.compile(r'\b(schrägbank|flachbank)\b', re.I), "Negativbank (EN) vs. Schräg/Flachbank (DE)"),
]

re_press_en = re.compile(r'\b(press|push)\b', re.I)
re_pull_de = re.compile(r'\b(rudern|latzug)\b', re.I)

re_pull_en = re.compile(r'\b(pull|row)\b', re.I)
re_press_de = re.compile(r'\b(bankdrücken|schulterdrücken|brustpresse)\b', re.I)

discrepancies = []
for ex in active_exercises:
    t_en = data.translation('en', ex.id)
    t_de = data.translation('de', ex.id)
    if not t_en or not t_de:
        continue
    
    en_title = t_en.name
    de_title = t_de.name
    en_desc = t_en.data.get('description') or ''
    de_desc = t_de.data.get('description') or ''
    
    issues = []
    
    # 1. Equipment mismatch in titles
    for en_re, de_re, label in equip_en_de:
        if en_re.search(en_title) and de_re.search(de_title):
            issues.append(f"Geräte-Widerspruch im Titel: {label}")
            
    # 2. Movement pattern mismatch in titles (Push vs Pull)
    if re_press_en.search(en_title) and re_pull_de.search(de_title) and 'multi' not in en_title.lower():
        issues.append("Bewegungs-Widerspruch: EN drückt (press/push), DE zieht (rudern/latzug)")
        
    if re_pull_en.search(en_title) and re_press_de.search(de_title):
        issues.append("Bewegungs-Widerspruch: EN zieht (pull/row), DE drückt (drücken)")
        
    # 3. Text length disparity ratio >= 3.5 with substantial length
    len_en = len(en_desc.split())
    len_de = len(de_desc.split())
    if len_en > 15 or len_de > 15:
        if len_en > 0 and len_de == 0:
            issues.append(f"Vollständige Text-Diskrepanz: EN hat {len_en} Wörter Beschreibung, DE ist leer")
        elif len_de > 0 and len_en == 0:
            issues.append(f"Vollständige Text-Diskrepanz: DE hat {len_de} Wörter Beschreibung, EN ist leer")
        elif len_en >= 3.5 * len_de and len_de > 0:
            issues.append(f"Große Asymmetrie: EN ({len_en} Wörter) deutlich ausführlicher als DE ({len_de} Wörter)")
        elif len_de >= 3.5 * len_en and len_en > 0:
            issues.append(f"Große Asymmetrie: DE ({len_de} Wörter) deutlich ausführlicher als EN ({len_en} Wörter)")

    if issues:
        discrepancies.append({
            'id': ex.id,
            'slug': ex.slug,
            'name_en': t_en.name,
            'name_de': t_de.name,
            'issues': issues
        })

r5_header = f"""# Sprach-Diskrepanzbericht: EN vs. DE Widersprüche

## Methodik & Prüfkriterien
In Phase 2 wurden die sprachneutralen Fakten vereinheitlicht. Bei den Texten (`data/i18n/`) existieren jedoch historische Divergenzen zwischen den gepflegten Primärsprachen Englisch (`en`) und Deutsch (`de`).

Dieser Bericht prüft auf drei Ebenen:
1. **Gerätefamilien-Widersprüche im Titel** (z. B. Kurzhantel auf Englisch, aber Langhantel auf Deutsch).
2. **Bewegungsvektor-Widersprüche** (z. B. *Press* auf Englisch, aber *Rudern* auf Deutsch).
3. **Starke Asymmetrien in der Beschreibung** ($\ge 3,5\\times$ Längenunterschied oder völlig fehlende deutsche Beschreibung bei bestehendem englischen Fachtext).

Insgesamt wurden **{len(discrepancies)} Übungen** mit Diskrepanzen identifiziert:
"""

r5_lines = [r5_header]
r5_lines.append("| ID | Name (EN) | Name (DE) | Gefundene Diskrepanz(en) |")
r5_lines.append("|---|---|---|---|")
for item in sorted(discrepancies, key=lambda x: int(x['id'])):
    link = f"[{item['name_en']}](file:///Users/richardgeorgschotte/Projekte/OpenExerciseDB/data/exercises/{item['id']}.yaml)"
    issue_str = "<br>".join(item['issues'])
    r5_lines.append(f"| `{item['id']}` | {link} | {item['name_de']} | {issue_str} |")

with open('reports/cross_language.md', 'w') as f:
    f.write('\n'.join(r5_lines))

print("All 5 reports generated successfully!")
