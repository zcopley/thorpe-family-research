import json
from pathlib import Path

# Configuration
LIFESPANS_FILE = Path("lifespans.json")
TOPICS_DIR = Path("Topics")

ERAS = [
    (1700, 1750),
    (1750, 1800),
    (1800, 1850),
    (1850, 1900),
    (1900, 1950),
    (1950, 2026)
]

def generate_era_page(start, end, people):
    # Filter people alive during this era
    contemporaries = []
    for p in people:
        if p['birth'] < end and p['death'] >= start:
            contemporaries.append(p)
            
    if not contemporaries: return
    
    # Sort by birth year
    contemporaries.sort(key=lambda x: x['birth'])
    
    # Limit to 30 people per chart for readability
    contemporaries = contemporaries[:30]
    
    filename = f"Ancestors of the {start}-{end} Era.md"
    title = f"Ancestors of the {start}-{end} Era"
    
    content = f"""---
title: {title}
date: 2026-04-30
tags:
  - "#thorpe-family"
  - "#topic"
  - "#timeline"
---

# {title}

This page visualizes the ancestors who were alive during the years {start} to {end}. This helps identify which family members from different branches (Thorpe, Bellamy, Spicer, Prior) were contemporaries.

## Timeline of Contemporaries

```mermaid
gantt
    title Ancestors Alive {start} - {end}
    dateFormat  YYYY
    axisFormat  %Y
    tickInterval 5y
"""
    
    for p in contemporaries:
        name = p['name'].replace(':', '-')
        # Mermaid gantt needs start date and end date or duration
        # We'll use actual years. Gantt usually handles dates, but we can try YYYY format.
        content += f"    {name} : {p['birth']}, {p['death']}\n"
        
    content += "```\n\n"
    
    content += "## Individual Profiles\n\n"
    for p in contemporaries:
        content += f"- [[{p['path']}|{p['name']}]] ({p['birth']} - {p['death']})\n"
        
    (TOPICS_DIR / filename).write_text(content, encoding='utf-8')
    print(f"Generated: {filename}")

def main():
    if not LIFESPANS_FILE.exists(): return
    with open(LIFESPANS_FILE, "r", encoding='utf-8') as f:
        people = json.load(f)
        
    for start, end in ERAS:
        generate_era_page(start, end, people)

if __name__ == "__main__":
    main()
