from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('cart/', OrderCartView.as_view(), name='cart'),
    path('all/', OrderTotalView.as_view(), name='user_orders'),
]