from django.http import HttpResponse, Http404, JsonResponse
from django.utils.decorators import method_decorator
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from items.serializers import ItemsSerializer
from .serializers import *

from brake.decorators import ratelimit
from sematext import log_engine
from django.db.models import Q, Prefetch, OuterRef, Subquery
from .serializers import *

ratelimit_m = '10/m'


class OrderTotalView(APIView):
    queryset = OrderTotal.objects.all()
    serializer_class = OrderTotalSerializer


class OrderCartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        user_cart = OrderCart.objects.filter(related_user=user).select_related('related_item__item_category__room'
                                                                               ).prefetch_related(
            Prefetch('related_item__photo', queryset=ItemPhoto.objects.all(), to_attr='prefetched_photos'),
            Prefetch('related_item__hard_body', queryset=ItemHardBody.objects.all(), to_attr='prefetched_hard_body'),
            Prefetch('related_item__soft_body', queryset=ItemSoftBody.objects.all(), to_attr='prefetched_soft_body'),
            Prefetch('related_item__review', queryset=ItemReview.objects.all(), to_attr='prefetched_reviews'),
            Prefetch('related_item__discount', queryset=ItemDiscount.objects.all(), to_attr='prefetched_discounts')
        )

        if not user_cart.exists():
            return JsonResponse({'message': 'Cart is empty'}, status=204)

        serializer = OrderCartSerializer(user_cart, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False, status=200)

    def post(self, request):
        user = request.user
        data = request.data.copy()
        data['related_user'] = user.id
        serializer = OrderCartCreateSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)  # 201 Created
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request):
        user = request.user
        related_item_id = request.data.get('id')

        if related_item_id:
            try:
                cart = OrderCart.objects.get(related_user=user, id=related_item_id)
                cart.delete()
                return JsonResponse({'message': f'Item id={related_item_id} is deleted'}, status=200)
            except OrderCart.DoesNotExist:
                return JsonResponse({'message': f'Item with id={related_item_id} not found'}, status=404)
        else:
            cart_items = OrderCart.objects.filter(related_user=user)

            if cart_items.exists():
                cart_items.delete()
                return JsonResponse({'message': 'Cart is cleaned'}, status=200)
            else:
                return JsonResponse({'message': 'Cart is empty'}, status=204)
