# Kindle Vocab To Anki
Kindle stores word lookups in vocab.db file which I'd want to use for my Anki. <br> Kindle does not store definitions along with looked up words and existing Anki
plugins only operate on one card a time. <br> I have more than 700 looked up words saved in my Anki. <br>
== Idea!
## Goals of this app:
1. Reading from vocab.db through Python with SQLite. ☑️
2. Retrieving stem of looked up words along with context each word was used in. ☑️
  - [x] fetch stem words and context
  - [x] organise, so context matches word
  - [x] get rid of repeated words
3. Converting above data into .xlsx file (Excel).  ☑️ <br>
4. Using Free Dictionary API (https://dictionaryapi.dev/) to automatically add a definition to all looked up words in Excel vocab sheet. ☑️ <br>
**Far into the future**↓
5. Create a website, so others can do it too :)
## Progress updates:
Every Kindle user has in their device little file named vocab.db and in it there's a table named LOOKUPS with this data: <br>
![image](https://github.com/hebiscus/vocabConverter/assets/107350293/c1e72308-0c87-4fd2-b0cd-ed2c08278d7b) <br><br>
What I wanted to retrieve and convert to Excel file is only the word_key (without the "en:" stem) and usage (context sentence each word was highlighted in the book) columns. <br>
### Update #1 <br> 
no word duplicates and "en:" stem removed, export to xlsx thanks to pandas python data analysis library <br><br>
![image](https://github.com/hebiscus/vocabConverter/assets/107350293/24dff3be-8e60-49e6-a502-b67ee3ac7a35) <br><br>
### Update #2 
Unfortunately Words API I've planned to use for definitions initially has it's free tier limited to 2.5k requests a day, which is not nearly enough. I've resolved to Free Dictionary API and with it comes another set of issues. It's dabatabase of definitions is built on Google Dictionary API - not ideal. Out of 756 words I've tested it on 44 definitions were not found. Is it terrible, especially since my set of words looked up is old-fashioned? No. Nevertheless, it's not perfect. Another issue is speed. The same set of words took around 5-7 minutes to complete fetching all definitions. Again, not terrible, but not great either. Any other dictionary API is not generous with it's free plan. 
### Final result:
![image](https://github.com/hebiscus/KindleVocabToAnki/assets/107350293/e81d1c24-c1dd-4402-8853-e81fc769a004)

