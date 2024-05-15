
# Create your models here.
from django.db import models

class Flight(models.Model):
    sector = models.CharField(max_length=255)
    origin = models.CharField(max_length=3)
    destination = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.origin} to {self.destination}"
