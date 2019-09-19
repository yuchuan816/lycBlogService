from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer

# Create your views here.


class CommentViewSet(viewsets.GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.ListModelMixin):

    queryset = Comment.objects.filter(comments_id=None)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        request.data.update({'user': request.user.id})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
