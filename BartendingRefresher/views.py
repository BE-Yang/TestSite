# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse
from django.views import generic
from django.apps import apps
from .models import Drink, Russian, Ingredient, Bartender

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'BartendingRefresher/index.html'
    context_object_name = 'DrinkTypes'

    #TODO-Fix: Drink model no longer used; Drink has no objects attribute
    def get(self, request):
        # VodkaDrinks = Ingredient.objects.get(Ingredient='Vodka')
        #
        # return VodkaDrinks.russian_Alcohol.all()
        Drink_Types = {}
        for model in apps.get_app_config('BartendingRefresher').get_models():
            if issubclass(model, Drink) and model is not Drink:
                Drink_Types[model.__name__] = model
        #TODO-Fix: Make it return all objects of the model or just the model name
        return HttpResponse(Drink_Types)


# def IndexView(request):
#     model_list = []
#     for model in apps.get_app_config('BartendingRefresher').get_models():
#         if issubclass(model, Drink) and model is not Drink:
#             model_list[model.__name__] = model
#
#     return HttpResponse(model_list)

# class DetailView(generic.ListView):
#
#     def get(self, request, Model):
#         model = Bartender(Model)
#         return HttpResponse(model.objects.all())

def DetailView(request, Model):
	bartender = Bartender()
	model = bartender.MakeDrink(Model)
	return HttpResponse(model.__class__.objects.all())



class SubmitView(generic.DetailView):
    pass