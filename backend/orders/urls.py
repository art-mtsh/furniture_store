from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('all/', OrderTotalView.as_view(), name='user_orders'),
    path('add-item/', OrderTotalView.as_view(), name='add_item'),
    path('create-order/', OrderTotalView.as_view(), name='create_order'),
    path('auth/', include('rest_framework.urls')),
]