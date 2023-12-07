# Kindle Vocab To Anki<br> https://kindle-vocab-to-anki.vercel.app/
This app allows you to turn your Kindle english vocabulary (word you highlighted) along with definitions and context for each word into a .csv file, which can be then used for Anki flashcards!<br><br>
Important note: Definitions for only "open-class words": nouns, verbs, adjectives, and adverbs. Thus, excluded words include determiners, prepositions, pronouns, conjunctions, and particles.
## Built with:
Typescript, React, Django (rest framework, nltk wordnet), Tailwind
## Performance:
Definitions are fetched out of Wordnet using nltk wordnet module: https://www.nltk.org/howto/wordnet.html, https://wordnet.princeton.edu/<br>
Out of 755 words I had to get definitions for 19 failed - which is amazing. Among those "failed" were words like: "what", "doth", "of", etc. - not open-class words as it is required by Wordnet itself. That said, there's definitely some legitimate words Wordnet doesn't have in its database like "almshouse" or "henpeck" or real archaic ones like "vittle", which is important to keep in mind. 
## Instructions:
Video version: https://www.youtube.com/watch?v=oYFIydvBSEk<br>
1. First you need to get your looked up words out of you Kindle via USB. Fortunately, they’re stored for us at: Kindle/system/vocabulary/vocab.db. If you can’t find it, go to the main Kindle folder and search for vocab.db. It’s hiding somewhere!
2. Next, upload the same file on the homepage after clicking “Choose a file” and “Upload”.
3. Tadahh! If everything went smoothly (ekhem, my other server didn’t crash) you should see a big purple “Download” button. Click on it and save your words.csv file onto your device. 

Next comes the Anki part for which you’ll use the file you just downloaded. 

1. Open your Anki and go to Tools > Manage Note Types. Depending on the style you wish to pick for your flashcards you’ll need to click “Add”. If you want good old default flashcards pick Add:Basic. 
2. Give it some name, click on it when it shows up in your list of note types and click “Fields”. 
3. That’s the place you’re formatting the fields of the notes. Naming doesn’t matter much (although you must remember it for next step, so it’s best you keep it Word, Context and…
4. Add a new field and call it Definition! Don’t forget about saving your changes.
5. Next up you have to format the flashcard itself. For that click “Cards”.
6. Formatting a card is totally up to you. I’ve went for a simple layout where there’s two sides: Word on the front and Context + Definition on the back. As you can see on the video instructions to include Definition on the back you need to do this: {{Definition}}. All the other styles are simple HTML styles to make it a little prettier. 
7. Click that save! 
8. On the main screen of Anki click “Import File” and pick words.csv file you downloaded.
9. Here go the important parts: for field separator choose “Comma”, Allow for HMTL in fields, for the Notetype choose the one you made a minute ago and click “Import”. 
10. You’ll see a new deck name “Default” with all your flashcards!
