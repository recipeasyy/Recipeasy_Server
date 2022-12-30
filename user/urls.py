from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user.views import kakao_login_view, update_nickname_view, login_url_view

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('login', login_url_view, name="login_url"),
    path('auth/kakao', kakao_login_view, name="kakao_login"),

    path('user/nickname', update_nickname_view, name='update_nickname')
]