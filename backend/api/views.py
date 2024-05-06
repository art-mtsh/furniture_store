from django.http import JsonResponse, HttpResponse
from .serializers import *

from django.utils.decorators import method_decorator
from rest_framework import generics
from brake.decorators import ratelimit

from sematext import log_engine


@ratelimit(block=True, rate='5/m')
def button_view(request):
    return JsonResponse({'message': 'Hello World'})


class RoomTypeView(generics.ListCreateAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer

    try:
        @method_decorator(ratelimit(block=False, rate='5/m'))
        def dispatch(self, request, *args, **kwargs):
            log_engine.info('Request to RoomTypeView')
            if getattr(request, 'limits', {}):
                log_engine.warning('Too many requests for RoomTypeView')
                return HttpResponse('Too many requests', status=429, content_type='text/plain')
            return super().dispatch(request, *args, **kwargs)
    except Exception as e:
        log_engine.error("An error occurred: %s", str(e), exc_info=True)


class ItemCategoryView(generics.ListCreateAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer

    try:
        @method_decorator(ratelimit(block=False, rate='5/m'))
        def dispatch(self, request, *args, **kwargs):
            log_engine.info('Request to ItemCategoryView')
            if getattr(request, 'limits', {}):
                log_engine.warning('Too many requests for ItemCategoryView')
                return HttpResponse('Too many requests', status=429, content_type='text/plain')
            return super().dispatch(request, *args, **kwargs)
    except Exception as e:
        log_engine.error("An error occurred: %s", str(e), exc_info=True)


class ManufacturerView(generics.ListCreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

    try:
        @method_decorator(ratelimit(block=False, rate='5/m'))
        def dispatch(self, request, *args, **kwargs):
            log_engine.info('Request to ManufacturerView')
            if getattr(request, 'limits', {}):
                log_engine.warning('Too many requests for ManufacturerView')
                return HttpResponse('Too many requests', status=429, content_type='text/plain')
            return super().dispatch(request, *args, **kwargs)
    except Exception as e:
        log_engine.error("An error occurred: %s", str(e), exc_info=True)


class CollectionView(generics.ListCreateAPIView):
    queryset = ItemCollection.objects.all()
    serializer_class = ItemCollectionSerializer

    try:
        @method_decorator(ratelimit(block=False, rate='5/m'))
        def dispatch(self, request, *args, **kwargs):
            log_engine.info('Request to CollectionView')
            if getattr(request, 'limits', {}):
                log_engine.warning('Too many requests for CollectionView')
                return HttpResponse('Too many requests', status=429, content_type='text/plain')
            return super().dispatch(request, *args, **kwargs)
    except Exception as e:
        log_engine.error("An error occurred: %s", str(e), exc_info=True)


class ItemsView(generics.ListCreateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

    try:
        @method_decorator(ratelimit(block=False, rate='5/m'))
        def dispatch(self, request, *args, **kwargs):
            log_engine.info('Request to ItemsView')
            if getattr(request, 'limits', {}):
                log_engine.warning('Too many requests for ItemsView')
                return HttpResponse('Too many requests', status=429, content_type='text/plain')
            return super().dispatch(request, *args, **kwargs)
    except Exception as e:
        log_engine.error("An error occurred: %s", str(e), exc_info=True)


class ColourView(generics.ListCreateAPIView):
    queryset = ItemColour.objects.all()
    serializer_class = ItemColourSerializer

    try:
        @method_decorator(ratelimit(block=False, rate='5/m'))
        def dispatch(self, request, *args, **kwargs):
            log_engine.info('Request to ColourView')
            if getattr(request, 'limits', {}):
                log_engine.warning('Too many requests for ColourView')
                return HttpResponse('Too many requests', status=429, content_type='text/plain')
            return super().dispatch(request, *args, **kwargs)
    except Exception as e:
        log_engine.error("An error occurred: %s", str(e), exc_info=True)


class MaterialView(generics.ListCreateAPIView):
    queryset = ItemMaterial.objects.all()
    serializer_class = ItemMaterialSerializer

    try:
        @method_decorator(ratelimit(block=False, rate='5/m'))
        def dispatch(self, request, *args, **kwargs):
            log_engine.info('Request to MaterialView')
            if getattr(request, 'limits', {}):
                log_engine.warning('Too many requests for MaterialView')
                return HttpResponse('Too many requests', status=429, content_type='text/plain')
            return super().dispatch(request, *args, **kwargs)
    except Exception as e:
        log_engine.error("An error occurred: %s", str(e), exc_info=True)


class ItemPhotoView(generics.ListCreateAPIView):
    queryset = ItemPhoto.objects.all()
    serializer_class = ItemPhotoSerializer

    try:
        @method_decorator(ratelimit(block=False, rate='5/m'))
        def dispatch(self, request, *args, **kwargs):
            log_engine.info('Request to ItemPhotoView')
            if getattr(request, 'limits', {}):
                log_engine.warning('Too many requests for ItemPhotoView')
                return HttpResponse('Too many requests', status=429, content_type='text/plain')
            return super().dispatch(request, *args, **kwargs)
    except Exception as e:
        log_engine.error("An error occurred: %s", str(e), exc_info=True)


class ItemReviewView(generics.ListCreateAPIView):
    queryset = ItemReview.objects.all()
    serializer_class = ItemReviewSerializer

    try:
        @method_decorator(ratelimit(block=False, rate='5/m'))
        def dispatch(self, request, *args, **kwargs):
            log_engine.info('Request to ItemReviewView')
            if getattr(request, 'limits', {}):
                log_engine.warning('Too many requests for ItemReviewView')
                return HttpResponse('Too many requests', status=429, content_type='text/plain')
            return super().dispatch(request, *args, **kwargs)
    except Exception as e:
        log_engine.error("An error occurred: %s", str(e), exc_info=True)
