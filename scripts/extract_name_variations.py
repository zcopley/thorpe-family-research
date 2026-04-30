import re
import os
from pathlib import Path

# Configuration
CENSUS_FILE = Path("References/raw/extracted/CensusSummaryIndividual.txt")
PEOPLE_DIR = Path("People")
TOPICS_DIR = Path("Topics")

def normalize_name_to_filename(name_str):
    name_str = name_str.replace('.', '').strip()
    if ',' in name_str:
        parts = [p.strip() for p in name_str.split(',')]
        last = parts[0]
        first_mid = parts[1]
        if ' Jr' in last:
            last = last.replace(' Jr', '').strip()
            return f"{first_mid} {last} Jr"
        return f"{first_mid} {last}"
    return name_str

def find_person_page(name_raw):
    norm = normalize_name_to_filename(name_raw)
    path = PEOPLE_DIR / f"{norm}.md"
    if path.exists(): return path
    norm_slash = norm.replace('/', '-')
    path = PEOPLE_DIR / f"{norm_slash}.md"
    if path.exists(): return path
    for p in PEOPLE_DIR.glob("*.md"):
        if p.stem.lower() == norm.lower() or p.stem.lower() == name_raw.lower() or p.stem.lower() == norm_slash.lower():
            return p
    return None

def extract_cross_references():
    if not CENSUS_FILE.exists(): return
    content = CENSUS_FILE.read_text(encoding='utf-8')
    parts = content.split("CROSS REFERENCES")
    if len(parts) < 2: return
    table_text = parts[-1].strip()
    
    variation_map = {}
    
    # regex for "ALIAS. See PRIMARY"
    # We'll allow anything in ALIAS and PRIMARY except the ". See " separator
    pattern = re.compile(r'([A-Za-z ,()]+)\.\s+See\s+([A-Za-z ,()]+)')
    
    for line in table_text.split('\n'):
        line = line.strip()
        matches = pattern.findall(line)
        for alias, primary in matches:
            alias = alias.strip()
            primary = primary.strip()
            if primary not in variation_map:
                variation_map[primary] = []
            if alias not in variation_map[primary]:
                variation_map[primary].append(alias)

    print(f"DEBUG: Processed {len(variation_map)} primary names.")

    count = 0
    for primary, aliases in variation_map.items():
        page_path = find_person_page(primary)
        if page_path:
            print(f"Updating: {page_path.name} with aliases {aliases}")
            content = page_path.read_text(encoding='utf-8')
            
            section = "\n## Name Variations\n\n"
            section += "> [!info] Known aliases or census misspellings from Butch Thorpe's cross-reference table.\n>\n"
            for a in sorted(aliases):
                section += f"> - **{a}**\n"
            
            if "## Name Variations" in content:
                content = re.sub(r'## Name Variations\n\n.*?(?=\n## |\Z)', section, content, flags=re.DOTALL)
            else:
                if "## Overlapping Lifespans" in content:
                    content = content.replace("## Overlapping Lifespans", section + "## Overlapping Lifespans")
                elif "## Source Indicators" in content:
                    content = content.replace("## Source Indicators", section + "## Source Indicators")
                elif "## Sources" in content:
                    content = content.replace("## Sources", section + "## Sources")
                else:
                    content += "\n" + section
            
            page_path.write_text(content, encoding='utf-8')
            count += 1
    print(f"Total pages updated with variations: {count}")

def extract_methodology():
    if not CENSUS_FILE.exists(): return
    content = CENSUS_FILE.read_text(encoding='utf-8')
    match = re.search(r'Introduction\n(.*?)(?=\f|Thorpe Pedigree Timeline)', content, re.DOTALL)
    if match:
        intro_text = match.group(1).strip()
        page_content = f"""---
title: Butch Thorpe Research Methodology
date: 2026-04-30
tags:
  - "#thorpe-family"
  - "#topic"
  - "#meta"
---

# Butch Thorpe Research Methodology

The following is an extract from the **Introduction** of Robert "Butch" Thorpe's *Census Summary for the Individual Ancestors of Lancelot and Wendolyn Thorpe*, originally published October 26, 2009.

## Introduction

> {intro_text}

---
*Source: [[References/raw/extracted/CensusSummaryIndividual.txt|CensusSummaryIndividual.txt]]*
"""
        (TOPICS_DIR / "Butch Thorpe Research Methodology.md").write_text(page_content, encoding='utf-8')
        print("Generated Butch Thorpe Research Methodology.md")

if __name__ == "__main__":
    extract_cross_references()
    extract_methodology()
