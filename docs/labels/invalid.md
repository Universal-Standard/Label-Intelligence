# Label: `invalid`

## Purpose
Marks reports or requests that are not actionable as submitted.

## When to Use
- Insufficient reproduction after follow-up
- Out-of-scope or unsupported environment reports
- Incorrect assumptions about project behavior

## When Not to Use
- Reports that need clarification but are potentially valid

## Related Labels
- `duplicate`
- `question`
- `wontfix`

## Sample Scenario
A pull request is opened to address work matching **invalid** scope. During triage, maintainers confirm the intent aligns with this label and apply related labels for routing, risk, and size.

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
