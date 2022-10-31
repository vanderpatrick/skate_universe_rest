from rest_framework import serializers
from .models import Profile
from Follower.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_author = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()

    def get_is_author(self, obj):
        request = self.context['request']
        return request.user == obj.author

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                author=user, followed=obj.author
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'author', 'created_at', 'updated_at',
            'name', 'image', 'bio', 'is_author', 'following_id', 'posts_count',
            'following_count', 'followers_count'
        ]
