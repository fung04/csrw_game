from . import views
from django.urls import path


app_name = 'game_2048'

urlpatterns = [
    path('', views.game, name='game'),
    path('result/', views.set_score, name='set_score'),
]