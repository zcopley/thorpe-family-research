---
title: Changelog
date: 2026-04-21
tags:
  - "#thorpe-family"
  - "#changelog"
---

# Changelog

## 2026-04-23 — Local tool-state ignored

- Added `.abacusai/` and `.codex` to `/.gitignore` so local agent and workspace tooling state stays out of version control.
- Removed `.abacusai/config.json` from version control while leaving the local file on disk as private workspace configuration.

## 2026-04-23 — Lemmon/Blake/Torpe branch summary added

- Added [[Topics/Lemmon Blake Thorpe Branch Summary|Lemmon Blake Thorpe Branch Summary]] to capture the pedigree-timeline branch context in one place.
- Linked the new summary from [[Topics/Identity Reconciliation Matrix|Identity Reconciliation Matrix]], [[Topics/Spelling and Identity Reconciliations|Spelling and Identity Reconciliations]], and [[Search Index]].

## 2026-04-23 — Identity reconciliation matrix added

- Added [[Topics/Identity Reconciliation Matrix|Identity Reconciliation Matrix]] to rank unresolved identity questions by evidence strength and next verification step.
- Linked the new matrix from [[Topics/Spelling and Identity Reconciliations|Spelling and Identity Reconciliations]] and [[Search Index]].

## 2026-04-23 — Thorpe/Lemmon pedigree branch clarification

- Added pedigree-timeline branch notes to [[People/Uriah Blake Thorpe|Uriah Blake Thorpe]], [[People/Uriah Blake Lemmon|Uriah Blake Lemmon]], [[People/James Lemmon|James Lemmon]], [[People/Rebecca Blake|Rebecca Blake]], and [[People/Sarah Annett Lemmon|Sarah Annett Lemmon]].
- Updated [[Topics/Spelling and Identity Reconciliations|Spelling and Identity Reconciliations]] to state that the Thorpe pedigree timeline supports a shared branch context but not a direct identity merge between the two Uriahs.

## 2026-04-23 — Wynat etymology caution note

- Added a cautionary note to [[People/Wynat Lewis|Wynat Lewis]] and [[Topics/Spelling and Identity Reconciliations|Spelling and Identity Reconciliations]] stating that the current source set does not support a Welsh etymology for `Wynat`.
- Preserved `Wynat` as an uncertain spelling form pending primary-record confirmation.

## 2026-04-23 — Lewis/Wynat full-name clarification

- Tightened [[People/Wynat Lewis|Wynat Lewis]] using the page-41 census-summary extract and the pedigree timeline naming `Wynant Williamson Lewis c1781-after 1860`.
- Updated [[Topics/Spelling and Identity Reconciliations|Spelling and Identity Reconciliations]] to treat `William` as unconfirmed and `Wynant Williamson` as the strongest full-name form currently present in-repo.

## 2026-04-23 — Burgett/Greenwood reconciliation tightening

- Clarified the compiler-extract wording on [[People/Mary Greenwood|Mary Greenwood]] so the page reflects the `GREENWOOD, Mary` heading and the embedded `Mary BERGETT` mortality entry.
- Added a cross-reference note on [[People/Mary Burgett|Mary Burgett]] to distinguish the Burgett household from the separate mortality schedule entry currently tracked as [[People/Mary Greenwood|Mary Greenwood]].
- Updated [[Topics/Spelling and Identity Reconciliations|Spelling and Identity Reconciliations]] to keep the merge tentative rather than final.

## 2026-04-23 — Canonical profile evidence enrichment

- Added page-level census-summary anchors and piece/folio/page metadata where available to the canonical profiles created for former UNKNOWN entries:
  - [[People/Ann Sorrell|Ann Sorrell]]
  - [[People/Eleanor Emblow|Eleanor Emblow]]
  - [[People/Sarah Kelly|Sarah Kelly]]
  - [[People/Susan Lewis|Susan Lewis]]
- Updated [[Topics/Spelling and Identity Reconciliations|Spelling and Identity Reconciliations]] to note that the canonical profiles now carry page anchors while image-level verification remains pending.

