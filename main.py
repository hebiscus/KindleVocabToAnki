import sqlite3

connection = sqlite3.connect("vocab.db")

cursor = connection.cursor()

# cursor.execute("SELECT * FROM WORDS")

# threeWords = cursor.fetchmany(3)

# cursor.execute("SELECT * FROM LOOKUPS")

# threeContext = cursor.fetchmany(3)

# def list_three():
#     for x in range(3):
#         print("stem:" + " " + threeWords[x][2] + " " + "context:" + " " + threeContext[x][5])

# list_three()


# cursor.execute("SELECT word_key, COUNT(*) AS CNT FROM LOOKUPS GROUP BY word_key HAVING COUNT(*) > 1")

# cursor.execute("SELECT DISTINCT word_key FROM LOOKUPS")

# print(cursor.fetchall())

# cursor.execute("SELECT COUNT(DISTINCT word_key), usage FROM LOOKUPS")

cursor.execute("DELETE FROM LOOKUPS WHERE EXISTS (SELECT 1 FROM LOOKUPS P2 WHERE LOOKUPS.word_key = p2.word_key AND LOOKUPS.rowid > p2.rowid)")

cursor.execute("SELECT COUNT(word_key) FROM LOOKUPS")
print(cursor.fetchall())

cursor.execute("SELECT word_key, usage FROM LOOKUPS")
print(cursor.fetchall())

connection.commit()

connection.close()