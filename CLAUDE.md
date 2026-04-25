---
title: CLAUDE.md — AI Agent Instructions
date: 2026-04-21
draft: true
---

# CLAUDE.md — Thorpe Family Research Vault

Read this file before making changes.

## Project Overview

A genealogical research wiki for the Thorpe family, maintained as a separate project from the Copley family vault. This vault is currently in early-source-ingestion phase.

- **Local clone:** `/mnt/c/Users/zach/Projects/thorpe-family-research`
- **Stack:** Quartz v4, Obsidian-style Markdown, GitHub Actions deployment
- **Initial source package:** Butch email + two `.cdr` pedigree timelines

## Repository Structure

- `People/` — person profiles
- `Places/` — place pages
- `Topics/` — thematic and methodology pages
- `References/` — source summaries
- `References/raw/` — raw source files (including binary source artifacts)
- `index.md` — public homepage
- `Home.md` — vault orientation
- `People Directory.md` — person index
- `Search Index.md` — keyword and entity index
- `CHANGELOG.md` — chronological change log with WikiLinks

## Landing Page Semantics

- `index.md` is the public landing page at `/`.
- `Home.md` is a secondary orientation page.
- When a request mentions the "home page" or "landing page," default to `index.md` unless the user explicitly means `Home.md`.

## Content Rules

### Frontmatter
Every page should include:
- `title`
- `date` (`YYYY-MM-DD`)
- `tags`

### Linking
- Use `[[WikiLinks]]` for all internal links.
- Use full-path links from root pages when helpful: `[[People/Full Name|Display Name]]`.

### Source Quality
- Distinguish clearly between confirmed facts and extraction plans.
- Do not infer unverified names/dates from binary `.cdr` files.
- Cite source files explicitly, including `References/raw/...` paths.
- For living people, avoid unsourced personal details.

### Changelog
- Every session update should be reflected in `CHANGELOG.md`.
- Include WikiLinks to all pages added or changed.

## Build and Deployment

- Required runtime: Node 22+
- Build command: `npm run build`
- Do not use `npx quartz build` without `-d .`
- After landing-page changes, verify the generated `public/index.html` matches the intended source before pushing.
- After a successful build, commit and push to `main` so the GitHub Actions deploy job can publish the update.

## Current Priority

Convert or export pedigree `.cdr` files into machine-readable form (PDF or images), then begin structured extraction into person and relationship pages.
