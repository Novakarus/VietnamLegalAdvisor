---
{"name": "legal-quality-audit", "description": "Audit a proposed legal answer or deliverable for evidence, consistency and professional quality before delivery."}
---

# legal-quality-audit

## Scope and activation
Audit a proposed legal answer or deliverable for evidence, consistency and professional quality before delivery.
Read [professional protocol](../instructions/references/professional-protocol.md) before analysis, and [source access](../instructions/references/source-access.md) when sources must be retrieved. Apply these even on direct invocation.

## Inputs
Draft, task scope, facts, source ledger, validity matrix, risk register and unresolved questions.
Record missing material inputs; do not invent them.

## Workflow
1. Check task coverage, Vietnamese default language and distinction between facts, rules, practice and inference. Check the requested work product itself, even for LIMITED/OFFLINE answers: a conditional structure comparison must distinguish options, an unavailable-source answer must give an actionable verification sequence, and opposing review must pair labeled hypotheses with specific evidence to seek. A list of names, empty column headings or an offer to do the work later does not satisfy these outputs. Ask for missing facts without withholding the safe, useful part available now.
2. Sample all dispositive claims, then inspect every legal citation and date-dependent conclusion against source and validity ledgers.
3. Check contradictions, missing exceptions, invented facts, redline integrity and separation of legal/commercial risk. Where the router or owning skill requires an opposing pass, check that the actual work product includes a challenge/alternative explanation and an evidence response, not merely the skill name or a claim of review.
4. Classify defects: critical, major, minor. Critical includes fabricated authority, false verification, wrong governing period or unsupported categorical advice. For a claim of source verification contradicted by a tool log, state the classification rule explicitly in the user-facing answer and defect record: "False verification, if confirmed, is critical (lỗi cấp critical)." Do not replace the severity label with only "serious" or "nghiêm trọng". Separate severity from proof: confirmed false verification is critical; an unsupported claim remains CHƯA XÁC MINH, with potential severity critical if the claim is shown false. Search unavailability alone does not prove that no direct browsing, other tool or previously obtained source was used; request the corresponding retrieval/text evidence without assuming those alternatives occurred. Until the decisive verification claim is supported or corrected, retain LIMITED/BLOCKED and do not issue READY or release the advice as verified. An unavailable tool alone is not a critical defect or proof that the legal conclusion is wrong.
5. Return targeted repair requests once to the relevant skill and re-audit; if blockers remain, issue a bounded provisional answer or explain why the conclusion must be withheld.

## Professional checklist
- All dispositive claims checked
- No unsupported verification badge
- Material open items disclosed
- No invented completion of tool actions

## Legal authority checks
Use the shared source and claim ledgers. Confirm source identity and exact text, then provision-level validity and applicability to the matter date. For this module, explicitly verify: all dispositive claims checked and material open items disclosed. If unavailable, label the affected conclusion unverified. Reuse existing verified work only for the same source version, matter date and scope; do not reset uncertainty during handoff.

## Quality criteria
Release only if zero critical/major defects; minor defects disclosed or corrected. Limited answers must visibly retain limitations.
Use the quality audit before releasing a substantive conclusion; do not recursively invoke this same module while its review is in progress.

## Output
Audit disposition READY / LIMITED / BLOCKED; defects with locations; corrective actions; user-facing caveats and next step. For a suspected verification defect, record separately: claim/location | evidence status (confirmed false / unsupported / supported) | severity (critical when confirmed false; potential critical while unresolved) | missing evidence | release restriction. Keep the same explicit severity in the answer and audit record; never present a potential defect as a confirmed event.

## Limits and handoff
Do not loop indefinitely or claim independent review. Route defects to the owning module; do not conceal missing evidence by polishing language.
Pass the matter brief, evidence/claim ledgers, artifacts and unresolved questions to the next skill. Route by exact sibling skill name in [router](../instructions/SKILL.md); load its SKILL.md and perform it in the same session if no separate invocation facility exists.
