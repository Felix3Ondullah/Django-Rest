from django.urls import path
from .views import genericApiView


urlpatterns = [
    # path('posts/', Posts),
    # path('postsdetails/<int:pk>/', posts_detail),
    path('genericApiView/<int:id>/', genericApiView.as_view()),
    path('genericApiView/', genericApiView.as_view()),
  
    
]