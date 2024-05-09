from django.urls import path
from .views import *


urlpatterns = [
    path('button/', button_view, name='button_view'),
    path('room-type/', ItemRoomTypeView.as_view(), name='room-type'),
    path('category/', ItemCategoryView.as_view(), name='category'),
    path('manufacturer/', ManufacturerView.as_view(), name='manufacturer'),
    path('collection/', CollectionView.as_view(), name='collection'),
    path('item/', ItemsView.as_view(), name='item'),
    path('materials/', ItemMaterialsView.as_view(), name='materials'),
    path('hard-body/', ItemHardBodyView.as_view(), name='hard-body'),
    path('soft-body/', ItemSoftBodyView.as_view(), name='soft-body'),
    path('photo/', ItemPhotoView.as_view(), name='photo'),
    path('review/', ItemReviewView.as_view(), name='review')
]

