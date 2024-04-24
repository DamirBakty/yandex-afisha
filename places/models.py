from django.db import models
from tinymce.models import HTMLField

# Create your models here


class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.CharField(max_length=255)
    description_long = HTMLField()
    coordinates = models.JSONField(default=dict())

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class PlaceImage(models.Model):
    order = models.PositiveIntegerField(default=0, blank=True, null=True)
    image = models.ImageField(upload_to='place_images/')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')


    def __str__(self):
        return f"{self.order} {self.place}"

    class Meta:
        ordering = ['order']


