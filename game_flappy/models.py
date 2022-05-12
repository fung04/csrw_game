from django.conf import settings
from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.


class GameFlappy(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE,
                                related_name="user")
    best_score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.first_name}'
