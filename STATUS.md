# Project Status — single source of truth

This is the only place that records the current status. `history/CHANGES-*.md`, `releases/*/RELEASE.md` and `tests/runs/*` are historical records as of the time they were created; if they conflict with this file, this file prevails. `scripts/check_consistency.py` checks that the figures below match the manifests, `release.json` and `tests/results.json`.

Current version: 0.70.0
Status: CANDIDATE
Ready for public release: no
Updated: 2026-11-08

## Statuses and transition conditions

| Status | Meaning | Condition to enter |
|---|---|---|
| DRAFT | Being edited; behavioral tests not yet run | There is a change in `plugin/` |
| CANDIDATE | Packaged; a new round of behavioral tests is run | Version bumped, `validate.py` passes, ZIP packaged and SHA-256 recorded |
| FROZEN_LOCAL_RELEASE_CANDIDATE | The tested ZIP is preserved byte for byte | A results record and `release.json` exist |
| ACCEPTED | Meets the acceptance conditions, not yet published | All of the "acceptance gates" below |
| RELEASED | Published | ACCEPTED + the Publisher approves the Terms and the license |

Change the status only by editing this file together with `release.json`. Do not raise the status on the basis of preliminary AI scoring.

## Versioning rules

1. Any change in `plugin/` (including an instruction-only edit) creates a new version, and the affected cases plus one control case must be retested. Do not carry a PASS over from a previous version.
2. Changes outside `plugin/` (documentation, scripts, licenses, website) do not raise the plugin version and do not change the SHA-256 of a frozen package. Record them in the Git history, not in `history/CHANGES-*.md`.
3. `CHANGES-<version>.md` is written once, at the time of the edit, and is not edited afterwards; add a "Test results" section in another historical record if needed.
4. Do not repackage the ZIP of a frozen version. To change the package, create a new version.

## Status of version 0.70.0

- Candidate (2026-11-04): added `plugin/LICENSE.md` (a CC BY 4.0 license notice, effective 2026-11-04). Skill content unchanged. See `history/CHANGES-0.70.0.md`.
- Packaged: `dist/Vietnam-Legal-Advisor-0.70.0.zip` (SHA-256 in the `.sha256` file next to it). Static checks pass.
- Change after round 4 (2026-11-08): only `plugin/LICENSE.md` (the logo is also under CC BY 4.0 to the extent the Publisher holds rights; the notice was translated into English). Skill content, instructions and both manifests are unchanged. The ZIP was repackaged; the current SHA-256 is recorded in `tests/results.json` (`post_test_changes.current_zip_sha256`). The round 4 evidence ran on the earlier ZIP, SHA-256 `ebbd7e606fe3d4c0de6a74194ede4f4726b3e6d5607aed39fed37c001eedb839`, kept at `tests/runs/2026-11-04-round4/`. `validate.py` compares the two archives file by file and fails if any other file differs. This must be re-confirmed on a real host in the formal round (round 5 uses the current ZIP).
- Behavioral tests: round 4 ran on 2026-11-04 (22/22 provisional PASS, AI-graded; see the Protocol v2 gap section below). Round 5 on a real host is in preparation and has not been graded.
- Formal acceptance: not yet.

## Version 0.69.3 (removed from the repository, 2026-11-08)

- The Publisher decided to remove the package, release page and report of 0.69.3 from the repository; only the round 1–3 test records (run by Codex) are kept as history. The frozen ZIP had SHA-256 `40120521e43173191ab4babbc93180445fef33fb819f9d24ed2c25fb31dd7fa6`.
- Round 3 behavioral tests: 22/22 PASS, provisionally AI-graded; static checks 109/109 (before the record was imported) and 131/131 (after); technical regression 14/14. Records are at `tests/history/0.69.3/round3-results.json` and `tests/runs/2026-10-21-round3/`.

## Gap against Protocol v2

Round 4 (Claude, 2026-11-04) was rerun with 22 isolated Claude Code subagent sessions (one session per case; Read/Edit tools only, no web or shell, so OFFLINE was enforced technically; model ID `claude-sonnet-5-5` as reported by the host; raw transcripts and a SHA-256 per case; the runner was not given `must_include`/`must_not`). Result: 22/22 provisional PASS; `run_integrity.py` still FAILs with 2 errors: (1) the grader is Claude, the same model family as the runner; (2) the plugin has not been run on a real production host with the plugin installed. A lawyer review and live cases with answer keys are also still missing. Limitations: the subagents used the system prompt of the agent type that configures the status line; the coordinator had previously seen `cases.json`.

Round 3 (Codex):

Result of running `python tests/run_integrity.py tests/runs/2026-10-21-round3` on 2026-11-03: **FAIL**. Round 3 fails because there is no `run_manifest.json`, no exact model ID, the grader is in the same model family as the runner (both Codex/OpenAI), OFFLINE was enforced only by instruction, it did not run on a real host, and there are no raw transcripts. The candidate ZIP matches its SHA-256. Round 4 had to meet Protocol v2 (see `tests/EVALUATION.md`).
