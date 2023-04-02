from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from .models import Product, Choices, Images, Videos, Category


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class VideosDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'


class VideosListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'


class ImagesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class ImagesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class ChoicesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = '__all__'


class ChoicesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = '__all__'


class ProductDetailSerializer(WritableNestedModelSerializer):
    choices = ChoicesListSerializer(many=True)
    images = ImagesListSerializer(many=True, read_only=True)
    videos = VideosListSerializer(many=True)
    category = CategoryListSerializer()

    class Meta:
        model = Product
        fields = ['id', 'user', 'name', 'choice_cat', 'choices',
                  'specifications', 'equipment', 'images', 'videos',
                  'category', 'created_at', 'price',
                  'count'
                  ]


class ProductListSerializer(serializers.ModelSerializer):
    choices = ChoicesListSerializer(many=True)
    images = ImagesListSerializer(many=True)
    videos = VideosListSerializer(many=True)
    category = CategoryListSerializer()

    class Meta:
        model = Product
        fields = ['id', 'user', 'name', 'choice_cat', 'choices',
                  'specifications', 'equipment', 'images', 'videos',
                  'category', 'created_at', 'price',
                  'count'
                  ]
