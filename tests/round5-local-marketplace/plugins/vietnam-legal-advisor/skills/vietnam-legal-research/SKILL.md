---
{"name": "vietnam-legal-research", "description": "Research Vietnamese legislation and compare provisions for a defined legal question."}
---

# vietnam-legal-research

## Scope and activation
Research Vietnamese legislation and compare provisions for a defined legal question.
Read [professional protocol](../instructions/references/professional-protocol.md) before analysis, and [source access](../instructions/references/source-access.md) when sources must be retrieved. Apply these even on direct invocation.

## Inputs
Question, jurisdiction, event dates, entities, sector, supplied documents and desired depth.
Record missing material inputs; do not invent them.

## Workflow
1. Decompose the question into issues and factual predicates; identify missing material facts.
2. Search primary sources by exact identifier and legal concepts, including synonyms; record search scope and retrieval failures.
3. Read operative provisions and linked amendments; send applicability questions to legal-validity-verification.
4. Build a claim-to-source matrix; compare general and sector-specific provisions without assuming the latter automatically prevails.
5. Apply each supported rule to known facts; give conditional conclusions and the remaining research tasks. If offline, without texts or without a defined topic, provide an immediate verification sequence rather than only offering to make a plan later: define the issue/jurisdiction/event and review dates -> obtain the operative original from an official publication channel -> read exact provisions and linked amendments, repeal and transition -> verify provision-level applicability to the event -> record source identity, pinpoint, retrieval evidence and unresolved claims before answering. If the topic is absent, leave search terms/identifiers to be filled after clarification; do not invent them. State that these are planned steps, not completed searches.

## Professional checklist
- Coverage of exceptions and definitions
- National versus local competence
- Conflicting provisions and hierarchy
- No inference from search silence

## Legal authority checks
Use the shared source and claim ledgers. Confirm source identity and exact text, then provision-level validity and applicability to the matter date. For this module, explicitly verify: coverage of exceptions and definitions and conflicting provisions and hierarchy. If unavailable, label the affected conclusion unverified. Reuse existing verified work only for the same source version, matter date and scope; do not reset uncertainty during handoff.

## Quality criteria
Each dispositive proposition has an applicable source or an explicit unverified label; competing interpretations are addressed.
Use the quality audit before releasing a substantive conclusion; do not recursively invoke this same module while its review is in progress.

## Output
Answer-first memo: issue | applicable rule | source ID and pinpoint | application | uncertainty; finish with sources and next steps.

## Limits and handoff
Historical applicability goes to legal-validity-verification; contract edits go to vietnam-contract-review; do not assert exhaustive research or provide a categorical answer when key sources are unavailable.
Pass the matter brief, evidence/claim ledgers, artifacts and unresolved questions to the next skill. Route by exact sibling skill name in [router](../instructions/SKILL.md); load its SKILL.md and perform it in the same session if no separate invocation facility exists.
