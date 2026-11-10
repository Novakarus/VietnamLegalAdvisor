# Record of AI-Assisted Content

Updated 2026-11-08 per the Publisher's (Thanh Nguyen's) confirmation. This record states facts; it is not a legal conclusion.

## Publisher's confirmation

- The content of `plugin/`, `docs/`, `scripts/` and related documents was drafted only with OpenAI's ChatGPT and Codex.
- Only a personal account in Vietnam on the ChatGPT Pro plan was used (confirmed 2026-11-04). No business account (Business, Enterprise) or API was used.
- Contribution (confirmed 2026-11-04): the Publisher wrote the content under the guidance of ChatGPT/Codex.

## Addendum: content drafted by Claude (Anthropic) in working sessions from 2026-11-02 to 2026-11-08

The "only ChatGPT and Codex" confirmation above does not cover the files below. They were written by Claude (Anthropic) in these working sessions at the Publisher's request, so they are declared separately:

- Code: `scripts/import_host_run.py`, `tests/run_integrity.py`, and the edits to `scripts/validate.py` (skipping the ZIP comparison when `dist/` is absent, comparing the tested archive, and the 2026-11-10 simplification that replaced the Pillow image check and absorbed the former `scripts/check_consistency.py`) (`SPDX-License-Identifier: Apache-2.0` headers).
- Documents: `STATUS.md`, `LICENSE.md`, `NOTICE`, `LICENSE-CC-BY-4.0.md`, `THIRD_PARTY_NOTICES.md`, `PROVENANCE-LOGO.md`, `PROVENANCE-AI-CONTENT.md`, `CHANGELOG.md`, the "Protocol v2" section at the end of `tests/EVALUATION.md`, `tests/HOST_RUNBOOK.md`, the warning line at the top of `history/CHANGES-0.69.2.md` and `history/CHANGES-0.69.3.md`, the License and Status sections of `README.md`, new lines in `tests/README.md`, and the English translation of the repository documents carried out on 2026-11-08.
- Website: Article 5 in `docs/terms/index.html` and `docs/terms/vi/index.html` (the Vietnamese pages restore the Publisher-approved text with the Article 5 update), the content of `docs/terms/source-license.html`, and the English translation of the `docs/` pages.
- Verbatim public license texts: `LICENSE-Apache-2.0.txt` (from the Debian `common-licenses` package, SHA-256 `cfc7749b…3d30`) and `LICENSE-CC-BY-4.0.txt` (from the SPDX `license-list-data` repository, SHA-256 `d557539d…3744`). These are standard license texts, not original writing.

Anthropic's terms: the Claude account is **Claude Pro** (personal; confirmed 2026-11-04), so the Consumer Terms of Service (Audience: Individual) apply. The official page https://www.anthropic.com/legal/consumer-terms was read directly in a browser on 2026-11-04:
- Effective: Oct 8, 2025. SHA-256 of the displayed page text (29,251 characters): `ef54655f279d4dafd599ef228237da3835aab02229ef178cc54f59500c60a4ac`. This is the page as displayed on the day it was read; Claude's working sessions took place from 2026-11-02 to 2026-11-04, in the same period, but the page's version history ("See version history") has not been cross-checked.
- The section on Inputs and Outputs (summary, not verbatim): to the extent permitted by law, the user retains rights in Input; subject to compliance with the Terms, Anthropic assigns to the user all of its rights (if any) in Outputs. It also states that Outputs may be inaccurate and that users should not rely on them without verification.
- The page has a "Download PDF" button for saving the official copy into `terms-archive/`.

## Applicable terms (personal account, outside the EEA/Switzerland/UK)

