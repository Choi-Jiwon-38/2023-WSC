from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post
# from django.shortcuts import render <- unused

# Create your views here.
class PostViewSet(ModelViewSet):
    queryset            = Post.objects.all()    # queryset 작성
    serializer_class    = PostSerializer        # serializer 매핑