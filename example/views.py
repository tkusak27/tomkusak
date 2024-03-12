# \simple_test_root\pages\views.py
from django.shortcuts import render
from . models import Page

def index(request):
    pg = Page.objects.get(permalink='/')
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }
    return render(request, 'index.html', context)

def projects(request):
    pg = Page.objects.get(permalink='/projects')
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }
    return render(request, 'projects.html', context)


def about(request):
    pg = Page.objects.get(permalink='/about')
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }
    return render(request, 'about.html', context)


