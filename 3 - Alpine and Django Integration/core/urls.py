from django.urls import path
from core import views

from core.api import api 


urlpatterns = [
    path('', views.index, name='index'),
    path('api/', api.urls)
]
