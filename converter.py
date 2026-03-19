import json
import os

def convert_to_universal(filename, lang_key):
    path = f"./languages/{filename}"
    if not os.path.exists(path):
        print(f"Fichier {filename} introuvable.")
        return

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # On transforme chaque objet pour utiliser la clé 'foreign'
    universal_data = [
        {
            "rank": item.get("rank"),
            "foreign": item.get(lang_key),
            "english": item.get("english")
        }
        for item in data
    ]

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(universal_data, f, indent=2, ensure_ascii=False)
    print(f"Conversion terminée pour {filename}")

# Exemples d'utilisation :
# convert_to_universal("spanish_english.json", "spanish")
# convert_to_universal("korean_english.json", "korean")
