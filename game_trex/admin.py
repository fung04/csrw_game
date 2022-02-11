from django.contrib import admin
from .models import GameTrex
# Register your models here.

# admin.site.register(game_trex)

class Display(admin.ModelAdmin):
    list_display = ['__str__', 'user',  'best_score']
    list_display_links = ('user', 'best_score')
    fields = ['user', 'best_score', 'best_distance']


admin.site.register(GameTrex, Display)