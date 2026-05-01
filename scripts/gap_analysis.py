import re
import json
from pathlib import Path

PEOPLE_DIR = Path("People")

def analyze_gaps(page_path):
    content = page_path.read_text(encoding='utf-8')
    
    # 1. Find indicated census years from Source Indicators
    # Example: > - **Census Records**: Found in 1850, 1860
    indicated_years = []
    indicator_match = re.search(r'> - \*\*Census Records\*\*: Found in ([\d, ]+)', content)
    if indicator_match:
        years_str = indicator_match.group(1)
        indicated_years = [y.strip() for y in years_str.split(',')]

    # 2. Find transcripts in Census Records section
    # We look for years mentioned in headers within the ## Census Records section
    transcript_years = []
    census_section = re.search(r'## Census Records\n\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
    if census_section:
        section_text = census_section.group(1)
        # Look for years like 1850, 1860 in the text
        transcript_years = re.findall(r'\b(18\d0|19\d0)\b', section_text)
        transcript_years = list(set(transcript_years))

    # 3. Identify Gaps
    gaps = [y for y in indicated_years if y not in transcript_years]
    
    return {
        'name': page_path.stem,
        'indicated': indicated_years,
        'transcripts': transcript_years,
        'gaps': gaps
    }

def main():
    report = []
    for p in PEOPLE_DIR.glob("*.md"):
        result = analyze_gaps(p)
        if result['gaps']:
            report.append(result)
            
    # Sort report by number of gaps
    report.sort(key=lambda x: len(x['gaps']), reverse=True)
    
    print(f"Gap Analysis Results: {len(report)} people have missing transcripts.")
    
    # Save report
    with open("gap_report.json", "w", encoding='utf-8') as f:
        json.dump(report, f, indent=2)
    
    # Print top 10 people with gaps
    for entry in report[:10]:
        print(f"- {entry['name']}: Missing {', '.join(entry['gaps'])}")

if __name__ == "__main__":
    main()
