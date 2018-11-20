from django.contrib import admin

from .models import *

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('position_in_menu', 'title',)
    list_filter = ('position_in_menu', 'title',)

@admin.register(Numeral)
class NumeralAdmin(admin.ModelAdmin):
    list_display = ('position_in_menu', 'title', 'name',)
    list_filter = ('position_in_menu', 'title', 'name',)

@admin.register(SubNumeral)
class SubNumeralAdmin(admin.ModelAdmin):
    list_display = ('position_in_menu', 'numeral', 'name',)
    list_filter = ('position_in_menu', 'numeral', 'name',)
