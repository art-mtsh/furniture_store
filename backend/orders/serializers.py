from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *


class OrderTotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTotal
        fields = ['related_user', 'order_number', 'status', 'order_date']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['related_order', 'related_item', 'quantity', 'soft_item', 'hard_item']
