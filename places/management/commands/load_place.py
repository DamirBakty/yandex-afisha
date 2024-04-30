import json
import requests
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.core.management.base import BaseCommand
from django.db import transaction
from django.core.files.base import ContentFile

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
                    return self.stdout.write(self.style.ERROR('Invalid Place URL'))

                place_data = place_response.json()

                title = place_data['title']
                description_short = place_data['description_short']
                description_long = place_data['description_long']
                lat = place_data['coordinates']['lat']
                lng = place_data['coordinates']['lng']
                place, created = Place.objects.get_or_create(
                    title=title,
                    defaults={
                        'short_description': description_short,
                        'long_description': description_long,
                        'lat': lat,
                        'lng': lng
                    }
                )

                if not created:
                    return self.stdout.write(self.style.ERROR('Place is already loaded'))

                images_urls = place_data['imgs']
                places_images = []

                for image_url in images_urls:
                    image_response = requests.get(image_url)
                    if image_response.status_code != 200:
                        return self.stdout.write(self.style.ERROR('Invalid Image URL'))

                    image = Image.open(BytesIO(image_response.content))
                    temp_image = BytesIO()
                    image.save(temp_image, format='JPEG')
                    temp_image.seek(0)

                    content_file = ContentFile(temp_image.getvalue())

                    place_image = PlaceImage(place=place)

                    place_image.image.save('place_image.jpg', content_file)
                    places_images.append(place_image)

                PlaceImage.objects.bulk_create(places_images, ignore_conflicts=True)

                print('Finished Creating a place')
            except Exception as e:
                return self.stdout.write("Error", self.style.ERROR(e))
