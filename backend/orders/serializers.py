from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from items.serializers import ItemsSerializer, ItemSoftBodySerializer, ItemHardBodySerializer
from .models import *


class OrderTotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTotal
        fields = '__all__'



class SimpleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['title', 'price', 'article_code']

class OrderCartSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()
    soft_body = ItemSoftBodySerializer()
    hard_body = ItemHardBodySerializer()


    class Meta:
        model = OrderCart
        fields = ['id', 'item', 'quantity', 'soft_body', 'hard_body']

    def get_item(self, obj):
        data = SimpleItemSerializer(obj.related_item).data
        return data

    # def get_soft_body(self, obj):
    #     if obj.soft_body:
    #         return {
    #             'id': obj.soft_body.id,
    #             'sleep_place': obj.soft_body.sleep_place,
    #             'sleep_size': obj.soft_body.sleep_size,
    #             'springs_type': obj.soft_body.springs_type,
    #             'linen_niche': obj.soft_body.linen_niche,
    #             'mechanism': obj.soft_body.mechanism,
    #             'filler': obj.soft_body.filler,
    #             'counter_claw': obj.soft_body.counter_claw,
    #             'armrests': obj.soft_body.armrests,
    #             'max_weight': obj.soft_body.max_weight,
    #             'upholstery_material': obj.soft_body.upholstery_material.title,
    #             'other': obj.soft_body.other,
    #         }
    #     return None
    #
    # def get_hard_body(self, obj):
    #     if obj.hard_body:
    #         return {
    #             'id': obj.hard_body.id,
    #             'body_material': obj.hard_body.body_material,
    #             'facade_material': obj.hard_body.facade_material,
    #             'tabletop_material': obj.hard_body.tabletop_material,
    #         }
    #     return None

class OrderCartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCart
        fields = ['id', 'related_item', 'quantity', 'soft_body', 'hard_body']
        # read_only_fields = ('related_user',)

    def validate(self, data):
        related_item = data.get('related_item')
        hard_body = data.get('hard_body')
        soft_body = data.get('soft_body')

        if hard_body and hard_body.related_item.id != related_item.id:
            raise serializers.ValidationError(f"Selected hard body is not valid for the related item. HARD_BODY item: {hard_body.related_item.id}, current item is {related_item.id}")

        if soft_body and soft_body.related_item.id != related_item.id:
            raise serializers.ValidationError(f"Selected soft body is not valid for the related item. SOFT_BODY item: {soft_body.related_item.id}, current item is {related_item.id}")

        return data

    def create(self, validated_data):
        related_user = validated_data.get('related_user')
        related_item = validated_data.get('related_item')
        quantity = validated_data.get('quantity')
        soft_body = validated_data.get('soft_body', None)
        hard_body = validated_data.get('hard_body', None)

        order_cart = OrderCart.objects.create(
            related_user=related_user,
            related_item=related_item,
            quantity=quantity,
            soft_body=soft_body,
            hard_body=hard_body
        )
        return order_cart

    def save(self, **kwargs):
        validated_data = {**self.validated_data, **kwargs}
        validated_data['related_user'] = self.context['request'].user
        return super().create(validated_data)