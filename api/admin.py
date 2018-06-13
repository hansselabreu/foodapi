# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .forms import CustomUserAdminCreationForm, CustomUserAdminChangeForm
from models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserAdminCreationForm
    form = CustomUserAdminChangeForm
    model = CustomUser
    list_display = ('username', 'argentum_id',)

admin.site.register(CustomUser, CustomUserAdmin)
