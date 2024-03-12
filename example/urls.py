# example/urls.py
from django.urls import path

from example.views import index, projects, about


urlpatterns = [
    path('', index),
    path('projects/', projects, name='projects'),
    path('about/', about, name='about'),
]