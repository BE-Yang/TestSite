# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
# from django.template import loader
import random
# Create your views here.


def index(request):
    latest_questions_list = Question.objects.order_by('pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {'latest_questions_list':latest_questions_list}
    # message = ', '.join([q.question_text for q in latest_questions_list])
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def random_generator(request, max_rand):
    random_int = random.randrange(0, int(max_rand))
    message = 'Random number generated between 0 and %s: %d' % (max_rand, random_int)
    return HttpResponse(message)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." %question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

