# example/urls.py
from django.urls import path

from example.views import index, about, fantasy


urlpatterns = [
    path('', index),
    path('about/', about, name='about'),
    path('fantasy/', fantasy, name='fantasy')
]