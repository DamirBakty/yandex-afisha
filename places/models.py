from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    short_description = models.TextField(verbose_name='Короткое описание', null=True, blank=True)
    long_description = HTMLField(verbose_name='Полное описание', null=True, blank=True)
    lng = models.FloatField(null=True, blank=True, verbose_name='Долгота')
    lat = models.FloatField(null=True, blank=True, verbose_name='Широта')

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'
        ordering = ['id']

    def __str__(self):
        return self.title

    @property
    def get_coordinates(self):
        return {
            'lng': self.lng,
            'lat': self.lat
        }


class PlaceImage(models.Model):
    order = models.PositiveIntegerField(default=0, verbose_name='Порядковый номер')
    image = models.ImageField(upload_to='place_images/', verbose_name='Картинка')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', verbose_name='Локация')

    def __str__(self):
        return f'{self.order} {self.place}'

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        ordering = ['order']
        indexes = [
            models.Index(fields=['order'])
        ]
