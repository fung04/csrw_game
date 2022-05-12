from django.conf import settings
from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.


class GameTrex(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='game_trex')
    best_score = models.IntegerField(default=0)
    best_distance = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.first_name}'
