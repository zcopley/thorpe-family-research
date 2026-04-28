---
draft: true
title: Agent Handoff — Phase 2U
date: 2026-04-28
---

# Phase 2U Handoff: Book Outprints Pilot Extraction

## What Changed

- Processed the first book-outprints pilot batch from Thorpe Shared Intake.
- Extracted text from the two Watson Moses Risden Grand Army PDFs into `References/raw/processed/2026-04-24-book-outprints/Risden-Watson-Moses/`.
- Manually reviewed the image-only Sandusky-Beers John M. Lemmon PDF after `pdftotext` produced no usable text.
- Manually reviewed selected *Genealogy and History of Samuel Miller* GIF pages 240-242 because no local OCR engine was available.
- Created [[People/John McIntyre Lemmon|John McIntyre Lemmon]] and added book-source evidence to the Lemmon, Risden, Miller, and Tallman pages touched in this pass.

## Files Edited or Created

- [[People/John McIntyre Lemmon|People/John McIntyre Lemmon.md]]
- [[References/Book Outprints — Grand Army Records Watson Moses Risden|References/Book Outprints — Grand Army Records Watson Moses Risden.md]]
- [[References/Book Outprints — Sandusky-Beers Lemmon John M|References/Book Outprints — Sandusky-Beers Lemmon John M.md]]
- [[References/Book Outprints — Genealogy and History of Samuel Miller|References/Book Outprints — Genealogy and History of Samuel Miller.md]]
- [[References/Book Outprints Collection|References/Book Outprints Collection.md]]
- [[People/Watson Moses Risden|People/Watson Moses Risden.md]]
- [[People/Uriah Blake Lemmon|People/Uriah Blake Lemmon.md]]
- [[People/James Lemmon|People/James Lemmon.md]]
- [[People/Rebecca Blake|People/Rebecca Blake.md]]
- [[People/Emily Amanda MacIntyre|People/Emily Amanda MacIntyre.md]]
- [[People/Mathias Miller|People/Mathias Miller.md]]
- [[People/Romancy Miller|People/Romancy Miller.md]]
- [[People/Benjamin B Tallman|People/Benjamin B Tallman.md]]
- [[People/Miller Mathias Tallman|People/Miller Mathias Tallman.md]]
- [[Topics/Sandusky County Ohio - Lemmon Ault Settlement|Topics/Sandusky County Ohio - Lemmon Ault Settlement.md]]
- [[Topics/Linn County Iowa - Spicer Risden Settlement|Topics/Linn County Iowa - Spicer Risden Settlement.md]]
- [[People Directory|People Directory.md]]
- [[Search Index|Search Index.md]]
- [[CHANGELOG|CHANGELOG.md]]

## Verified vs Uncertain

- **Verified:** `pdftotext` successfully extracted the Grand Army text files.
- **Verified:** The Sandusky-Beers PDF is image-only under `pdftotext`; claims added from it were manually checked against generated page images.
- **Verified:** People Directory and Search Index now each link 112 person pages, matching the 112 person files.
- **Uncertain:** Grand Army gives Watson Moses Risden's death as 23 Jun 1932, while burial/census-summary sources give 30 Jun 1932.
- **Uncertain:** Sandusky-Beers gives Uriah Blake Lemmon's death as 16 Feb 1887 and Emily Amanda MacIntyre Lemmon's death as 12 Jul 1860, conflicting with earlier burial-derived dates.
- **Uncertain:** The Miller genealogy names Benjamin as Benjamin F. Tallman and Miller Mathias Tallman's wife as Lizzie Wimmer, conflicting with current vault naming and census-linked spouse evidence.

## Next Recommended Steps

1. Resolve the newly surfaced date/name conflicts against primary records before changing canonical facts.
2. Run OCR on the remaining GIF-heavy book outprints, starting with *Genealogy and History of Samuel Miller*, *Pioneer People of Fairfield County Ohio*, *MacIntyre*, and *Settlers by the Long Grey Trail*.
3. If OCR tooling is installed later, replace manual page summaries with fuller page-level transcriptions where needed.
