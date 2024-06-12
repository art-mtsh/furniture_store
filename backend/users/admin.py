from django.contrib import admin
from .models import *


class UserBioAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'related_user',
                    'phone',
                    'birth_date',)

    list_display_links = ('related_user',)
    search_fields = ('related_user',)
    # list_editable = ('quantity',)
    # list_filter = ('related_user',)


class UserFavoritesAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'related_user',
                    'related_item',)

    list_display_links = ('related_user',)
    search_fields = ('related_user', 'related_item',)
    # list_editable = ('quantity',)
    # list_filter = ('related_user',)


admin.site.register(UserBio, UserBioAdmin)
admin.site.register(UserFavorites, UserFavoritesAdmin)
