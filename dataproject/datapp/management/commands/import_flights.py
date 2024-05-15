import json
from django.core.management.base import BaseCommand
from datapp.models import Flight

class Command(BaseCommand):
    help = 'Import flights data from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The JSON file containing flights data')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        with open(json_file, 'r') as file:
            data = json.load(file)

            for flight_data in data['data']:
                flight, created = Flight.objects.get_or_create(
                    sector=flight_data['Sector'],
                    origin=flight_data['Origin'],
                    destination=flight_data['Destination']
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Successfully added flight: {flight}"))
                else:
                    self.stdout.write(f"Flight already exists: {flight}")
