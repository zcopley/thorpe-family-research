import os
import re
import json
from pathlib import Path

PEOPLE_DIR = Path("People")

def parse_person_page(file_path):
    content = file_path.read_text(encoding='utf-8')
    
    birth = None
    death = None
    title = ""
    
    # Title from frontmatter
    title_match = re.search(r'title: (.*)', content)
    if title_match:
        title = title_match.group(1).strip()
    
    # Pattern 1: - **Dates:** 1800-1850
    dates_match = re.search(r'-\s+\*\*Dates:\*\*\s+(\d{4})\??\s*-\s*(\d{4}|\?)\??', content)
    if dates_match:
        birth = int(dates_match.group(1))
        if dates_match.group(2) != '?':
            death = int(dates_match.group(2))
    
    # Pattern 2: - **Birth/Death:** Born ... 1769; died ... 1852
    if not birth:
        bd_match = re.search(r'-\s+\*\*Birth/Death:\*\*.*?(\d{4}).*?(\d{4}|\?)', content, re.DOTALL)
        if bd_match:
            birth = int(bd_match.group(1))
            if bd_match.group(2) != '?':
                death = int(bd_match.group(2))

    # Pattern 3: Name (1800 - 1850)
    if not birth:
        paren_match = re.search(r'\((\d{4})\??\s*-\s*(\d{4}|\?)\??\)', content)
        if paren_match:
            birth = int(paren_match.group(1))
            if paren_match.group(2) != '?':
                death = int(paren_match.group(2))

    # Pattern 4: years in title
    if not birth:
        title_year_match = re.search(r'(\d{4})\??\s*-\s*(\d{4}|\?)\??', title)
        if title_year_match:
            birth = int(title_year_match.group(1))
            if title_year_match.group(2) != '?':
                death = int(title_year_match.group(2))

    if not death:
        death = 2026 # Default for living or unknown death

    return {
        'name': title or file_path.stem,
        'filename': file_path.name,
        'birth': birth,
        'death': death,
        'path': f"People/{file_path.name}"
    }

def main():
    all_people = []
    for p in PEOPLE_DIR.glob("*.md"):
        data = parse_person_page(p)
        if data['birth']:
            all_people.append(data)
            
    with open("lifespans.json", "w", encoding='utf-8') as f:
        json.dump(all_people, f, indent=2)
    print(f"Collated lifespans for {len(all_people)} people. Saved to lifespans.json")

if __name__ == "__main__":
    main()
