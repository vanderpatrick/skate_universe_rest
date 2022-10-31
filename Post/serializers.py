from rest_framework import serializers
from Post.models import Post
from Like.models import Like
from dislike.models import Dislike


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_author = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='author.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='author.profile.image.url')
    like_id = serializers.SerializerMethodField()
    dislike_id = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializer.ValidationError(
                'image size larger than 2MB'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'image width larger than 4096px'
            )

        if value.image.height > 4096:
            raise serializers.ValidationError(
                'image height larger than 4096px'
            )
        return value

    def get_is_author(self, obj):
        request = self.context['request']
        return request.user == obj.author

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                author=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def get_dislike_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            dislike = Dislike.objects.filter(
                author=user, post=obj
            ).first()
            return dislike.id if dislike else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'author', 'is_author', 'profile_id', 'profile_image',
            'content', 'created_at', 'updated_at',
            'post_category_filter', 'image', 'like_id', 'dislike_id'
        ]
