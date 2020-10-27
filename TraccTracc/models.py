# the models.py file provides the data layer, which Django uses to construct our database schema and queries
# A Django model is a class with attributes that define the schema or underlying structure of a database table. These classes will provide built-in methods for making queries on the associated tables.
from django.db import models

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    artist = models.CharField(max_length=255, null=True, blank=True)
    year_released = models.CharField(max_length=4, null=True, blank=True)
    cover_art = models.URLField(max_length=200, null=True, blank=True) 

    def __str__(self):
        return self.title
