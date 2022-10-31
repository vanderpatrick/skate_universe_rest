from rest_framework import serializers
from django.db import IntegrityError
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    followed_name = serializers.ReadOnlyField(source="followed.username")

    class Meta:
        model = Follower
        fields = [
            'id', 'author', 'followed', 'created_at', 'followed_name'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
