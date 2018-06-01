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
        future_time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=future_time)

        self.assertIs(future_question.was_recently_published(), False)


