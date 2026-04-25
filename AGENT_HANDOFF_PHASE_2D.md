---
draft: true
title: Agent Handoff — Phase 2D
date: 2026-04-25
---

# Phase 2D Handoff: Agent Build and Publish Guardrails

## Overview

This session strengthened the shared agent instructions so future agents are less likely to confuse the public landing page with the separate `Home.md` page, or stop after a local build without pushing the deploy commit.

## What Changed

- Added landing-page semantics to the repo-wide agent instructions:
  - `index.md` is the public landing page at `/`
  - `Home.md` is a secondary orientation page
  - "Home page" should default to `index.md` unless the user explicitly means `Home.md`
- Added build/deploy guardrails:
  - use the local Quartz bootstrap wired through `npm run build`
  - verify `public/index.html` after landing-page changes
  - commit and push after a successful build so GitHub Pages redeploys
- Added the same guidance to `CLAUDE.md` and `GEMINI.md`.

## Files Edited

- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`
- `AGENT_HANDOFF_PHASE_2D.md`

## Verified

- The repository now clearly distinguishes the root landing page from the orientation page.
- The docs now tell the next agent to inspect the generated landing page and push the commit after a successful build.

## Uncertain

- The docs have been rebuilt locally, but the changes still need to be committed and pushed.

## Next Recommended Steps

1. Commit and push the doc guardrail updates so the next agent inherits them.
2. Keep the landing-page/image distinction in mind for future presentation edits: `index.md` is the root site entry point, `Home.md` is not.
