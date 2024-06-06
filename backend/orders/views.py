from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from users.models import UserBio
from django.db.models import Prefetch
from .serializers import *
from rest_framework.response import Response

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

            soft = i.soft_body
            hard = i.hard_body

            if soft != None:
                soft_body = {
                    'sleep_place': soft.sleep_place if soft.sleep_place != None else '',
                    'sleep_size': soft.sleep_size if soft.sleep_size != None else '',
                    'springs_type': soft.springs_type if soft.springs_type != None else '',
                    'linen_niche': soft.linen_niche if soft.linen_niche != None else '',
                    'mechanism': soft.mechanism if soft.mechanism != None else '',
                    'filler': soft.filler if soft.filler != None else '',
                    'counter_claw': soft.counter_claw if soft.counter_claw != None else '',
                    'armrests': soft.armrests if soft.armrests != None else '',
                    'max_weight': soft.max_weight if soft.max_weight != None else '',
                    # 'upholstery_material': soft.upholstery_material if soft.upholstery_material != None else '',
                    'other': soft.other if soft.other != None else '',
                }
            else:
                soft_body = ''

            if hard != None:
                hard_body = {
                    'body_material': hard.body_material.title if hard.body_material != None else '',
                    'facade_material': hard.facade_material.title if hard.facade_material != None else '',
                    'tabletop_material': hard.tabletop_material.title if hard.tabletop_material != None else ''
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
            'hard_body__body_material',
            'hard_body__facade_material',
            'hard_body__tabletop_material',
            'hard_body',
            'soft_body')

        if not user_cart.exists():
            return JsonResponse({'message': 'Cart is empty'}, status=404)

        cart_ids = OrderCartSerializer(user_cart, many=True, context={'request': request})

        return Response(cart_ids.data, status=200)

    def post(self, request):
        user = request.user
        data = request.data.copy()
        data['related_user'] = user.id
        serializer = OrderCartCreateSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()

            return JsonResponse({'Item added to cart': serializer.data}, status=201)  # 201 Created
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
