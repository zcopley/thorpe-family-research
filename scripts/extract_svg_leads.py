import re
import json
from pathlib import Path

# Configuration
RAW_FILES = [
    Path("References/raw/extracted/PedigreeTimelines2025_raw.txt"),
    Path("References/raw/extracted/PedigreeTimelines2019Descendants2_raw.txt")
]
PEOPLE_DIR = Path("People")

# Colors
COLOR_BLUE = "#009ee0"
COLOR_RED = "#e30016"
COLOR_GRAY = "#eceded" # used for RIP box

def parse_raw_file(file_path):
    content = file_path.read_text(encoding='utf-8')
    
    # Extract Year Markers
    years = {}
    # Pattern for years: startTextObject ... insertText (1700)
    text_objects = re.split(r'startTextObject', content)
    for obj in text_objects:
        x_match = re.search(r'svg:x: (-?\d+\.\d+)in', obj)
        y_match = re.search(r'svg:y: (-?\d+\.\d+)in', obj)
        text_match = re.search(r'insertText \((1700|1800|1900|2000)\)', obj)
        if x_match and y_match and text_match:
            year = int(text_match.group(1))
            x = float(x_match.group(1))
            # Year markers are usually at the bottom, y around 8.0
            if float(y_match.group(1)) > 7.0:
                years[year] = x

    if not years:
        # Fallback to defaults found in research
        years = {1700: -0.2336, 1800: 2.7664, 1900: 5.7664, 2000: 8.7664}
    
    # X-Scale: pixels per year
    # We use center of box: x + width/2. Width is 1.4512
    x_offset = 1.4512 / 2
    def x_to_year(x):
        # Linear interpolation
        sorted_years = sorted(years.keys())
        for i in range(len(sorted_years) - 1):
            y1, y2 = sorted_years[i], sorted_years[i+1]
            x1, x2 = years[y1] + x_offset, years[y2] + x_offset
            if x1 <= x <= x2:
                return y1 + (x - x1) * (y2 - y1) / (x2 - x1)
        # Extrapolate
        y1, y2 = sorted_years[0], sorted_years[1]
        x1, x2 = years[y1] + x_offset, years[y2] + x_offset
        return y1 + (x - x1) * (y2 - y1) / (x2 - x1)

    people = []
    # Pattern for people names: insertText (Name 1900 - 2000)
    # They are in TextObjects
    for obj in text_objects:
        text_match = re.search(r'insertText \(([A-Za-z\s\.,/-]+ \d{4}.*?)\)', obj)
        if text_match:
            full_text = text_match.group(1)
            # Filter out things like "Compiled by...", "RIP", "Obit", etc.
            if any(x in full_text for x in ["Compiled by", "RIP", "Obit", "Found in Census"]):
                continue
                
            x_match = re.search(r'svg:x: (-?\d+\.\d+)in', obj)
            y_match = re.search(r'svg:y: (-?\d+\.\d+)in', obj)
            if x_match and y_match:
                people.append({
                    'text': full_text,
                    'x': float(x_match.group(1)),
                    'y': float(y_match.group(1)),
                    'leads': {'census': [], 'records': [], 'burial': False, 'obit': False}
                })

    # Extract Dots and Icons
    # These are in Layers or just setStyle calls
    dots = []
    style_blocks = re.split(r'setStyle', content)
    for block in style_blocks:
        color_match = re.search(r'draw:fill-color: (#\w+)', block)
        if color_match:
            color = color_match.group(1)
            path_match = re.search(r'drawPath \(svg:d: \(.*?, svg:x: (-?\d+\.\d+)in, svg:y: (-?\d+\.\d+)in\)', block)
            if path_match:
                x = float(path_match.group(1))
                y = float(path_match.group(2))
                dots.append({'color': color, 'x': x, 'y': y})

    # Extract all text again to find ref numbers near red dots
    all_text = []
    for obj in text_objects:
        text_match = re.search(r'insertText \((.*?)\)', obj)
        x_match = re.search(r'svg:x: (-?\d+\.\d+)in', obj)
        y_match = re.search(r'svg:y: (-?\d+\.\d+)in', obj)
        if text_match and x_match and y_match:
            all_text.append({'text': text_match.group(1), 'x': float(x_match.group(1)), 'y': float(y_match.group(1))})

    # Assign to people
    for person in people:
        py = person['y']
        
        # Parse years from text "Name 1800 - 1850"
        birth, death = None, None
        year_match = re.search(r'(\d{4})\??\s*-\s*(\d{4}|\?)\??', person['text'])
        if year_match:
            birth = int(year_match.group(1))
            death = int(year_match.group(2)) if year_match.group(2) != '?' else 2025
            
        for dot in dots:
            # Check proximity (bar/dots are ~0.2in below name)
            # Use tighter tolerance
            if abs(dot['y'] - (py + 0.20)) < 0.05:
                if dot['color'] == COLOR_BLUE:
                    year = round(x_to_year(dot['x']))
                    # Census years are usually multiples of 10
                    if abs(year % 10) <= 2: year = (year // 10) * 10
                    
                    # Sanity check with lifespan
                    if birth and death:
                        if birth - 5 <= year <= death + 5:
                            person['leads']['census'].append(year)
                elif dot['color'] == COLOR_RED:
                    # Find nearest ref number text
                    nearest_ref = None
                    min_dist = 0.5
                    for t in all_text:
                        # Ref numbers are usually 3 digits or lists
                        if re.match(r'^\d{3}(, \d{3})*$', t['text']):
                            dist = abs(t['y'] - dot['y']) + abs(t['x'] - dot['x'])
                            if dist < min_dist:
                                min_dist = dist
                                nearest_ref = t['text']
                    if nearest_ref:
                        person['leads']['records'].append(nearest_ref)
        
        # Deduplicate and sort
        person['leads']['census'] = sorted(list(set(person['leads']['census'])))
        person['leads']['records'] = sorted(list(set(person['leads']['records'])))

        # Check for RIP/Obit text near the person
        for t in all_text:
            if abs(t['y'] - (py + 0.2)) < 0.2:
                if t['text'] == "RIP":
                    person['leads']['burial'] = True
                if t['text'] == "Obit":
                    person['leads']['obit'] = True

    return people

def main():
    all_results = []
    for file_path in RAW_FILES:
        if file_path.exists():
            print(f"Processing {file_path}...")
            results = parse_raw_file(file_path)
            all_results.extend(results)
    
    # Save results
    with open("svg_leads.json", "w", encoding='utf-8') as f:
        json.dump(all_results, f, indent=2)
    print(f"Extracted leads for {len(all_results)} entries. Saved to svg_leads.json")

if __name__ == "__main__":
    main()
