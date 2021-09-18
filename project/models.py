from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class Cartegory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Events(models.Model):
    cartegory = models.ForeignKey('Cartegory', on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)