# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse
from django.views import generic
from django.apps import apps
from .models import Drink, Russian, Ingredient, Bartender

# Create your views here.

class IndexView(generic.ListView):

    #TODO-Fix: Drink model no longer used; Drink has no objects attribute
    def get(self, request):
        # VodkaDrinks = Ingredient.objects.get(Ingredient='Vodka')
        #
        # return VodkaDrinks.russian_Alcohol.all()
        Drink_Types = []
        for model in apps.get_app_config('BartendingRefresher').get_models():
            if issubclass(model, Drink) and model is not Drink:
                Drink_Types.append(model.__name__)

        #TODO-Fix: Make it return all objects of the model or just the model name
        return render(request, 'BartendingRefresher/index.html', {'DrinkTypes':Drink_Types})

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

def DrinkView(request, Model):
	bartender = Bartender()
	model = bartender.MakeDrink(Model)
	context = {'ListOfDrinks': model.__class__.objects.all(), 'Model': Model}
	return render(request, 'BartendingRefresher/ListOfDrinks.html', context)

class DetailView(generic.ListView):
	template_name = 'BartendingRefresher/detail.html'
	context_object_name = 'Ingredients'

	def get_queryset(self):
		context=super(DetailView, self).get_context_data(self)
		return


# def DetailView(request, Drink):
# 	context = {'test':Drink}
#
# 	return render(request, 'BartendingRefresher/detail.html', context)
#
#


class SubmitView(generic.DetailView):
    pass