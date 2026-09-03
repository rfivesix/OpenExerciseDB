# Invarianten (CI-Gate)

Diese Regeln laufen bei jedem Push. Sie sind der eigentliche Qualitätsmechanismus
— sie fangen den Großteil des KI-Unsinns automatisch ab, sodass der menschliche
Review sich auf das konzentriert, was eine Maschine nicht entscheiden kann.

## Struktur

1. Jede Datei unter `data/exercises/` validiert gegen `exercise.schema.json`.
2. Jeder Vokabular-Wert existiert in der zugehörigen `vocab/*.yaml`.
3. `slug` ist global eindeutig; `id` ist global eindeutig.
3b. **IDs innerhalb von `vocab/muscles.yaml` sind ebenenübergreifend eindeutig.**
    Gruppe, Muskel und Kopf teilen sich im Build eine Tabelle mit einem
    Primärschlüssel — eine Gruppe `hamstrings` und ein Muskel `hamstrings`
    dürfen also nicht beide existieren. Dieselbe Regel gilt in `equipment.yaml`
    über `primary_equipment` und `setup` hinweg.
4. Jede in `vocab/languages.yaml` als `curated` markierte Sprache hat für jede
   `status: active`-Übung eine Datei unter `data/i18n/<lang>/`.
5. Jede `data/i18n/<lang>/<id>.yaml` hat ein `data/exercises/<id>.yaml`.
6. `status: merged` ⇒ `merged_into` gesetzt, Ziel existiert, Ziel ist `active`.
7. Kein Alias zeigt auf eine ID, die selbst ein Alias ist (keine Ketten).

## Inhaltliche Plausibilität

8. Mindestens ein Muskel mit `role: primary`.
9. Kein Muskel doppelt; kein Muskel gleichzeitig primary und secondary.
10. Kein Muskel-Knoten zusammen mit einem seiner Vorfahren oder Nachfahren
    (`latissimus_dorsi` + `back` ist redundant, `trapezius` + `traps_upper` auch).
11. `primary_equipment: bodyweight` ⇒ kein Krafthantel-Setup in `setup`
    (`squat_rack`, `power_rack`, `cable_tower`, `landmine` verboten).
12. `modality: cardio` ⇒ `tracking_type` ∈ {`time`, `distance_time`, `distance_only`}.
13. `modality: strength` ⇒ `tracking_type` ∉ {`distance_only`}.
14. `mechanic: isolation` ⇒ höchstens 2 primäre Muskeln.
15. `mechanic: compound` ⇒ mindestens 2 beteiligte Muskeln insgesamt.
16. *(gestrichen)* Die Regel lautete `supports_assistance: true ⇒
    primary_equipment: bodyweight` — und war die Ursache des Fehlers, den sie
    verhindern sollte. Sie sperrte die Aussage „wird unterstützt" auf
    Körpergewichtsübungen und erzwang damit für die Assistenzmaschine die
    sachlich falsche Antwort. `supports_assistance` ist ersatzlos entfallen;
    was gemeint war, sagt jetzt `load_mode: assisted` (Invariante 25).
17. `supports_added_weight: true` ⇒ `tracking_type` ∈ {`bodyweight_reps`, `time`}.
18. `force_vector: static` ⇒ `tracking_type` ∈ {`time`, `time_weight`}.
19. `movement_pattern` passt zu `force_vector`
    (`*_push` ⇒ `push`, `*_pull` ⇒ `pull`, `anti_*` ⇒ `static`).
20. Primärmuskel-Gruppe muss zum `movement_pattern` passen — Tabelle in
    `vocab/pattern_muscle_expectations.yaml`. Verstoß ist eine **Warnung**,
    kein Fehler: Ausnahmen existieren, aber jede will einmal angeschaut werden.

## Regression

21. Kein `status: active` verschwindet zwischen zwei Releases, ohne dass ein
    Alias oder `merged_into` auf einen Nachfolger zeigt.
22. Die Gesamtzahl aktiver Übungen fällt nie um mehr als 5 % gegenüber dem
    letzten Release (Schwelle wie `WGER_FAIL_ON_REMOVED_THRESHOLD` heute).
23. Das Golden Set (`test/golden/*.yaml`, ~50 handgeprüfte Übungen) stimmt
    feldweise überein. Läuft vor jedem KI-Batch als Eval für Prompt-Änderungen.
