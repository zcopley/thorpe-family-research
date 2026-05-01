import re
from pathlib import Path

# Configuration
RAW_FILE = Path("References/raw/extracted/PedigreeTimelines2019Descendants2_raw.txt")
TOPICS_DIR = Path("Topics")

def extract_descendants():
    if not RAW_FILE.exists(): return
    content = RAW_FILE.read_text(encoding='utf-8')
    
    # We need to extract names and their X-coordinates to infer hierarchy.
    text_objects = re.split(r'startTextObject', content)
    
    nodes = []
    for obj in text_objects:
        x_match = re.search(r'svg:x: (-?\d+\.\d+)in', obj)
        y_match = re.search(r'svg:y: (-?\d+\.\d+)in', obj)
        text_match = re.search(r'insertText \((.*?)\)', obj)
        
        if x_match and y_match and text_match:
            x = float(x_match.group(1))
            y = float(y_match.group(1))
            text = text_match.group(1).strip()
            
            # Filter out non-names
            if any(term in text for term in ["Compiled by", "RIP", "Obit", "Found in Census", "September 2019"]):
                continue
                
            # Filter out numeric years by themselves or short text
            if re.match(r'^\d{4}$', text) or len(text) < 3:
                continue

            nodes.append({'text': text, 'x': x, 'y': y})
            
    if not nodes: return
    
    # Sort nodes by Y coordinate (top to bottom reading order)
    nodes.sort(key=lambda n: n['y'])
    
    # Infer hierarchy based on X coordinate (indentation)
    mermaid = "```mermaid\ngraph LR\n"
    
    # Rounded X coordinates to group them into "generations"
    x_levels = sorted(list(set(round(n['x'], 2) for n in nodes)))
    
    stack = [None] * len(x_levels)
    node_id_counter = 0
    
    for node in nodes:
        x_rounded = round(node['x'], 2)
        closest_level_idx = 0
        min_diff = 1000
        for i, level in enumerate(x_levels):
            if abs(x_rounded - level) < min_diff:
                min_diff = abs(x_rounded - level)
                closest_level_idx = i
                
        depth = closest_level_idx
        node_id = f"N{node_id_counter}"
        node_id_counter += 1
        
        clean_text = node['text'].replace('"', '').replace('<', '').replace('>', '')
        mermaid += f"  {node_id}[\"{clean_text}\"]\n"
        
        if depth > 0:
            parent_id = None
            for i in range(depth - 1, -1, -1):
                if stack[i] is not None:
                    parent_id = stack[i]
                    break
            
            if parent_id:
                mermaid += f"  {parent_id} --> {node_id}\n"
                
        stack[depth] = node_id
        for i in range(depth + 1, len(stack)):
            stack[i] = None
            
    mermaid += "```\n"
    
    page_content = f"""---
title: Descendants Chart (2019 Extraction)
date: 2026-04-30
tags:
  - "#thorpe-family"
  - "#topic"
  - "#diagram"
---

# Descendants Chart (2019 Extraction)

This diagram was programmatically extracted from the `PedigreeTimelines2019Descendants2` source file. Unlike the pedigree charts that trace backward, this chart follows Forward-Line Descent.

The hierarchy below was inferred by analyzing the spatial indentation levels in the original CorelDRAW data.

{mermaid}

---
*Source: `References/raw/extracted/PedigreeTimelines2019Descendants2_raw.txt`*
"""
    
    (TOPICS_DIR / "Descendants Chart 2019.md").write_text(page_content, encoding='utf-8')
    print("Generated Descendants Chart 2019.md")

if __name__ == "__main__":
    extract_descendants()
