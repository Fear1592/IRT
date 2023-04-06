from rest_framework import generics

from .serializers import OrderListSerializer, OrderDetailSerializer, \
    OrderItemDetailSerializer, OrderItemListSerializer
from .models import Order, OrderItem


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderDetailSerializer


class OrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()


class OrderItemCreateView(generics.CreateAPIView):
    serializer_class = OrderItemDetailSerializer


class OrderItemListView(generics.ListAPIView):
    serializer_class = OrderItemListSerializer
    queryset = OrderItem.objects.all()


class OrderItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemDetailSerializer
    queryset = OrderItem.objects.all()
