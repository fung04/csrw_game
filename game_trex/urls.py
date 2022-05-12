from django.urls import path

from . import views

app_name = 'game_trex'

urlpatterns = [
    path('', views.game, name='game'),
    path('set-result/', views.set_result),
    path('get-result/', views.get_result),
]