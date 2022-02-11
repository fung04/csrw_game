"""csrw_game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls', namespace='homepage')),
    path('game-flappy/', include('game_flappy.urls', namespace='game-flappy')),
    path('game-2048/', include('game_2048.urls', namespace='game_2048')),
    path('game-trex/', include('game_trex.urls', namespace='game_trex')),
    path('oauth/', include('social_django.urls', namespace='social')),
]