- OpenAI Terms of Use, Effective 2026-01-01, a contract with OpenAI OpCo, LLC. Wayback copy of 2026-10-16 14:11:08 UTC and hashes: see [PROVENANCE-LOGO.md](PROVENANCE-LOGO.md).
- To the extent permitted by law, the user owns Output and OpenAI assigns all of its rights (if any) in Output. Output may not be unique; the assignment does not include other users' Output or third-party Output.
- The terms state that they apply to ChatGPT, DALL·E and OpenAI's other services for individuals, and include the Service Terms (Service Terms: updated 2026-10-16).
- **Service Terms:** https://openai.com/policies/service-terms/ . The page printed on 2026-11-04 reads "Updated: October 16, 2026", so this version's update date coincides with the 2026-10-16 reference date (no Wayback copy is needed; the Wayback copy near that date is only an HTTP 403 block page). PDF: `terms-archive/openai-terms-2026-10-16.pdf` (10 pages), SHA-256 `c95c3001d8a56c5cacdb53fbab9054033ca65748b10295378f9ce88cd83678c2`. Limitation: this is the page as displayed, not a time-stamped capture, so it proves only that the version updated 2026-10-16 was in force through 2026-11-04.
  - SHA-256 of the displayed page text (19,381 characters), read on 2026-11-04: `67b22b2b16e54279632410b2e2e71b40dce7cab85238c2fa9f9a602088312b61`
  - Section 4 "Codex and Code Generation" (summary, not verbatim): results from the service's code generation features, including OpenAI Codex, may be subject to third-party licenses, including open-source licenses. This section has no separate rule on ownership of Codex Output; ownership of Output is under the Terms of Use above.

## Meaning for the license (assessment, not legal advice)

1. Under the terms, the Publisher is the assignee of rights in Output, so no OpenAI term (in the version read) prohibits relicensing Output under Apache 2.0 or CC BY 4.0.
2. The Publisher can license only the rights actually held. The terms use "if any" and "to the extent permitted by law", so they do not guarantee that Output is protected by copyright. If part is unprotected, a license over that part means little, but it does no harm.
3. Output may resemble other people's Output and, for Codex specifically, under the Service Terms may be subject to third-party licenses, including open source. This risk mainly concerns code (`scripts/`, `tests/*.py`), because Apache 2.0 cannot grant rights over a code fragment carrying another license. The code should be reviewed before publication (see "Remaining").
4. Both providers' consumer terms restrict the user from using the services (Anthropic) or Output (OpenAI) to develop competing AI models (checked in the stored PDFs on 2026-11-08). Licensing the output under CC BY 4.0 does not lift that restriction for the Publisher; see `LICENSE.md`, section 3.
5. The parts the Publisher wrote or edited with creative significance are the most likely to be protected. This level of contribution should be recorded.

## Remaining

- [x] The Terms of Use PDF of 2026-10-16 is stored in `terms-archive/` (see `terms-archive/INDEX.md`).
- [x] The OpenAI Service Terms PDF was stored and cross-checked: section 4 "Codex and Code Generation" matches what was recorded.
- [x] Review of code written by ChatGPT/Codex (`scripts/validate.py`, `scripts/package.py`, and the since-removed `tests/run_technical.py` and `tests/validate.py`): see `THIRD_PARTY_NOTICES.md`. Done 2026-11-04.
- [x] Anthropic's terms (Consumer Terms, Claude Pro account) were read on the official page and the hash recorded above.
- [x] The Consumer Terms PDF was stored (`terms-archive/anthropic-terms.pdf`, 14 pages, SHA-256 `7222642462bf559fa450982aa75ad4c7d3c1ed5c24e6e1517d7b4cf9f22806d4`); the sentence "we assign to you all of our right, title, and interest—if any—in Outputs" was cross-checked in the PDF.

## Test round 4 (2026-11-04)

All of `tests/runs/2026-11-04-round4/` was created by Claude: the answers and transcripts were produced by 22 isolated Claude Code subagent sessions; `evidence.json`, `results.json`, `run_manifest.json` and the report were written by the coordinating Claude, which also graded them (configured model `claude-sonnet-5-5`). The round 1–3 results were produced by Codex and are kept unchanged. These records are licensed under CC BY 4.0 to the extent the Publisher holds rights (see `LICENSE.md`, section 3).
