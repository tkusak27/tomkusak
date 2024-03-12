from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_date')
    ordering = ('title',)
    search_field = ('title',)

# Register your models here.
admin.site.register(Page, PageAdmin)
