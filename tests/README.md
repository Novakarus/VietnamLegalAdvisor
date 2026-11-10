# Tests — Vietnam Legal Advisor

- `cases.json`: 22 behavioral specifications and expected skill routes; not a test runner.
- `fixtures.md`: synthetic evidence, never real Vietnamese legal authority.
- `EVALUATION.md`: execution and scoring protocol (including Protocol v2).
- `results.json`: the record for the current version; `scripts/validate.py` checks it against the tested ZIP. Evidence paths are relative to the repository root.
- `runs/`: one folder per test round with its report and evidence. Current status and the meaning of each round are in `../STATUS.md`.
- `run_integrity.py`: checks a run folder against Protocol v2.
- `HOST_RUNBOOK.md`: how to run the 22 cases on a real host and import the transcripts with `scripts/import_host_run.py`.
- `history/`: earlier source-state records.
