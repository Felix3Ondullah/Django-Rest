from django.urls import path, include
from .views import  PostViewSets
from rest_framework import routers

router = routers.SimpleRouter()

router.register('posts',PostViewSets, basename= 'posts')

urlpatterns = [
    # path('posts/', Posts),
    # path('postsdetails/<int:pk>/', posts_detail),
    # path('genericApiView/<int:id>/', genericApiView.as_view()),
    # path('genericApiView/', genericApiView.as_view()),
    path('', include (router.urls)),
  
    
]