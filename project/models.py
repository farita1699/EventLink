from django.db import models

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

