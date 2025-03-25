from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Post, Customer, Product, Order, Category, Review, Payment
from .serializers import (
    PostSerializer, CustomerSerializer, ProductSerializer, OrderSerializer, 
    CategorySerializer, ReviewSerializer, PaymentSerializer
)

# Authentication and Permissions can be customized as needed
class BaseViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, 
                  mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

# Post ViewSet
class PostViewSet(BaseViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

# Customer ViewSet
class CustomerViewSet(BaseViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

# Product ViewSet
class ProductViewSet(BaseViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

# Order ViewSet
class OrderViewSet(BaseViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

# Category ViewSet
class CategoryViewSet(BaseViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

# Review ViewSet
class ReviewViewSet(BaseViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

# Payment ViewSet
class PaymentViewSet(BaseViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
