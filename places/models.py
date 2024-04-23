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


class PlaceImage(models.Model):
    order = models.IntegerField(default=0)
    image = models.ImageField(upload_to='place_images/')
    place = models.ForeignKey(Place, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.order} {self.place}"