# \simple_test_root\pages\views.py
from django.shortcuts import render
from . models import Page, Project, Career

def index(request):
    pg = Page.objects.get(permalink='/')
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }
    return render(request, 'index.html', context)

def blog(request):
    context = {
        
    }
    return render(request, 'blog.html', context)
    

def career(request):
    pg = Page.objects.get(permalink='/career')
    career = Career.objects.all()
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
        #'interests': career.interests,
        #'past_experience': career.past_experience,
        #'upcoming': career.upcoming,
    }
    return render(request, 'career.html', context)


def projects(request):
    pg = Page.objects.get(permalink='/projects')
    projects = Project.objects.all()
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
        'projects': projects,
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


