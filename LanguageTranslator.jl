using Pkg
Pkg.activate(".")

using HTTP, JSON3

# -------- CONFIG --------
INPUT_FILE = "languages/spanish_english.js"
OUTPUT_FILE = "languages/spanish_french.js"
TARGET_LANG = "fr"
SOURCE_LANG = "es"

API_URL = "http://localhost:6666/translate"

# -------- PARSE JS FILE --------
function parse_js_words(filename)
    text = read(filename, String)
    matches = eachmatch(r"\"foreign\"\s*:\s*\"([^\"]+)\"", text)
    # On s'assure d'extraire uniquement la String du premier groupe de capture
    words = [String(m.captures[1]) for m in matches]
    return words
end

# -------- BUILD OUTPUT --------
function build_output(words, translations)
    lines = ["const translated_words = ["]
    for (i, (w, t)) in enumerate(zip(words, translations))
        push!(lines, "  { \"rank\": $i, \"foreign\": \"$w\", \"translated\": \"$t\" },")
    end
    push!(lines, "];")
    return join(lines, "\n")
end

# -------- TRANSLATION FUNCTION --------
function translate_chunks(all_words; chunk_size=20)
    all_translations = String[]

    for i in 1:chunk_size:length(all_words)
        upper_limit = min(i + chunk_size - 1, length(all_words))
        chunk = all_words[i:upper_limit]

        println("Traductions mots $i à $upper_limit sur $(length(all_words))...")

        try
            body = JSON3.write(Dict(
                "q" => chunk,
                "source" => SOURCE_LANG,
                "target" => TARGET_LANG,
                "format" => "text"
            ))

            response = HTTP.post(
                API_URL,
                ["Content-Type" => "application/json"],
                body
            )

            data = JSON3.read(String(response.body))

            # Extraction propre des résultats
            if haskey(data, :translatedText)
                append!(all_translations, Vector{String}(data.translatedText))
                println("   ✅ Succès")
            else
                error("Format de réponse inconnu")
            end

            sleep(1.5) # Pause de sécurité

        catch e
            println("   ❌ Échec du paquet $i : ", e)
            append!(all_translations, fill("ERROR", length(chunk)))
        end
    end
    return all_translations
end

# -------- MAIN --------
function main()
    if !isfile(INPUT_FILE)
        println("Erreur : Fichier '$INPUT_FILE' non trouvé.")
        return
    end

    println("1. Lecture des mots...")
    words = parse_js_words(INPUT_FILE)

    if isempty(words)
        println("Aucun mot trouvé.")
        return
    end

    println("2. Traduction de $(length(words)) mots...")
    translations = translate_chunks(words, chunk_size=15) # Taille réduite pour la stabilité

    println("3. Écriture du fichier...")
    output = build_output(words, translations)
    write(OUTPUT_FILE, output)

    println("Fini ! Résultat dans $OUTPUT_FILE")
end

main()
