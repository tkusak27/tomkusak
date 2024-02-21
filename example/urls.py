# example/urls.py
from django.urls import path

from example.views import index, about, blog_index


urlpatterns = [
    path('', index),
    path('about/', about, name='about'),
    path('blog/', blog_index, name='blog')
]