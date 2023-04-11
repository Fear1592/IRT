from rest_framework import generics
from rest_framework import serializers

from .serializers import OrderListSerializer, OrderDetailSerializer, \
    OrderItemDetailSerializer, OrderItemListSerializer, AdressDetailSerializer, \
    AdressListSerializer
from .models import Order, OrderItem, Adress
from product.models import Choices


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()


class OrderItemCreateView(generics.CreateAPIView):
    serializer_class = OrderItemDetailSerializer
    queryset = OrderItem.objects.all()

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        quantity = request.POST.get('quantity')
        choices = request.POST.get('choices')
        count = Choices.objects.get(id=choices)
        quantity = int(quantity)
        count.count -= quantity
        if count.count == 0:
            count.in_stock = False
        count.save()

        return response


class OrderItemListView(generics.ListAPIView):
    serializer_class = OrderItemListSerializer
    queryset = OrderItem.objects.all()


class OrderItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemDetailSerializer
    queryset = OrderItem.objects.all()


class AdressCreateView(generics.CreateAPIView):
    serializer_class = AdressDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AdressListView(generics.ListAPIView):
    serializer_class = AdressListSerializer
    queryset = Adress.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AdressDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AdressDetailSerializer
    queryset = Adress.objects.all()
