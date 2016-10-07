from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Counter(models.Model):

    counter = models.IntegerField(default=0)
