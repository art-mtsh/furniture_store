from django.urls import path
from . import views

urlpatterns = [
    path('button/', views.button_view, name='button_view'),
]
