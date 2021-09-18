from rest_framework import serializers
from django.contrib.auth.models import User
from project.models import Cartegory

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CartegorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartegory
        fields = '__all__'

# class CreateUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'password')