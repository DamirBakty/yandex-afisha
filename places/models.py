from django.db import models
from django.contrib.gis.db.models import PointField

# Create your models here


class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.CharField(max_length=255)
    description_long = models.TextField()
    coordinates = models.JSONField(default=dict())

    def __str__(self):
        return self.title