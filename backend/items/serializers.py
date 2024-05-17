from django.db.models import Avg
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
    item_category = serializers.IntegerField(source='item_category.id', read_only=True)
    item_room = serializers.IntegerField(source='item_category.room.id', read_only=True)
    photos = serializers.SerializerMethodField()
    hard_body = serializers.SerializerMethodField()
    soft_body = serializers.SerializerMethodField()
    discount = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Items
        fields = [
            'id',
            'title',
            'price',
            'discount',
            'rating',
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
            'item_room',
            'collection',
            'created_at',
            'is_published',
            'hard_body',
            'soft_body',
            'photos'
        ]

    def get_photos(self, obj):
        photos_qs = ItemPhoto.objects.filter(related_item=obj)
        serializer = ItemPhotoSerializer(instance=photos_qs, many=True)
        data_list = serializer.data
        if len(data_list) != 0:
            photos = [x.values() for x in data_list]
        else:
            photos = []
        return photos

    def get_hard_body(self, obj):
        hard_body = ItemHardBody.objects.filter(related_item=obj)
        serializer = ItemHardBodySerializer(instance=hard_body, many=True)
        return serializer.data

    def get_soft_body(self, obj):
        soft_body = ItemSoftBody.objects.filter(related_item=obj)
        serializer = ItemSoftBodySerializer(instance=soft_body, many=True)
        return serializer.data

    def get_discount(self, obj):
        item_price = Items.objects.filter(id=obj.id).values_list('price', flat=True)
        item_price = item_price[0]
        discount = ItemDiscount.objects.filter(related_item=obj)
        serializer = ItemDiscountSerializer(instance=discount, many=True)
        discount = serializer.data
        if len(discount) != 0:
            discount = discount[0]
            discount = discount.get('discount_percent')
            discounted_price = item_price - (item_price * (discount / 100))
            discounted_price = float('{:.2f}'.format(discounted_price))
        else:
            discounted_price = item_price
        return discounted_price

    def get_rating(self, obj):
        rating = ItemReview.objects.filter(related_item=obj).aggregate(average_rating=Avg('rating'))
        rating = rating['average_rating']
        rating = float('{:.1f}'.format(rating))
        return rating
