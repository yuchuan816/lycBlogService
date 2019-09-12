from rest_framework.authentication import TokenAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from datetime import timedelta
from django.utils import timezone


class ExpiringTokenAuthentication(TokenAuthentication):

    def authenticate_credentials(self, key):
        model = self.get_model()

        try:
            token = model.objects.get(key=key)
        except model.DoesNotExist:
            raise AuthenticationFailed('Invalid token')

        if not token.user.is_active:
            raise AuthenticationFailed('User inactive or deleted')

        # This is required for the time comparison
        utc_now = timezone.now()

        if token.created < utc_now - timedelta(hours=24):
            raise AuthenticationFailed('Token has expired')

        return (token.user, token)
