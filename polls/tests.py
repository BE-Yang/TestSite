# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

import datetime
from django.utils import timezone
from .models import Question
from django.core.urlresolvers import reverse
from django.test import TestCase

class QuestionModelTests(TestCase):
    def test_future_date(self):
        '''
        Return false if Question was created with publish date in the future
        '''

        future_time = timezone.now() + datetime.timedelta(days = 30)
        future_question = Question(pub_date=future_time)

        self.assertIs(future_question.was_recently_published(), False)

    def test_old_dates(self):
        '''
        Return False if question was older than 1 day
        '''

        old_time = timezone.now() - datetime.timedelta(days = 1, seconds = 1)
        oldQuestion = Question(pub_date = old_time)

        self.assertIs(oldQuestion.was_recently_published(), False)

    def test_same_day(self):
        '''
        Return True if question was published within the day
        '''

        time = timezone.now() - datetime.timedelta(hours = 23, minutes = 59, seconds = 59)
        recentQuestion = Question(pub_date = time)

        self.assertIs(recentQuestion.was_recently_published(), True)


def create_question(question_text, days):
    daysOffSet = timezone.now() + datetime.timedelta(days = days)
    return Question.objects.create(question_text = question_text, pub_date = daysOffSet)

class QuestionIndexViewTest(TestCase):

    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available.')
        self.assertQuerysetEqual(response.context['latest_questions_list'], [])

    def test_past_question(self):
        create_question('Past Day Test', -30)
        response = self.client.get(reverse('polls:index'))

        self.assertQuerysetEqual(response.context['latest_questions_list'],
                                 ['<Question: Past Day Test>'])

    def test_future_question(self):
        create_question('Future Day Test', 30)
        response = self.client.get(reverse('polls:index'))

        self.assertQuerysetEqual(response.context['latest_questions_list'], [])
        self.assertContains(response, 'No polls are available.')

    def test_future_past_question(self):
        create_question('Past Question', -30)
        create_question('Future Question', 30)

        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_questions_list'],
                                 ['<Question: Past Question>'])

    def test_two_past_days(self):
        create_question('Past Question 1', -2)
        create_question('Past Question 2', -3)

        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_questions_list'],
                                 ['<Question: Past Question 1>', '<Question: Past Question 2>'])

class QuestionDetailViewTest(TestCase):

    def test_past_question(self):
        past_question = create_question('Past Question', -2)
        url = reverse('polls:detail', args = (past_question.id,))
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, past_question.question_text)

    def test_future_question(self):
        future_question = create_question('Future Question', 30)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)