import os
from pathlib import Path
from datetime import datetime

PEOPLE_DIR = Path("People")
SEARCH_INDEX_FILE = Path("Search Index.md")
PEOPLE_DIRECTORY_FILE = Path("People Directory.md")
CHANGELOG_FILE = Path("CHANGELOG.md")
TODAY = datetime.now().strftime('%Y-%m-%d')

def get_all_people():
    people = []
    for p in PEOPLE_DIR.glob("*.md"):
        # Use stem for the display name
        people.append((p.stem, f"People/{p.name}"))
    return sorted(people, key=lambda x: x[0])

def update_search_index(people):
    content = f"""---
title: Search Index
date: {TODAY}
tags:
  - "#thorpe-family"
  - "#index"
---

# Search Index

## People
"""
    for name, path in people:
        content += f"- [[{path}|{name}]]\n"
    
    SEARCH_INDEX_FILE.write_text(content, encoding='utf-8')
    print("Updated Search Index.md")

def update_people_directory(people):
    content = f"""---
title: People Directory
date: {TODAY}
tags:
  - "#thorpe-family"
  - "#index"
---

# People Directory

"""
    for name, path in people:
        content += f"- [[{path}|{name}]]\n"
        
    PEOPLE_DIRECTORY_FILE.write_text(content, encoding='utf-8')
    print("Updated People Directory.md")

def update_changelog():
    # Gather files changed/created today in People/
    # For simplicity, we'll just list all files in People/ that have a date of today in frontmatter 
    # OR we just list the ones created by the script if we tracked them.
    # Here we'll just append a summary of the session.
    
    with open(CHANGELOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"\n## {TODAY}\n\n")
        f.write("- Automated extraction of pedigree and census data from Robert Thorpe's raw files.\n")
        f.write("- Created missing person pages and enriched existing pages with census records.\n")
        f.write("- Updated Search Index and People Directory.\n")

def main():
    people = get_all_people()
    update_search_index(people)
    update_people_directory(people)
    update_changelog()

if __name__ == "__main__":
    main()
