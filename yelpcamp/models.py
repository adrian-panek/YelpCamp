from django.db import models

class Campground(models.Model):
    title = models.CharField(max_length=500)
    price = models.CharField(max_length=5, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True)
    location = models.CharField(max_length=500)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.title