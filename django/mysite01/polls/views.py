# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(req):
	return HttpResponse("Hello, world. You're at the polls index.")
