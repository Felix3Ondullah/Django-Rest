from django.shortcuts import render
from .models import Post
from .serializers import PostSerializers
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def Posts(request):
    if request.method == 'GET':
        posts = Post.objects.all() #query set
        serializer = PostSerializers(posts, many = True)
        return JsonResponse (serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializers (data = data)

        if serializer.is_valid():
           serializer.save()
           return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)
