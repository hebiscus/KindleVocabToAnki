import sqlite3


def get_unique_words(db_file):
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM LOOKUPS WHERE EXISTS (SELECT 1 FROM LOOKUPS P2 WHERE LOOKUPS.word_key = p2.word_key AND LOOKUPS.rowid > p2.rowid)"
        )
        cursor.execute("UPDATE LOOKUPS SET word_key = SUBSTRING(word_key, 4)")
        cursor.execute("SELECT word_key, usage FROM LOOKUPS")

        non_duplicates = cursor.fetchall()

        connection.commit()
        connection.close()

        return non_duplicates
    except Exception as e:
        raise Exception(f"Database error: {str(e)}")
