from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import LoginView, UserRegisterView, RequestUserProfileView, AnotherUserProfileView

urlpatterns = [
    path('registration/', UserRegisterView.as_view(), name='user-registation'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', RequestUserProfileView.as_view(), name='user-profile'),
    path('<int:id>/profile/', AnotherUserProfileView.as_view(), name='another-user-profile'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]