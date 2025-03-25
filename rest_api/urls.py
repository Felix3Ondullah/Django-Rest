from django.urls import path, include
from rest_framework import routers
from .views import (
    PostViewSet, CustomerViewSet, ProductViewSet, OrderViewSet, 
    CategoryViewSet, ReviewViewSet, PaymentViewSet
)

# Use SimpleRouter to register all API endpoints
router = routers.SimpleRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('customers', CustomerViewSet, basename='customers')
router.register('products', ProductViewSet, basename='products')
router.register('orders', OrderViewSet, basename='orders')
router.register('categories', CategoryViewSet, basename='categories')
router.register('reviews', ReviewViewSet, basename='reviews')
router.register('payments', PaymentViewSet, basename='payments')

urlpatterns = [
    path('', include(router.urls)),  # Include all API routes
]
