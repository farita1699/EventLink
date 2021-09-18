from project.serializer import EventsSerializer
from project.models import Events
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = EventsSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer
