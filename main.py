import sqlite3
import pandas as pandas
from openpyxl import load_workbook
import config
import http.client
import requests

connection = sqlite3.connect("vocab.db")

cursor = connection.cursor()

def deleteDuplicates():
    cursor.execute("DELETE FROM LOOKUPS WHERE EXISTS (SELECT 1 FROM LOOKUPS P2 WHERE LOOKUPS.word_key = p2.word_key AND LOOKUPS.rowid > p2.rowid)")

def deleteEN():
    cursor.execute("UPDATE LOOKUPS SET word_key = SUBSTRING(word_key, 4)")

def getUpdatedWords():
    cursor.execute("SELECT word_key, usage FROM LOOKUPS")

deleteDuplicates()
deleteEN()
getUpdatedWords()
nonDuplicates = cursor.fetchall()

connection.commit()

connection.close()

def printNonDuplicates():
    for word in nonDuplicates:
        print(word)


def getDefinitions(row):
    word = row['Word']
    response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word)

    if (isinstance(response.json(), dict)):
        return "definition not found"

    wordData = response.json()[0]["meanings"]
    wordDefinitions = ""

    for wordType in wordData:
        wordDefinitions += wordType["definitions"][0]["definition"]
    
    return wordDefinitions


def ImportToExcel():
    df = pandas.DataFrame(nonDuplicates, columns=["Word", "Context"])
    df['Definition'] = df.apply(getDefinitions, axis=1)
    df.to_excel('result.xlsx', index = False)

ImportToExcel()



# def addDefinitions():
#     wb = load_workbook(filename="result.xlsx")
#     workSheet = wb.active

#     defCell = workSheet['C1']
#     defCell.value = "Definitions"

#     wordColumn = workSheet['A'] - workSheet['A1']

#     for index, word in enumerate(wordColumn, start=2):
#         print(str(word.value))
#         wordDefinitions = getDefinitions(word)
#         workSheet['C'+str(index)] = wordDefinitions


#     wb.save('definitions.xlsx')

# addDefinitions()

