from django.contrib import admin
from .models import Game2048

# Register your models here.

# admin.site.register(game_2048)

class Display(admin.ModelAdmin):
    list_display = ['__str__', 'user',  'best_score']
    list_display_links = ('user', 'best_score')
    fields = ['user', 'best_score', 'game_state']


admin.site.register(Game2048, Display)