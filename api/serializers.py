from rest_framework import serializers
from api.models import CustomUser, Food


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('url', 'username', 'password', 'argentum_id')


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ('url', 'order_date', 'description', 'user_that_ordered')