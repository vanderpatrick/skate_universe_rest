from rest_framework import permissions, generics, filters
from .models import VideoPost
from .serializers import VideoPostSerializer
from skate_rest.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class VideoPostListView(generics.ListCreateAPIView):
    serializer_class = VideoPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = VideoPost.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class VideoPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VideoPostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = VideoPost.objects.all()
