from django.db.models import Prefetch
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from requests import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from items.serializers import ItemsSerializer
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class CustomTokenObtainPairView(TokenObtainPairView):
    # перевантажуємо клас серіалізатора
    serializer_class = CustomTokenObtainPairSerializer


class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            user_bio = UserBio.objects.get(related_user=user)
            serializer = UserInfoSerializer(user_bio, context={'request': request})
            return JsonResponse(serializer.data, status=200)
        except UserBio.DoesNotExist:
            default_data = {
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                "phone": None,
                "birth_date": None,
            }
            return JsonResponse(default_data, status=200)

    def post(self, request):
        user = request.user
        try:
            user_bio = UserBio.objects.get(related_user=user)
            serializer = UserInfoSerializer(user_bio, data=request.data, partial=True, context={'request': request})
        except UserBio.DoesNotExist:
            # Create a new UserBio object
            serializer = UserInfoSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save(related_user=user)
                return JsonResponse(serializer.data, status=201)  # 201 Created
        else:
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)


class UserFavoritesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        user_favorites = UserFavorites.objects.filter(related_user=user).prefetch_related(
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

        if not user_favorites.exists():
            return JsonResponse({'message': 'Favorites not found'}, status=404)

        items = [favorite.related_item for favorite in user_favorites]
        serializer = ItemsSerializer(items, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False, status=200)

    def post(self, request):
        user = request.user
        data = request.data.copy()
        data['related_user'] = user.id
        serializer = UserFavoritesSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save(related_user=user)
            return JsonResponse(serializer.data, status=201)  # 201 Created
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request):
        user = request.user
        related_item_id = request.data.get('related_item')
        try:
            favorite = UserFavorites.objects.get(related_user=user, related_item_id=related_item_id)
            favorite.delete()
            return JsonResponse({'message': f'Favorite with id={related_item_id} is deleted'}, status=204)
        except UserFavorites.DoesNotExist:
            return JsonResponse({'message': f'Favorite with id={related_item_id} not found'}, status=404)
