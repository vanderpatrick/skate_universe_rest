from rest_framework import serializers
from .models import VideoPost
from Like.models import Like
from dislike.models import Dislike


class VideoPostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_author = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='author.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='author.profile.image.url')
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()
    dislikes_count = serializers.ReadOnlyField()

    def get_is_author(self, obj):
        request = self.context['request']
        return request.user == obj.author

    class Meta:
        model = VideoPost
        fields = [
            'id', 'author', 'is_author', 'profile_id', 'profile_image',
            'content', 'created_at', 'updated_at',
            'post_categorys_filter', 'video',
            'likes_count', 'comments_count', 'dislikes_count'
        ]
