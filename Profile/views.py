from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerializer
from skate_rest.permissions import IsOwnerOrReadOnly


class ProfileListView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
