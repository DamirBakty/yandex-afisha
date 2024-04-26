from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    short_description = models.TextField(verbose_name='Короткое описание')
    long_description = HTMLField(verbose_name='Полное описание')
    coordinates = models.JSONField(default=dict(), verbose_name='Координаты')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'
        ordering = ['id']


class PlaceImage(models.Model):
    order = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name='Порядковый номер')
    image = models.ImageField(upload_to='place_images/', verbose_name='Картинка')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', verbose_name='Локация')

    def __str__(self):
        return f"{self.order} {self.place}"

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        ordering = ['order']
