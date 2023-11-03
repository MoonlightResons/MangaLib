from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions, status
from .serializer import MyTokenObtainPairSerializer, MangaUserSerializer, UserProfileSerializer
from .models import MangalibUser, MangaUser
from .permisions import AnnonPermission
from django.shortcuts import get_object_or_404



class LoginView(TokenObtainPairView):
    permission_classes = (AnnonPermission,)
    serializer_class = MyTokenObtainPairSerializer


class UserRegisterView(APIView):
    def post(self,request):
        serializer = MangaUserSerializer(data=request.data)
        if serializer.is_valid():
            mangauser = MangaUser.objects.create_user(
                email=request.data['email'],
                username=request.data['username'],
                # avatar=request.data['avatar'],
            )
            mangauser.set_password(request.data['password'])
            mangauser.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    permissions = [permissions.AllowAny]

    def get(self, request, id):
        profile = get_object_or_404(MangaUser, id=id)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
