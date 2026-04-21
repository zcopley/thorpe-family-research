---
title: GEMINI.md — AI Agent Instructions
date: 2026-04-21
draft: true
---

# Gemini Agent Protocol — Thorpe Family Research Vault

These instructions define how agents should operate in this repository.

## Purpose

Maintain a source-grounded Thorpe family genealogy wiki in Quartz v4 as a standalone project.

## Mandatory Standards

1. Use source-first workflows.
2. Preserve uncertainty explicitly.
3. Use `[[WikiLinks]]` for all internal references.
4. Keep `Search Index.md` and `People Directory.md` synchronized with newly added pages.
5. Update `CHANGELOG.md` each session with WikiLinks to all changed or created pages.

## Source Handling Rules

- Current core sources include:
  - `References/raw/butch-thorpe-email.txt`
  - `References/raw/PedigreeTimelines2025.cdr`
  - `References/raw/PedigreeTimelines2019Descendants2.cdr`
- `.cdr` files are not directly parseable as genealogical text in this environment; export is required before person-level extraction.
- Do not assert names, dates, or relationships not visible in an accessible source.

## Frontmatter Format

```yaml
---
title: Full Name or Page Title
date: YYYY-MM-DD
tags:
  - "#thorpe-family"
  - "#..."
---
```

## Build and Deploy

- Node: `>=22`
- Build: `npm run build`
- Deployment workflow: `.github/workflows/deploy.yml`

## Working Principle

When uncertain, capture as a research gap and link to the exact source file that needs extraction or verification.
