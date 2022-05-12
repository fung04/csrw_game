from django.urls import path

from . import views

app_name = 'game_flappy'

urlpatterns = [
    path('', views.flappy, name='game'),
    path('set-result/', views.set_result, name='result'),
    path('get-result/', views.get_result),
]
