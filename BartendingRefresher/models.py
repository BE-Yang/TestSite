# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Drink(models.Model):
    glass = models.CharField(max_length=50, default="Old Fashion")
    alcohol = models.CharField(max_length=50, default='Vodka')
    method = models.CharField(max_length=50, default='Build')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')

    class Meta:
        abstract=True

class Martini(models.Model):
    pass

class Russian(Drink):
    glass = models.CharField(max_length=10, default='Rocks')
    alcohol = 'vodka'
    method = 'Build'
    type = 'Russian'
    garnish = 'Cherry'


# class God(Drink):
#     glass = 'Rocks'
#     type = 'Build'
#     garnish = 'None'


class Screws(models.Model):
    pass

class FizzSours(models.Model):
    pass


class Bartender():
    menu = {'Russian': Russian}

    def MakeDrink(self, type, **kwargs):

        return self.menu[type.capitalize()](**kwargs)