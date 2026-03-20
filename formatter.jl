using Pkg
Pkg.activate(".")

using JSON

# 1. Lecture du fichier
input_file = "languages/spanish_english.js"
content = read(input_file, String)

# 2. Extraction du JSON via Regex (le 's' permet de gérer les sauts de ligne)
m = match(r"\[.*\]"s, content)

if m === nothing
    error("Impossible de trouver le tableau JSON dans le fichier.")
end

# 3. Parsing du JSON
data = JSON.parse(m.match)

# 4. Modification des clés
for entry in data
    if haskey(entry, "english")
        # On stocke la valeur, on crée la nouvelle clé, on supprime l'ancienne
        val = entry["english"]
        entry["translated"] = val
        delete!(entry, "english")
    end
end

# 5. Conversion en chaîne JSON formatée (4 espaces pour l'indentation)
updated_json = JSON.json(data, 4)

# 6. Reconstruction de la structure JavaScript
final_output = "const spanish_english = " * updated_json * ";"

# 7. Écriture
write("votre_fichier_modifie.js", final_output)
println("Succès ! Les clés 'english' ont été renommées en 'translation'.")
