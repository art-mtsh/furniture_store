from django.urls import path
from .views import *

urlpatterns = [
    path('room/', ItemRoomTypeView.as_view(), name='room'),
    path('room/<int:room_id>', ItemCategoryView.as_view(), name='categories_by_room'),
    path('room/category/<int:cat_id>/', ItemsView.as_view(), name='items_by_category'),
    path('room/category/items/', ItemsView.as_view(), name='all_items'),
    path('room/category/items/search/', ItemsSearchView.as_view(), name='search_items'),
]
