from django.db import models


class Volume(models.Model):
    uid = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    description = models.TextField(blank=True)
