from rest_framework import serializers
from .models import Post

class PostSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    author= serializers.CharField(max_length=100)
    email = serializers.EmailField(default="")


    def create(self, validated_data):
        return Post.objects.create(validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', validated_data)
        instance.author = validated_data.get('author', validated_data)
        instance.email = validated_data.get('email', validated_data)