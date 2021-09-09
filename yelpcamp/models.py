from django.db import models

class Campground(models.Model):
    title = models.CharField(max_length=500)
    price = models.DecimalField(decimal_places=2, max_digits=3, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True)
    location = models.CharField(max_length=500)

    def __str__(self):
        return self.title