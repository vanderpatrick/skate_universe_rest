from rest_framework import generics, permissions
from skate_rest.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer


class LikeListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LikeDetailView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