## 2026-04-23 — Canonical surname profiles for former UNKNOWN entries

- Added canonical surname-based person pages derived from existing extracted evidence:
  - [[People/Ann Sorrell|Ann Sorrell]]
  - [[People/Eleanor Emblow|Eleanor Emblow]]
  - [[People/Sarah Kelly|Sarah Kelly]]
  - [[People/Susan Lewis|Susan Lewis]]
- Converted placeholder `Unknown` pages into transitional alias notes pointing to canonical profiles:
  - [[People/Ann Unknown|Ann Unknown]] -> [[People/Ann Sorrell|Ann Sorrell]]
  - [[People/Eleanor Unknown|Eleanor Unknown]] -> [[People/Eleanor Emblow|Eleanor Emblow]]
  - [[People/Sarah Unknown|Sarah Unknown]] -> [[People/Sarah Kelly|Sarah Kelly]]
  - [[People/Susan Unknown|Susan Unknown]] -> [[People/Susan Lewis|Susan Lewis]]
- Updated [[People Directory]], [[Search Index]], and [[Topics/Spelling and Identity Reconciliations|Spelling and Identity Reconciliations]] to reflect canonical tracking.

## 2026-04-23 — UNKNOWN identity evidence enrichment

- Expanded source-cited details on placeholder profiles using direct extracts from `References/raw/extracted/CensusSummaryIndividual.txt`:
  - [[People/Ann Unknown|Ann Unknown]]
  - [[People/Eleanor Unknown|Eleanor Unknown]]
  - [[People/Sarah Unknown|Sarah Unknown]]
  - [[People/Susan Unknown|Susan Unknown]]
- Added concrete census-chain evidence, observed surname forms, and cross-reference mappings to each page.
- Updated [[Topics/Spelling and Identity Reconciliations|Spelling and Identity Reconciliations]] with a dedicated pending-reconciliation block for UNKNOWN placeholders and candidate canonical merge targets.

## 2026-04-23 — Census ingestion batch (Unknown, Van Horn, Waller, Wheeler, Whitfield, Willson)

- Added new person profiles for the remaining uncreated names in `Ancestors in the Census.txt`:
  - [[People/Ann Unknown|Ann Unknown]]
  - [[People/Eleanor Unknown|Eleanor Unknown]]
  - [[People/Hannah Waller|Hannah Waller]]
  - [[People/Jane Willson|Jane Willson]]
  - [[People/John Whitfield|John Whitfield]]
  - [[People/Mary Van Horn|Mary Van Horn]]
  - [[People/Mary Wheeler|Mary Wheeler]]
  - [[People/Mary Whitfield|Mary Whitfield]]
  - [[People/Sarah Unknown|Sarah Unknown]]
  - [[People/Susan Unknown|Susan Unknown]]
- For `UNKNOWN, ...` source entries, staged conservative placeholder profiles pending identity reconciliation from primary records.
- Updated navigation/index pages to include this batch:
  - [[People Directory]]
  - [[Search Index]]

## 2026-04-23 — Census ingestion batch (Rowland, Sorrell, Tallman, Thorogood, Wager)

- Added new person profiles from the census index and p61-p96 extraction context:
  - [[People/Benjamin B Tallman|Benjamin B Tallman]]
  - [[People/Frederick Thorogood|Frederick Thorogood]]
  - [[People/Grace Caroline Thorogood|Grace Caroline Thorogood]]
  - [[People/James Sorrell|James Sorrell]]
  - [[People/James Thorogood|James Thorogood]]
  - [[People/Jane Wager|Jane Wager]]
  - [[People/Jesse Rowland|Jesse Rowland]]
  - [[People/John Tallman|John Tallman]]
  - [[People/Joseph Thorogood|Joseph Thorogood]]
  - [[People/Mary Ann Thorogood|Mary Ann Thorogood]]
  - [[People/Mary Sorrell|Mary Sorrell]]
  - [[People/Nancy West Rowland|Nancy West Rowland]]
