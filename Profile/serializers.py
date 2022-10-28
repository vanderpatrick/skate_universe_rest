from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='owner.username')
    is_author = serializers.SerializerMethodField()

    def get_is_author(self, obj):
        request = self.context['request']
        return request.user == obj.author

    class Meta:
        model = Profile
        fields = [
            'id', 'author', 'created_at', 'updated_at',
            'name', 'image', 'bio', 'is_author',
        ]
