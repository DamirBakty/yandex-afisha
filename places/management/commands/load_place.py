import json
import requests
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.core.management.base import BaseCommand
from django.db import transaction
from places.models import PlaceImage, Place


class Command(BaseCommand):
    help = 'Create'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    @transaction.atomic
    def handle(self, *args, **options):
            url = options['url']
            try:
                place_response = requests.get(url)
                if place_response.status_code != 200:
                    self.stdout.write(self.style.ERROR('Invalid URL'))

                title = place_response.json()['title']
                description_short = place_response.json()['description_short']
                description_long = place_response.json()['description_long']
                coordinates = place_response.json()['coordinates']
                place = Place(
                    title=title,
                    description_long=description_long,
                    coordinates=coordinates,
                    description_short=description_short
                )
                place.save()

                images_urls = place_response.json()['imgs']
                places_images = []

                for image_url in images_urls:
                    r = requests.get(image_url)
                    image = Image.open(BytesIO(r.content))
                    temp_image = BytesIO()
                    image.save(temp_image, format='JPEG')
                    temp_image.seek(0)

                    place_image = PlaceImage(
                        place=place
                    )
                    place_image.image.save('place_image.jpg', File(temp_image))
                    places_images.append(place_image)

                PlaceImage.objects.bulk_create(places_images, ignore_conflicts=True)

                print('Finished Creating a place')
            except Exception as e:
                self.stdout.write(self.style.ERROR(e))
