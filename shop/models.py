from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=250)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name