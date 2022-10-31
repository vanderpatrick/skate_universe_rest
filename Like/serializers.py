from rest_framework import serializers
from Like.models import Like
from django.db import IntegrityError


class LikeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Like
        fields = [
            'id', 'author', 'post', 'created_at'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidateError({
                'detail': 'possible duplicate'
            })
