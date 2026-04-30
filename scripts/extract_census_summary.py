import os
import re
from pathlib import Path

# Configuration
PEOPLE_DIR = Path("People")
CENSUS_FILE = Path("References/raw/extracted/CensusSummaryIndividual.txt")
RAW_REF_PATH = "References/raw/extracted/CensusSummaryIndividual.txt"

def normalize_name_to_filename(name_str):
    """
    Convert "LAST, First Middle" to "First Middle Last".
    Handle suffixes like Jr.
    """
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

def get_person_page(name):
    path = PEOPLE_DIR / f"{name}.md"
    if path.exists(): return path
    normalized = normalize_name_to_filename(name)
    path = PEOPLE_DIR / f"{normalized}.md"
    if path.exists(): return path
    for p in PEOPLE_DIR.glob("*.md"):
        if p.stem.lower() == name.lower() or p.stem.lower() == normalized.lower():
            return p
    return None

def append_census_data(page_path, census_text):
    content = page_path.read_text(encoding='utf-8')
    if "## Census Records" in content and "CENSUS SUMMARY - INDIVIDUALS" in content:
        print(f"Skipping {page_path.name} (already updated)")
        return
    census_section = f"\n## Census Records\n\n> [!info] Extract from {RAW_REF_PATH}\n\n```text\n{census_text.strip()}\n```\n"
    if "## Sources" in content:
        parts = content.split("## Sources")
        new_content = parts[0] + census_section + "\n## Sources" + parts[1]
    else:
        new_content = content + census_section
    page_path.write_text(new_content, encoding='utf-8')
    print(f"Updated: {page_path.name}")

def main():
    if not CENSUS_FILE.exists(): return
    content = CENSUS_FILE.read_text(encoding='utf-8')
    # Split by the form feed character ^L which is \x0c
    sections = content.split('\x0c')
    print(f"Total sections found: {len(sections)}")
    
    processed = 0
    for section in sections:
        section = section.strip()
        if not section:
            continue
            
        lines = section.split('\n')
        header = lines[0].strip()
        # Match "SURNAME, Firstname (Dates)"
        match = re.search(r'^([A-Z\s,]+)\s*\((.*?)\)', header, re.IGNORECASE)
        if match:
            full_name_raw = match.group(1).strip()
            print(f"Match: {full_name_raw}")
            page_path = get_person_page(full_name_raw)
            if page_path:
                append_census_data(page_path, section)
                processed += 1
            else:
                print(f"  Missing: {full_name_raw}")

    print(f"Total updated: {processed}")

if __name__ == "__main__":
    main()
