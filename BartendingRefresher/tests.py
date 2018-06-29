# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from BartendingRefresher.models import Drink, Russian, Bartender

# Create your tests here.


class RussianInheritanceTest(TestCase):

    def test_Inheritance_Glass(self):
        Bar = Bartender()
        Russian = Bar.MakeDrink('Russian', name = 'TestRussian')

        self.assertEqual(Russian.glass, 'Rocks')