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


    def get_queryset(self):
        return models.Drink.objects.all()


