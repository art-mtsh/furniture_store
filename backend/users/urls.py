from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('create-user/', CreateUserView.as_view(), name='register'),
    path('get-token/', CustomTokenObtainPairView.as_view(), name='get_token'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('info/', UserInfoView.as_view(), name='user_info'),

    # path('favorites/', UserFavoritesView.as_view(), name='user_favorites'),
    # path('add-favorite/', UserFavoritesView.as_view(), name='add_favorite'),
    # path('reviews/', UserFavoritesView.as_view(), name='reviews'),
    # path('add-review/', UserFavoritesView.as_view(), name='add_review'),
    # path('auth/', include('rest_framework.urls')),
]