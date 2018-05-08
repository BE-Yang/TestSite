# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.core.urlresolvers import reverse
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
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question':question,
                                                     'error_message': "You didn't select a choice."})
    else:
        select_choice.votes += 1
        select_choice.save()
        #Return HttpResponseRedirect after successfully dealing with POST data. Prevent duplicate submits in
        #scenario of user pushing back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

    return HttpResponse("You're voting on question %s." % question_id)

