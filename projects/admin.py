from django.contrib import admin

from .models import *

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin')
    list_filter = ('name', 'admin')

@admin.register(Project_SubNumeral)
class Project_SubNumeralAdmin(admin.ModelAdmin):
    list_display = ('project', 'subnumeral')
    list_filter = ('project', 'subnumeral')
