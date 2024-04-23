from django.urls import path

from places.views import index, place_detail

app_name = 'places'

urlpatterns = [
    path('', index, name='index'),
    path('place/<int:place_id>/', place_detail, name='place_detail'),
]
