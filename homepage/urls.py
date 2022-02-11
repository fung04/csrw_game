from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'homepage'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('score/', views.score, name='score'),
]