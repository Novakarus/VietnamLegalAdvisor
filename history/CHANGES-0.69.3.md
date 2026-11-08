> **HISTORY — not the current status.** Records the state at the time of the edit. The current status is in `STATUS.md`.

> Note: the statements "not tested" and "NOT_RUN" below were true when written (2026-10-20). Version 0.69.3 later went through test round 3 (2026-10-21, 22/22 provisional PASS graded by AI); see `STATUS.md`.

# Candidate 0.69.3 — Q01 clarification, not tested

Saved 2026-10-20 after round-2 provisional AI scoring of 0.69.2: 21 PASS, Q01 FAIL. The observed Q01 answer retained LIMITED but did not explicitly identify the critical severity of false verification.

- legal-quality-audit now requires the explicit user-facing label "critical (lỗi cấp critical)" for confirmed false verification and the same label in its defect record. A generic "serious/nghiêm trọng" alone is insufficient.
- Severity and evidence status remain distinct: unsupported retrieval claims are CHƯA XÁC MINH with potential severity critical if shown false; Search unavailability alone does not prove false verification, rule out other access methods, or establish that a legal conclusion is wrong.
- legal-source-verification now hands off the retrieval claim, actual evidence, unresolved status and explicit conditional critical classification. LIMITED/BLOCKED and the restriction on publishing as verified remain until the decisive claim is supported or corrected.

Both manifests are 0.69.3. The source result record for 0.69.2 is preserved under tests/history/0.69.2/results.json; its actual provisional round-2 report/evidence remains in the chat outputs/round2. The new tests/results.json records 0.69.3 as NOT_RUN. No prior PASS is attributed to this revision.

As requested, no test runner, static validator, behavioral invocation, packaging, host reload or deployment was run. Only source readback, scope review and metadata parsing were performed. This is an instruction edit, not proof that Q01 behavior is fixed.
