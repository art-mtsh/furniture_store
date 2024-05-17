from django.db.models import Avg
from rest_framework import serializers
from .models import *


class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = ['id', 'title']


class RoomTypeSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()

    class Meta:
        model = ItemRoomType
        fields = ['id',
                  'title',
                  'categories']

    def get_categories(self, obj):
        categories = obj.itemcategory_set.all()
        return ItemCategorySerializer(categories, many=True).data


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemManufacturer
        fields = ['title', 'about']


class ItemCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCollection
        fields = ['title', 'manufacturer']


class ItemPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPhoto
        fields = ['photo']


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


class ItemDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDiscount
        fields = ['related_item', 'discount_percent']


class ItemReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemReview
        fields = ['related_item', 'first_name', 'last_name', 'review', 'rating', 'review_usefulness_counter']


class ItemsSerializer(serializers.ModelSerializer):

    photo = serializers.SerializerMethodField()
    hard_body = serializers.SerializerMethodField()
    soft_body = serializers.SerializerMethodField()
    review = serializers.SerializerMethodField()
    discount = serializers.SerializerMethodField()
    room = serializers.SerializerMethodField()

    def get_photo(self, obj):
        data = ItemPhotoSerializer(obj.prefetched_photos, many=True).data
        data = [p.get('photo') for p in data]
        return data
    def get_hard_body(self, obj):
        data = ItemHardBodySerializer(obj.prefetched_hard_body, many=True).data
        return data
    def get_soft_body(self, obj):
        data = ItemSoftBodySerializer(obj.prefetched_soft_body, many=True).data
        return data
    def get_review(self, obj):
        data = ItemReviewSerializer(obj.prefetched_reviews, many=True).data
        rate = [d.get('rating') for d in data]
        rate = sum(rate) / len(rate)
        rate = round(rate, 2)
        return rate
    def get_discount(self, obj):
        price = obj.price
        data = ItemDiscountSerializer(obj.prefetched_discounts, many=True).data
        if len(data) != 0:
            data = data[0]
            discount_percent = data['discount_percent']
            discount = price - (discount_percent / 100) * price
            discount = round(discount, 2)
        else:
            discount = price
        return discount

    def get_room(self, obj):
        return obj.item_category.room.id
    class Meta:
        model = Items
        fields = [
            'id',
            'title',
            'price',
            'discount',
            'review',
            'article_code',
            'description',
            'colour',
            'avaliability',
            'in_stock',
            'sold',
            'length',
            'width',
            'height',
            'form',
            'item_category',
            'room',
            'collection',
            'created_at',
            'is_published',
            'hard_body',
            'soft_body',
            'photo'
        ]

