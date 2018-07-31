#!/usr/bin/python
#coding=utf-8

# 属性的获

from selenium import webdriver
import time, os

driver = webdriver.Chrome()
filePath = 'file:///' + os.path.abspath('attributes.html')
driver.get(filePath)

inputs = driver.find_elements_by_tag_name('input')
for ipt in inputs:
	if ipt.get_attribute('data-node') == '594434499':
		ipt.click()
time.sleep(2)

driver.quit()
