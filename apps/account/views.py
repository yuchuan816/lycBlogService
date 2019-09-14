from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.utils import timezone


class ObtainExpiringAuthToken(ObtainAuthToken):

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                token = Token.objects.get(
                    user=serializer.validated_data['user'])
            except Token.DoesNotExist:
                token = None

            if token:
                token.delete()

            token = Token.objects.create(
                user=serializer.validated_data['user'])

            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
