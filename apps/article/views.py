from rest_framework import viewsets, mixins, permissions
from utils.permissions import IsOwnerOrReadOnly

from .models import Article
from .serializers import ArticleSerializer, ArticleListSerializer


# Create your views here.
class ArticleViewSet(viewsets.GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        else:
            return ArticleSerializer

    def get_permissions(self):
        if self.action == 'partial_update':
            return [IsOwnerOrReadOnly()]

        return []
