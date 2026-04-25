---
draft: true
title: Agent Handoff — Phase 2G
date: 2026-04-25
---

# Phase 2G Handoff: Landing Page Image Swap and Resize

## Overview

This session replaced the oversized Sandusky title-page image on the public landing page with a more visually interesting Tallman cemetery monument photo and scaled it down to half-width.

## What Changed

- Added `assets/tallman-monument.png` from the extracted burial image set.
- Updated `index.md` so the landing page now uses the Tallman monument image instead of the Sandusky title page.
- Sized the image with inline HTML so it renders at about half the previous visual width and stays centered.
- Recorded the change in `CHANGELOG.md`.

## Files Edited

- `index.md`
- `CHANGELOG.md`
- `AGENT_HANDOFF_PHASE_2G.md`

## Verified

- The image source exists at `References/raw/extracted/images/burials/burial-150.png`.
- The copied asset exists at `assets/tallman-monument.png`.
- The landing-page markup now points to the new image and constrains its width.

## Uncertain

- I have not yet rebuilt the site after the image swap in this session.
- The existing `Home.md` page still uses the old title-page image, by design for now.

## Next Recommended Steps

1. Run `npm run build` and confirm `public/index.html` shows the new image.
2. If you want the same treatment on `Home.md`, update that page separately.
3. Push the commit so GitHub Pages picks up the new landing page presentation.
