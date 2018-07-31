#!/usr/bin/python
#coding=utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time, unittest, sys

sys.path.append('\public')

class TestCnblogs(self):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.baseUrl = 'https://home.cnblogs.com/'
		self.verificationErrors = []
		self.accept_next_alert = True
		
	def testLogin(self):
		driver = self.driver
		
		driver.get(self.baseUrl)
		login.login(self)
		
		driver.find_element_by_xpath('//*[@id="header_user_right"]/a[5]').click()
		
		driver.switch_to_alert().accept()
		
		
		