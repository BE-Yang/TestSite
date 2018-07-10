# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse
from django.views import generic
from . import models

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'BartendingRefresher/index.html'
    context_object_name = 'DrinkTypes'

    #TODO-Fix: Drink model no longer used; Drink has no objects attribute
    def get_queryset(self):
        VodkaDrinks = models.Ingredient.objects.get(Ingredient='Vodka')

        return VodkaDrinks.russian_Alcohol.all()


class SubmitView(generic.DetailView):
    pass