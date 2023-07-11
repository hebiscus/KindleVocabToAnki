import sqlite3

connection = sqlite3.connect("vocab.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM WORDS")

threeWords = cursor.fetchmany(3)

cursor.execute("SELECT * FROM LOOKUPS")

threeContext = cursor.fetchmany(3)

def list_three():
    for x in range(3):
        print("stem:" + " " + threeWords[x][2] + " " + "context:" + " " + threeContext[x][5])

list_three()

connection.commit()

connection.close()