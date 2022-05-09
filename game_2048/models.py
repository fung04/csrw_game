from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


class Game2048(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='game_2048')
    best_score = models.IntegerField(default=0)
    game_state = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f'{self.user.first_name}'
