#!/usr/bin/python
#coding=utf-8

import sys

sys.path.append('\testCase')
from testCase import baidu
from testCase import youdao

def caseList():
	allTestNames = [
		baidu.TestBaidu,
		youdao.TestYoudao,
	]
	print 'success read all case list !!!'
	
	return allTestNames