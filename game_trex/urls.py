from . import views
from django.urls import path


app_name = 'game_trex'

urlpatterns = [
    path('', views.game, name='game'),
    path('result/', views.get_score),
]