from django.http import JsonResponse
from .serializers import *

from django.utils.decorators import method_decorator
from rest_framework import generics
from brake.decorators import ratelimit


@ratelimit(block=True, rate='5/m')
def button_view(request):
    return JsonResponse({'message': 'Hello World'})


class RoomTypeView(generics.ListCreateAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer

    @method_decorator(ratelimit(block=True, rate='5/m'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ItemCategoryView(generics.ListCreateAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer

    @method_decorator(ratelimit(block=True, rate='5/m'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ManufacturerView(generics.ListCreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

    @method_decorator(ratelimit(block=True, rate='5/m'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CollectionView(generics.ListCreateAPIView):
    queryset = ItemCollection.objects.all()
    serializer_class = ItemCollectionSerializer

    @method_decorator(ratelimit(block=True, rate='5/m'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ItemsView(generics.ListCreateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

    @method_decorator(ratelimit(block=True, rate='5/m'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ColourView(generics.ListCreateAPIView):
    queryset = ItemColour.objects.all()
    serializer_class = ItemColourSerializer

    @method_decorator(ratelimit(block=True, rate='5/m'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class MaterialView(generics.ListCreateAPIView):
    queryset = ItemMaterial.objects.all()
    serializer_class = ItemMaterialSerializer

    @method_decorator(ratelimit(block=True, rate='5/m'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ItemPhotoView(generics.ListCreateAPIView):
    queryset = ItemPhoto.objects.all()
    serializer_class = ItemPhotoSerializer

    @method_decorator(ratelimit(block=True, rate='5/m'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ItemReviewView(generics.ListCreateAPIView):
    queryset = ItemReview.objects.all()
    serializer_class = ItemReviewSerializer

    @method_decorator(ratelimit(block=True, rate='5/m'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
