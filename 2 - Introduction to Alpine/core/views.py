from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def people(request):
    people = [
        {"name": 'Mark', "image": 'https://via.placeholder.com/150'},
        {"name": 'Jeff', "image": 'https://via.placeholder.com/150'}
    ]
    import time
    time.sleep(1.)
    return JsonResponse(people, safe=False)