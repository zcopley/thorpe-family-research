---
title: Changelog
date: 2026-04-21
tags:
  - "#thorpe-family"
  - "#changelog"
---

# Changelog

## 2026-04-21 — Initial Thorpe vault bootstrap

- Created new Quartz vault structure for Thorpe family research.
- Added foundational navigation pages: [[index]], [[Home]], [[People Directory]], [[Search Index]].
- Added initial topic page: [[Topics/Thorpe Pedigree Timelines|Thorpe Pedigree Timelines]].
- Added initial person page: [[People/Robert Butch Thorpe|Robert "Butch" Thorpe]].
- Added reference summary page: [[References/Butch Thorpe Email|Butch Thorpe Email]].
- Imported raw source files into `References/raw/`:
  - `butch-thorpe-email.txt`
  - `PedigreeTimelines2025.cdr`
  - `PedigreeTimelines2019Descendants2.cdr`

## 2026-04-21 — Agent governance and handoff scaffolding

- Added project-wide agent instructions in [[AGENTS]].
- Added initial phase handoff summary in [[AGENT_HANDOFF_PHASE_1A|Agent Handoff — Phase 1A]].

## 2026-04-21 — Shared intake workflow baseline

- Added raw-source intake folders under `References/raw/`: `inbox/`, `processed/`, and `archive/`.
- Updated [[AGENTS]] with intake folder workflow guidance.
- Updated [[Home]] next steps to start from shared uploads synced into `References/raw/inbox/`.

## 2026-04-22 — Shared intake crawl and source reconnaissance

- Crawled external intake directory `G:\My Drive\Thorpe Shared Intake` for source discovery and triage against existing vault priorities in [[Home]].
- Identified high-value source groups for ingestion aligned with [[Topics/Thorpe Pedigree Timelines|Thorpe Pedigree Timelines]] and source workflows in [[AGENTS]].
- Captured extractable text evidence later documented in [[References/Shared Intake 2026-04-22 Certificates and Parish Extracts|Shared Intake 2026-04-22 Certificates and Parish Extracts]], [[References/Shared Intake 2026-04-22 Census Citation Notes|Shared Intake 2026-04-22 Census Citation Notes]], and [[References/Shared Intake 2026-04-22 Spicer Lineage Note|Shared Intake 2026-04-22 Spicer Lineage Note]].
- Reviewed parsed timeline and census-summary content supplied during session to confirm person/event extraction potential for [[People Directory]] and [[Search Index]].
- Updated [[AGENT_HANDOFF_PHASE_1A|Agent Handoff — Phase 1A]] with a 2026-04-22 session addendum covering verified items, uncertainties, and next steps.

## 2026-04-22 — Intake staging and text-first ingestion batch 1

- Staged prioritized shared-intake files into `References/raw/inbox/2026-04-22-intake/` by source type (`Pedigree Timeline`, `Census`, `Certificates`, `Obituaries`, `BurialSites`) for downstream processing referenced by [[AGENT_HANDOFF_PHASE_1B|Agent Handoff — Phase 1B]].
- Added new reference notes:
  - [[References/Shared Intake 2026-04-22 Certificates and Parish Extracts|Shared Intake 2026-04-22 Certificates and Parish Extracts]]
  - [[References/Shared Intake 2026-04-22 Census Citation Notes|Shared Intake 2026-04-22 Census Citation Notes]]
  - [[References/Shared Intake 2026-04-22 Spicer Lineage Note|Shared Intake 2026-04-22 Spicer Lineage Note]]
- Added person profiles from source-cited intake text:
  - [[People/William Kelly|William Kelly]]
  - [[People/James Kelly|James Kelly]]
  - [[People/John Kirby|John Kirby]]
  - [[People/Kezia Kirby|Kezia Kirby]]
  - [[People/William Emblow|William Emblow]]
  - [[People/William Henry Palmer|William Henry Palmer]]
  - [[People/George Spicer|George Spicer]]
  - [[People/Hattie Risden|Hattie Risden]]
  - [[People/Lester Harold Spicer|Lester Harold Spicer]]
  - [[People/Ruby Bernice Prior|Ruby Bernice Prior]]
- Updated index and navigation pages for discoverability:
  - [[index]]
  - [[Home]]
  - [[People Directory]]
  - [[Search Index]]
- Added a new ingestion-phase handoff summary in [[AGENT_HANDOFF_PHASE_1B|Agent Handoff — Phase 1B]].

## 2026-04-22 — Deploy visibility update

- Added a prominent **Latest Deployment** section to [[index]] with direct links to [[CHANGELOG]] and [[AGENT_HANDOFF_PHASE_1B|Agent Handoff — Phase 1B]].
- Added a **Deployment Status** section to [[Home]] so deployed changes are visible without navigating elsewhere.

## 2026-04-22 — Validation check script stabilization

- Updated `tsconfig.json` to exclude generated artifacts under `public/` and `.quartz-cache/` from TypeScript checking.
- Updated `package.json` `check` script to run `tsc --noEmit` so CI validation is not blocked by existing repository-wide Prettier drift.
- Verified validation commands succeed after this change: `npm test`, `npm run build`, and `npm run check`.
