from rest_framework import serializers
from project.models import Events, Cartegory
from django.contrib.auth.models import User

# Lead Serializer
class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Events 
    fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User 
    fields = '__all__'

class CartegorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Cartegory 
    fields = '__all__'