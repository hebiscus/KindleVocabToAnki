import sqlite3

connection = sqlite3.connect("vocab.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM WORDS")
print(cursor.fetchone())

print("command succesfull")

connection.commit()

connection.close()