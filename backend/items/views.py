from django.http import JsonResponse, HttpResponse, Http404
from django.utils.decorators import method_decorator
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *

from brake.decorators import ratelimit
from sematext import log_engine

ratelimit_m = '10/m'


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
    serializer_class = ItemCategorySerializer

    def get_queryset(self):
        room_id = self.kwargs.get('room_id')
        if room_id is not None:
            obj = ItemCategory.objects.filter(room_id=room_id)
            if not obj:
                raise Http404('Categories not found.')
            return obj

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
    serializer_class = ItemsSerializer

    def get_queryset(self):
        cat_id = self.kwargs.get('cat_id')
        if cat_id is not None:
            obj = Items.objects.filter(item_category_id=cat_id)
            if not obj:
                raise Http404('Items not found.')
            return obj
        return Items.objects.all()



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
