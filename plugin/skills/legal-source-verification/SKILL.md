---
{"name": "legal-source-verification", "description": "Verify the existence, identity, text and support of legal citations and source claims."}
---

# legal-source-verification

## Scope and activation
Verify the existence, identity, text and support of legal citations and source claims.
Read [professional protocol](../instructions/references/professional-protocol.md) before analysis, and [source access](../instructions/references/source-access.md) when sources must be retrieved. Apply these even on direct invocation.

## Inputs
Claim list, citations, URLs, quoted text, supplied files and claimed verification status.
Record missing material inputs; do not invent them.

## Workflow
1. Assign source and claim IDs; retrieve the cited document from an official source when possible.
2. Match issuer, title, identifier, date, document type and exact article/clause; do not trust a matching page title alone.
3. Read the relevant text and context; compare the quotation and whether it supports the proposition.
4. Classify official normative text, official guidance, adopted precedent, other judgment, secondary commentary and professional inference separately.
5. Record verified, partial, inaccessible, mismatched or not found within searched scope; send temporal applicability to legal-validity-verification. When auditing a claim that retrieval or verification occurred, match that claim to actual tool results or supplied retrieval evidence, including the text inspected and timing. Search unavailability alone does not rule out another access method. If evidence is absent, mark the claim CHƯA XÁC MINH, request proof of any alternative method, and hand off to legal-quality-audit with the explicit rule: false verification, if confirmed, is critical (lỗi cấp critical). Record potential severity critical separately from the unresolved factual status. Do not call a missing tool itself critical, infer that the cited law is wrong, or preserve an unsupported verified badge.

## Professional checklist
- URL content matches citation
- Quote fidelity and context
- Precedent status actually checked
- Search snippet is not proof

## Legal authority checks
Use the shared source and claim ledgers. Confirm source identity and exact text, then provision-level validity and applicability to the matter date. For this module, explicitly verify: url content matches citation and precedent status actually checked. If unavailable, label the affected conclusion unverified. Reuse existing verified work only for the same source version, matter date and scope; do not reset uncertainty during handoff.

## Quality criteria
No invented identifiers or URLs; verification status reflects retrieved evidence rather than domain reputation.
Use the quality audit before releasing a substantive conclusion; do not recursively invoke this same module while its review is in progress.

## Output
Claim ID | source ID | pinpoint | retrieved text summary | supports/contradicts/unclear | access status | follow-up.

## Limits and handoff
Does not establish applicability by itself. Not found is not nonexistent. Legal conclusions await validity and substantive analysis; supplied files alone do not prove official authenticity.
Pass the matter brief, evidence/claim ledgers, artifacts and unresolved questions to the next skill. Route by exact sibling skill name in [router](../instructions/SKILL.md); load its SKILL.md and perform it in the same session if no separate invocation facility exists.
