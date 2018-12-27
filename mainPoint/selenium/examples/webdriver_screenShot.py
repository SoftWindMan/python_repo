#!/usr/bin/python
#coding=utf-8

# 截图

from selenium import webdriver
import time

url = 'http://www.baidu.com'
driver = webdriver.Chrome()
driver.get(url)

try:
	kw = driver.find_element_by_id('kwss')
	kw.clear()
	kw.send_keys('selenium')

	driver.find_element_by_id('su').click()
	time.sleep(2)
except:
 	# 参数必须是绝对路径
	driver.get_screenshot_as_file('E:\\error_log.png')

driver.quit()
