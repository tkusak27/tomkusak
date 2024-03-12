# \simple_test_root\pages\views.py
from django.shortcuts import render

def index(request, pagename=''):
    context = {}
    return render(request, 'index.html', context)

def projects(request):
    context = {}
    return render(request, 'projects.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)


