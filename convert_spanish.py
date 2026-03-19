#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convert Spanish 1000-word frequency list to JavaScript format"""

import re

def convert_spanish_to_js():
    """Convert spanish_1000.txt to JavaScript array format"""

    # Read the input file
    with open('./languages/spanish_1000.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    js_entries = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Split by tab
        parts = line.split('\t')
        if len(parts) != 3:
            print(f"Warning: Skipping malformed line: {line}")
            continue

        rank, spanish_word, english_translation = parts

        # Clean up the data
        rank = int(rank.strip())
        spanish_word = spanish_word.strip()
        english_translation = english_translation.strip()

        # Add politeness/formality notes where relevant
        if spanish_word in ['usted', 'señor', 'señora', 'señorita']:
            english_translation += " (formal)"
        elif spanish_word in ['tú', 'vos']:
            english_translation += " (informal)"
        elif spanish_word == 'vosotros':
            english_translation += " (informal plural, Spain)"
        elif spanish_word == 'ustedes':
            english_translation += " (formal plural or informal plural in Latin America)"

        # Create the JavaScript object
        js_entry = f'  {{ "rank": {rank}, "foreign": "{spanish_word}", "english": "{english_translation}" }}'
        js_entries.append(js_entry)

    # Create the complete JavaScript file
    js_content = """const spanish_english = [
""" + ',\n'.join(js_entries) + """
];"""

    # Write to file
    with open('./languages/spanish_english.js', 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"Converted {len(js_entries)} entries to spanish_english.js")

if __name__ == "__main__":
    convert_spanish_to_js()