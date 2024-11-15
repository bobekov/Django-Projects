from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models
from travel_project.user_profile.managers import AppUserManager
from travel_project.user_profile.validators import validate_profile_name, validate_phone_number


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AppUserManager()


UserModel = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    username = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(3),
            validate_profile_name,
        ],
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        max_length=15,
        validators=[
            validate_phone_number,
        ],
        null=True,
        blank=True,
    )
    address = models.CharField(
        max_length=40,
        null=True,
        blank=True,
    )
    info = models.TextField(
        null=True,
        blank=True
    )
    profile_picture = models.URLField(
        blank=True,
        null=True
    )
