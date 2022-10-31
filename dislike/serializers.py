from rest_framework import serializers
from .models import Dislike
from django.db import IntegrityError


class DislikeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Dislike
        fields = [
            'id', 'author', 'post', 'created_at'
        ]
