from django.db import models
from tinymce.models import HTMLField

# Create your models here


class Place(models.Model):
    """
    Моделька Place
    """
    title = models.CharField(max_length=255, verbose_name='Название')
    description_short = models.CharField(max_length=255, verbose_name='Короткое описание')
    description_long = HTMLField(verbose_name='Полное описание')
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


