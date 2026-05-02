import re
import os
from pathlib import Path

PEOPLE_DIR = Path("People")
PLACES_DIR = Path("Places")

def normalize_place(place_str):
    # Remove newlines
    place_str = place_str.replace('\n', ' ').replace('\r', '')
    # Remove junk like (as child), (as household head), etc.
    place_str = re.sub(r'\(as.*?\)', '', place_str)
    # Remove "Census — "
    place_str = place_str.replace('Census — ', '')
    # Remove leading years
    place_str = re.sub(r'^\d{4}\s*', '', place_str)
    # Remove page numbers
    place_str = re.sub(r', Page \d+.*', '', place_str)
    place_str = re.sub(r', p\..*', '', place_str)
    
    # Filter out long narrative strings (places are usually short)
    if len(place_str) > 60: return None
    
    # Remove colons from title (breaks YAML)
    place_str = place_str.replace(':', ' -')
    
    # Final check for keywords that don't belong in a place name
    if any(x in place_str.lower() for x in ["name", "relationship", "head", "wife", "son", "daughter", "servant"]):
        return None
        
    return place_str.strip()

def extract_places():
    places = {} # Map normalized place name to list of (Person Name, Year)
    
    for p in PEOPLE_DIR.glob("*.md"):
        content = p.read_text(encoding='utf-8')
        person_name = p.stem
        
        # Match headers like ### 1850 Iowa Census — Jones County, Rome Township
        # Or raw lines like 1871 Essex, Felstead, Village
        # Use regex to match only lines that look like a location (Year State/County)
        matches = re.findall(r'(?m)^(?:###\s*)?(\d{4})\s+([A-Za-z][A-Za-z\s,.-]{3,60})(?=\n|$)', content)
        
        for year, location in matches:
            if not (1790 <= int(year) <= 1950): continue
            
            # Clean location
            loc = normalize_place(location)
            if not loc or len(loc) < 3 or any(x in loc.lower() for x in ["ref #", "burial", "dates:", "born", "died", "married", "census"]): continue
            
            if loc not in places:
                places[loc] = []
            places[loc].append((person_name, year))
            
    return places

def main():
    if not PLACES_DIR.exists(): PLACES_DIR.mkdir()
    
    places = extract_places()
    print(f"Found {len(places)} unique locations.")
    
    directory_content = """---
title: Places Directory
date: 2026-04-30
tags:
  - "#thorpe-family"
  - "#index"
  - "#geography"
---

# Places Directory

This directory organizes the Thorpe family ancestors by the locations where they were recorded in census and historical records.

"""

    # Group by State/Country for the directory
    groups = {}
    for place in sorted(places.keys()):
        parts = [p.strip() for p in place.split(',')]
        # Last part is usually State or Country
        top_level = parts[0] # Fallback
        if len(parts) >= 2:
            # Check if first part is a year-state combo or just state
            # "Iowa Census" -> "Iowa"
            top_level = parts[0].split(' ')[0]
            
        if top_level not in groups: groups[top_level] = []
        groups[top_level].append(place)
        
        # Create individual place page
        safe_filename = place.replace(',', '-').replace(' ', '-').replace('--', '-').strip('-')
        page_path = PLACES_DIR / f"{safe_filename}.md"
        
        # Consolidate people/years
        residents = {}
        for name, year in places[place]:
            if name not in residents: residents[name] = []
            residents[name].append(year)
            
        residents_list = ""
        for name in sorted(residents.keys()):
            years = ", ".join(sorted(list(set(residents[name]))))
            residents_list += f"- [[People/{name}|{name}]] ({years})\n"
            
        page_content = f"""---
title: {place}
date: 2026-04-30
tags:
  - "#thorpe-family"
  - "#place"
---

# {place}

Ancestors recorded in this location:

{residents_list}

---
*For a full list of locations, see the [[Places Directory]].*
"""
        page_path.write_text(page_content, encoding='utf-8')

    # Build Directory
    for group in sorted(groups.keys()):
        directory_content += f"## {group}\n\n"
        for place in sorted(groups[group]):
            safe_filename = place.replace(',', '-').replace(' ', '-').replace('--', '-').strip('-')
            directory_content += f"- [[Places/{safe_filename}|{place}]]\n"
        directory_content += "\n"
        
    Path("Places Directory.md").write_text(directory_content, encoding='utf-8')
    print("Generated Places Directory.md and individual place pages.")

if __name__ == "__main__":
    main()
