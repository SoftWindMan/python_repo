#!/usr/bin/env python 
#coding=utf-8 

import requests, json, unittest, time
from bs4 import BeautifulSoup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class TestTranlatorApi(unittest.TestCase):
	def setUp(self):
		self.url = 'http://fy.webxml.com.cn/webservices/EnglishChinese.asmx/TranslatorSentenceString'

	# 方法必须以test开头
	def testEnglist(self):
		data = {'wordKey':'study'}
		r = requests.post(self.url, data=data)
		assert 'study' in r.content	
		
	def testChinese(self):
		data = {'wordKey':'学习'}
		r = requests.post(self.url, data=data)
		assert '学习' in r.content
		
	def testEmpty(self):
		data = {'wordKey':''}
		r = requests.post(self.url, data=data)
		assert 'Empty' in r.content
		
	def testNumber(self):
		data = {'wordKey':'12'}
		r = requests.post(self.url, data=data)
		assert 'Empty' in r.content
	
	def testSpecialChar(self):
		data = {'wordKey':'@'}
		r = requests.post(self.url, data=data)
		assert 'Empty' in r.content
		
	def tearDown(self):
		pass

#	with open('s.html', 'wb') as f:
		 
#url = 'http://fy.webxml.com.cn/webservices/EnglishChinese.asmx/TranslatorSentenceString' 
#data = {
#	"wordKey":" "
#}
#
#r = requests.post(url, data=data, verify=False)
#print r.content


 