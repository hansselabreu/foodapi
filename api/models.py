# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth import get_user_model
# Create your models here.


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, argentum_id, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not argentum_id:
            raise ValueError('The argentum id must be set')
        user = self.model(username=username, argentum_id=argentum_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, argentum_id, **extra_fields):
        import pdb;pdb.set_trace()
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, argentum_id, **extra_fields)

    def create_superuser(self, username, password, argentum_id,  **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, argentum_id, **extra_fields)

class CustomUser(AbstractUser):
    argentum_id = models.PositiveIntegerField()
    objects = CustomUserManager()
    # USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('argentum_id',)


class Food(models.Model):
    User = get_user_model()
    order_date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=200)
    user_that_ordered = models.OneToOneField(User, on_delete=models.CASCADE)