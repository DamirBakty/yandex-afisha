from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from places.models import Place, PlaceImage


def index(request):
    places = Place.objects.all().prefetch_related('images')
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
                    "detailsUrl": f"/place/{place.id}"
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
    return JsonResponse(data, safe=False)
