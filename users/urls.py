from django.urls import path

from .views import (
    UserCreateView,
    CustomObtainAuthTokenView,
    )

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('token/', CustomObtainAuthTokenView.as_view(), name='token')
]