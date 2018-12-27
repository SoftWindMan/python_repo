#!/usr/bin/python
#coding=utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, re, time

class TestYoudao(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.baseUrl = 'http://www.youdao.com'
		self.verificationErrors = []
		self.accept_next_alert = True
		
	def testYoudaoSearch(self):
	
		'''有道搜索'''
		driver = self.driver
		driver.get(self.baseUrl + '/')
		
		word = driver.find_element_by_id('translateContent')
		word.clear()
		word.send_keys(u'世界')
		driver.find_element_by_xpath('//*[@id="form"]/button').click()
		time.sleep(1)
		
		driver.close()
		
	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)
		
if __name__ == '__main__':
	unittest.main()