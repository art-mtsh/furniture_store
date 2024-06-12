from django.contrib import admin
from .models import *


class OrderCartAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'related_user',
                    'related_item',
                    'quantity',
                    'soft_body',
                    'hard_body')

    list_display_links = ('id',)
    search_fields = ('related_item',)
    list_editable = ('quantity',)
    list_filter = ('related_user',)

class OrderTotalAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'related_user',
                    # 'phone_number',
                    'order_number',
                    # 'items',
                    'order_sum',
                    # 'payment_type',
                    # 'promocode',
                    'status',
                    # 'region',
                    # 'location',
                    # 'warehouse',
                    'order_date')
    list_display_links = ('order_number',)
    search_fields = ('order_number',)
    list_editable = ('status',)
    list_filter = ('related_user',
                   'status')


admin.site.register(OrderCart, OrderCartAdmin)
admin.site.register(OrderTotal, OrderTotalAdmin)

