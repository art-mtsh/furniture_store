from django.contrib import admin
from django.urls import path, include
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', include('items.urls')),
    path('users/', include('users.urls')),
    path('orders/', include('orders.urls')),
    path('__debug__/', include(debug_toolbar.urls))
]
