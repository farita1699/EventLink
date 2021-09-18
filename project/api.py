from django.contrib.auth.models import User
from project.models import Cartegory, Events
from rest_framework import viewsets, permissions, generics
from .serializer import UserSerializer, CartegorySerializer, EventSerializer
from rest_framework.views import APIView
from rest_framework.response import Response



class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = EventSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer

class CartegoryViewSet(viewsets.ModelViewSet):
    queryset = Cartegory.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CartegorySerializer



