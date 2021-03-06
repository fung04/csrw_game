# Generated by Django 3.2.4 on 2022-01-20 03:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game2048',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('best_score', models.IntegerField(default=0)),
                ('game_state', models.TextField(default='null')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_2048', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
