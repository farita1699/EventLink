from django.contrib.auth.models import User
from project.models import Cartegory
from rest_framework import viewsets, permissions, generics
from .serializers import UserSerializer, CartegorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from project import serializers

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

# class CreateUserView(APIView):
#     serializer_class = CreateUserSerializer

#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             username = serializer.data.username
#             password = serializer.data.password

#         user = User(username=username, password=password)
#         user.save()



