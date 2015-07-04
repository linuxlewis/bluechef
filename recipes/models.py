from django.db import models
from django.contrib.postgres.fields import ArrayField
from jsonfield import JSONField


class Recipe(models.Model):

    name = models.TextField()
    external_id = models.CharField(max_length=1024, blank=True, unique=True)
    ingredients = ArrayField(models.CharField(max_length=2048))
    steps = JSONField()
