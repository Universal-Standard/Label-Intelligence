# Label Intelligence Documentation

## Purpose
This repository operationalizes label governance as a production system:
- Human-readable guidance for every label.
- Automation hooks for GitHub-native workflows.
- Repeatable governance with auditable updates.

## Production Rollout Checklist
- Enable **GitHub Pages** and publish from `/docs`.
- Enable **Discussions** and create categories: `Q&A`, `Policy`, `Automation`.
- Enable **Wiki** for process playbooks and postmortems.
- Enable **Projects** with columns: `Ideas`, `In Progress`, `Review`, `Done`.
- Enable **Issues** and retain the templates in `.github/ISSUE_TEMPLATE`.

## Governance Model
- Label guide files are source-of-truth for humans and bots.
- Changes to automation must be coupled with guide updates.
- Releases should include a short label-governance changelog entry.

## Core Docs
- Label catalog: [`labels/index.md`](labels/index.md)
- Changelog: [`meta/changelog.md`](meta/changelog.md)
