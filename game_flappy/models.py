from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.


class FlappyScore(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE,
                                related_name="user")
    score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.first_name}'
