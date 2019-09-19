from rest_framework import viewsets, mixins, status
from utils.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
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
    filter_fields = ('tags', 'category')

    def create(self, request, *args, **kwargs):
        request.data.update({'author': request.user.id})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        else:
            return ArticleSerializer

    def get_permissions(self):
        if self.action == 'partial_update':
            return [IsOwnerOrReadOnly()]

        return super(ArticleViewSet, self).get_permissions()
