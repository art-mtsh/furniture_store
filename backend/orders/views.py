from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from rest_framework import generics, filters

from .serializers import *

from brake.decorators import ratelimit
from sematext import log_engine
from django.db.models import Q, Prefetch, OuterRef, Subquery
from .serializers import *

ratelimit_m = '10/m'

class OrderTotalView(generics.ListCreateAPIView):
    queryset = OrderTotal.objects.all()
    serializer_class = OrderTotalSerializer

class OrderItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer