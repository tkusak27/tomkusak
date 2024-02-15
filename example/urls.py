# example/urls.py
from django.urls import path

from example.views import index, about, blog


urlpatterns = [
    path('', index),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog')
]