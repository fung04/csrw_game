from . import views
from django.urls import path


app_name = 'game_2048'

urlpatterns = [
    path('', views.game, name='game'),
    path('set-result/', views.set_result),
]