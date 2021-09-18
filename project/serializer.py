from rest_framework import serializers
from project.models import Events 

# Lead Serializer
class EventsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Events 
    fields = '__all__'