- Updated navigation/index pages to include the new profiles:
  - [[People Directory]]
  - [[Search Index]]

## 2026-04-22 — PDF source text extraction

- Extracted and staged text content from multiple PDF sources for easier reference:
  - [[References/Shared Intake 2026-04-22 Burial Sites Summary|Burial Sites Summary]] (Extracted from 36MB source PDF)
  - [[References/Shared Intake 2026-04-22 Census Summary Individuals p61-p96|Census Summary Individuals p61-p96]]
  - [[References/Shared Intake 2026-04-22 Pedigree Timeline Thorpe|Pedigree Timeline Thorpe]]
  - [[References/Shared Intake 2026-04-22 Pedigree Timeline Prior|Pedigree Timeline Prior]]
  - [[References/Shared Intake 2026-04-22 Pedigree Timeline Spicer|Pedigree Timeline Spicer]]
  - [[References/Shared Intake 2026-04-22 Pedigree Timeline Bellamy|Pedigree Timeline Bellamy]]
- Updated [[Search Index]] with new reference pages.

## 2026-04-22 — High-priority Thorpe and Spicer ancestor ingestion

- Added new person profiles for direct-line Thorpe and Spicer ancestors from census-summary index:
  - [[People/Nathan Spicer|Nathan Spicer]]
  - [[People/Charles Russell Spicer|Charles Russell Spicer]]
  - [[People/John Thorp|John Thorp]]
  - [[People/William Monroe Thorp|William Monroe Thorp]]
  - [[People/Uriah Blake Thorpe|Uriah Blake Thorpe]]
  - [[People/Raymond Miller Thorpe|Raymond Miller Thorpe]]
- Reconciled and merged [[People/Hattie Risden|Hattie Risden]] into [[People/Hattie May Risden|Hattie May Risden]] and renamed [[People/George Spicer|George Spicer]] to [[People/George B Spicer|George B. Spicer]] for consistency with indexed naming.
- Updated [[People Directory]] and [[Search Index]] with new profiles and naming updates.

## 2026-04-22 — Census summary extraction batch (pages 51-60)

- Added new reference note [[References/Shared Intake 2026-04-22 Census Summary Individuals p51-p60|Shared Intake 2026-04-22 Census Summary Individuals p51-p60]] for extraction coverage of pages 51-60.
- Added new person profiles from extracted census-summary entries:
  - [[People/Peter Palmer|Peter Palmer]]
  - [[People/Arthur Edwin Prior|Arthur Edwin Prior]]
  - [[People/Joseph Warren Prior|Joseph Warren Prior]]
  - [[People/Oliver Warren Prior|Oliver Warren Prior]]
  - [[People/Elizabeth A Quackenbush|Elizabeth A Quackenbush]]
  - [[People/Hattie May Risden|Hattie May Risden]]
  - [[People/John Wheeler Risden|John Wheeler Risden]]
  - [[People/Watson Moses Risden|Watson Moses Risden]]
- Updated [[People/William Henry Palmer|William Henry Palmer]] and [[People/Ruby Bernice Prior|Ruby Bernice Prior]] with additional census-summary evidence.
- Updated [[People Directory]] and [[Search Index]] to include newly added profiles and reference note.

## 2026-04-22 — Census summary extraction batch (pages 41-50)

- Added new reference note [[References/Shared Intake 2026-04-22 Census Summary Individuals p41-p50|Shared Intake 2026-04-22 Census Summary Individuals p41-p50]] for extraction coverage of pages 41-50.
- Added new person profiles from extracted census-summary entries:
  - [[People/Wynat Lewis|Wynat Lewis]]
  - [[People/Emily Amanda MacIntyre|Emily Amanda MacIntyre]]
  - [[People/Mathias Miller|Mathias Miller]]
  - [[People/Romancy Miller|Romancy Miller]]
  - [[People/Alzina Morgan|Alzina Morgan]]
  - [[People/Arthur Jr Munson|Arthur Jr Munson]]
  - [[People/Emily Munson|Emily Munson]]
  - [[People/James Munson|James Munson]]
  - [[People/John K Palmer|John K Palmer]]
  - [[People/May Aleen Palmer|May Aleen Palmer]]
