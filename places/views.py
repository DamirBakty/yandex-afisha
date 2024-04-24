import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place


def index(request):
    places = Place.objects.all()
    context = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(place.coordinates.get('lng')), float(place.coordinates.get('lat'))]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse('places:place_detail', kwargs={'place_id': place.id})
                }
            } for place in places]
    }
    return render(request, 'map/index.html',
                  context={
                      'data': context
                  })


def place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    data = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': place.coordinates,
    }
    data = json.dumps(data, ensure_ascii=False)
    return HttpResponse(data, content_type='application/json')
