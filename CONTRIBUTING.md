# Contributing

## Scope
Use this repository to define and maintain label semantics, automation rules, and contributor guidance.

## Contribution Rules
1. Update the relevant `docs/labels/<label>.md` file for any semantic change.
2. Keep `docs/labels/index.md` aligned with label additions/removals.
3. If automation behavior changes, update workflows/scripts in the same PR.
4. Use issue templates for proposing new labels or documentation fixes.

## Pull Request Expectations
- Explain the intended label behavior change.
- Include the affected label guides.
- Confirm docs quality checks pass.
- Apply at least one `size/*` label and one purpose label (`bug`, `enhancement`, etc.).

## Review Standards
- Avoid ambiguous overlap between labels.
- Preserve backward compatibility where possible.
- Document migration strategy when meaning changes significantly.
