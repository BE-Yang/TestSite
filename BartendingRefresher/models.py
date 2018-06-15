# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Drink(models.Model):
    name = models.CharField(max_length=50)
    glass = models.CharField(max_length=50)
    alcohol = models.CharField(max_length=50)
    garnish = models.CharField(max_length=50)
    method = models.CharField(max_length=50)
    type = models.CharField(max_length=50)


