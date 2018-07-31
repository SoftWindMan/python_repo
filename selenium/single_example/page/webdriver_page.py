#!/usr/bin/python
#coding=utf-8

# 下拉框式分页处理

from selenium import webdriver
import time, os

driver = webdriver.Chrome()
filePath = 'file:///' + os.path.abspath('pages.html')
driver.get(filePath)

optionCount = len(driver.find_element_by_id('pageElm_a74e_ce2c').find_elements_by_tag_name('option'))
opts = driver.find_element_by_id('pageElm_a74e_ce2c').find_elements_by_tag_name('option')
for opt in opts:
	opt.click()
	time.sleep(2)

driver.quit()
