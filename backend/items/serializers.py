from rest_framework import serializers
from .models import *


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemRoomType
        fields = ['id', 'title']


class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = ['id', 'title', 'room']


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemManufacturer
        fields = ['title', 'about']


class ItemCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCollection
        fields = ['title', 'manufacturer']


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = [
            'id',
            'title',
            'price',
            'article_code',
            'description',
            'colour',
            'avaliability',
            'in_stock',
            'length',
            'width',
            'height',
            'form',
            'item_category',
            'collection',
            'created_at',
            'created_at',
            'is_published'
        ]


class ItemMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMaterials
        fields = ['material_type', 'manufacturer', 'title', 'colour', 'photo']


class ItemHardBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemHardBody
        fields = ['related_item', 'body_material', 'facade_material', 'tabletop_material']


class ItemSoftBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSoftBody
        fields = ['related_item',
                  'sleep_place',
                  'sleep_size',
                  'springs_type',
                  'linen_niche',
                  'mechanism',
                  'filler',
                  'counter_claw',
                  'armrests',
                  'max_weight',
                  'upholstery_material',
                  'other',
                  ]


class ItemPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPhoto
        fields = ['related_item', 'photo']


class ItemReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemReview
        fields = ['related_item', 'first_name', 'second_name', 'review', 'rating', 'review_usefulness_counter']
