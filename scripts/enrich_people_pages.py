import json
import re
from pathlib import Path

# Configuration
LEADS_FILE = Path("svg_leads.json")
PEOPLE_DIR = Path("People")

def normalize_name(text):
    # Extract name part: "First Last 1800 - 1850" -> "First Last"
    match = re.match(r'^([A-Za-z\s\.,/-]+)\s+\d{4}', text)
    if match:
        return match.group(1).strip()
    return text.strip()

def find_page(name):
    # Try direct match
    path = PEOPLE_DIR / f"{name}.md"
    if path.exists(): return path
    
    # Try normalized name
    # "Wager/Dodge" -> "Wager-Dodge"
    norm = name.replace('/', '-')
    path = PEOPLE_DIR / f"{norm}.md"
    if path.exists(): return path
    
    # Case insensitive
    for p in PEOPLE_DIR.glob("*.md"):
        if p.stem.lower() == name.lower() or p.stem.lower() == norm.lower():
            return p
    return None

def enrich_page(page_path, leads):
    content = page_path.read_text(encoding='utf-8')
    
    # Build the indicators section
    indicators = "\n## Source Indicators\n\n"
    indicators += f"> [!info] Indicators from Pedigree Timeline Diagrams\n>\n"
    
    if leads['census']:
        years = ", ".join(map(str, sorted(leads['census'])))
        indicators += f"> - **Census Records**: Found in {years}\n"
    
    if leads['records']:
        refs = ", ".join(leads['records'])
        indicators += f"> - **Official Records**: Ref #{refs}\n"
        
    if leads['burial']:
        indicators += f"> - **Burial**: Verified (RIP marker)\n"
        
    if leads['obit']:
        indicators += f"> - **Obituary**: Available (Obit marker)\n"

    if not leads['census'] and not leads['records'] and not leads['burial'] and not leads['obit']:
        return # Nothing to add

    # Check if section already exists
    if "## Source Indicators" in content:
        # Replace existing section
        content = re.sub(r'## Source Indicators\n\n.*?(?=\n## |\Z)', indicators, content, flags=re.DOTALL)
    else:
        # Insert before Sources
        if "## Sources" in content:
            parts = content.split("## Sources")
            content = parts[0] + indicators + "\n## Sources" + parts[1]
        else:
            content += "\n" + indicators

    page_path.write_text(content, encoding='utf-8')
    print(f"Enriched: {page_path.name}")

def main():
    if not LEADS_FILE.exists():
        print("Error: svg_leads.json not found.")
        return

    with open(LEADS_FILE, "r", encoding='utf-8') as f:
        leads_data = json.load(f)
    
    count = 0
    for entry in leads_data:
        name = normalize_name(entry['text'])
        page_path = find_page(name)
        if page_path:
            enrich_page(page_path, entry['leads'])
            count += 1
        else:
            # print(f"Page not found for: {name}")
            pass

    print(f"Total pages enriched: {count}")

if __name__ == "__main__":
    main()
