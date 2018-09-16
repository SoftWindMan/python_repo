# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question, Choice

#admin.site.register(Question)
#admin.site.register(Choice)

# admin.StackedInline
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 0
	
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['question_text']}),
		('Date information', {'fields':['pub_date'], 'classes':['collapse']}),
	]
	
	list_display = ('question_text', 'pub_date')
	
	inlines = [ChoiceInline]
	
admin.site.register(Question, QuestionAdmin)
