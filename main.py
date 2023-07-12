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



# cursor.execute("SELECT word, usage FROM WORDS INNER JOIN LOOKUPS on LOOKUPS.timestamp == WORDS.timestamp")

# print(cursor.fetchall())

# cursor.execute("SELECT word_key, COUNT(*) AS CNT FROM LOOKUPS GROUP BY word_key HAVING COUNT(*) > 1")

# cursor.execute("SELECT DISTINCT word_key FROM LOOKUPS")

# print(cursor.fetchall())

# cursor.execute("SELECT COUNT(DISTINCT word_key), usage FROM LOOKUPS")

cursor.execute("SELECT word_key,usage, COUNT(*) as cnt FROM LOOKUPS GROUP BY word_key HAVING COUNT(*) > 1")

print(cursor.fetchall())

cursor.execute("SELECT COUNT(DISTINCT word_key) FROM LOOKUPS")
print(cursor.fetchall())
# cursor.execute("SELECT * FROM LOOKUPS WHERE word_key NOT IN( SELECT MAX(word_key) FROM LOOKUPS GROUP BY word_key)")

# print(cursor.fetchall())

connection.commit()

connection.close()