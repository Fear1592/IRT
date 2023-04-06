from django.urls import path
from .views import *

urlpatterns = [
    path('create_order/', OrderCreateView.as_view()),
    path('order/all/', OrderListView.as_view()),
    path('order/detail/<int:pk>/', OrderDetailView.as_view()),
    path('create_orderitem/', OrderItemCreateView.as_view()),
    path('orderitem/all/', OrderItemListView.as_view()),
    path('orderitem/detail/<int:pk>/', OrderItemDetailView.as_view()),

]
