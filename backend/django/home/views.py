from .services.save_temp_file import save_temp_file
from .services.get_unique_words import get_unique_words
from .services.generate_csv import generate_csv
from django.http import FileResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import os


@api_view(['POST'])
def upload_vocab(request):
  vocab_file = request.FILES['file']

  try:
      db_file_path = save_temp_file(vocab_file)
      unique_words = get_unique_words(db_file_path)
      generate_csv(unique_words)

      return FileResponse(open('result.csv', 'rb'))

  except Exception as e:
      return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  finally:
      if os.path.exists(db_file_path):
          os.remove(db_file_path)