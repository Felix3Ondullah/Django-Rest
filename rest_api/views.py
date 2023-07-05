from django.shortcuts import render
from .models import Post
from .serializers import PostSerializers
from rest_framework import status
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics


class genericApiView(generics.GenericAPIView, mixins.ListModelMixin, 
mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class= PostSerializers
    queryset = Post.objects.all()
    lookup_field = 'id'

    def get(self, request, id):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post (self, request):
        return self.create(request)
    
    def put (self, request, id=None):
        return self.update(request, id)
    
    def delete (self, request, id):
        return self.destroy(request,id)



















# @api_view (['GET', 'POST'])
# def Posts(request):
#     if request.method == 'GET':
#         posts = Post.objects.all() #query set
#         serializer = PostSerializers(posts, many = True)
#         return Response (serializer.data)
    
#     elif request.method == 'POST':
#         serializer = PostSerializers (data = request.data)

#         if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def posts_detail(request, pk):

#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         post = Post.objects.get(pk=pk)
#     except post.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = PostSerializers(post)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = PostSerializers(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
