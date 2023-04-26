from rest_framework import viewsets
from api.models import Post
from api.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer
    permission_classes = []
