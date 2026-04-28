---
title: Shared Intake 2026-04-24 Census InDesign Summaries
date: 2026-04-24
tags:
  - "#thorpe-family"
  - "#census"
  - "#source"
---

# Shared Intake 2026-04-24: Census InDesign Summaries

## Overview

This intake batch contains 88 individual Census InDesign summary PDFs extracted from the shared intake folder. Each PDF is a professionally formatted single-page census summary for one person, compiled from UK Census records (primarily 1841-1871).

## Source Format & Quality

- **Format:** InDesign-compiled PDFs with structured census data tables
- **Coverage:** Primarily UK censuses (HO107, RG9, RG10, RG11, RG12, RG13 series)
- **Time span:** 1841-1871 (some individuals span wider date ranges)
- **Data included per person:**
  - Birth/death dates (when available)
  - Multiple census year entries with locations
  - Household composition (relationships, ages, occupations)
  - Precise source citations (class, piece, folio, page, GSU roll)
  - Geographic locations (parish, township, street address)

## Index of 88 Individuals

### A
- Ault, Andrew
- Ault, Elizabeth
- Ault, Frederick

### B
- Bangle, Elizabeth
- Bangle, Louis S
- Barton, Sarah
- Baxter, Matilda
- Bellamy, Henry James
- Bellamy, James
- Bellamy, James A
- Bellamy, Richard
- Beneworthworth, Hannah
- Bevis, Ann
- Blake, Rebecca
- Brooks, Elizabeth
- Burdick, Saphronia

### C
- Caswell, Angeline
- Critton, Amy

### D
- Darling, Erastus
- Darling, Sarah
- Dunham, William

### E
- Eke, George
- Emblow, Eleanor
- Emblow, Joseph
- Emblow, Kezia

### F
- Filkins, Catherine
- Flowers, Samuel
- Flowers, William

### G
- Granger, Louisa
- Greenwood, Mary
- Greenwood, Sarah
- Grookey, Hannah
- Gunther, John

### H
- Harrison, Elizabeth
- Houghton, William

### I
- Ireland, Eleanor
- Ireland, James

### K
- Kelly, James
- Kelly, Martha
- Kelly, Sarah
- Kirby, Alice
- Kirby, John

### L
- Lemmon, Hugh
- Lemmon, James
- Lemmon, Martha
- Lewis, Oliver
- Lewis, Susan
- Lewis, Wynat

### M
- McIntyre, Emily
- McIntyre, William
- Meadows, Alice
- Medford, George
- Miller, Samuel
- Molyneux, John
- Monson, Arthur
- Morgan, Alzina
- Mullet, John

### N
- Neilson, John

### P
- Palmer, Elizabeth
- Palmer, John K
- Palmer, William Henry
- Prior, Arthur Edwin
- Prior, Oliver Warren
- Prior, Ruby Bernice
- Pryor, Alzina

### Q
- Quackenbush, Elizabeth A

### R
- Risden, Watson Moses
- Risden, John Wheeler
- Rowland, Nancy West

### S
- Smedley, Damaris
- Sorrell, Ann
- Sorrell, Mary
- Spicer, Charles Russell
- Spicer, George B
- Spicer, Lester Harold
- Spicer, Nathan
- Spicer, Ruby Bernice

### T
- Tallman, Benjamin B
- Tallman, Lenore Hetty
- Tallman, Miller Mathias
- Thorogood, Frederick
- Thorogood, Grace Caroline
- Thorogood, James
- Thorpe, Uriah Blake
- Thorpe, Raymond Miller

### V
- Van Horn, Mary

### W
- Watson, George
- Westwood, George
- Wheeler, Mary
- Whitfield, John
- Whitfield, Mary
- Willson, Jane

## Extraction Method

Text extracted from PDF using `pdftotext -layout` to preserve table structure:

```bash
pdftotext -layout "CensusSummary-{FirstName}{LastName}.pdf" "CensusSummary-{FirstName}{LastName}.txt"
```

## Files Generated

- Individual .txt files for each of 88 people: `CensusSummary-{FirstName}{LastName}.txt`
- Located in: `References/raw/inbox/2026-04-24-census-indesign/`

## Next Steps for Integration

1. Cross-reference these summaries with existing [[People Directory]] entries
2. For individuals without existing pages, create new profiles with this census data
3. For individuals with existing pages, augment with detailed census household and location information
4. Create additional reference pages by thematic group (e.g., UK parishes, occupation clusters)
5. Mark ambiguous identities (e.g., Eleanor Emblow vs Eleanor Ireland) for reconciliation

## Related Sources

- [[References/Shared Intake 2026-04-22 Census Summary Individuals p1-p10|Census Summary Individuals p1-p10]] (earlier batch)
- [[References/Shared Intake 2026-04-22 Census Summary Individuals p11-p20|Census Summary Individuals p11-p20]]
- `References/raw/inbox/2026-04-22-intake/Census/CensusSummaryIndividual.pdf` (original bulk extract)
- `References/raw/inbox/2026-04-22-intake/Census/Ancestors in the Census.txt` (indexed ancestor list)

## Notes

- Some individuals have spelling variants across census years (e.g., KELLY/KELLEY, RISDEN/RISDON)
- Birth/death dates in headers are compilations; image-level verification is recommended
- Occupation field OCR quality varies; some entries may have transcription artifacts
- GSU (Genealogical Society of Utah) roll numbers reference microfilm copies held by FamilySearch
