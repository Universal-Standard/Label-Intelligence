# Label: `group-b-auth`

## Purpose
Represents work scoped to Group B ownership for authentication domain.

## When to Use
- Auth-specific stories owned by Group B
- Permissions, identity, or session scope in Group B roadmap

## When Not to Use
- Unowned cross-team items without auth scope

## Related Labels
- `security`
- `critical`
- `workflow-builder`

## Sample Scenario
A pull request is opened to address work matching **group-b-auth** scope. During triage, maintainers confirm the intent aligns with this label and apply related labels for routing, risk, and size.

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
