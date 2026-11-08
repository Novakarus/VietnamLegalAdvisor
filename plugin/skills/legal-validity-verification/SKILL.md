---
{"name": "legal-validity-verification", "description": "Determine temporal applicability, amendments, repeal and transitional rules for specific provisions."}
---

# legal-validity-verification

## Scope and activation
Determine temporal applicability, amendments, repeal and transitional rules for specific provisions.
Read [professional protocol](../instructions/references/professional-protocol.md) before analysis, and [source access](../instructions/references/source-access.md) when sources must be retrieved. Apply these even on direct invocation.

## Inputs
Document identifiers or files, exact provisions, event dates, filing and decision dates, sector and locality.
Record missing material inputs; do not invent them.

## Workflow
1. Separate issue date, effective date, event date and date of review; do not use the newest text automatically.
2. Retrieve the original instrument, amendment and repeal instruments, effective clauses, corrigenda and transitional provisions.
3. Trace changes at article/clause level; distinguish partial repeal, suspension, future effectiveness and full replacement.
4. Build date intervals and test each event against the applicable interval and transitional predicates.
5. Return a provision-level status matrix; mark unresolved chains unknown and specify the document or fact needed.

## Professional checklist
- Partial versus full repeal
- Transitional eligibility
- Consolidated text versus underlying instruments
- Multiple relevant event dates

## Legal authority checks
Use the shared source and claim ledgers. Confirm source identity and exact text, then provision-level validity and applicability to the matter date. For this module, explicitly verify: partial versus full repeal and consolidated text versus underlying instruments. If unavailable, label the affected conclusion unverified. Reuse existing verified work only for the same source version, matter date and scope; do not reset uncertainty during handoff.

## Quality criteria
Every effective-status statement is tied to retrieved operative text and a date; unresolved status cannot be recorded as valid.
Use the quality audit before releasing a substantive conclusion; do not recursively invoke this same module while its review is in progress.

## Output
Timeline plus table: provision | version | effective interval | event | transition | evidence | status.

## Limits and handoff
Unclear identities go to legal-source-verification; conflicts go to legal-reasoning. A consolidated text alone does not prove current status.
Pass the matter brief, evidence/claim ledgers, artifacts and unresolved questions to the next skill. Route by exact sibling skill name in [router](../instructions/SKILL.md); load its SKILL.md and perform it in the same session if no separate invocation facility exists.