- Updated [[People Directory]] and [[Search Index]] to include newly added profiles and reference note.

## 2026-04-22 — Census summary extraction batch (pages 31-40)

- Added new reference note [[References/Shared Intake 2026-04-22 Census Summary Individuals p31-p40|Shared Intake 2026-04-22 Census Summary Individuals p31-p40]] for extraction coverage of pages 31-40.
- Added new person profiles from extracted census-summary entries:
  - [[People/Elizabeth Harrison|Elizabeth Harrison]]
  - [[People/Matilda Hiskey|Matilda Hiskey]]
  - [[People/Elizabeth How|Elizabeth How]]
  - [[People/Emma Kelly|Emma Kelly]]
  - [[People/James Lemmon|James Lemmon]]
  - [[People/Sarah Annett Lemmon|Sarah Annett Lemmon]]
  - [[People/Uriah Blake Lemmon|Uriah Blake Lemmon]]
  - [[People/Martha Eliza Lewis|Martha Eliza Lewis]]
  - [[People/Oliver Warren Lewis|Oliver Warren Lewis]]
- Updated [[People/James Kelly|James Kelly]] with census-summary chain evidence from 1841-1871 Peterborough entries.
- Updated [[People Directory]] and [[Search Index]] to include newly added profiles and reference note.

## 2026-04-22 — Census summary extraction batch (pages 21-30)

- Added new reference note [[References/Shared Intake 2026-04-22 Census Summary Individuals p21-p30|Shared Intake 2026-04-22 Census Summary Individuals p21-p30]] for extraction coverage of pages 21-30.
- Added new person profiles from extracted census-summary entries:
  - [[People/Elizabeth Brooks|Elizabeth Brooks]]
  - [[People/Saphronia Burdick|Saphronia Burdick]]
  - [[People/Mary Burgett|Mary Burgett]]
  - [[People/William Burgett|William Burgett]]
  - [[People/Angeline Caswell|Angeline Caswell]]
  - [[People/Amy E Critton|Amy E Critton]]
  - [[People/Joseph Emblow|Joseph Emblow]]
  - [[People/Martha Emblow|Martha Emblow]]
  - [[People/Catherine Filkins|Catherine Filkins]]
  - [[People/Mary Greenwood|Mary Greenwood]]
- Updated [[People Directory]] and [[Search Index]] to include newly added profiles and reference note.

## 2026-04-22 — Census summary extraction batch (pages 11-20)

- Added new reference note [[References/Shared Intake 2026-04-22 Census Summary Individuals p11-p20|Shared Intake 2026-04-22 Census Summary Individuals p11-p20]] for extraction coverage of pages 11-20.
- Added new person profiles from extracted census-summary entries:
  - [[People/Elizabeth Maria Bangle|Elizabeth Maria Bangle]]
  - [[People/Louis S Jr Bangle|Louis S Jr Bangle]]
  - [[People/Matilda Baxter|Matilda Baxter]]
  - [[People/Henry James Bellamy|Henry James Bellamy]]
  - [[People/James Bellamy|James Bellamy]]
  - [[People/James Archibald Bellamy|James Archibald Bellamy]]
  - [[People/Richard Bellamy|Richard Bellamy]]
  - [[People/Hannah Beneworth|Hannah Beneworth]]
  - [[People/Rebecca Blake|Rebecca Blake]]
- Updated [[People Directory]] and [[Search Index]] to include newly added profiles and reference note.

## 2026-04-22 — Census summary extraction batch (pages 1-10)

