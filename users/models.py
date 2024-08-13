from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from users.manager import CustomUserManager


class User(AbstractUser):
    phone_number = models.CharField(max_length=12, unique=True, blank=True)
    identifier = models.CharField(max_length=20, unique=False, blank=True)
    balance = models.IntegerField(blank=True, default=0)
    username = models.CharField(max_length=124, blank=True)

    # Set related_name to avoid conflicts
    groups = models.ManyToManyField(Group, related_name='custom_user_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions', blank=True)

    USERNAME_FIELD = "phone_number"

    objects = CustomUserManager()
