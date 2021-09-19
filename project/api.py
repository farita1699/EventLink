from django.contrib.auth.models import Group, User
from project.models import Cartegory, Events
from rest_framework import viewsets, permissions, status
from .serializer import UserSerializer, CartegorySerializer, EventSerializer, GroupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token



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

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GroupSerializer




