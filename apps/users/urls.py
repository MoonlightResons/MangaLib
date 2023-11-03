from django.urls import path
from .views import LoginView, UserRegisterView, UserProfileView

urlpatterns = [
    path('registration/', UserRegisterView.as_view(), name='user-registation'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('<int:id>/profile/', UserProfileView.as_view(), name='user-profile')
]