#!/usr/bin/python

from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^specifics/(\d+)/$', views.detail, name='detail'),
	url(r'^(\d+)/results/$', views.results, name='results'),
	url(r'^(\d+)/vote/$', views.vote, name='vote'),
]