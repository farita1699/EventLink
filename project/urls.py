from django.urls import path
from project import views
from rest_framework import routers
from .api import UserViewSet

router = routers.DefaultRouter()
router.register('api/users', UserViewSet, 'users')

urlpatterns = router.urls

# [
#     path('', views.get_name),
# ]