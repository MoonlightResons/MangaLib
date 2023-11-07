from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

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
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=MangaUser.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True
    )

    class Meta:
        model = MangaUser
        fields = [
            'id',
            'email',
            'username',
            'password',
            'password2',
        ]


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = MangaUser
        fields = ['username', 'lvl', 'avatar']


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangaUser
        fields = ['username', 'email', 'avatar']
