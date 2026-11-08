---
{"name": "regulatory-compliance", "description": "Map and assess Vietnamese regulatory obligations for a defined business activity."}
---

# regulatory-compliance

## Scope and activation
Map and assess Vietnamese regulatory obligations for a defined business activity.
Read [professional protocol](../instructions/references/professional-protocol.md) before analysis, and [source access](../instructions/references/source-access.md) when sources must be retrieved. Apply these even on direct invocation.

## Inputs
Activities, entities, locations, sector, size, data flows, licenses, operational dates and existing controls.
Record missing material inputs; do not invent them.

## Workflow
1. Define the regulated activities and responsible entity; identify sector and local requirements.
2. Create an obligation register from verified applicable provisions, including triggers, deadlines and evidence requirements.
3. Compare actual controls and records with each obligation; distinguish not applicable, compliant, gap and unknown.
4. Prioritize gaps by legal exposure and operational impact separately; assign remediation owners and dates.
5. Define event-driven rechecks for legal or business changes; label any proposed monitoring as manual unless a real scheduler is configured.

## Professional checklist
- Applicability conditions
- Deadline anchor and calendar basis
- Evidence of control operation
- Unknown versus noncompliant

## Legal authority checks
Use the shared source and claim ledgers. Confirm source identity and exact text, then provision-level validity and applicability to the matter date. For this module, explicitly verify: applicability conditions and evidence of control operation. If unavailable, label the affected conclusion unverified. Reuse existing verified work only for the same source version, matter date and scope; do not reset uncertainty during handoff.

## Quality criteria
Every obligation has a source, applicability predicate and evidence test; no compliance certificate from unchecked self-report.
Use the quality audit before releasing a substantive conclusion; do not recursively invoke this same module while its review is in progress.

## Output
Obligation | source | trigger | due date | control evidence | status | legal risk | commercial impact | owner.

## Limits and handoff
Effective-date changes go to legal-validity-verification; contracts to contract review. No automatic surveillance, regulator filing or notification is implied.
Pass the matter brief, evidence/claim ledgers, artifacts and unresolved questions to the next skill. Route by exact sibling skill name in [router](../instructions/SKILL.md); load its SKILL.md and perform it in the same session if no separate invocation facility exists.
