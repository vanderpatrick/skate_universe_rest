from rest_framework import permissions, generics, filters
from .models import Post
from .serializers import PostSerializer
from skate_rest.permissions import IsOwnerOrReadOnly
from django.db.models import Count
# Create your views here.


class PostListView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True),
        dislikes_count=Count('dislikes', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'dislikes_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
        dislikes_count=Count('dislikes', distinct=True),
    ).order_by('-created_at')
