from rest_framework import serializers
from .models import *


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['title']


class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = ['title', 'room']


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['title', 'about']


class ItemCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['title', 'manufacturer']


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['title',
                  'article_code',
                  'price',
                  'upholstery_material',
                  'upholstery_capacity',
                  'd_length',
                  'd_width',
                  'd_height',
                  'dimension_in_use_length',
                  'dimension_in_use_width',
                  'dimension_in_use_height',
                  'counter_claw',
                  'manufacturer',
                  'collection',
                  'item_category',
                  'room_type',
                  'created_at',
                  'created_at',
                  'is_published']


class ItemColourSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['title', 'item', 'photo']


class ItemMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['title', 'item', 'photo']


class ItemPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['photo', 'item']


class ItemReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['item', 'first_name', 'second_name', 'rating', 'review_usefulness_counter']
