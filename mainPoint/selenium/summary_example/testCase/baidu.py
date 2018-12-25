#!/usr/bin/python
#coding=utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, re, time

class TestBaidu(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.baseUrl = 'http://www.baidu.com'
		
		# 脚本运行时报错信息都会保存这个list中
		self.verificationErrors = []
		
		# 是否接受下一个警告
		self.accept_next_alert = True
	
	# 搜索测试
	def testBaiduSearch(self):
	
		'''百度搜索'''
		driver = self.driver
		driver.get(self.baseUrl + '/')
		
		driver.find_element_by_id('kw').send_keys('selenium webdriver')
		driver.find_element_by_id('su').click()
		time.sleep(1)
		
		driver.close()
	
	# 搜索设置测试
	def testBaiduSet(self):
	
		'''百度搜索设置'''
		driver = self.driver
		driver.get(self.baseUrl)
		
		driver.find_element_by_xpath('//*[@id="u1"]/a[8]').click()
		driver.find_element_by_class_name('setpref').click()
		#time.sleep(1)
		
		m = driver.find_element_by_name('NR')
		m.find_element_by_xpath('//option[2]').click()
		driver.find_element_by_class_name('prefpanelgo').click()
		#time.sleep(1)
		
		driver.switch_to_alert().accept()
		time.sleep(1)
		
		driver.close()
	
	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)
		
if __name__ == '__main__':
	unittest.main()
	
	
	

		