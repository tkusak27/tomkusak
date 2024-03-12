# example/urls.py
from django.urls import path

from example.views import index, career, projects, about


urlpatterns = [
    path('', index),
    path('career/', career, name='career'),
    path('projects/', projects, name='projects'),
    path('about/', about, name='about'),
]