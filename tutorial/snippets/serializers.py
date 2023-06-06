from rest_framework import serializers
from snippets.models import Snippet
from django.utils import timezone

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    class Meta:
        model   = User
        fields  = ['id', 'username', 'snippets']


class SnippetSerializer(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model   = Snippet
        # fields  = ['id', 'title', 'code', 'linenos', 'language', 'style']
        exclude = ['highlighted'] 

    def create(self, validated_data):
        requested_user  = self.context['request'].user
        now             = timezone.now()

        snippets        = Snippet.objects.create(
            owner = requested_user, created = now,
            **validated_data
        )
        return snippets

