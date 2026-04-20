# Label: `size/l`

## Purpose
Large scope change with broad impact and higher review complexity.

## When to Use
- Cross-cutting implementation touching many modules
- Substantial feature or migration work

## When Not to Use
- Small isolated patches

## Related Labels
- `size/m`
- `size/s`
- `critical`

## Sample Scenario
A pull request is opened to address work matching **size/l** scope. During triage, maintainers confirm the intent aligns with this label and apply related labels for routing, risk, and size.

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
