from django.db import models


class ShowItem(models.Model):
    video = models.BooleanField(default=False)
    video_link = models.TextField(blank=True, null=True)

    def clean(self):
        return self.video_link.replace('"', "")


