from django.db import models

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    artist = models.CharField(max_length=255, null=True, blank=True)
    year_released = models.CharField(max_length=4, null=True, blank=True)


    def __str__(self):
        return self.title