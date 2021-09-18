from rest_framework import routers
from .api import EventViewSet
from django.urls import path
from project import views
from .api import UserViewSet

router = routers.DefaultRouter()
router.register('api/events', EventViewSet, 'events')
router.register('api/users', UserViewSet, 'users')

urlpatterns = router.urls


