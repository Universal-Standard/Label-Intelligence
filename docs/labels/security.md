# Label: `security`

## Purpose
Flags vulnerabilities, risk mitigations, and security hardening work.

## When to Use
- Credential, authN/authZ, or data protection issues
- Dependency CVE remediation
- Policy, scanning, or threat mitigation updates

## When Not to Use
- General reliability issues without security impact

## Related Labels
- `critical`
- `dependencies`
- `group-b-auth`

## Sample Scenario
A pull request is opened to address work matching **security** scope. During triage, maintainers confirm the intent aligns with this label and apply related labels for routing, risk, and size.

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
