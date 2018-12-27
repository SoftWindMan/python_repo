#!/usr/bin/python
#coding=utf-8

# 多选框（多元素）定位问题

from selenium import webdriver
import os, time

driver = webdriver.Chrome()
filePath = 'file:///' + os.path.abspath('checkbox.html')
driver.get(filePath)

inputs = driver.find_elements_by_tag_name('input')
for ipt in inputs:
	if ipt.get_attribute('type') == 'checkbox':
		ipt.click()
		time.sleep(2)
time.sleep(2)
		
#driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()
		
driver.quit()
