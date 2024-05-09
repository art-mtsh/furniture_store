from django.urls import path
from .views import *

urlpatterns = [
    path('room/', ItemRoomTypeView.as_view(), name='room'),
    path('room/<int:room_id>', ItemCategoryView.as_view(), name='categories_by_room'),
    path('room/category/<int:cat_id>/', ItemsView.as_view(), name='items_by_category'),
    path('room/category/items/', ItemsView.as_view(), name='all_items'),

    # path('category/', ItemCategoryView.as_view(), name='category'),
    # path('category/<int:id>/', ItemCategoryView.as_view(), name='category-detail'),
    # path('manufacturer/<int:id>/', ManufacturerView.as_view(), name='manufacturer-detail'),
    # path('collection/<int:id>/', CollectionView.as_view(), name='collection-detail'),
    # path('item/<int:id>/', ItemsView.as_view(), name='item-detail'),
    # path('materials/<int:id>/', ItemMaterialsView.as_view(), name='materials-detail'),
    # path('hard-body/<int:id>/', ItemHardBodyView.as_view(), name='hard-body-detail'),
    # path('soft-body/<int:id>/', ItemSoftBodyView.as_view(), name='soft-body-detail'),
    # path('photo/<int:id>/', ItemPhotoView.as_view(), name='photo-detail'),
    # path('review/<int:id>/', ItemReviewView.as_view(), name='review-detail')
]
