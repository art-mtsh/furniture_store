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
    body_material = ItemMaterialsSerializer()
    facade_material = ItemMaterialsSerializer()
    tabletop_material = ItemMaterialsSerializer()

    class Meta:
        model = ItemHardBody
        fields = ['id', 'body_material', 'facade_material', 'tabletop_material']


class ItemSoftBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSoftBody
        # fields = '__all__'
        fields = ['id',
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
        fields = ['first_name', 'last_name', 'review', 'rating', 'review_usefulness_counter']


class ItemsSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()
    hard_body = ItemHardBodySerializer(many=True)
    soft_body = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    discount = serializers.SerializerMethodField()

    item_category = serializers.SerializerMethodField()
    room = serializers.SerializerMethodField()
    collection = serializers.SerializerMethodField()
    manufacturer = serializers.SerializerMethodField()

    def get_photo(self, obj):
        data = ItemPhotoSerializer(obj.photo, many=True).data
        data = [p.get('photo') for p in data]
        return data

    def get_soft_body(self, obj):
        data = ItemSoftBodySerializer(obj.soft_body, many=True).data
        return data

    def get_rating(self, obj):
        data = ItemReviewSerializer(obj.review, many=True).data
        rate = [d.get('rating') for d in data]
        rate = sum(rate) / len(rate)
        rate = round(rate, 2)
        return rate

    def get_reviews(self, obj):
        data = ItemReviewSerializer(obj.review, many=True).data
        return data

    def get_discount(self, obj):
        price = obj.price
        data = ItemDiscountSerializer(obj.discount, many=True).data
        if len(data) != 0:
            data = data[0]
            discount_percent = data['discount_percent']
            discount = price - (discount_percent / 100) * price
            discount = round(discount, 2)
        else:
            discount = price
        return discount

    def get_item_category(self, obj):
        return obj.item_category.title

    #
    def get_room(self, obj):
        return obj.item_category.room.title

    def get_manufacturer(self, obj):
        return obj.collection.manufacturer.title

    def get_collection(self, obj):
        return obj.collection.title

    class Meta:
        model = Items
        fields = [
            'id',
            'title',
            'price',
            'discount',
            'rating',
            'reviews',
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
            'room',
            'item_category',
            'manufacturer',
            'collection',
            'hard_body',
            'soft_body',
            'photo'
        ]
