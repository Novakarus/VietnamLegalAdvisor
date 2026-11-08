# Tests — Vietnam Legal Advisor

- `cases.json`: 22 behavioral specifications and expected skill routes; not a test runner.
- `fixtures.md`: synthetic evidence, never real Vietnamese legal authority.
- `EVALUATION.md`: execution and scoring protocol.
- `results.json`: current 0.70.0 record: round 4, executed by 22 isolated Claude subagent sessions with technical OFFLINE and raw transcripts, graded by Claude (22/22 provisional AI PASS; Protocol v2 integrity FAIL with 2 errors: same-vendor grader, non-production host; not for formal acceptance); evidence in `runs/2026-11-04-round4/`. The 0.69.3 round-3 record (22 provisional AI PASS; formal acceptance blocked) is kept at `history/0.69.3/round3-results.json`. Evidence paths are relative to repository root.
- `runs/`: imported reports/evidence and exact candidate ZIPs for rounds 1–3; `results.original.json` preserves the original record before evidence-path rebasing.
- `history/`: earlier source-state records, including the unexecuted 0.69.3 record before import.
- `validation.json`: generated static report for the current source; regenerate after changes.
- `run_integrity.py`: checks a run directory against Protocol v2 (see `EVALUATION.md`); `templates/run_manifest.template.json` is the manifest template for new rounds.
- `validate.py`: compatibility launcher for `../scripts/validate.py`.

Use Python 3.10 or newer, with Pillow installed from scripts/requirements.txt. Run `python scripts/validate.py` before packaging. Behavioral acceptance requires actual host/model execution and reviewed evidence, not just these scripts.
