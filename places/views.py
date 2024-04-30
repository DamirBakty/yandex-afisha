from django.db.models import Prefetch
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place, PlaceImage


def index(request):
    places = Place.objects.all()
    context = {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [
                        place.lng,
                        place.lat
                    ]
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.id,
                    'detailsUrl': reverse(
                        'places:place_detail',
                        kwargs={'place_id': place.id}
                    )
                }
            } for place in places
        ]
    }
    return render(
        request,
        'places/index.html',
        context={
            'data': context
        })


def place_detail(request, place_id):
    queryset = Place.objects.prefetch_related(Prefetch('images', queryset=PlaceImage.objects.all()))
    place = get_object_or_404(queryset, pk=place_id)
    place_details = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': place.get_coordinates,
    }

    return JsonResponse(place_details)
