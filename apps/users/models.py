from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Permission, Group
from .manager import CustomUserManager


class MangalibUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username', max_length=55, blank=True)
    email = models.EmailField('email address', unique=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    is_translator = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'


class MangaUser(MangalibUser):
    avatar = models.ImageField(upload_to='media', blank=True)
    background = models.ImageField(upload_to='media', blank=True)
    lvl = models.IntegerField(default=0)
    about = models.TextField(blank=True)
