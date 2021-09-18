from rest_framework import viewsets
from rest_framework import permissions
from project.serializer import EventsSerializer
from project.models import Events



class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = EventsSerializer