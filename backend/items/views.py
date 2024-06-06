from django.utils.decorators import method_decorator
from rest_framework import generics, filters
from .serializers import *
from brake.decorators import ratelimit
from sematext import log_engine
from django.db.models import Prefetch
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse, Http404
from .models import *
from .serializers import ItemsSerializer

ratelimit_m = '10/m'


class ItemRoomTypeView(generics.ListCreateAPIView):
    http_method_names = ['get']

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
    http_method_names = ['get']

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


class ItemsView(APIView):
    def get(self, request, cat_id):

        if cat_id is not None:
            category_exists = ItemCategory.objects.filter(id=cat_id).exists()
            if not category_exists:
                return HttpResponse('Category not found!', status=404, content_type='text/plain')

        queryset = Items.objects.all().prefetch_related(
            'photo',
            'hard_body__body_material',
            'hard_body__facade_material',
            'hard_body__tabletop_material',
            'soft_body',
            'review',
            'discount',
        ).select_related(
            'item_category',
            'collection',
            'item_category__room',
            'collection__manufacturer'
        )

        if cat_id is not None:
            queryset = queryset.filter(item_category_id=cat_id)

        serializer = ItemsSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=200)

    # try:
    #     @method_decorator(ratelimit(block=False, rate=ratelimit_m))
    #     def dispatch(self, request, *args, **kwargs):
    #         log_engine.info('Request to ItemsView')
    #         if getattr(request, 'limits', {}):
    #             log_engine.warning('Too many requests for ItemsView')
    #             return HttpResponse('Too many requests', status=429, content_type='text/plain')
    #         return super().dispatch(request, *args, **kwargs)
    # except Exception as e:
    #     log_engine.error("An error occurred: %s", str(e), exc_info=True)


class ItemsBestsellersView(generics.ListAPIView):
    serializer_class = ItemsSerializer

    def get_queryset(self):
        queryset = Items.objects.order_by('-sold')[:10].select_related(
            'item_category__room').prefetch_related(
            Prefetch('photo', queryset=ItemPhoto.objects.all(), to_attr='prefetched_photos'),
            Prefetch('hard_body', queryset=ItemHardBody.objects.all(), to_attr='prefetched_hard_body'),
            Prefetch('soft_body', queryset=ItemSoftBody.objects.all(), to_attr='prefetched_soft_body'),
            Prefetch('review', queryset=ItemReview.objects.all(), to_attr='prefetched_reviews'),
            Prefetch('discount', queryset=ItemDiscount.objects.all(), to_attr='prefetched_discounts'))

        return queryset


class ItemsSalesView(generics.ListAPIView):
    serializer_class = ItemsSerializer

    def get_queryset(self):
        discount_subquery = ItemDiscount.objects.filter(discount_percent__gte=20).values_list('related_item', flat=True)[:10]

        queryset = Items.objects.filter(id__in=discount_subquery).order_by('id').select_related('item_category__room').prefetch_related(
            Prefetch('photo', queryset=ItemPhoto.objects.all(), to_attr='prefetched_photos'),
            Prefetch('hard_body', queryset=ItemHardBody.objects.all(), to_attr='prefetched_hard_body'),
            Prefetch('soft_body', queryset=ItemSoftBody.objects.all(), to_attr='prefetched_soft_body'),
            Prefetch('review', queryset=ItemReview.objects.all(), to_attr='prefetched_reviews'),
            Prefetch('discount', queryset=ItemDiscount.objects.all(), to_attr='prefetched_discounts'))
        return queryset


class ItemsSearchView(generics.ListAPIView):
    queryset = Items.objects.all().select_related(
        'item_category__room').prefetch_related(
        Prefetch('photo', queryset=ItemPhoto.objects.all(), to_attr='prefetched_photos'),
        Prefetch('hard_body', queryset=ItemHardBody.objects.all(), to_attr='prefetched_hard_body'),
        Prefetch('soft_body', queryset=ItemSoftBody.objects.all(), to_attr='prefetched_soft_body'),
        Prefetch('review', queryset=ItemReview.objects.all(), to_attr='prefetched_reviews'),
        Prefetch('discount', queryset=ItemDiscount.objects.all(), to_attr='prefetched_discounts'))
    serializer_class = ItemsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'item_category__title', 'item_category__room__title', 'article_code', 'collection__title', 'collection__manufacturer__title']
