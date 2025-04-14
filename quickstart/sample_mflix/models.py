from django.db import models

class Client(models.Model):
    id = models.CharField(max_length=50, primary_key=True)  # Campo manual para el ID
    nombre = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    start = models.TimeField()
    end = models.TimeField()

    def __str__(self):
        return self.nombre