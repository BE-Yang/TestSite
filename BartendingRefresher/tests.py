# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from BartendingRefresher.models import Drink, Bartender

# Create your tests here.


class RussianInheritanceTest(TestCase):
    def setUp(self):
        self.bartender = Bartender()
        self.Russian = self.bartender.MakeDrink('Russian', name = 'Test Name')

    def test_Inheritance_Glass(self):
        self.assertEqual(self.Russian.glass, 'Rocks')

    def test_Inheritance_Name(self):
        self.assertEqual(self.Russian.name, 'Test Name')

    def tearDown(self):
        self.bartender = None