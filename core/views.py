from django.shortcuts import render

from .forms import GenreChoiceForm

# Create your views here.
def index(request):
    form = GenreChoiceForm()
    context = {'form': form}
    return render(request, 'index.html', context)