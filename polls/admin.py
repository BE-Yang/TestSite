# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Question, Choice

# Register your models here.

# admin.site.register(Question)
#Editing the display on the admin site for questions using classes


# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

class ChoiceInLine(admin.TabularInline):
# class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_recently_published')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_per_page = 20

    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date Information', {'fields':['pub_date'], 'classes':['collapse']})
    ]
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)