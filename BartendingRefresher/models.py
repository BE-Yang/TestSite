# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Ingredient(models.Model):
    Ingredient = models.CharField(max_length=20, primary_key=True)
    Type = models.CharField(max_length=10,
                            choices=[
                                ('Al', 'Alcohol'),
                                ('Li', 'Liqueur'),
                                ('Gr', 'Garnish'),
                                ('Fill', 'Filler')
                                ]
                            )

    def __repr__(self):
        return '%s, %s' %(self.Ingredient, self.Type)

class Drink(models.Model):
    name = models.CharField(max_length=30)
    glass = models.CharField(max_length=20)
    method = models.CharField(max_length=10)
    alcohol = models.CharField(max_length=10)

    class Meta:
        abstract = True

#
# class Martini(Drink):
#     pass

class Russian(Drink):
    method = models.CharField(max_length=10, default='Build')
    glass = models.CharField(max_length=20, default='Rocks')
    alcohol = models.CharField(max_length=20, default='Vodka')
    second_alcohol = models.CharField(max_length=20, default='Kahlua')
    garnish = models.CharField(max_length=10, default='Cherry')

    def __init__(self, **kwargs):
        super(Russian, self).__init__(**kwargs)

# class God(Drink):
#     glass = 'Rocks'
#     type = 'Build'
#     garnish = 'None'


# class Screws(Drink):
#     pass
#
# class FizzSours(Drink):#     pass


class Bartender():
    menu = {'Russian': Russian}

    def MakeDrink(self, type, **kwargs):

        return self.menu[type.capitalize()](**kwargs)
