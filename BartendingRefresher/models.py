# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Ingredient(models.Model):
	# TODO-Suggestion: Captial case the Ingredient field
	Ingredient = models.CharField(max_length=20, primary_key=True)
	Type = models.CharField(max_length=10,
							choices=[
								('Al', 'Alcohol'),
								('Li', 'Liqueur'),
								('Gr', 'Garnish'),
								('Fill', 'Filler')
							]
							)

	@classmethod
	def IngredientList(cls, type):
		# TODO-Fix: Return PK, this will throw queryset eerror
		return Ingredient.objects.filter(Type=type)

	def __repr__(self):
		return '%s, %s' %(self.Ingredient, self.Type)

	def __str__(self):
		return self.Ingredient

class Drink(models.Model):
	name = models.CharField(max_length=30, primary_key=True, blank=True, default='')
	glass = models.CharField(max_length=20)
	method = models.CharField(max_length=10)
	alcohol = models.CharField(max_length=10)

	class Meta:
		abstract = True

#
# class Martini(Drink):
#     pass

class Russian(Drink):
	#TODO-Suggestion Capital case the fields below
	method = models.CharField(max_length=10, default='Build')
	glass = models.CharField(max_length=20, default='Rocks')
	alcohol = models.ForeignKey(Ingredient, related_name='%(class)s_Alcohol', \
								on_delete=models.CASCADE, default='Vodka')
	second_alcohol = models.ForeignKey(Ingredient, related_name='%(class)s_Second', \
										on_delete=models.CASCADE, default='Kahlua',
										limit_choices_to=Ingredient.IngredientList('Al')
										)
	third_alcohol = models.ForeignKey(Ingredient, related_name='%(class)s_Third', \
										on_delete=models.CASCADE, blank=True, null=True, \
										limit_choices_to=Ingredient.IngredientList('Al')
										)
	garnish = models.ForeignKey(Ingredient, related_name='%(class)s_Garnish', \
								on_delete=models.CASCADE, blank=True, null=True, \
								limit_choices_to=Ingredient.IngredientList('GR')
								)
	filler = models.ForeignKey(Ingredient, related_name='%(class)s_Filler', \
								on_delete=models.CASCADE, blank=True, null=True,
								limit_choices_to=Ingredient.IngredientList('Fill')
								)

	def __init__(self, *args, **kwargs):
		super(Russian, self).__init__(*args, **kwargs)



	def __repr__(self):
		return '%s, %s, %s, %s, %s, %s' %(self.name, self.method, self.glass, \
											self.alcohol, self.second_alcohol, self.garnish)

	def __str__(self):
		return self.name
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
