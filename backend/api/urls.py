from django.urls import path
from .views import *


urlpatterns = [
    path('button/', button_view, name='button_view'),
    path('room-type/', RoomTypeView.as_view(), name='room-type'),
    path('category/', ItemCategoryView.as_view(), name='category'),
    path('manufacturer/', ManufacturerView.as_view(), name='manufacturer'),
    path('collection/', CollectionView.as_view(), name='collection'),
    path('item/', ItemsView.as_view(), name='item'),
    path('colour/', ColourView.as_view(), name='colour'),
    path('material/', MaterialView.as_view(), name='material'),
    path('photo/', ItemPhotoView.as_view(), name='photo'),
    path('review/', ItemReviewView.as_view(), name='review')
]

