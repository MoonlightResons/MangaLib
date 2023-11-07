from django.urls import path
from .views import LoginView, UserRegisterView, RequestUserProfileView, AnotherUserProfileView

urlpatterns = [
    path('registration/', UserRegisterView.as_view(), name='user-registation'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('profile/', RequestUserProfileView.as_view(), name='user-profile'),
    path('<int:id>/profile/', AnotherUserProfileView.as_view(), name='another-user-profile'),
]