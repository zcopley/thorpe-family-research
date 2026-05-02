import re
import os
from pathlib import Path

PEOPLE_DIR = Path("People")
TOPICS_DIR = Path("Topics")

def normalize_occupation(occ):
    occ = occ.strip().lower()
    if not occ or occ in ["none", "aged", "at home"]: return None
    
    # Grouping
    if "farm" in occ or "labr" in occ or "laborer" in occ: return "Agriculture"
    if "servant" in occ or "maid" in occ or "companion" in occ: return "Domestic Service"
    if "railway" in occ or "clerk" in occ: return "Clerical & Transport"
    if "carpenter" in occ or "blacksmith" in occ: return "Skilled Trades"
    if "dressmaker" in occ: return "Needlework & Tailoring"
    if "teamster" in occ: return "Transport & Labor"
    if "mayor" in occ or "judge" in occ or "law" in occ: return "Law & Public Service"
    
    return occ.title()

def extract_occupations():
    occ_map = {} # Map Normalized Category to list of (Person Name, Raw Occupation)
    
    for p in PEOPLE_DIR.glob("*.md"):
        content = p.read_text(encoding='utf-8')
        person_name = p.stem
        
        # Match "Occupation Farmer" or "Occupation [text]"
        # Matches in transcripts
        matches = re.findall(r'Occupation\s+(.*?)(?=\n|$)', content)
        # Also check "occ:"
        matches.extend(re.findall(r'Occ:\s+(.*?)(?=\n|$)', content, re.IGNORECASE))
        # Also check narrative "occupation farmer"
        matches.extend(re.findall(r'occupation ([a-z\s]{3,20})(?=\s|,|\.)', content, re.IGNORECASE))
        
        for occ_raw in matches:
            norm = normalize_occupation(occ_raw)
            if norm:
                if norm not in occ_map:
                    occ_map[norm] = []
                occ_map[norm].append((person_name, occ_raw.strip()))
                
    return occ_map

def main():
    occ_map = extract_occupations()
    print(f"Found {len(occ_map)} occupation categories.")
    
    content = """---
title: Family Trades and Occupations
date: 2026-04-30
tags:
  - "#thorpe-family"
  - "#topic"
  - "#social-history"
---

# Family Trades and Occupations

This page provides a social history of the Thorpe family and connected lines by categorizing ancestors by their trades and professions. This perspective shows the family's transition from the agricultural roots of the 18th and 19th centuries to the industrial and professional careers of the early 20th century.

## Trades and Professions

"""

    for cat in sorted(occ_map.keys()):
        content += f"### {cat}\n"
        # Unique names per category
        people = sorted(list(set(occ_map[cat])), key=lambda x: x[0])
        for name, raw in people:
            content += f"- [[People/{name}|{name}]] ({raw})\n"
        content += "\n"

    (TOPICS_DIR / "Family Trades and Occupations.md").write_text(content, encoding='utf-8')
    print("Generated Topics/Family Trades and Occupations.md")

if __name__ == "__main__":
    main()
