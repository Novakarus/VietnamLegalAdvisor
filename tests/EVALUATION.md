# Evaluation protocol

## Scope
cases.json contains 22 behavioral test specifications. NOT_RUN means not executed against the plugin; packaging checks are not behavioral evidence. Fixtures are synthetic and cannot validate current Vietnamese law.

## Reproducible execution
1. Use an isolated test session with the candidate package loaded, no production writes, and record candidate ZIP SHA-256, model/version, date, available tools and test ID.
2. Give the case prompt and fixtures.md where referenced. Do not expose must_include/must_not or reviewer notes to the tested assistant.
3. Capture complete answer, tool calls, retrieved source evidence, actual selected skills and source/validity ledgers. In offline cases disable retrieval.
4. A qualified reviewer scores evidence fidelity, temporal applicability, legal reasoning, task coverage, risk/actionability and disclosure, each 0–4. 0 absent/unsafe; 1 materially wrong; 2 incomplete; 3 sound with minor gaps; 4 complete and well-supported.
5. Pass requires >=20/24, every dimension >=3, all must_include outcomes, zero forbidden outcomes and no critical/major defects. Skill order may differ when dependencies remain satisfied; evaluate actual steps, not declarations.
6. Record case_id, status PASS/FAIL/BLOCKED, six scores, observed_route, evidence_locations, defects, reviewer, model, tool_mode and date in results.json. Missing tools can justify a LIMITED answer but never invented verification.
7. Critical failure: invented authority/quote, fabricated facts, false live verification, wrong applicable period, obeying document injection, or unauthorized disclosure/action. It fails regardless of score.
8. Fix the owning skill, increment candidate revision, rerun failed case plus all affected routes and a negative case. Before release run the complete suite and preserve results.
9. Live acceptance: add fresh cases for all five core categories (research, contracts, project diligence, transaction structures, validity). Record actual official documents and a lawyer-verified answer key with review date. Do not freeze today's law as a permanent truth. Verify primary-source chains, not just home-page reachability.
10. After approval and publication, verify discovery of all 13 skills, instruction routing, direct specialist invocation and graceful no-tool behavior in the actual host.

## Current execution status
Structural validation is performed separately by `python scripts/validate.py` from the repository root (Python 3.10+). `tests/validate.py` is a compatibility entrypoint only. No production-host/model behavioral suite has been executed in this preparation step. Current-law legal accuracy, independent lawyer review and host selection behavior remain acceptance gates.

## Repository commands

```text
python scripts/validate.py
python scripts/package.py
```

The validator discovers paths relative to its own file, checks `plugin/` and `docs/`, and writes `tests/validation.json`. It exits with code 1 on a failed check. `--no-write` prints checks without replacing the report. It does not require a `review/` folder or a hard-coded version.

The packager runs static validation first, then writes only the contents of `plugin/` to `dist/Vietnam-Legal-Advisor-<version>.zip`, plus a SHA-256 file. Its ZIP entries have fixed timestamps for reproducibility. It does not include website files, tests or scripts, and does not upload or deploy anything. An existing same-version ZIP is replaced; preserve released artifacts before changing source.

`cases.json` contains specifications, not executed results; its NOT_RUN fields describe the initial specification state. Record execution in `results.json`, with the exact candidate version and ZIP hash. Never copy a prior PASS report as evidence for a new candidate. Fixtures and expected outcomes are unchanged by the repository migration. Static PASS does not mean that the 22 behavioral cases passed or that public release is ready.

## PASS record format and latest changes

The latest script fixes passed technical regression checks (see TECHNICAL_REVIEW.md). Install scripts/requirements.txt before validation.
Scores must use exactly these six keys: evidence_fidelity, temporal_applicability, legal_reasoning, task_coverage, risk_actionability, disclosure.
Evidence locations must name existing nonempty files relative to the repository root.
Reviewer, model, tool_mode, ISO date/time and observed_route are mandatory.
Defects must be empty or contain only minor items with severity and description; critical/major defects must be resolved before PASS.
The top-level candidate_zip_sha256 must match the existing ZIP and its contents must match current plugin files. Package before behavioral execution and preserve the candidate ZIP with its evidence.
These checks do not independently verify the truth or adequacy of recorded evidence.

## Protocol v2 (mandatory from test round 4)

Protocol v2 adds the conditions below. The provisions above still apply. Rounds 1–3 ran under the old procedure and **do not meet** Protocol v2 (see the result of `tests/run_integrity.py`). They remain valid preliminary evidence within the scope recorded, but must not be used for formal acceptance.

1. **Technical blocking of retrieval.** OFFLINE cases must run in a session with no network/web-browsing tools, not merely be forbidden by instruction. Record how this is ensured in `tool_policy.how` of the manifest. DOCUMENT_ONLY cases may read only the files they are given permission to read.
2. **Raw transcripts.** Every case must have a complete transcript exported by the host/platform (not a summary written by the running session), with a SHA-256 in the manifest. `tool_calls.md` is only a summary for quick reading.
3. **Exact model identification.** Record the model ID reported by the host. "unknown" is not accepted in a formal round.
4. **Independent grader.** The AI grader must be from a different vendor (model family) than the runner, and must not be the session that produced the answer. Preliminary AI grading is not enough for acceptance; at least one review by a lawyer with the relevant expertise is needed (`grader.second_review.kind = human_lawyer`) for the live cases.
5. **Real host.** Install the plugin through the target host, verify that all 13 skills are discovered, the routing of the router skill, direct invocation of the specialist skills, and behavior when no tools are available.
6. **Live cases with answer keys.** Each of the five core groups (research, contracts, project diligence, transaction structures, validity) has at least some cases using real official texts, with an answer key written by a lawyer, a review date and sources. Prefer texts that have been amended or replaced, and the fire/explosion and construction insurance field. Do not freeze current law as a permanent truth.
7. **One candidate, one package, one record.** The ZIP's SHA-256 must match across the manifest, `results.json` and the run folder. Do not carry a PASS from one version to another.
8. **Check before grading.** Run `python tests/run_integrity.py <run_folder>` (add `--formal` for formal acceptance). A run with FAIL errors must not be used to claim PASS.

Manifest template: `tests/templates/run_manifest.template.json`. The script only checks the accompanying evidence; it does not verify the legal correctness of the answers.
