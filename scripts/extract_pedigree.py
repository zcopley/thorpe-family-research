import os
import re
from pathlib import Path
from datetime import datetime

# Configuration
PEOPLE_DIR = Path("People")
RAW_EXTRACTED_DIR = Path("References/raw/extracted")
TODAY = datetime.now().strftime('%Y-%m-%d')

# Regex to match Name followed by Lifespan (e.g., John Doe 1800-1850)
# Matches "Name Name 1800-1850" or "Name Name 1800 - 1850" or "Name Name 1800?-1850?"
PEDIGREE_PATTERN = re.compile(r'^([A-Za-z\s\.,/]+)\s+(\d{4}\??\s*-\s*\d{4}\??|\d{4}\??\s*-\s*\?|\?\s*-\s*\d{4}\??)$')

def normalize_name(name):
    """Normalize names to match existing file conventions."""
    name = name.strip()
    # Replace slashes with hyphens to avoid directory errors
    name = name.replace('/', '-')
    # Replace multiple spaces
    name = re.sub(r'\s+', ' ', name)
    return name

def create_person_stub(name, lifespan, source_file):
    """Create a new person markdown file if it doesn't exist."""
    filename = f"{name}.md"
    file_path = PEOPLE_DIR / filename
    
    if file_path.exists():
        print(f"Skipping: {name} (already exists)")
        return False

    content = f"""---
title: {name}
date: {TODAY}
tags:
  - "#thorpe-family"
  - "#person"
---

# {name}

## Biographical Profile

- **Name:** {name}
- **Dates:** {lifespan}

## Source-Cited Facts

- Identified in pedigree timeline source.

## Research Notes

- Initial stub created from pedigree timeline extraction.

## Sources

1. [[{source_file}|{source_file.name}]]
"""
    file_path.write_text(content, encoding='utf-8')
    print(f"Created: {name}")
    return True

def process_timeline_file(file_path):
    """Process a single pedigree timeline text file."""
    print(f"Processing: {file_path}")
    count = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            match = PEDIGREE_PATTERN.match(line)
            if match:
                name = normalize_name(match.group(1))
                lifespan = match.group(2)
                if create_person_stub(name, lifespan, file_path):
                    count += 1
    return count

def main():
    if not PEOPLE_DIR.exists():
        PEOPLE_DIR.mkdir()

    total_created = 0
    # Process specific pedigree files identified in research
    timeline_files = list(RAW_EXTRACTED_DIR.glob("PedigreeTimelines2025*.txt"))
    timeline_files.extend(list(RAW_EXTRACTED_DIR.glob("PedigreeTimeline2025*.txt")))
    
    # Use a set to handle duplicates if glob overlapping
    for file_path in set(timeline_files):
        total_created += process_timeline_file(file_path)
    
    print(f"\nTotal new stubs created: {total_created}")

if __name__ == "__main__":
    main()
