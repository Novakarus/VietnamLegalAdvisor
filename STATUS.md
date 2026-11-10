# Project Status — single source of truth

This is the only place that records the current status. `CHANGELOG.md` and `tests/runs/` are historical records as of the time they were created; if they conflict with this file, this file prevails. `scripts/validate.py` checks that the version below matches the manifests and `tests/results.json`.

Current version: 0.70.1
Status: ACCEPTED
Ready for public release: no
Updated: 2026-11-10

## Statuses

| Status | Meaning |
|---|---|
| DRAFT | `plugin/` is being edited; not packaged or tested |
| CANDIDATE | Version bumped, `validate.py` passes, ZIP packaged, behavioral tests run or in progress |
| ACCEPTED | Accepted by decision of the Publisher; not yet published |
| RELEASED | Published by decision of the Publisher |

## Acceptance

Acceptance is a decision of the Publisher, recorded here with its basis and limits.

Version 0.70.0 was accepted by the Publisher on 2026-11-10 on the basis of round 4 (22/22 PASS, AI-graded). Version 0.70.1 keeps that acceptance and was retested the same day in round 5 (22/22 PASS, AI-graded, on the 0.70.1 package). In both rounds the following were not met: the plugin was not run on a real host; the grader (Claude) is from the same vendor as the runner; there is no lawyer review of the answers and there are no live cases with answer keys. Acceptance is therefore not an independent certification of legal quality.

## Versioning rules

1. Any change in `plugin/` (including an instruction-only edit) creates a new version; the affected cases plus one control case must be retested. A PASS is not carried over from a previous version.
2. Changes outside `plugin/` (documentation, scripts, licenses, website) do not raise the plugin version. They are recorded in the Git history.
3. A tested ZIP is not repackaged; to change the package, create a new version. The one recorded exception is the `plugin/LICENSE.md` change of 2026-11-08 described below.

## Status of version 0.70.1

- Packaging-only change from 0.70.0 (2026-11-10): removed the redundant `.codex-plugin/plugin.json` (Codex reads the root `plugin.json` when it has `extensions.com.openai`), removed the empty `skills/instructions/lookup/knowledge-index.json` (not referenced by any skill), resized the logo to 512×512, and updated `plugin/LICENSE.md` (version number; reference to `PROVENANCE.md`). No `SKILL.md`, reference file or agent file changed.
- Behavioral tests: round 5 ran on 2026-11-10 on the 0.70.1 ZIP (SHA-256 `2d6bdad8971510252f12403b53cda784eef92a7103460c9dc6871943b66fc9b3`, kept with the evidence at `tests/runs/2026-11-10-round5/`). All 22 cases ran in isolated Claude subagent sessions (runner model `claude-sonnet-5-5` per the transcripts; Read/Edit tools only, so OFFLINE was enforced technically; raw transcripts with SHA-256). Graded by Claude Opus 5.5: 22/22 provisional PASS, totals 23–24 of 24, no critical or major defects; 8 cases carry minor defects (expected skills not read in R01, R03, M01, A01; MODE mislabelled in D01 and V02; stray "status line" sentences in R01, V01 and F01; L01 element mapping only at method level). `tests/results.json` is now this record. `run_integrity.py`: FAIL with the same 2 errors as round 4 (same-vendor grader; not a real host).
- Codex attempt: the round was first started on the real Codex host on the Publisher's computer (Codex CLI 0.163.0, model `gpt-5.6-terra`, read-only sandbox with network restricted, plugin 0.70.1 installed through a local marketplace, other plugins and connectors disabled). Only R01 completed, with a sound answer; the account then reached its Codex usage limit (reset given as 2026-12-05). By decision of the Publisher the round was rerun with Claude instead. The R01 Codex transcript is kept locally and is not part of the record.
- Install check (2026-11-10, Codex CLI 0.163.0 on the Publisher's computer): the 0.70.1 ZIP (SHA-256 `2d6bdad8971510252f12403b53cda784eef92a7103460c9dc6871943b66fc9b3`) installed from a temporary local marketplace with only the root manifest, and all 13 skills appeared in the model-visible skill list (`codex debug prompt-input`). This checks discovery only, not behavior. The temporary install was removed afterwards.
- The copy uploaded earlier to the ChatGPT plugin system is still 0.70.0 with the older `LICENSE.md` and duplicate logo files; it has not been updated.

## Status of version 0.70.0 (superseded)

- Candidate (2026-11-04): added `plugin/LICENSE.md` (a CC BY 4.0 license notice, effective 2026-11-04). Skill content unchanged.
- Packaged: `dist/Vietnam-Legal-Advisor-0.70.0.zip` (SHA-256 in the `.sha256` file next to it). Static checks pass.
- Change after round 4 (2026-11-08): only `plugin/LICENSE.md` (the logo is also under CC BY 4.0 to the extent the Publisher holds rights; the notice was translated into English). Skill content, instructions and both manifests are unchanged. The ZIP was repackaged; the current SHA-256 is recorded in `tests/results.json` (`post_test_changes.current_zip_sha256`). The round 4 evidence ran on the earlier ZIP, SHA-256 `ebbd7e606fe3d4c0de6a74194ede4f4726b3e6d5607aed39fed37c001eedb839`, kept at `tests/runs/2026-11-04-round4/`. Since 2026-11-10 `validate.py` only checks the SHA-256 of the tested ZIP against the record; it no longer compares that ZIP with the current `plugin/` files, so the statement that nothing else changed rests on the Git history.
- Behavioral tests: round 4 ran on 2026-11-04 (22/22 provisional PASS, AI-graded; see the Protocol v2 gap section below). Superseded by round 5 on 0.70.1.
- Acceptance: accepted by the Publisher on 2026-11-10 (see "Acceptance" above). Not published.

## Earlier versions

Versions 0.69.1–0.69.3 were tested in rounds 1–3 (run and graded by Codex, 2026-10-20 and 2026-10-21) and were removed from the repository on 2026-11-08; their test records were removed on 2026-11-10 (they did not meet Protocol v2 and could not be used for acceptance). Everything removed remains in the Git history.

## Gap against Protocol v2

Rounds 4 (0.70.0) and 5 (0.70.1) were both run with 22 isolated Claude Code subagent sessions and both end with `run_integrity.py` FAIL on the same 2 errors: (1) the grader is Claude, the same vendor as the runner; (2) the plugin was not run on a real production host with the plugin installed. A lawyer review and live cases with answer keys are also missing. Other limitations: the subagents used the system prompt of the agent type that configures the status line; the coordinator, who also graded, had seen `cases.json` before the run. Closing error (2) and, with Claude as grader, error (1) needs the round to be run on Codex, which the Publisher's Codex usage limit currently blocks.
