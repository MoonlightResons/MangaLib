from rest_framework import serializers
from .models import MangaUser, MangalibUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['email'] = user.email
        token['MangalibUser'] = user.is_active
        return token


class MangaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangaUser
        fields = "__all__"
