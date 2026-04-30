import json
import re
from pathlib import Path

# Configuration
LIFESPANS_FILE = Path("lifespans.json")
PEOPLE_DIR = Path("People")

def enrich_page_with_contemporaries(page_path, person, all_people):
    content = page_path.read_text(encoding='utf-8')
    
    # Find contemporaries (people with overlapping lives)
    # We'll pick up to 8 people who lived at the same time
    contemporaries = []
    for other in all_people:
        if other['name'] == person['name']: continue
        
        # Overlap check
        if other['birth'] < person['death'] and other['death'] >= person['birth']:
            # Calculate overlap amount
            overlap_start = max(person['birth'], other['birth'])
            overlap_end = min(person['death'], other['death'])
            overlap = overlap_end - overlap_start
            contemporaries.append((other, overlap))
            
    # Sort by overlap amount
    contemporaries.sort(key=lambda x: x[1], reverse=True)
    contemporaries = [c[0] for c in contemporaries[:10]]
    
    if not contemporaries: return

    # Build Mermaid Gantt
    mermaid = "\n## Overlapping Lifespans\n\n"
    mermaid += f"> [!info] Visualizing contemporaries in the vault during the life of {person['name']} ({person['birth']}-{person['death']}).\n\n"
    mermaid += "```mermaid\ngantt\n    dateFormat  YYYY\n    axisFormat  %Y\n"
    
    # Add the person themselves first
    mermaid += f"    {person['name']} : {person['birth']}, {person['death']}\n"
    
    for c in contemporaries:
        name = c['name'].replace(':', '-')
        mermaid += f"    {name} : {c['birth']}, {c['death']}\n"
        
    mermaid += "```\n"

    # Check if section already exists
    if "## Overlapping Lifespans" in content:
        content = re.sub(r'## Overlapping Lifespans\n\n.*?(?=\n## |\Z)', mermaid, content, flags=re.DOTALL)
    else:
        # Insert before Source Indicators or Sources
        if "## Source Indicators" in content:
            parts = content.split("## Source Indicators")
            content = parts[0] + mermaid + "\n## Source Indicators" + parts[1]
        elif "## Sources" in content:
            parts = content.split("## Sources")
            content = parts[0] + mermaid + "\n## Sources" + parts[1]
        else:
            content += "\n" + mermaid

    page_path.write_text(content, encoding='utf-8')
    print(f"Added contemporaries to: {page_path.name}")

def main():
    if not LIFESPANS_FILE.exists(): return
    with open(LIFESPANS_FILE, "r", encoding='utf-8') as f:
        all_people = json.load(f)
        
    for person in all_people:
        page_path = Path(person['path'])
        if page_path.exists():
            enrich_page_with_contemporaries(page_path, person, all_people)

if __name__ == "__main__":
    main()
