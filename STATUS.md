# Project Status — single source of truth

This is the only place that records the current status. `CHANGELOG.md`, `history/` and `tests/runs/` are historical records as of the time they were created; if they conflict with this file, this file prevails. `scripts/validate.py` checks that the version below matches the manifests and `tests/results.json`.

Current version: 0.70.0
Status: CANDIDATE
Ready for public release: no
Updated: 2026-11-10

## Statuses

| Status | Meaning |
|---|---|
| DRAFT | `plugin/` is being edited; not packaged or tested |
| CANDIDATE | Version bumped, `validate.py` passes, ZIP packaged, behavioral tests run or in progress |
| ACCEPTED | All acceptance gates below are met; not yet published |
| RELEASED | Published by decision of the Publisher |

Do not raise the status on the basis of provisional AI grading.

## Acceptance gates

1. `python tests/run_integrity.py <run folder> --formal` passes for a run of the current ZIP (see `tests/EVALUATION.md`, Protocol v2): real host, raw transcripts, exact model ID, grader from a different vendor.
2. A lawyer has reviewed the results, including live cases with answer keys.

## Versioning rules

1. Any change in `plugin/` (including an instruction-only edit) creates a new version; the affected cases plus one control case must be retested. A PASS is not carried over from a previous version.
2. Changes outside `plugin/` (documentation, scripts, licenses, website) do not raise the plugin version. They are recorded in the Git history.
3. A tested ZIP is not repackaged; to change the package, create a new version. The one recorded exception is the `plugin/LICENSE.md` change of 2026-11-08 described below.

## Status of version 0.70.0

- Candidate (2026-11-04): added `plugin/LICENSE.md` (a CC BY 4.0 license notice, effective 2026-11-04). Skill content unchanged. See `history/CHANGES-0.70.0.md`.
- Packaged: `dist/Vietnam-Legal-Advisor-0.70.0.zip` (SHA-256 in the `.sha256` file next to it). Static checks pass.
- Change after round 4 (2026-11-08): only `plugin/LICENSE.md` (the logo is also under CC BY 4.0 to the extent the Publisher holds rights; the notice was translated into English). Skill content, instructions and both manifests are unchanged. The ZIP was repackaged; the current SHA-256 is recorded in `tests/results.json` (`post_test_changes.current_zip_sha256`). The round 4 evidence ran on the earlier ZIP, SHA-256 `ebbd7e606fe3d4c0de6a74194ede4f4726b3e6d5607aed39fed37c001eedb839`, kept at `tests/runs/2026-11-04-round4/`. `validate.py` compares the two archives file by file and fails if any other file differs. This must be re-confirmed on a real host in the formal round (round 5 uses the current ZIP).
- Behavioral tests: round 4 ran on 2026-11-04 (22/22 provisional PASS, AI-graded; see the Protocol v2 gap section below). Round 5 on a real host is in preparation and has not been graded.
- Formal acceptance: not yet.

## Earlier versions

Versions 0.69.1–0.69.3 were tested in rounds 1–3 (run and graded by Codex, 2026-10-20 and 2026-10-21) and were removed from the repository on 2026-11-08. Their test records are kept under `tests/runs/` as history; they do not meet Protocol v2 and must not be used for acceptance.

## Gap against Protocol v2

Round 4 (Claude, 2026-11-04) was rerun with 22 isolated Claude Code subagent sessions (one session per case; Read/Edit tools only, no web or shell, so OFFLINE was enforced technically; model ID `claude-sonnet-5-5` as reported by the host; raw transcripts and a SHA-256 per case; the runner was not given `must_include`/`must_not`). Result: 22/22 provisional PASS; `run_integrity.py` still FAILs with 2 errors: (1) the grader is Claude, the same model family as the runner; (2) the plugin has not been run on a real production host with the plugin installed. A lawyer review and live cases with answer keys are also still missing. Limitations: the subagents used the system prompt of the agent type that configures the status line; the coordinator had previously seen `cases.json`.
