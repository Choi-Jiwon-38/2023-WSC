from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

# ListCreateAPIView
from rest_framework import generics

# from django.shortcuts import render <- unused

# Create your views here.
class PostViewSet(ModelViewSet):
    queryset            = Post.objects.all()    # queryset 작성
    serializer_class    = PostSerializer        # serializer 매핑

class PublicPostListAPIView(generics.ListCreateAPIView):
    queryset            = Post.objects.all()    # queryset 작성
    serializer_class    = PostSerializer        # serializer 매핑