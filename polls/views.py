# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def index(request):
    return HttpResponse("Hello World (Polls Index)")


def random_generator(request, max_rand):
    random_int = random.randrange(0, int(max_rand))
    message = 'Random number generated between 0 and %s: %d' % (max_rand, random_int)
    return HttpResponse(message)