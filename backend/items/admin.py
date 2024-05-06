from django.contrib import admin
from .models import *


class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('title',)
    search_fields = ('title',)
    # list_editable = ('title',)
    # list_filter = ('is_published', 'category')


class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'room',)
    list_display_links = ('title',)
    search_fields = ('title', 'room',)
    # list_editable = ('title', 'room',)
    list_filter = ('room',)

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'about',)
    list_display_links = ('title',)
    search_fields = ('title', 'about',)
    # list_editable = ('title', 'about',)
    # list_filter = ('room')

class ItemCollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'manufacturer',)
    list_display_links = ('title',)
    search_fields = ('title', 'manufacturer',)
    # list_editable = ('title', 'manufacturer',)
    list_filter = ('manufacturer',)

class ItemsAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'title',
                    'article_code',
                    'price',
                    'manufacturer',
                    'collection',
                    'item_category',
                    'room_type',
                    'updated_at',
                    'is_published',
                    )
    list_display_links = ('title',)
    search_fields = ('id',
                    'title',
                    'article_code',
                    'manufacturer',
                    'collection',
                    'item_category',
                    'room_type',
                    )
    # list_editable = ('title',
    #                 'article_code',
    #                 'price',
    #                 'upholstery_material',
    #                 'upholstery_capacity',
    #                 'd_length',
    #                 'd_width',
    #                 'd_height',
    #                 'dimension_in_use_length',
    #                 'dimension_in_use_width',
    #                 'dimension_in_use_height',
    #                 'counter_claw',
    #                 'manufacturer',
    #                 'collection',
    #                 'item_category',
    #                 'room_type',
    #                 'is_published',
    #                 )
    list_filter = ('id',
                    'title',
                    'article_code',
                    'manufacturer',
                    'collection',
                    'item_category',
                    'room_type',
                    )

class ItemColourAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'item', 'photo',)
    list_display_links = ('title',)
    search_fields = ('item',)
    # list_editable = ('item',)
    list_filter = ('item',)

class ItemMaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'item', 'photo',)
    list_display_links = ('title',)
    search_fields = ('item',)
    # list_editable = ('item',)
    list_filter = ('item',)

class ItemPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'item',)
    list_display_links = ('item',)
    search_fields = ('item',)
    # list_editable = ('item',)
    list_filter = ('item',)

class ItemReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'first_name', 'second_name', 'review', 'rating', 'review_usefulness_counter',)
    list_display_links = ('item',)
    search_fields = ('item', 'rating',)
    # list_editable = ('item', 'rating',)
    list_filter = ('item', 'rating',)

admin.site.register(RoomType, RoomTypeAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(ItemCollection, ItemCollectionAdmin)
admin.site.register(Items, ItemsAdmin)
admin.site.register(ItemColour, ItemColourAdmin)
admin.site.register(ItemMaterial, ItemMaterialAdmin)
admin.site.register(ItemPhoto, ItemPhotoAdmin)
admin.site.register(ItemReview, ItemReviewAdmin)
