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
                    'price',
                    'article_code',
                    'colour',
                    'availability',
                    'in_stock',
                    'item_category',
                    'collection',
                    'updated_at',
                    'is_published',
                    )
    list_display_links = ('title',)
    search_fields = ('id',
                     'title',
                     'article_code',
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
                   )


class ItemMaterialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'material_type', 'manufacturer', 'title', 'colour')
    list_display_links = ('title',)
    search_fields = ('title',)
    # list_editable = ('related_item',)
    list_filter = ('material_type', 'manufacturer', 'title', 'colour')


class ItemHardBodyAdmin(admin.ModelAdmin):
    list_display = ('id', 'related_item', 'body_material', 'facade_material', 'tabletop_material')
    list_display_links = ('related_item',)
    search_fields = ('related_item',)
    # list_editable = ('related_item',)
    list_filter = ('related_item',)


class ItemSoftBodyAdmin(admin.ModelAdmin):
    list_display = ('id', 'related_item',)
    list_display_links = ('related_item',)
    search_fields = ('related_item',)
    # list_editable = ('related_item',)
    list_filter = ('related_item',)


class ItemPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'related_item', 'photo',)
    list_display_links = ('related_item',)
    search_fields = ('related_item',)
    # list_editable = ('related_item',)
    list_filter = ('related_item',)


class ItemReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'related_item', 'first_name', 'last_name', 'rating', 'review_usefulness_counter',)
    list_display_links = ('related_item',)
    search_fields = ('related_item', 'rating',)
    # list_editable = ('related_item', 'rating',)
    list_filter = ('related_item', 'rating',)


admin.site.register(ItemRoomType, RoomTypeAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)
admin.site.register(ItemManufacturer, ManufacturerAdmin)
admin.site.register(ItemCollection, ItemCollectionAdmin)
admin.site.register(Items, ItemsAdmin)
admin.site.register(ItemMaterials, ItemMaterialsAdmin)
admin.site.register(ItemHardBody, ItemHardBodyAdmin)
admin.site.register(ItemSoftBody, ItemSoftBodyAdmin)
admin.site.register(ItemPhoto, ItemPhotoAdmin)
admin.site.register(ItemReview, ItemReviewAdmin)
