from django.core.management.base import BaseCommand

from . import bands
from core.models import Band

class Command(BaseCommand):
    help = 'Create bands and associate w/ genres'

    def handle(self, *args, **kwargs):
        if Band.objects.count() > 0:
            print("Bands already exist in the database")
            return
        
        
        Band.objects.bulk_create(
            [Band(name=b, genre='Classic Rock') for b in bands.CLASSIC_ROCK]
        )
        Band.objects.bulk_create(
            [Band(name=b, genre='Punk') for b in bands.PUNK]
        )
        Band.objects.bulk_create(
            [Band(name=b, genre='Post Punk') for b in bands.POST_PUNK]
        )
        Band.objects.bulk_create(
            [Band(name=b, genre='Jazz') for b in bands.JAZZ]
        )
        Band.objects.bulk_create(
            [Band(name=b, genre='Hip Hop') for b in bands.HIP_HOP]
        )
        Band.objects.bulk_create(
            [Band(name=b, genre='Post Rock') for b in bands.POST_ROCK]
        )
        
