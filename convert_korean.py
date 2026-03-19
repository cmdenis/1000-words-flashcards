#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from hangul_utils.unicode import decompose

# Korean romanization mapping
KOREAN_ROMANIZATION = {
    # Consonants (자음)
    'ㄱ': 'g', 'ㄲ': 'kk', 'ㄴ': 'n', 'ㄷ': 'd', 'ㄸ': 'dd', 'ㄹ': 'r',
    'ㅁ': 'm', 'ㅂ': 'b', 'ㅃ': 'bb', 'ㅅ': 's', 'ㅆ': 'ss', 'ㅇ': '',
    'ㅈ': 'j', 'ㅉ': 'jj', 'ㅊ': 'ch', 'ㅋ': 'k', 'ㅌ': 't', 'ㅍ': 'p',
    'ㅎ': 'h',
    # Vowels (모음)
    'ㅏ': 'a', 'ㅑ': 'ya', 'ㅓ': 'eo', 'ㅕ': 'yeo', 'ㅗ': 'o', 'ㅛ': 'yo',
    'ㅜ': 'u', 'ㅠ': 'yu', 'ㅡ': 'eu', 'ㅣ': 'i',
    'ㅐ': 'ae', 'ㅒ': 'yae', 'ㅔ': 'e', 'ㅖ': 'oe', 'ㅘ': 'wa', 'ㅝ': 'wo',
    'ㅞ': 'we', 'ㅙ': 'wae', 'ㅚ': 'o', 'ㅝ': 'wo',
    'ㅢ': 'ui', 'ㅥ': 'wi', 'ㅤ': '',
}

def romanize_korean(korean_word):
    """Convert Korean word to romanization."""
    try:
        # Try using hangul-utils if available
        from hangul_utils import decompose, compose
        result = ""
        for char in korean_word:
            if ord(char) >= 0xAC00 and ord(char) <= 0xD7A3:  # Hangul syllable range
                cho, jung, jong = decompose(char)
                result += KOREAN_ROMANIZATION.get(cho, '')
                result += KOREAN_ROMANIZATION.get(jung, '')
                if jong:
                    result += KOREAN_ROMANIZATION.get(jong, '')
            else:
                result += char
        return result
    except:
        # Fallback for common words if library not available
        manual_romanization = {
            '로': 'ro', '나는': 'naneun', '그의': 'geuui', '그': 'geu',
            '했다': 'haetda', '에 대한': 'e daehae', '에': 'e', '아르': 'areu',
            '와': 'wa', '그들': 'geudeu', '있다': 'itda', '일': 'il',
            '이': 'i', '부터': 'buteo', '에 의해': 'e uihae', '뜨거운': 'tteugeoun',
            '단어': 'dan-eo', '하지만': 'hajiman', '무엇': 'mueos', '다소': 'daseo',
            '이다': 'ida', '당신': 'dangshin', '또는': 'toneun', '의': 'ui',
            '과': 'gwa', '우리': 'uri', '수': 'su', '아웃': 'aut',
            '다른': 'dareun', '하는': 'haneun', '할': 'hal', '자신의': 'jasineur',
            '시간': 'sigan', '면': 'myeon', '것': 'geot', '방법': 'bangbeob',
            '말했다': 'malhaetda', '각': 'gak', '이야기': 'iyagi',
        }
        return manual_romanization.get(korean_word, korean_word)

# Read the korean_1000.txt file
with open('/Users/christiandenis/Desktop/Autres/Hobbies/Programmation/2026/1000-words-flashcards/languages/korean_1000.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Process each line
entries = []
for line in lines:
    parts = line.strip().split('\t')
    if len(parts) >= 3:
        rank, korean, english = parts[0], parts[1], parts[2]
        pronunciation = romanize_korean(korean)
        entries.append({
            'rank': int(rank),
            'korean': korean,
            'pronunciation': pronunciation,
            'english': english
        })

# Generate JavaScript
js_output = "const korean_english = [\n"
for entry in entries:
    js_output += f'  {{ "rank": {entry["rank"]}, "foreign": "{entry["korean"]}", "pronunciation": "{entry["pronunciation"]}", "english": "{entry["english"]}" }},\n'
js_output += "];\n"

# Write output
with open('/Users/christiandenis/Desktop/Autres/Hobbies/Programmation/2026/1000-words-flashcards/languages/korean_english.js', 'w', encoding='utf-8') as f:
    f.write(js_output)

print(f"Converted {len(entries)} Korean words to korean_english.js")
