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
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return JsonResponse({'message': 'Authorization header missing'}, status=401)

        user = request.user
        user_total = OrderTotal.objects.filter(related_user=user)

        if not user_total.exists():
            return JsonResponse({'message': 'Order not found'}, status=404)

        serializer = OrderTotalSerializer(user_total, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False, status=200)

    def post(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return JsonResponse({'message': 'Authorization header missing'}, status=401)

        user = request.user
        try:
            user_bio = UserBio.objects.get(related_user=user.id)
        except UserBio.DoesNotExist:
            return Response({"error":
                                 "Please add phone number for this user! "
                                 "Use POST to users/info with phone=<phone number> (digits only)"}, status=404)

        if user_bio.phone is None:
            return Response({"error":
                                 "Please add phone number for this user! "
                                 "Use POST to users/info with phone=<phone number> (digits only)"}, status=404)
        else:
            phone_number = user_bio.phone

        cart_items = OrderCart.objects.filter(related_user=user.id)
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

        region = request.data.get('region')
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
            'region': region,
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

        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return JsonResponse({'message': 'Authorization header missing'}, status=401)

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

        related_item = data.get('related_item')
        if not related_item:
            return JsonResponse({'error': 'related_item is required'}, status=400)

        quantity = data.get('quantity')
        if not quantity:
            return JsonResponse({'error': 'quantity is required'}, status=400)

        if abs(int(quantity)) > 100:
            return JsonResponse({'error': 'too much items, max=100'}, status=400)

        hard_body = data.get('hard_body', None)
        soft_body = data.get('soft_body', None)

        # Check if an item with the same related_item, hard_body, and soft_body already exists
        item_exists = OrderCart.objects.filter(
            related_user=user,
            related_item=related_item,
            hard_body=hard_body,
            soft_body=soft_body
        ).first()

        if item_exists:
            if item_exists.quantity + int(quantity) > 100:
                return JsonResponse({'error': 'too much items, max=100'}, status=400)
            elif item_exists.quantity + int(quantity) < 0:
                return JsonResponse({'error': 'trying to delete more items than was added'}, status=400)
            elif item_exists.quantity + int(quantity) == 0:
                return JsonResponse({'error': 'trying to delete same quantity of items as was added, use DELETE method instead'}, status=400)
            else:
                item_exists.quantity += int(quantity)
                item_exists.save()
                return JsonResponse({
                    'message': 'Item quantity updated',
                    'item_cart_id': f'{item_exists.id}',
                    'item': OrderCartCreateSerializer(item_exists).data}, status=200)  # 200 OK
        else:
            serializer = OrderCartCreateSerializer(data=data, context={'request': request})
            if serializer.is_valid():
                new_item = serializer.save()
                return JsonResponse({
                    'message': 'Item added to cart',
                    'item_cart_id': f'{new_item.id}',
                    'item': serializer.data}, status=201)  # 201 Created

            return JsonResponse(serializer.errors, status=400)

    def delete(self, request):
        user = request.user
        item_cart_id = request.data.get('item_cart_id')

        if item_cart_id:
            try:
                cart = OrderCart.objects.get(related_user=user, id=item_cart_id)
                cart.delete()
                return JsonResponse({'message': f'item_cart_id={item_cart_id} is deleted'}, status=200)
            except OrderCart.DoesNotExist:
                return JsonResponse({'message': f'item_cart_id={item_cart_id} not found'}, status=404)
        else:
            cart_items = OrderCart.objects.filter(related_user=user)

            if cart_items.exists():
                cart_items.delete()
                return JsonResponse({'message': 'Cart is cleaned'}, status=200)
            else:
                return JsonResponse({'message': 'Cart is empty'}, status=200)
