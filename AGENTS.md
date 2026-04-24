---
title: AGENTS.md — Thorpe Family Research Vault
date: 2026-04-21
draft: true
---

# AGENTS.md — Thorpe Family Research Vault

This file sets project-wide guidance for any AI agent working in this repository.

## Scope

These instructions apply to the entire `thorpe-family-research` repository.

## Project Intent

Build and maintain a source-grounded genealogical wiki for the Thorpe family as a standalone Quartz vault.

## Content Requirements

- Use `[[WikiLinks]]` for internal links.
- Keep source provenance explicit on every substantive claim.
- Do not infer names, dates, or relationships from inaccessible binary files.
- Treat living-person details conservatively unless confirmed by the user.

## Source Handling

Current seed sources:
- `References/raw/butch-thorpe-email.txt`
- `References/raw/PedigreeTimelines2025.cdr`
- `References/raw/PedigreeTimelines2019Descendants2.cdr`

Intake workflow folders:
- `References/raw/inbox/` for newly synced external files
- `References/raw/processed/` for files that have been reviewed and indexed
- `References/raw/archive/` for older material retained for provenance

The `.cdr` files require export to PDF/image before structured extraction can proceed.

## Required Session Outputs

At the end of each meaningful work session:
- Update `CHANGELOG.md` with WikiLinks to all changed pages.
- Create or update an `AGENT_HANDOFF_PHASE_*.md` file summarizing:
  - What changed
  - Which files were edited/created
  - What is verified vs uncertain
  - Next recommended steps

## Build and Validation

- Runtime: Node 22+
- Validate with:
  - `npm run test`
  - `npm run build`

## Mermaid Diagram Styling

All Mermaid diagrams must include explicit styling to ensure text legibility in both light and dark themes:

```
%%{init: {'flowchart': {'htmlLabels': true}, 'theme': 'default', 'themeVariables': {'primaryTextColor': '#000000', 'primaryBorderColor': '#333333', 'lineColor': '#333333', 'fontSize': '14px'}}}%%
```

Add this as the first line inside each Mermaid code block. This ensures:
- Dark text (#000000) for maximum contrast
- Dark border and line colors (#333333)
- Readable font size (14px)

Test diagrams in both light and dark browser themes before committing.

## Agent Files and Vault Privacy

- **Agent coordination files** (`AGENTS.md`, `AGENT_HANDOFF_PHASE_*.md`, `CLAUDE.md`, `GEMINI.md`) must have `draft: true` in frontmatter to exclude them from the published vault.
- Files with `draft: true` are invisible to human visitors but fully accessible in git and to agents reading the working repo.
- This keeps internal working notes out of the public wiki while preserving handoff continuity.
- When creating new agent guidance or handoff files, always remember to add `draft: true` to the frontmatter.

## Do Not

- Do not modify the Quartz framework internals unless explicitly requested.
- Do not add unsourced genealogical assertions.
- Do not remove raw source files from `References/raw/`.
- Do not publish agent coordination files to the human-facing vault (always use `draft: true`).
