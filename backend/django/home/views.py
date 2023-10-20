from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['POST'])
def upload_vocab(request):
  return JsonResponse({"message": "test message"})