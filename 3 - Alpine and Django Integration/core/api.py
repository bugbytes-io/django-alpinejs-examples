from typing import List
from ninja import NinjaAPI, ModelSchema
from django.http import JsonResponse

from .models import Band

api = NinjaAPI()

class BandSchema(ModelSchema):
    class Config:
        model = Band
        model_fields = ['name', 'genre']

@api.get('bands/', response=List[BandSchema])
def bands(request):
    return Band.objects.all()