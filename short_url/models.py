from __future__ import unicode_literals

from django.db import models

# Create your models here.
class One(models.Model):
    absolute_url = models.CharField(max_length=200)
    relative_url = models.CharField(max_length=50)

    def __str__(self):
        return self.absolute_url