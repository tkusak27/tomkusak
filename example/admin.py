from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Page, Project, Career


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_date')
    ordering = ('title',)
    search_field = ('title',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    ordering = ('title',)
    search_field = ('title',)

class CareerAdmin(admin.ModelAdmin):
    list_display = ('interests',)
    ordering = ('interests',)
    search_field = ('interests',)

# Register your models here.
admin.site.register(Page, PageAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Career, CareerAdmin)
