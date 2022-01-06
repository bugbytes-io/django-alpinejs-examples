from django import forms
from .models import Band

class GenreChoiceForm(forms.Form):

    GENRE_CHOICES = [
        (g, g) for g in Band.objects.values_list('genre', flat=True).distinct()
    ]

    # genre = forms.ChoiceField(choices=GENRE_CHOICES)

    genre = forms.MultipleChoiceField(
        choices=GENRE_CHOICES,
        widget=forms.CheckboxSelectMultiple()
    )