import re
import os
from pathlib import Path

PEOPLE_DIR = Path("People")
CENSUS_INDEX = Path("References/raw/processed/2026-04-22-intake/Census/Ancestors in the Census.txt")

def find_page(last, first):
    last = last.strip().lower()
    first = first.strip().lower()
    for p in PEOPLE_DIR.glob("*.md"):
        stem = p.stem.lower()
        if last in stem and first in stem:
            return p
    return None

def update_life_pulse_dates():
    if not CENSUS_INDEX.exists(): return
    content = CENSUS_INDEX.read_text(encoding='utf-8')
    lines = content.split('\n')
    count = 0
    for line in lines:
        line = line.strip()
        if not line: continue
        match = re.search(r'([A-Za-z ,.]+)\s+\((.*?)\)', line)
        if match:
            name_raw = match.group(1).strip()
            dates = match.group(2).strip()
            parts = name_raw.split(',')
            if len(parts) >= 2:
                page_path = find_page(parts[0], parts[1])
                if page_path:
                    txt = page_path.read_text(encoding='utf-8')
                    new_line = f"- **Dates:** {dates}"
                    if "- **Dates:**" in txt:
                        txt = re.sub(r'-\s+\*\*Dates:\*\*\s+.*', new_line, txt)
                    elif "- **Birth/Death:**" in txt:
                        txt = re.sub(r'-\s+\*\*Birth/Death:\*\*\s+.*', new_line, txt)
                    else:
                        if "## Biographical Profile" in txt:
                            txt = txt.replace("## Biographical Profile", f"## Biographical Profile\n\n{new_line}")
                    page_path.write_text(txt, encoding='utf-8')
                    count += 1
    print(f"Total updates: {count}")

if __name__ == "__main__":
    update_life_pulse_dates()
