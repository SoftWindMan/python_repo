# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

#class IndexView(generic.ListView):
#	template_name = 'polls/index.html'
#	context_object_name = 'latest_question_list'
#	
#	def get_queryset(self):
#		return Question.objects.order_by('-pub_date')[:5]
#		
#class DetailView(generic.DetailView):
#	model = Question
#	template_name = 'polls/detail.html'
#	
#class ResultsView(generic.DetailView):
#	model = Question
#	template_name = 'polls/results.html'

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
	question = get_object_or_404(Question, id = question_id)
	return render(req, 'polls/results.html', {'question':question})
		
def vote(req, question_id):
	question = get_object_or_404(Question, id=question_id)
	
	try:
		selected_choice = question.choice_set.get(id=req.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(req, 'polls/detail.html', {
			'question':question,
			'error_message':"You're didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
	
	
	
