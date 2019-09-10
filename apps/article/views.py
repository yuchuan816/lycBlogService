from rest_framework import viewsets, mixins
from utils.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Article
from .serializers import ArticleSerializer, ArticleListSerializer


# Create your views here.
class ArticleViewSet(viewsets.GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,):

    permission_classes = (IsAuthenticatedOrReadOnly,)
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

        return super(ArticleViewSet, self).get_permissions()
