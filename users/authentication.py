from django.conf import settings
from rest_framework.authentication import TokenAuthentication

class CustomTokenAuthentication(TokenAuthentication):
    def authentication(self, reques):
        token = reques.COOKIES.get(settings.AUTH_COOKIE)

        if not token:
            return None
        return self.authenticate_credentials(token)