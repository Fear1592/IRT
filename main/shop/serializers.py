from rest_framework import serializers
from product.serializers import ChoicesListSerializer
from .models import Order, OrderItem


class OrderItemDetailSerializer(serializers.ModelSerializer):
    choices = ChoicesListSerializer(read_only=True)

    class Meta:
        model = OrderItem


class OrderItemListSerializer(serializers.ModelSerializer):
    choices = ChoicesListSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'get_cost', 'choices', 'quantity']


class OrderDetailSerializer(serializers.ModelSerializer):
    order = OrderItemListSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['created', 'user', 'updated', 'paid', 'get_total_price', 'order']


class OrderListSerializer(serializers.ModelSerializer):
    order = OrderItemListSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['created', 'user', 'updated', 'paid', 'get_total_price', 'order']
