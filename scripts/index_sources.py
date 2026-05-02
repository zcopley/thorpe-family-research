import re
import os
from pathlib import Path

PEOPLE_DIR = Path("People")
TOPICS_DIR = Path("Topics")

def extract_source_refs():
    source_map = {} # Map Ref Number to list of Person Name
    
    for p in PEOPLE_DIR.glob("*.md"):
        content = p.read_text(encoding='utf-8')
        person_name = p.stem
        
        # Match "- **Official Records**: Ref #015, 017"
        match = re.search(r'- \*\*Official Records\*\*: Ref #([\d, ]+)', content)
        if match:
            refs = [r.strip() for r in match.group(1).split(',')]
            for r in refs:
                # Sanitize to 3 digits
                r = r.zfill(3)
                if r not in source_map:
                    source_map[r] = []
                source_map[r].append(person_name)
                
    return source_map

def main():
    source_map = extract_source_refs()
    print(f"Found {len(source_map)} unique source reference numbers.")
    
    content = """---
title: Master Source Index
date: 2026-04-30
tags:
  - "#thorpe-family"
  - "#index"
  - "#meta"
---

# Master Source Index

This index reverse-maps the 3-digit reference numbers used by Robert "Butch" Thorpe in his physical archive to the ancestors mentioned in those documents. If multiple people share the same reference number, they likely appear in the same primary record (e.g., a family Bible, probate file, or land deed).

## Reference Numbers

"""

    for ref in sorted(source_map.keys()):
        content += f"### Ref #{ref}\n"
        for name in sorted(list(set(source_map[ref]))):
            content += f"- [[People/{name}|{name}]]\n"
        content += "\n"

    (TOPICS_DIR / "Master Source Index.md").write_text(content, encoding='utf-8')
    print("Generated Topics/Master Source Index.md")

if __name__ == "__main__":
    main()
