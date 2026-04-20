# Label: `ai-providers`

## Purpose
Tracks work that integrates, evaluates, or updates AI/LLM provider services.

## When to Use
- Adding or changing provider SDK adapters
- Updating model routing, provider failover, or credentials flow
- Adding provider-specific QA, cost, or latency controls

## When Not to Use
- Generic prompt updates without provider-specific logic
- UI-only wording changes

## Related Labels
- `workflow-builder`
- `security`
- `enhancement`

## Sample Scenario
A pull request is opened to address work matching **ai-providers** scope. During triage, maintainers confirm the intent aligns with this label and apply related labels for routing, risk, and size.

## Automation Expectations
- If this label is applied to an issue/PR, automation should post a short guidance comment linking to this document.
- Label suggestion systems should treat this guide as source-of-truth for relevance scoring.
- Any rule changes for this label must be captured in this file in the same PR as workflow updates.

## Quality Checklist
- Usage boundaries are clear and non-overlapping with adjacent labels.
- At least one maintainers' workflow or triage action is documented.
- Related labels represent realistic co-labeling patterns.

## Last Updated
2026-04-20
