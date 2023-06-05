from rest_framework.serializers import ModelSerializer
from .models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model   = Post      # model 지정
        fields  = '__all__' # 모든 field 지정 