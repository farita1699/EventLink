from django.urls import path, include
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', include('project.urls')),
    path('admin/', admin.site.urls),
    path('login/', obtain_auth_token,)
]
