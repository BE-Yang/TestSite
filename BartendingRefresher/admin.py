# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models
# Register your models here.



class IngredientAdmin(admin.ModelAdmin):
	list_display = ('Ingredient', 'Type')

admin.site.register(models.Russian)
admin.site.register(models.Ingredient, IngredientAdmin)