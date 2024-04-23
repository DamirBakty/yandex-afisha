from django.urls import path

from map.views import index

app_name = 'map'

urlpatterns = [
    path('', index, name='index'),
]
