from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from skate_rest.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class ProfileListView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count('author__post', distinct=True),
        followers_count=Count('author__followed', distinct=True),
        following_count=Count('author__following', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'author__following__created_at',
        'author__followed__created_at',
    ]
    filterset_fields = [
        'author__following__followed__profile'
    ]


class ProfileDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('author__post', distinct=True),
        followers_count=Count('author__followed', distinct=True),
        following_count=Count('author__following', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
