from django.db import models
from django.contrib.auth.models import User

class Campground(models.Model):
    title = models.CharField(max_length=500)
    price = models.CharField(max_length=5, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True)
    location = models.CharField(max_length=500)
    image = models.CharField(max_length=1000)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title