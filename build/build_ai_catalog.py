#!/usr/bin/env python3
"""Export a compact exercise catalog and a no-JavaScript lookup page from SQLite."""

from __future__ import annotations

import html
import json
import sqlite3
from pathlib import Path
from typing import Any


def export_catalog(database: Path, output: Path) -> None:
    connection = sqlite3.connect(database)
    connection.row_factory = sqlite3.Row
    meta = {row["key"]: row["value"] for row in connection.execute("SELECT key, value FROM metadata")}

    def name_map(rows: list[sqlite3.Row]) -> dict[str, str]:
        return {row["language_code"]: row["name"] for row in rows if row["name"]}

    muscle_names = {row["muscle_id"]: row["name"] for row in connection.execute(
        "SELECT muscle_id, name FROM muscle_translations WHERE language_code = 'en'"
    )}
    equipment_names = {row["equipment_id"]: row["name"] for row in connection.execute(
        "SELECT equipment_id, name FROM equipment_translations WHERE language_code = 'en'"
    )}

    records: list[dict[str, Any]] = []
    for row in connection.execute("SELECT * FROM exercises ORDER BY id"):
        exercise_id = row["id"]
        translations = list(connection.execute(
            "SELECT language_code, name FROM exercise_translations WHERE exercise_id = ? ORDER BY language_code",
            (exercise_id,),
        ))
        names = name_map(translations)
        muscles = []
        for muscle in connection.execute(
            """SELECT em.muscle_id, em.role, mt.name AS name_en
               FROM exercise_muscles em LEFT JOIN muscle_translations mt
                 ON mt.muscle_id = em.muscle_id AND mt.language_code = 'en'
               WHERE em.exercise_id = ? ORDER BY em.role, em.muscle_id""",
            (exercise_id,),
        ):
            muscles.append({"id": muscle["muscle_id"], "role": muscle["role"]})
        equipment = []
        for item in connection.execute(
            """SELECT ee.equipment_id, ee.kind FROM exercise_equipment ee
               WHERE ee.exercise_id = ? ORDER BY ee.kind, ee.equipment_id""",
            (exercise_id,),
        ):
            equipment.append({"id": item["equipment_id"], "kind": item["kind"]})
        tags = [r[0] for r in connection.execute(
            "SELECT tag FROM exercise_tags WHERE exercise_id = ? ORDER BY tag", (exercise_id,)
        )]
        record = {
            "id": exercise_id,
            "name": names.get("en") or names.get("de") or row["slug"],
            "names": names,
            "slug": row["slug"],
            "status": row["status"],
            "recommended_for_routines": row["status"] == "active" and bool(names.get("en")),
            "category": row["category_name"],
            "body_region": row["body_region"],
            "modality": row["modality"],
            "muscles": muscles,
            "equipment": equipment,
            "tracking_type": row["tracking_type"],
            "load_mode": row["load_mode"],
            "difficulty": row["difficulty"],
            "movement_pattern": row["movement_pattern"],
            "mechanic": row["mechanic"],
            "laterality": row["laterality"],
            "usage_tags": tags,
        }
        records.append(record)

    catalog = {
        "catalog": "OpenExerciseDB",
        "version": meta.get("version"),
        "schema_version": int(meta.get("schema_version", "1")),
        "source": "https://github.com/rfivesix/OpenExerciseDB",
        "license": "CC-BY-SA-4.0",
        "attribution": "https://github.com/rfivesix/OpenExerciseDB/blob/main/ATTRIBUTION.md",
        "generated_at": meta.get("generated_at"),
        "id_contract": "Copy id exactly into Train Libre routine exercise uuid; IDs are strings.",
        "records": records,
    }
    output.mkdir(parents=True, exist_ok=True)
    json_path = output / "exercises.json"
    json_path.write_text(json.dumps(catalog, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    page = output / "exercise-search.html"
    entries = []
    for item in records:
        names = " · ".join(f'{code}: {name}' for code, name in item["names"].items())
        muscles_text = ", ".join(f'{muscle_names.get(m["id"], m["id"])} ({m["role"]})' for m in item["muscles"])
        equipment_text = ", ".join(equipment_names.get(e["id"], e["id"]) for e in item["equipment"])
        status_note = " · RECOMMENDED FOR ROUTINES" if item["recommended_for_routines"] else " · NOT RECOMMENDED FOR NEW ROUTINES"
        entries.append(
            f'<article id="exercise-{html.escape(item["id"], quote=True)}"><h3>{html.escape(item["name"])}'
            f' <code>id/uuid: {html.escape(item["id"])}</code></h3><p>{html.escape(names)}<br>'
            f'<strong>{html.escape(item["status"])}{status_note}</strong> · {html.escape(item["slug"])}</p>'
            f'<p>Category: {html.escape(item["category"] or "—")} · Body region: {html.escape(item["body_region"] or "—")} · '
            f'Modality: {html.escape(item["modality"] or "—")}</p><p>Muscles: {html.escape(muscles_text or "—")}<br>'
            f'Equipment: {html.escape(equipment_text or "—")}</p><p>Tracking: {html.escape(item["tracking_type"] or "—")} · '
            f'Load: {html.escape(item["load_mode"] or "—")} · Difficulty: {html.escape(item["difficulty"] or "—")} · '
            f'Pattern: {html.escape(item["movement_pattern"] or "—")} · Mechanic: {html.escape(item["mechanic"] or "—")} · '
            f'Laterality: {html.escape(item["laterality"] or "—")} · Tags: {html.escape(", ".join(item["usage_tags"]) or "—")}</p></article>'
        )
    active_count = sum(1 for x in records if x["recommended_for_routines"])
    page.write_text(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Search the OpenExerciseDB catalog by name, language, ID, muscle, or equipment. Stable IDs map to Train Libre routine UUIDs.">
<title>Exercise Search · OpenExerciseDB</title><style>body{{font:16px/1.55 system-ui,sans-serif;max-width:78rem;margin:auto;padding:1.25rem;color:#172033}}article{{border-top:1px solid #ccd3de;padding:.8rem 0}}h1,h2,h3{{line-height:1.25}}code{{background:#eef2f7;padding:.15rem .35rem}}.links{{background:#eef5fb;padding:1rem}}@media print{{body{{max-width:none}}}}</style></head>
<body><header><p>OpenExerciseDB · version {html.escape(str(meta.get("version", "unknown")))}</p><h1>Exercise search and catalog</h1>
<p>Use your browser’s Find command to search names in any language, stable IDs, muscles, or equipment. Each entry lists the catalog ID to copy exactly into a Train Libre routine’s <code>uuid</code>. This page works without JavaScript.</p>
<p class="links"><a href="exercises.json">Download machine-readable JSON catalog</a> · <a href="index.html">Interactive database explorer</a> · <a href="https://trainlibre.com/docs/user-guide/ai-workout-routines/">Train Libre AI routine guide</a></p>
<p>{len(records)} records total; {active_count} active records recommended for new routines. Retired and merged records are shown with status but not recommended.</p></header>
<main><h2>Exercises</h2>{''.join(entries)}</main><footer><p>Data license: CC BY-SA 4.0. <a href="https://github.com/rfivesix/OpenExerciseDB/blob/main/ATTRIBUTION.md">Attribution</a>.</p></footer></body></html>''', encoding="utf-8")
    connection.close()
    print(f"Wrote {json_path} and {page} ({len(records)} records, {active_count} recommended)")
