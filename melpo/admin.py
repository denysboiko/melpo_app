from django.contrib import admin
from melpo.models import *
# Register your models here.

class TheaterAdmin(admin.ModelAdmin):
    list_display = ['name','city','address']

admin.site.register(Theater, TheaterAdmin)