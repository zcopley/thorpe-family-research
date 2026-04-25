---
draft: true
title: Agent Handoff — Phase 2C
date: 2026-04-25
---

# Phase 2C Handoff: Landing Page Image Placement

## Overview

This session moved the historical title-page image onto the actual site landing page (`index.md`), which is what the user meant by "home page."

## What Changed

- Added the Sandusky and Ottawa, Ohio title-page image to `index.md` so it renders on the landing page at `/`.
- Kept the existing image on `Home.md` unchanged.
- Added a changelog entry documenting the presentation change.

## Files Edited

- `index.md`
- `CHANGELOG.md`
- `AGENT_HANDOFF_PHASE_2C.md`

## Verified

- The image path already exists at `assets/sandusky-ottawa-1896-titlepage.gif`.
- `public/Home.html` previously rendered the image correctly.
- The root landing page now has the same image in source.

## Uncertain

- The site has been rebuilt in this session, so `public/index.html` now includes the landing-page image, but the change still needs to be pushed.

## Next Recommended Steps

1. Push the current commit so GitHub Pages picks up the updated landing page.
2. If the root page still looks wrong after deploy, re-check `index.md` rather than `Home.md`.
