from rest_framework import serializers
from project.models import Events 

class EventsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Events 
    fields = '__all__'