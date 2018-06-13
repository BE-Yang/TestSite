# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def index(request):
    message = 'Welcome to Bartending Refresher Game. Currently under construction'
    return HttpResponse(message)

def drinkstype1(request):
    pass

def drinkstype2(request):
    pass