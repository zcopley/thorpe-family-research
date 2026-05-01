import json
import re
from pathlib import Path

PEOPLE_DIR = Path("People")

def inject_gaps():
    if not Path("gap_report.json").exists(): return
    
    with open("gap_report.json", "r", encoding='utf-8') as f:
        report = json.load(f)
        
    for entry in report:
        name = entry['name']
        gaps = entry['gaps']
        page_path = PEOPLE_DIR / f"{name}.md"
        
        if page_path.exists():
            content = page_path.read_text(encoding='utf-8')
            
            section = "\n## Research Gaps\n\n"
            section += "> [!warning] Priority Research Leads\n"
            section += "> The following census records are indicated in the pedigree diagrams but matching transcripts are missing from the vault:\n"
            for g in gaps:
                note = ""
                if g == 1890:
                    note = " (Note: The 1890 US Federal Census was largely destroyed by fire)"
                section += f"> - **{g} Census**: Transcript needed to verify household context.{note}\n"
            
            # Remove old Research Gaps section if it exists and is short/stubby
            # Or just append to it.
            if "## Research Gaps" in content:
                # Find existing section
                content = re.sub(r'## Research Gaps\n\n.*?(?=\n## |\Z)', section, content, flags=re.DOTALL)
            else:
                # Insert before Sources
                if "## Sources" in content:
                    parts = content.split("## Sources")
                    content = parts[0] + section + "\n## Sources" + parts[1]
                else:
                    content += "\n" + section
            
            page_path.write_text(content, encoding='utf-8')
            print(f"Injected gaps into: {name}")

if __name__ == "__main__":
    inject_gaps()
