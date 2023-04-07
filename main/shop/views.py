from rest_framework import generics

from .serializers import OrderListSerializer, OrderDetailSerializer, \
    OrderItemDetailSerializer, OrderItemListSerializer, AdressDetailSerializer, \
    AdressListSerializer, ChoicesUpdateSerializer
from .models import Order, OrderItem, Adress
from product.models import Choices



class UpdateChoicesDetailView(generics.UpdateAPIView):
    serializer_class = ChoicesUpdateSerializer
    queryset = Choices.objects.all()

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


class AdressCreateView(generics.CreateAPIView):
    serializer_class = AdressDetailSerializer


class AdressListView(generics.ListAPIView):
    serializer_class = AdressListSerializer
    queryset = Adress.objects.all()


class AdressDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AdressDetailSerializer
    queryset = Adress.objects.all()
