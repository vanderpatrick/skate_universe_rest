from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from skate_rest.permissions import IsOwnerOrReadOnly
# Create your views here.


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(
            posts, many=True, context={'request': request}
        )
        return Response(serializer.data)