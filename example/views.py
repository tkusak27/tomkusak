# \simple_test_root\pages\views.py
from django.shortcuts import render
from . models import Page

def index(request, pagename=''):
    context = {}
    return render(request, 'index.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def fantasy(request):
    context = {}
    return render(request, 'fantasy.html', context)
