import re
import json
from pathlib import Path

PEOPLE_DIR = Path("People")

def analyze_gaps(page_path):
    content = page_path.read_text(encoding='utf-8')
    
    # 1. Find indicated census years from Source Indicators
    indicated_years = []
    indicator_match = re.search(r'> - \*\*Census Records\*\*: Found in ([\d, ]+)', content)
    if indicator_match:
        years_str = indicator_match.group(1)
        indicated_years = [int(y.strip()) for y in years_str.split(',')]

    # 2. Find transcripts in Census Records section
    transcript_years = []
    census_section = re.search(r'## Census Records\n\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
    if census_section:
        section_text = census_section.group(1)
        # Find any 4-digit years in the range 1790-1950
        found_years = re.findall(r'\b(1[789]\d\d)\b', section_text)
        transcript_years = [int(y) for y in found_years if 1790 <= int(y) <= 1950]
        transcript_years = list(set(transcript_years))

    # 3. Identify Gaps with +/- 1 year tolerance (for UK 1-ending years vs US 0-ending)
    gaps = []
    for iy in indicated_years:
        found = False
        for ty in transcript_years:
            if abs(iy - ty) <= 1:
                found = True
                break
        if not found:
            gaps.append(iy)
    
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
            
    report.sort(key=lambda x: len(x['gaps']), reverse=True)
    print(f"Refined Gap Analysis Results: {len(report)} people have missing transcripts.")
    
    with open("gap_report.json", "w", encoding='utf-8') as f:
        json.dump(report, f, indent=2)
    
    for entry in report[:15]:
        print(f"- {entry['name']}: Missing {', '.join(map(str, entry['gaps']))}")

if __name__ == "__main__":
    main()
