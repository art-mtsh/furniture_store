from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from requests import Response
from rest_framework import generics, status
from rest_framework.views import APIView

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
                "state": None,
                "city": None,
                "post_office": None
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


class UserFavoritesView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserFavorites.objects.all()
    serializer_class = UserFavoritesSerializer
