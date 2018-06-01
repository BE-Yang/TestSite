# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.core.urlresolvers import reverse
from django.views import generic
# from django.template import loader
import random
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_questions_list'

    def get_queryset(self):
        """Returns the last five published questions"""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

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

def random_generator(request, max_rand):
    random_int = random.randrange(0, int(max_rand))
    message = 'Random number generated between 0 and %s: %d' % (max_rand, random_int)
    return HttpResponse(message)