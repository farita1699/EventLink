from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('project.urls')),
    path('admin/', admin.site.urls),
]
