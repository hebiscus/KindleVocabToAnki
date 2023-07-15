import sqlite3
import pandas as pandas
from openpyxl import load_workbook
import config
import http.client

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

# printNonDuplicates()

def ImportToExcel():
    df = pandas.DataFrame(nonDuplicates, columns=["Word", "Context"])
    df.to_excel('result.xlsx', index = False)

ImportToExcel()

wb = load_workbook(filename="result.xlsx")
workSheet = wb.active

def iterateOverWords():
    for column in workSheet.iter_cols(min_row=2, max_col=1, values_only=True):
        for value in column:
            print(value)

def connectToAPI():
    conn = http.client.HTTPSConnection("wordsapiv1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': config.api_key,
        'X-RapidAPI-Host': "wordsapiv1.p.rapidapi.com"
    }

    conn.request("GET", "/words/hatchback/definitions", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))