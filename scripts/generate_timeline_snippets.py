import json
import re
from pathlib import Path

# Configuration
LEADS_FILE = Path("svg_leads.json")
ASSETS_DIR = Path("assets/snippets")
PEOPLE_DIR = Path("People")

# SVG Constants
WIDTH = 600
HEIGHT = 60
START_YEAR = 1700
END_YEAR = 2025
PIXELS_PER_YEAR = WIDTH / (END_YEAR - START_YEAR)

def year_to_x(year):
    return (year - START_YEAR) * PIXELS_PER_YEAR

def normalize_filename(text):
    match = re.match(r'^([A-Za-z\s\.,/-]+)\s+\d{4}', text)
    name = match.group(1).strip() if match else text.strip()
    return name.replace('/', '-')

def generate_svg(entry):
    name_text = entry['text']
    leads = entry['leads']
    
    # Parse lifespan
    match = re.search(r'(\d{4})\??\s*-\s*(\d{4}|\?)\??', name_text)
    if not match: return None
    
    birth = int(match.group(1))
    death = int(match.group(2)) if match.group(2) != '?' else 2025
    
    x_birth = year_to_x(birth)
    x_death = year_to_x(death)
    
    svg = f'<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">\n'
    # Background Grid
    for y in range(1700, 2050, 50):
        x = year_to_x(y)
        svg += f'  <line x1="{x}" y1="0" x2="{x}" y2="{HEIGHT}" stroke="#e5e5e5" stroke-width="1" />\n'
        svg += f'  <text x="{x+2}" y="12" font-family="Arial" font-size="10" fill="#b8b8b8">{y}</text>\n'
    
    # Lifespan Bar
    svg += f'  <rect x="{x_birth}" y="25" width="{x_death - x_birth}" height="10" fill="#81b29a" rx="2" />\n'
    
    # Dots
    for census_year in leads['census']:
        x = year_to_x(census_year)
        svg += f'  <circle cx="{x}" cy="30" r="4" fill="#009ee0" stroke="white" stroke-width="1" />\n'
        
    for i, rec in enumerate(leads['records']):
        # We don't have exact years for records, so we place them near birth/middle/death?
        # For simplicity, let's just skip them in the visual or place them at the start
        pass
        
    if leads['burial']:
        svg += f'  <text x="{x_death + 5}" y="35" font-family="Arial" font-size="10" fill="#4e4e4e">RIP</text>\n'
        
    svg += f'  <text x="10" y="55" font-family="Arial" font-size="12" fill="#2b2b2b">{name_text}</text>\n'
    svg += '</svg>'
    return svg

def main():
    if not LEADS_FILE.exists(): return
    if not ASSETS_DIR.exists(): ASSETS_DIR.mkdir(parents=True)
    
    with open(LEADS_FILE, "r", encoding='utf-8') as f:
        leads_data = json.load(f)
        
    for entry in leads_data:
        svg_content = generate_svg(entry)
        if svg_content:
            filename = normalize_filename(entry['text'])
            svg_path = ASSETS_DIR / f"{filename}.svg"
            svg_path.write_text(svg_content, encoding='utf-8')
            
            # Update markdown to include the snippet at the top
            page_path = PEOPLE_DIR / f"{filename}.md"
            if page_path.exists():
                content = page_path.read_text(encoding='utf-8')
                snippet_tag = f"![[assets/snippets/{filename}.svg]]\n\n"
                if f"assets/snippets/{filename}.svg" not in content:
                    # Insert after frontmatter
                    if content.startswith("---"):
                        parts = content.split("---", 2)
                        if len(parts) == 3:
                            new_content = f"---{parts[1]}---\n\n{snippet_tag}{parts[2].lstrip()}"
                            page_path.write_text(new_content, encoding='utf-8')
    
    print(f"Generated {len(leads_data)} timeline snippets.")

if __name__ == "__main__":
    main()
