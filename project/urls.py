from rest_framework import routers
from django.urls import path
from project import views
from rest_framework import routers
from .api import UserViewSet, CartegoryViewSet, EventViewSet
from django.contrib.auth.models import User


router = routers.DefaultRouter()
router.register('api/events', EventViewSet, 'events')
router.register('api/users', UserViewSet, 'users')
router.register('api/categories', CartegoryViewSet, 'cartegory')


urlpatterns = router.urls


