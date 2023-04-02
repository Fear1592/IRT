from rest_framework import generics
from .serializers import ProductDetailSerializer, ProductListSerializer, \
    ChoicesDetailSerializer, ChoicesListSerializer, ImagesDetailSerializer, \
    ImagesListSerializer, VideosDetailSerializer, VideosListSerializer, \
    CategoryDetailSerializer, CategoryListSerializer

from .models import Product, Choices, Images, Videos, Category


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategoryDetailSerializer


class CategoryListView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()


class VideosCreateView(generics.CreateAPIView):
    serializer_class = VideosDetailSerializer


class VideosListView(generics.ListAPIView):
    serializer_class = VideosListSerializer
    queryset = Videos.objects.all()


class VideosDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VideosDetailSerializer
    queryset = Videos.objects.all()


class ImagesCreateView(generics.CreateAPIView):
    serializer_class = ImagesDetailSerializer


class ImagesListView(generics.ListAPIView):
    serializer_class = ImagesListSerializer
    queryset = Images.objects.all()


class ImagesDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImagesDetailSerializer
    queryset = Images.objects.all()


class ChoicesCreateView(generics.CreateAPIView):
    serializer_class = ChoicesDetailSerializer


class ChoicesListView(generics.ListAPIView):
    serializer_class = ChoicesListSerializer
    queryset = Choices.objects.all()


class ChoicesDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChoicesDetailSerializer
    queryset = Choices.objects.all()


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductDetailSerializer


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()

    # def get_queryset(self):
    #     user = self.request.user
    #     return Product.objects.filter(user=user)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()

    # def get_queryset(self):
    #     user = self.request.user
    #     return Product.objects.filter(user=user)