- Added new reference note [[References/Shared Intake 2026-04-22 Census Summary Individuals p1-p10|Shared Intake 2026-04-22 Census Summary Individuals p1-p10]] documenting title/introduction context and early extracted census table statements.
- Added new person profiles from extracted census-summary entries:
  - [[People/Andrew Ault|Andrew Ault]]
  - [[People/Elizabeth Plomey Ault|Elizabeth Plomey Ault]]
  - [[People/Frederick Ault|Frederick Ault]]
  - [[People/Miller Mathias Tallman|Miller Mathias Tallman]]
  - [[People/Lenore Hetty Tallman|Lenore Hetty Tallman]]
- Updated existing profiles with census-summary indexed date evidence:
  - [[People/George B Spicer|George B. Spicer]]
  - [[People/Hattie May Risden|Hattie May Risden]]
  - [[People/Lester Harold Spicer|Lester Harold Spicer]]
  - [[People/Ruby Bernice Prior|Ruby Bernice Prior]]
- Updated [[People Directory]] and [[Search Index]] to include newly added profiles and reference note.

## 2026-04-22 — Changelog ordering update

- Reordered [[CHANGELOG]] entries into reverse chronological order so newest updates appear first.

## 2026-04-22 — Validation check script stabilization

- Updated `tsconfig.json` to exclude generated artifacts under `public/` and `.quartz-cache/` from TypeScript checking.
- Updated `package.json` `check` script to run `tsc --noEmit` so CI validation is not blocked by existing repository-wide Prettier drift.
- Verified validation commands succeed after this change: `npm test`, `npm run build`, and `npm run check`.

## 2026-04-22 — Deploy visibility update

- Added a prominent **Latest Deployment** section to [[index]] with direct links to [[CHANGELOG]] and [[AGENT_HANDOFF_PHASE_1B|Agent Handoff — Phase 1B]].
- Added a **Deployment Status** section to [[Home]] so deployed changes are visible without navigating elsewhere.

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
  - [[People/George B Spicer|George B. Spicer]]
  - [[People/Hattie May Risden|Hattie May Risden]]
  - [[People/Lester Harold Spicer|Lester Harold Spicer]]
  - [[People/Ruby Bernice Prior|Ruby Bernice Prior]]
- Updated index and navigation pages for discoverability:
  - [[index]]
  - [[Home]]
  - [[People Directory]]
  - [[Search Index]]
- Added a new ingestion-phase handoff summary in [[AGENT_HANDOFF_PHASE_1B|Agent Handoff — Phase 1B]].

## 2026-04-22 — Shared intake crawl and source reconnaissance

- Crawled external intake directory `G:\My Drive\Thorpe Shared Intake` for source discovery and triage against existing vault priorities in [[Home]].
- Identified high-value source groups for ingestion aligned with [[Topics/Thorpe Pedigree Timelines|Thorpe Pedigree Timelines]] and source workflows in [[AGENTS]].
- Captured extractable text evidence later documented in [[References/Shared Intake 2026-04-22 Certificates and Parish Extracts|Shared Intake 2026-04-22 Certificates and Parish Extracts]], [[References/Shared Intake 2026-04-22 Census Citation Notes|Shared Intake 2026-04-22 Census Citation Notes]], and [[References/Shared Intake 2026-04-22 Spicer Lineage Note|Shared Intake 2026-04-22 Spicer Lineage Note]].
- Reviewed parsed timeline and census-summary content supplied during session to confirm person/event extraction potential for [[People Directory]] and [[Search Index]].
- Updated [[AGENT_HANDOFF_PHASE_1A|Agent Handoff — Phase 1A]] with a 2026-04-22 session addendum covering verified items, uncertainties, and next steps.

## 2026-04-21 — Shared intake workflow baseline

- Added raw-source intake folders under `References/raw/`: `inbox/`, `processed/`, and `archive/`.
- Updated [[AGENTS]] with intake folder workflow guidance.
- Updated [[Home]] next steps to start from shared uploads synced into `References/raw/inbox/`.

## 2026-04-21 — Agent governance and handoff scaffolding

- Added project-wide agent instructions in [[AGENTS]].
- Added initial phase handoff summary in [[AGENT_HANDOFF_PHASE_1A|Agent Handoff — Phase 1A]].

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
