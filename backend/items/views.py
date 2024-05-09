from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *

from brake.decorators import ratelimit
from sematext import log_engine

ratelimit_m = '10/m'


@ratelimit(block=True, rate=ratelimit_m)
def button_view(request):
    return JsonResponse({'message': 'Hello World'})


# 1234

class ItemRoomTypeView(generics.ListCreateAPIView):
    queryset = ItemRoomType.objects.all()
    serializer_class = RoomTypeSerializer
    try:
        @method_decorator(ratelimit(block=False, rate=ratelimit_m))
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
        @method_decorator(ratelimit(block=False, rate=ratelimit_m))
        def dispatch(self, request, *args, **kwargs):
            log_engine.info('Request to ItemCategoryView')
            if getattr(request, 'limits', {}):
                log_engine.warning('Too many requests for ItemCategoryView')
                return HttpResponse('Too many requests', status=429, content_type='text/plain')
            return super().dispatch(request, *args, **kwargs)
    except Exception as e:
        log_engine.error("An error occurred: %s", str(e), exc_info=True)


class ManufacturerView(generics.ListCreateAPIView):
    queryset = ItemManufacturer.objects.all()
    serializer_class = ManufacturerSerializer

    try:
        @method_decorator(ratelimit(block=False, rate=ratelimit_m))
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
        @method_decorator(ratelimit(block=False, rate=ratelimit_m))
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
        @method_decorator(ratelimit(block=False, rate=ratelimit_m))
        def dispatch(self, request, *args, **kwargs):
            log_engine.info('Request to ItemsView')
            if getattr(request, 'limits', {}):
                log_engine.warning('Too many requests for ItemsView')
                return HttpResponse('Too many requests', status=429, content_type='text/plain')
            return super().dispatch(request, *args, **kwargs)
    except Exception as e:
        log_engine.error("An error occurred: %s", str(e), exc_info=True)


class ItemMaterialsView(generics.ListCreateAPIView):
    queryset = ItemMaterials.objects.all()
    serializer_class = ItemMaterialsSerializer

    try:
        @method_decorator(ratelimit(block=False, rate=ratelimit_m))
        def dispatch(self, request, *args, **kwargs):
            log_engine.info('Request to ItemMaterials')
            if getattr(request, 'limits', {}):
                log_engine.warning('Too many requests for ItemMaterials')
                return HttpResponse('Too many requests', status=429, content_type='text/plain')
            return super().dispatch(request, *args, **kwargs)
    except Exception as e:
        log_engine.error("An error occurred: %s", str(e), exc_info=True)


class ItemHardBodyView(generics.ListCreateAPIView):
    queryset = ItemHardBody.objects.all()
    serializer_class = ItemHardBodySerializer

    try:
        @method_decorator(ratelimit(block=False, rate=ratelimit_m))
        def dispatch(self, request, *args, **kwargs):
            log_engine.info('Request to ItemHardBody')
            if getattr(request, 'limits', {}):
                log_engine.warning('Too many requests for ItemHardBody')
                return HttpResponse('Too many requests', status=429, content_type='text/plain')
            return super().dispatch(request, *args, **kwargs)
    except Exception as e:
        log_engine.error("An error occurred: %s", str(e), exc_info=True)


class ItemSoftBodyView(generics.ListCreateAPIView):
    queryset = ItemSoftBody.objects.all()
    serializer_class = ItemSoftBodySerializer

    try:
        @method_decorator(ratelimit(block=False, rate=ratelimit_m))
        def dispatch(self, request, *args, **kwargs):
            log_engine.info('Request to ItemSoftBody')
            if getattr(request, 'limits', {}):
                log_engine.warning('Too many requests for ItemSoftBody')
                return HttpResponse('Too many requests', status=429, content_type='text/plain')
            return super().dispatch(request, *args, **kwargs)
    except Exception as e:
        log_engine.error("An error occurred: %s", str(e), exc_info=True)


class ItemPhotoView(generics.ListCreateAPIView):
    queryset = ItemPhoto.objects.all()
    serializer_class = ItemPhotoSerializer

    try:
        @method_decorator(ratelimit(block=False, rate=ratelimit_m))
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
        @method_decorator(ratelimit(block=False, rate=ratelimit_m))
        def dispatch(self, request, *args, **kwargs):
            log_engine.info('Request to ItemReviewView')
            if getattr(request, 'limits', {}):
                log_engine.warning('Too many requests for ItemReviewView')
                return HttpResponse('Too many requests', status=429, content_type='text/plain')
            return super().dispatch(request, *args, **kwargs)
    except Exception as e:
        log_engine.error("An error occurred: %s", str(e), exc_info=True)
