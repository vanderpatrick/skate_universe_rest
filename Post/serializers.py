from rest_framework import serializers
from Post.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_author = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='author.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='author.profile.image.url')

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

    class Meta:
        model = Post
        fields = [
            'id', 'author', 'is_author', 'profile_id', 'profile_image',
            'content', 'video', 'created_at', 'updated_at',
            'post_category_filter', 'image'
        ]
