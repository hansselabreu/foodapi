# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import CustomUserSerializer, FoodSerializer
from api.models import CustomUser, Food
# Create your views here.



class CustomUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class FoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows foods to be viewed or edited.
    """
    queryset = Food.objects.all()
    serializer_class = FoodSerializer