from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model   = Post      # model 지정
        fields  = [
            'pk',
            'username',
            'message',
            'created_at',
            'updated_at',
        ]