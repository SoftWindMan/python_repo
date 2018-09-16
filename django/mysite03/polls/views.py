# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Question

def index(req):
	#	return HttpResponse("Hello, world. You're at the polls index.")

#	latest_question_list = Question.objects.order_by('-pub_date')[:5]
#	output = ', '.join([q.question_text for q in latest_question_list])
#	return HttpResponse(output)

#	latest_question_list = Question.objects.order_by('-pub_date')[:5]
#	template = loader.get_template('polls/index.html')
#	context = {'latest_question_list':latest_question_list}
#	return HttpResponse(template.render(context, req))

	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list':latest_question_list}
	return render(req, 'polls/index.html', context)

def detail(req, question_id):
#	return HttpResponse("You're looking at question %s." % question_id)
	
#	try:
#		question = Question.objects.get(id=question_id)
#	except Question.DoesNotExist:
#		raise Http404('Question does not exist.')
#	return render(req, 'polls/index.html', {'question':question})
	
	question = get_object_or_404(Question, id=question_id)
	return render(req, 'polls/detail.html', {'question':question})
	
def results(req, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)
	
def vote(req, question_id):
	return HttpResponse("You're voting on question %s." % question_id)
