from django.conf import settings

from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserSerializer, AuthTokenSerializer

class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer

#class obtain auth token 
class CustomObtainAuthTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            token = response.data.get('token')

            response.set_cookie(
                #Los datos viene del archivo settings
                settings.AUTH_COOKIE,
                token,
                max_age=settings.AUTH_COOKIE_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )
        return response