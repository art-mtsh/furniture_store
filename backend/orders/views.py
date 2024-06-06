from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from users.models import UserBio
from django.db.models import Prefetch
from .serializers import *

ratelimit_m = '10/m'


class OrderTotalView(APIView):
    queryset = OrderTotal.objects.all()
    serializer_class = OrderTotalSerializer

    def get(self, request):
        user = request.user

        user_total = OrderTotal.objects.filter(related_user=user)

        if not user_total.exists():
            return JsonResponse({'message': 'Order not found'}, status=404)

        serializer = OrderTotalSerializer(user_total, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False, status=200)

    def post(self, request):
        user = request.user
        cart_items = OrderCart.objects.filter(related_user=user.id)
        user_bio = UserBio.objects.get(related_user=user.id)
        phone_number = user_bio.phone

        if not cart_items:
            return JsonResponse({'message': 'Cart is empty'}, status=404)

        items = {}
        order_sum = 0
        order_number = 0

        for i in cart_items:

            if i.soft_body != None:
                sb_obj = ItemSoftBody.objects.get(id=i.soft_body.id)
                soft_body = {
                    'sleep_place': sb_obj.sleep_place,
                    'sleep_size': sb_obj.sleep_size,
                    'springs_type': sb_obj.springs_type,
                    'linen_niche': sb_obj.linen_niche,
                    'mechanism': sb_obj.mechanism,
                    'filler': sb_obj.filler,
                    'counter_claw': sb_obj.counter_claw,
                    'armrests': sb_obj.armrests,
                    'max_weight': sb_obj.max_weight,
                    'upholstery_material': sb_obj.upholstery_material.title,
                    'other': sb_obj.other
                }
            else:
                soft_body = ''

            if i.hard_body != None:
                hb_obj = ItemHardBody.objects.get(id=i.hard_body.id)
                hard_body = {
                    'body_material': hb_obj.body_material.title,
                    'facade_material': hb_obj.facade_material.title,
                    'tabletop_material': hb_obj.tabletop_material.title
                }
            else:
                hard_body = ''

            item_data = {
                'title': i.related_item.title,
                'price': i.related_item.price,
                'article_code': i.related_item.article_code,
                'quantity': i.quantity,
                'soft_body': soft_body,
                'hard_body': hard_body
            }

            items[i.id] = item_data
            order_sum += i.related_item.price * i.quantity
            order_number = 333333 - i.id * 34

        order_sum = round(order_sum, 2)
        payment_type = request.data.get('payment_type', 'готівка')
        promocode = request.data.get('promocode', '')

        area = request.data.get('area')
        region = request.data.get('region')
        location_type = request.data.get('location_type')
        location = request.data.get('location')
        warehouse = request.data.get('warehouse')

        order_data = {
            # 'related_user': user.id,  # Pass user id instead of the user object
            'phone_number': phone_number,
            'order_number': order_number,
            'items': items,
            'order_sum': order_sum,
            'payment_type': payment_type,
            'promocode': promocode,
            'status': 'В обробці',
            'area': area,
            'region': region,
            'location_type': location_type,
            'location': location,
            'warehouse': warehouse,
            'related_user': user.id
        }

        serializer = OrderTotalSerializer(data=order_data)



        if serializer.is_valid():
            serializer.save()
            OrderCart.objects.filter(related_user=user).delete()

            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request):
        user = request.user
        order_id = request.data.get('id')

        if order_id:
            try:
                cart = OrderTotal.objects.filter(related_user=user, id=order_id)
                cart.delete()
                return JsonResponse({'message': f'Order id={order_id} is deleted'}, status=200)
            except OrderTotal.DoesNotExist:
                return JsonResponse({'message': f'Order id={order_id} not found'}, status=404)
        else:
            cart_items = OrderTotal.objects.filter(related_user=user)

            if cart_items.exists():
                cart_items.delete()
                return JsonResponse({'message': 'All orders are deleted'}, status=200)
            else:
                return JsonResponse({'message': 'Orders not found'}, status=200)

class OrderCartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        user_cart = OrderCart.objects.filter(related_user=user).prefetch_related(
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

        if not user_cart.exists():
            return JsonResponse({'message': 'Cart is empty'}, status=200)

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
                return JsonResponse({'message': 'Cart is empty'}, status=200)
