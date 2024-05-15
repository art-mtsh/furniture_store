from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from rest_framework import generics, views

from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *

from brake.decorators import ratelimit
from sematext import log_engine
from django.db.models import Q

ratelimit_m = '10/m'


class ItemRoomTypeView(generics.ListCreateAPIView):
    queryset = ItemRoomType.objects.all().order_by('id')
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
            obj = ItemCategory.objects.filter(room_id=room_id).order_by('id')
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


class ItemsView(generics.ListCreateAPIView):
    serializer_class = ItemsSerializer

    def get_queryset(self):
        cat_id = self.kwargs.get('cat_id')
        if cat_id is not None:
            obj = Items.objects.filter(item_category_id=cat_id).order_by('id')
            if not obj:
                raise Http404('Items not found.')
            return obj
        return Items.objects.all().order_by('id')

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


class ItemsSearchView(generics.ListAPIView):
    serializer_class = ItemsSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get('text', None)

        queryset = Items.objects.all().order_by('id')

        search_terms = search_query.split('+')

        q_objects = [
            Q(title__icontains=term) | Q(article_code__icontains=term) | Q(item_category__title__icontains=term) | Q(item_category__room__title__icontains=term)
            for term in search_terms
        ]

        if search_query:
            queryset = Items.objects.filter(
                models.Q(title__icontains=search_query) |
                models.Q(article_code__icontains=search_query) |
                models.Q(item_category__title__icontains=search_query) |
                models.Q(item_category__room__title__icontains=search_query)
            ).order_by('id')

        if not queryset.exists():
            raise Http404('Items not found.')

        return queryset


class ItemPhotoUploadView(generics.ListCreateAPIView):

    serializer_class = ItemPhotoSerializer
    queryset = ItemPhoto.objects.all().order_by('id')

    # def post(self, request, format=None):
    #     serializer = ItemPhotoSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return HttpResponse(content=serializer.data, status=201)
    #         # return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     return HttpResponse(content=serializer.data, status=400)