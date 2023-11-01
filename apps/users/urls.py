from django.urls import path
from .views import LoginView, UserRegisterView

urlpatterns = [
    path('registration/', UserRegisterView.as_view(), name='user-registation'),
    path('login/', LoginView.as_view(), name='user-login'),
]