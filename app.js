// --- CONFIGURATION ---
// "data" doit correspondre exactement au nom de la variable dans vos fichiers .js
const availableLanguages = [
    { name: "Espagnol", data: spanish_english },
    { name: "Coréen", data: korean_english }
];

let allWords = [];
const card = document.getElementById('flashcard');
const sideMenu = document.getElementById('side-menu');

// 1. Génération du menu
function initMenu() {
    const langList = document.getElementById('lang-list');
    langList.innerHTML = "";
    
    availableLanguages.forEach(lang => {
        const btn = document.createElement('button');
        btn.className = 'lang-btn';
        btn.textContent = lang.name;
        btn.onclick = () => {
            selectLanguage(lang.data, lang.name);
            sideMenu.classList.remove('open');
        };
        langList.appendChild(btn);
    });
}

// 2. Sélection de la langue
function selectLanguage(data, name) {
    allWords = data;
    document.getElementById('app-title').textContent = `1000 Mots : ${name}`;
    updateWord();
}

// 3. Logique Flashcard (Inchangée)
function updateWord() {
    if (!allWords || allWords.length === 0) return;
    
    const poolSize = parseInt(document.getElementById('pool-size').value) || 1000;
    const pool = allWords.slice(0, poolSize);
    const randomWord = pool[Math.floor(Math.random() * pool.length)];
    
    card.classList.remove('flipped');
    
    setTimeout(() => {
        // Dans votre fonction updateWord :
        document.getElementById('foreign-word').textContent = randomWord.foreign;


        
        // Construction du contenu de la face arrière
        let backContent = randomWord.english;
        
        // Si une prononciation est disponible (comme pour le coréen), on l'ajoute
        console.log(randomWord.pronunciation)
        if (randomWord.pronunciation) {
            console.log(true)
            backContent = `<small style="display:block; font-size: 0.8em; opacity: 0.7; margin-bottom: 5px;">[${randomWord.pronunciation}]</small>` + backContent;
        }
        
        // On utilise innerHTML au lieu de textContent pour permettre le <small>
        document.getElementById('translation-word').innerHTML = backContent; 
    }, 200);
}


// Événements
document.getElementById('menu-toggle').onclick = () => sideMenu.classList.toggle('open');
document.getElementById('next-btn').onclick = updateWord;
card.onclick = () => card.classList.toggle('flipped');

// Lancement
initMenu();
// Charge la première langue de la liste par défaut
selectLanguage(availableLanguages[0].data, availableLanguages[0].name);
