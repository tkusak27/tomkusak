# example/urls.py
from django.urls import path

from example.views import index, blog, career, projects, about

# need to clean up some of this
urlpatterns = [
    path('', index),
    path('blog/', blog, name='blog'),
    path('career/', career, name='career'),
    path('projects/', projects, name='projects'),
    path('about/', about, name='about'),
]