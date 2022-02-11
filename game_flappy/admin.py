from django.contrib import admin
from .models import FlappyScore
from django.conf import settings
# Register your models here.


class Display(admin.ModelAdmin):
    list_display = ['__str__', 'user',  'score']
    list_display_links = ('user', 'score')
    fields = ['user', 'score']


admin.site.register(FlappyScore, Display)
# admin.site.register(flappy_scores)
