from django.urls import path
from .views import Posts, posts_detail


urlpatterns = [
    path('posts/', Posts),
    path('postsdetails/<int:pk>/', posts_detail),
]