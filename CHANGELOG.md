# Changelog

## 0.70.0 — candidate (CANDIDATE), not public — 2026-11-04

Renumbered from 0.69.3 (frozen). License update (Apache-2.0 for code; CC BY 4.0 for documents and plugin content; the logo, test evidence and AI output are also CC BY 4.0 to the extent the Publisher holds rights), records of the provenance of AI content and of the logo, and archiving of third-party terms. Protocol v2 test round 4: 22 isolated Claude sessions, 22/22 provisional PASS graded by AI; `tests/run_integrity.py` still has 2 errors (grader from the same vendor, not yet run on a real host), so there is no formal acceptance. Added `scripts/import_host_run.py` and `tests/HOST_RUNBOOK.md` for the real-host round. `validate.py` skips the ZIP comparison when `dist/` is absent (CI) and prints a warning. The website now has a single source, `docs/` (GitHub Pages serves from /docs); the root copy, `sync_site.py` and the `release.yml` workflow were removed. Version 0.69.3 (package, release page, report) was removed from the repository; the round 1–3 test records are kept. All repository documents and the plugin manifests/license notice were translated into English on 2026-11-08 (the skills and the test evidence remain in Vietnamese). The Terms of Use and source-license pages are also published in Vietnamese (`docs/terms/vi/`), which is the official text; Terms version stays 1.0.

## 0.69.3 — plugin update 2026-10-22

Clarified Q01: false source verification, if proven, is a critical error; confirmed errors are separated from claims with no evidence. No inference is drawn from an unavailable search tool to a conclusion that false verification occurred.

## 0.69.2

Added conditional structure comparison when facts are missing; an in-answer verification procedure for offline use; a map of hypotheses and evidence for adversarial review; substantive checks of the adversarial step and of output quality.

## Source and website publication — 2026-10-22

Published the source, documents and a summary of the tests. The license and website were published separately; the tested 0.69.3 plugin package was kept unchanged, and no license was added to the historical ZIP. The source file plugin/LICENSE.md is a new document alongside the 20 original files and does not change the skill instructions.

## Details of each change

Detailed records (history only, not the current status; the status is in `STATUS.md`): [0.69.2](history/CHANGES-0.69.2.md) · [0.69.3](history/CHANGES-0.69.3.md) · [0.70.0](history/CHANGES-0.70.0.md).
