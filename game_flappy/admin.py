from django.conf import settings
from django.contrib import admin

from .models import GameFlappy

# Register your models here.


class Display(admin.ModelAdmin):
    list_display = ['__str__', 'user',  'best_score']
    list_display_links = ('user', 'best_score')
    fields = ['user', 'best_score']


admin.site.register(GameFlappy, Display)
# admin.site.register(flappy_scores)
