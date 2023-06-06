from rest_framework import serializers
from snippets.models import Snippet
from django.utils import timezone

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