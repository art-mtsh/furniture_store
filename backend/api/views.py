from django.http import JsonResponse
from rest_framework import generics
# from .models import TestTextModel
# from .serializers import TestTextSerializer


def button_view(request):
    return JsonResponse({'message': 'Hello World'})


# class TestTextModelListCreate(generics.ListCreateAPIView):
#     queryset = TestTextModel.objects.all()
#     serializer_class = TestTextSerializer
