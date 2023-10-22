from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import sqlite3
import tempfile
import os
import pandas
from dictionary import word_dict

@api_view(['POST'])
def upload_vocab(request):
  vocab_file = request.FILES['file']

  if vocab_file and vocab_file.name.endswith('.db'):
    try: 
      with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                for chunk in vocab_file.chunks():
                    temp_file.write(chunk)
      
      connection = sqlite3.connect(temp_file.name)
      cursor = connection.cursor()

      cursor.execute("DELETE FROM LOOKUPS WHERE EXISTS (SELECT 1 FROM LOOKUPS P2 WHERE LOOKUPS.word_key = p2.word_key AND LOOKUPS.rowid > p2.rowid)")
      cursor.execute("UPDATE LOOKUPS SET word_key = SUBSTRING(word_key, 4)")
      cursor.execute("SELECT word_key, usage FROM LOOKUPS")

      nonDuplicates = cursor.fetchall()

      connection.commit()
      connection.close()

      df = pandas.DataFrame(nonDuplicates, columns=["Word", "Context"])
      df['Definitions'] = df.apply(getDefinitions, axis=1)
      df.to_csv('result.csv', index = False)

    except Exception as e:
      return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    finally:
      temp_file.close()
      os.unlink(temp_file.name)

  return JsonResponse({"message": "test message"})


def getDefinitions(row):
    word = row['Word'].capitalize()

    wordDef = word_dict.get(word, "definition not found")
    
    return wordDef 