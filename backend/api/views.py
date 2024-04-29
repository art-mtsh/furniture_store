from django.http import JsonResponse
from rest_framework import generics
from .models import *
from .serializers import *


def button_view(request):
    return JsonResponse({'message': 'Hello World'})


class RoomTypeView(generics.ListCreateAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer



class ItemCategoryView(generics.ListCreateAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer


class ManufacturerView(generics.ListCreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class CollectionView(generics.ListCreateAPIView):
    queryset = ItemCollection.objects.all()
    serializer_class = ItemCollectionSerializer


class ItemsView(generics.ListCreateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer


class ColourView(generics.ListCreateAPIView):
    queryset = ItemColour.objects.all()
    serializer_class = ItemColourSerializer


class MaterialView(generics.ListCreateAPIView):
    queryset = ItemMaterial.objects.all()
    serializer_class = ItemMaterialSerializer


class ItemPhotoView(generics.ListCreateAPIView):
    queryset = ItemPhoto.objects.all()
    serializer_class = ItemPhotoSerializer


class ItemReviewView(generics.ListCreateAPIView):
    queryset = ItemReview.objects.all()
    serializer_class = ItemReviewSerializer
