# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

import datetime
from django.utils import timezone
from .models import Question

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
