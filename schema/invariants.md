# Invarianten (CI-Gate)

Diese Regeln laufen bei jedem Push. Sie sind der eigentliche Qualitätsmechanismus
— sie fangen den Großteil des KI-Unsinns automatisch ab, sodass der menschliche
Review sich auf das konzentriert, was eine Maschine nicht entscheiden kann.

## Hart und weich

Die Regeln sind nicht gleich viel wert, und sie so zu behandeln hat Schaden
angerichtet.

**HART** (1, 2, 3, 3b, 4, 5, 6, 7, 8, 9, 10, 17, 21, 22, 23, 24, 25) sind
strukturell und referenziell: eine ID zeigt ins Leere, ein Vokabularwert
existiert nicht, ein Muskel steht zweimal da. Dafür gibt es keine legitime
Ausnahme, und ein Verstoß blockiert.

**WEICH** (11, 12, 13, 14, 15, 20) sind Plausibilitätsregeln. Sie
formulieren Korrelationen, keine Gesetze. „Cardio wird nicht in Wiederholungen
geloggt" stimmt meistens — aber Burpees. „Verbundübung hat mindestens zwei
Muskeln" stimmt meistens — aber es gibt Grenzfälle.

**Der Schaden einer zu strengen Regel ist nicht der Fehlalarm.** Ein Fehlalarm
ist sichtbar. Der Schaden ist die still verbogene Annotation: das Ergebnis
wäre eine grüne CI und ein falscher Wert in den Daten — genau die Sorte
Fehler, die dieses Regelwerk verhindern soll.

Eine weiche Invariante wird deshalb pro Übung entschärfbar:

```yaml
exceptions:
  invariant_12: "Squat Thrust / Burpee ist eine Cardio-/Ganzkörperübung, wird aber nach Wiederholungen geloggt."
```

Dafür gilt:

- Eine Ausnahme auf eine **harte** Invariante ist selbst ein Fehler.
- Eine Ausnahme **ohne Begründungstext** ist ein Fehler.
- Eine Ausnahme, die **gar nicht greift**, ist eine Warnung. Sonst sammeln sich
  Karteileichen an, die niemand mehr zuordnen kann.
- `build/validate.py` zählt am Ende pro weicher Invariante, wie oft sie gefeuert
  hat und wie oft sie entschärft wurde. **Häufung ist ein Signal, dass die Regel
  falsch ist und nicht die Daten.**

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

Alles hier ist **weich**, sofern nicht anders vermerkt: entschärfbar über
`exceptions`, mit Begründung.

8. **(hart)** Mindestens ein Muskel mit `role: primary`.
9. **(hart)** Kein Muskel doppelt; kein Muskel gleichzeitig primary und secondary.
10. **(hart)** Kein Muskel-Knoten zusammen mit einem seiner Vorfahren oder Nachfahren
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
17. **(hart)** `supports_added_weight: true` ⇒ `tracking_type` ∈
    {`bodyweight_reps`, `time`}.
18. *(gestrichen)* Die Regel lautete `movement_pattern anti_* ⇒ tracking_type ∈ {time, time_weight}`.
    Da `anti_*` beschreibt, WOGEGEN gearbeitet wird (und nicht ob gehalten oder
    bewegt wird), ist die Vorhersage des Logging-Typs prinzipiell nicht möglich
    (Rollouts, Pallof Press, Walkouts etc. sind dynamisch). Die Information
    steckt bereits in `tracking_type`.
19. *(strukturell erfüllt)* Die Regel lautete „`movement_pattern` passt zu
    `force_vector`". `force_vector` wird nicht mehr annotiert, sondern vom Build
    aus `force_vector_by_pattern` in `vocab/classification.yaml` abgeleitet — ein
    Verstoß ist damit nicht mehr formulierbar. Die Regel ist nicht abgeschafft,
    sie ist in die Datenstruktur gewandert, und das ist die bessere Sorte
    Invariante: eine, die man nicht brechen kann, statt einer, die man prüft.
20. Primärmuskel-Gruppe muss zum `movement_pattern` passen — Tabelle in
    `vocab/pattern_muscle_expectations.yaml`. Jede Primärmuskelgruppe einer Übung
    wird gegen die für das Muster erwarteten Gruppen geprüft. `movement_pattern: other`
    ist von der Prüfung ausgenommen. Verstoß ist eine **Warnung**, kein Fehler:
    Ausnahmen existieren, aber jede will einmal angeschaut werden.

## Aus `load_mode`

24. **(hart)** `supports_added_weight: true` ⇒ `load_mode: bodyweight`. Etwas
    dazuzuladen setzt voraus, dass die Grundform das eigene Körpergewicht ist.
25. **(hart)** `load_mode: assisted` ⇒ `primary_equipment` ∈ {`machine`,
    `resistance_band`}. Entlastung erzeugt entweder eine Maschine oder ein Band.

Mehr nicht. Der Rest der denkbaren Regeln um `load_mode` sind Korrelationen, und
Korrelationen zu Gesetzen zu machen war der Fehler, der diese Aufteilung nötig
gemacht hat.

## Regression

21. Kein `status: active` verschwindet zwischen zwei Releases, ohne dass ein
    Alias oder `merged_into` auf einen Nachfolger zeigt.
22. Die Gesamtzahl aktiver Übungen fällt nie um mehr als 5 % gegenüber dem
    letzten Release (Schwelle wie `WGER_FAIL_ON_REMOVED_THRESHOLD` heute).
23. Das Golden Set (`test/golden/*.yaml`, ~50 handgeprüfte Übungen) stimmt
    feldweise überein. Läuft vor jedem KI-Batch als Eval für Prompt-Änderungen.
