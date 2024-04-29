from django.urls import path
from .views import button_view #, TestTextModelListCreate

urlpatterns = [
    path('button/', button_view, name='button_view'),
    # path('text/', TestTextModelListCreate.as_view(), name='text'),
]
