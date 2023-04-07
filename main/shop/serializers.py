from rest_framework import serializers
from product.serializers import ChoicesListSerializer
from .models import Order, OrderItem, Adress
from product.models import Choices



class ChoicesUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = ['count']

class AdressDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adress
        fields = ['id', 'country', 'region', 'city', 'street', 'phone', 'postal_code']


class AdressListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adress
        fields = ['id', 'country', 'region', 'city', 'street', 'phone', 'postal_code']


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
        fields = ['id', 'created', 'user', 'updated', 'paid', 'get_total_price', 'order']


class OrderListSerializer(serializers.ModelSerializer):
    order = OrderItemListSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'created', 'user', 'updated', 'paid', 'get_total_price', 'order']
