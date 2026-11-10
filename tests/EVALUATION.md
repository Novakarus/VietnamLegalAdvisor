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

## PASS record format

`scripts/validate.py` enforces the format of every PASS in `results.json`:
- Scores use exactly these six keys: evidence_fidelity, temporal_applicability, legal_reasoning, task_coverage, risk_actionability, disclosure.
- Evidence locations name existing nonempty files relative to the repository root.
- Reviewer, model, tool_mode, ISO date/time and observed_route are mandatory.
- Defects are empty or contain only minor items with severity and description.
- The top-level candidate_zip_sha256 matches the tested ZIP, and its contents match the current plugin files (apart from files listed in post_test_changes). Package before behavioral execution and keep the tested ZIP with its evidence.

These checks do not verify the truth or adequacy of the recorded evidence. Never copy a prior PASS as evidence for a new candidate.

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

`scripts/import_host_run.py` writes `run_manifest.json` for a host run. The script only checks the accompanying evidence; it does not verify the legal correctness of the answers.
