from django.urls import path

from places.views import index

app_name = 'places'

urlpatterns = [
    path('', index, name='index'),
]
