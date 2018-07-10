# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse
from django.views import generic
from django.apps import apps
from .models import Drink, Russian, Ingredient

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'BartendingRefresher/index.html'
    context_object_name = 'DrinkTypes'

    #TODO-Fix: Drink model no longer used; Drink has no objects attribute
    def get_queryset(self):
        # VodkaDrinks = Ingredient.objects.get(Ingredient='Vodka')
        #
        # return VodkaDrinks.russian_Alcohol.all()
        Drink_Types = []
        for models in apps.get_app_config('BartendingRefresher').get_models():
            if issubclass(models, Drink) and models is not Drink:
                Drink_Types.append(models)
        #TODO-Fix: Make it return all objects of the model or just the model name
        return Drink_Types


class SubmitView(generic.DetailView):
    pass