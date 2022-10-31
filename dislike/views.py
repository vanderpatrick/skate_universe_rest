from rest_framework import generics, permissions
from skate_rest.permissions import IsOwnerOrReadOnly
from .models import Dislike
from .serializers import DislikeSerializer


class DislikeListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DislikeSerializer
    queryset = Dislike.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DislikeDetailView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = DislikeSerializer
    queryset = Dislike.objects.all()