# Reports

These reports describe the data at the time of their review or generation; they are not necessarily current. Historical round logs live in `archive/`. Generated reports retain their original paths so existing build scripts continue to work. Commands below run from the repository root and overwrite their reports; they were not run during cleanup.

- [invariant_20_outliers.md](invariant_20_outliers.md) — Movement-pattern/primary-muscle outliers and review rationale; regenerable with `PYTHONPATH=. python3 build/generate_reports.py` (all five generated reports are overwritten; manual commentary may differ).
- [family_consistency.md](family_consistency.md) — Classification differences within exercise families; regenerable with `PYTHONPATH=. python3 build/generate_reports.py`.
- [unclassifiable.md](unclassifiable.md) — Missing classification and unresolved exercise cases; regenerable with `PYTHONPATH=. python3 build/generate_reports.py`.
- [name_overrides.md](name_overrides.md) — Heuristic conflicts between exercise names and primary muscles; regenerable with `PYTHONPATH=. python3 build/generate_reports.py`.
- [cross_language.md](cross_language.md) — Heuristic English/German text discrepancies; regenerable with `PYTHONPATH=. python3 build/generate_reports.py`.
- [expanded_descriptions.md](expanded_descriptions.md) — Description expansion audit against commit `6d11cf7`; no retained generator found, so the original audit is preserved.
- [text_changes_phase2.md](text_changes_phase2.md) — Historical curated English/German text changes; regenerable with `python3 build/report_text_changes.py --reference <reference.db> --database <catalog.db>` plus the corresponding YAML provenance, with the original inputs needed to reproduce this exact report; kept here because it is a build script's default output.
- [curation_notes.md](curation_notes.md) — Durable schema and contribution guidance retained from the removed session handover; manually maintained, no generator.
- [archive/job_a_review_report.md](archive/job_a_review_report.md) — Semantic English/German review round, decisions and unresolved findings; manual/model review, no retained generator.
- [archive/job_b_report.md](archive/job_b_report.md) — German description batches and exceptions; historical work log, no retained generator.
- [archive/name_changes.md](archive/name_changes.md) — Proposed English name standardizations and merge rationale; historical review, no retained generator.
- [archive/existing_fr_it_check.md](archive/existing_fr_it_check.md) — Review of inherited French/Italian descriptions before translation; no retained generator, original inputs needed to repeat the checks.
- [archive/thin_sources.md](archive/thin_sources.md) — Triage and corrections from the round reviewing thin English sources; historical review, no retained generator.
