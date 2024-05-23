from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from rest_framework import generics

from .serializers import *

from brake.decorators import ratelimit
from sematext import log_engine
from django.db.models import Q, Prefetch

ratelimit_m = '10/m'


class ItemRoomTypeView(generics.ListCreateAPIView):
    queryset = ItemRoomType.objects.all().order_by('id').prefetch_related('itemcategory_set')
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

        queryset = Items.objects.all().select_related(
            'item_category__room').prefetch_related(
            Prefetch('photo', queryset=ItemPhoto.objects.all(), to_attr='prefetched_photos'),
            Prefetch('hard_body', queryset=ItemHardBody.objects.all(), to_attr='prefetched_hard_body'),
            Prefetch('soft_body', queryset=ItemSoftBody.objects.all(), to_attr='prefetched_soft_body'),
            Prefetch('review', queryset=ItemReview.objects.all(), to_attr='prefetched_reviews'),
            Prefetch('discount', queryset=ItemDiscount.objects.all(), to_attr='prefetched_discounts'))

        if cat_id is not None:
            queryset = queryset.filter(item_category_id=cat_id)
        return queryset

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


class ItemsBestsellers(generics.ListAPIView):
    serializer_class = ItemsSerializer

    def get_queryset(self):
        cat_id = self.kwargs.get('cat_id')

        queryset = Items.objects.order_by('-sold')[:10].select_related(
            'item_category__room').prefetch_related(
            Prefetch('photo', queryset=ItemPhoto.objects.all(), to_attr='prefetched_photos'),
            Prefetch('hard_body', queryset=ItemHardBody.objects.all(), to_attr='prefetched_hard_body'),
            Prefetch('soft_body', queryset=ItemSoftBody.objects.all(), to_attr='prefetched_soft_body'),
            Prefetch('review', queryset=ItemReview.objects.all(), to_attr='prefetched_reviews'),
            Prefetch('discount', queryset=ItemDiscount.objects.all(), to_attr='prefetched_discounts'))

        if cat_id is not None:
            queryset = queryset.filter(item_category_id=cat_id)
        return queryset


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
