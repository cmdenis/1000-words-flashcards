# 1000-words-flashcards

A vibe-coded website with flashcards to learn a thousand words in a bunch of languages. Made using a mix of gemini, copilot and chatgpt.

To add languages or a collection to the flashcards, add in a `.js` file formatted the same way that the other ones are. You'll also need to modify the `availableLanguages` variable in the `app.js` script to include your new flashcard set. Furthermore, you'll need to reference your `.js` file containing your "question-answer" pair in the `index.html` file using a tag like

```html
<script src="languages/sourceLanguage_targetLanguage.js"></script>
```

where you can replace `sourceLanguage_targetLanguage` with the name of your file. I kept the `.txt` files in the `languages` folder just in case. I got them from the [1000mostcommonwords.com](https://1000mostcommonwords.com/) website.
