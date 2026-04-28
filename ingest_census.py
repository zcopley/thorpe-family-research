#!/usr/bin/env python3
"""
Ingest census summary files from References/raw/inbox/2026-04-24-census-indesign/
into corresponding person pages.
"""

import os
import re
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Tuple

INBOX_DIR = Path("References/raw/inbox/2026-04-24-census-indesign")
PEOPLE_DIR = Path("People")
RAW_INBOX_REF = "References/raw/inbox/2026-04-24-census-indesign"

def parse_census_summary(file_path: Path) -> Dict:
    """Parse a census summary file and extract key information."""
    content = file_path.read_text(encoding='utf-8')

    result = {
        'file_path': file_path,
        'filename': file_path.name,
        'full_content': content,
        'name': None,
        'dates': None,
        'birth_date': None,
        'death_date': None,
        'birth_location': None,
        'census_entries': []
    }

    lines = content.split('\n')

    # First line usually contains: NAME, (Birth Date - Death Date)
    if lines:
        first_line = lines[0].strip()
        # Extract name and dates from first line
        if '(' in first_line and ')' in first_line:
            name_part = first_line[:first_line.index('(')].strip()
            dates_part = first_line[first_line.index('(')+1:first_line.index(')')].strip()
            result['name'] = name_part
            result['dates'] = dates_part

            # Parse birth/death dates
            if '-' in dates_part:
                parts = [p.strip() for p in dates_part.split('-')]
                if len(parts) >= 1:
                    result['birth_date'] = parts[0]
                if len(parts) >= 2:
                    result['death_date'] = parts[1]

    return result

def normalize_person_name(name: str) -> str:
    """Convert census name format to person page filename format."""
    # Handle multi-part files like "PalmerMay p1" -> just "PalmerMay"
    name = re.sub(r'\s+p\d+$', '', name)
    # Insert space before capital letters (CamelCase to Title Case)
    # "JohnSmith" -> "John Smith"
    result = []
    for i, char in enumerate(name):
        if i > 0 and char.isupper() and name[i-1].islower():
            result.append(' ')
        result.append(char)
    return ''.join(result)

def find_person_page(census_name: str) -> Optional[Path]:
    """Find the corresponding person page for a census entry."""
    normalized = normalize_person_name(census_name)

    # Try exact match first
    candidate = PEOPLE_DIR / f"{normalized}.md"
    if candidate.exists():
        return candidate

    # Try case-insensitive search
    if PEOPLE_DIR.exists():
        for page in PEOPLE_DIR.glob("*.md"):
            if page.stem.lower() == normalized.lower():
                return page

    return None

def read_person_page(page_path: Path) -> str:
    """Read an existing person page."""
    return page_path.read_text(encoding='utf-8')

def enrich_person_page(page_content: str, census_data: Dict) -> str:
    """Enrich a person page with census data."""
    census_file = census_data['filename']

    # Check if already has a reference to this census file
    if census_file in page_content:
        # Already processed
        return page_content

    # Add reference to the census file at the end of the Sources section
    # Find the Sources section
    sources_match = re.search(r'## Sources\n+(.*?)(\n## [A-Z]|\Z)', page_content, re.DOTALL)

    if sources_match:
        sources_section = sources_match.group(1)
        sources_end = sources_match.start(1) + len(sources_section)

        # Add reference to the census file
        census_ref = f"- `{RAW_INBOX_REF}/{census_file}`"
        if census_ref not in page_content:
            page_content = page_content[:sources_end] + f"{census_ref}\n" + page_content[sources_end:]

    return page_content

def create_placeholder_page(census_name: str, census_data: Dict) -> str:
    """Create a new person page from census data."""
    name = census_data['name'] or census_name
    normalized = normalize_person_name(census_name)

    today = datetime.now().strftime('%Y-%m-%d')

    page = f"""---
title: {name}
date: {today}
tags:
  - "#thorpe-family"
  - "#person"
---

# {name}

## Biographical Profile

- **Name:** {name}
- **Role in this project:** Individual indexed in Census InDesign summary (2026-04-24 intake).

## Source-Cited Facts

- Birth/death dates and detailed census records are available in census summaries.
- **Dates:** {census_data['dates'] if census_data['dates'] else '(see census summary)'}

## Census Records

Detailed census household data is available in the source file below.

## Research Notes

- Birth/death dates and exact relationships require image-level verification from original census records.
- Occupations, ages, and locations are transcribed from census summaries but should be verified against primary sources.

## Sources

1. [[References/Shared Intake 2026-04-24 Census InDesign Summaries|Shared Intake 2026-04-24 Census InDesign Summaries]]
2. `{RAW_INBOX_REF}/{census_data['filename']}`

"""
    return page

def process_census_files():
    """Process all census summary files and update person pages."""
    census_files = sorted(INBOX_DIR.glob("CensusSummary-*.txt"))

    print(f"Found {len(census_files)} census summary files")

    processed = 0
    created = 0
    updated = 0

    # Group files by person (handle multi-part files)
    file_groups = {}
    for f in census_files:
        # Extract person name from filename
        match = re.match(r'CensusSummary-(.+?)(?:\sp\d+)?\.txt', f.name)
        if match:
            person_name = match.group(1)
            if person_name not in file_groups:
                file_groups[person_name] = []
            file_groups[person_name].append(f)

    for person_name, files in sorted(file_groups.items()):
        # Parse all parts of this person's census data
        combined_data = None
        for census_file in files:
            data = parse_census_summary(census_file)
            if combined_data is None:
                combined_data = data
            # For multi-part files, we'll just reference the first file in the page

        # Find or create person page
        person_page = find_person_page(person_name)

        if person_page:
            # Update existing page
            page_content = read_person_page(person_page)
            new_content = enrich_person_page(page_content, combined_data)
            if new_content != page_content:
                person_page.write_text(new_content, encoding='utf-8')
                updated += 1
                print(f"✓ Updated: {person_page.name}")
        else:
            # Create new page
            normalized = normalize_person_name(person_name)
            new_page = PEOPLE_DIR / f"{normalized}.md"
            page_content = create_placeholder_page(person_name, combined_data)
            new_page.write_text(page_content, encoding='utf-8')
            created += 1
            print(f"+ Created: {new_page.name}")

        processed += 1

    print(f"\nSummary:")
    print(f"  Processed: {processed}")
    print(f"  Updated: {updated}")
    print(f"  Created: {created}")

if __name__ == '__main__':
    os.chdir('/mnt/c/Users/zach/Projects/thorpe-family-research')
    process_census_files()
