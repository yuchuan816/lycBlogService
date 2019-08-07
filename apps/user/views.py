from rest_framework import viewsets, mixins
from django.contrib.auth.models import User

from .serializers import UserSerializer


# Create your views here.
class UserViewSet(viewsets.GenericViewSet,
                  mixins.CreateModelMixin):

    authentication_classes = ()

    queryset = User.objects.all()
    serializer_class = UserSerializer
