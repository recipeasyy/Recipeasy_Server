from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user.views import KakaoLoginView, UpdateNicknameView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('auth/kakao', KakaoLoginView, name="kakao_login"),

    path('user/nickname', UpdateNicknameView, name='update_nickname')
]