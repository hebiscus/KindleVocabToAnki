# vocabConverter
Kindle stores word lookups in vocab.db file which I'd want to use for my Anki. <br> Kindle does not store definitions along with looked up words and existing Anki
plugins only operate on one card a time. <br> I have more than 700 looked up words saved in my Anki. <br>
== Idea!
## Goals of this app:
1. Reading from vocab.db through Python with SQLite. ☑️
2. Retrieving stem of looked up words along with book name and context each word was used in.
  - [x] fetch stem words and context
  - [x] organise, so context matches word
  - [x] get rid of repeated words
3. Converting above data into .xls file (Excel). <br>
**Far into the future**↓
4. Using WordsAPI (https://www.wordsapi.com) to automatically add a definition to all looked up words in Excel vocab sheet. <br>
**Even more far into the future**↓
5. Create a website, so others can do it too :)
