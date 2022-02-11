from . import views
from django.urls import path

app_name = 'game_flappy'

urlpatterns = [
    path('', views.flappy, name='game'),
    path('result/', views.result, name='result'),
]
