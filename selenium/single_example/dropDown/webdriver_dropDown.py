#!/usr/bin/python
#coding=utf-8

# 下拉框处理

from selenium import webdriver
import time, os

driver = webdriver.Chrome()
filePath = 'file:///' + os.path.abspath('dropDown.html')
driver.get(filePath)

selectId = driver.find_element_by_id('ShippingMethod')
selectId.find_element_by_xpath('//option[@value="10.69"]').click()
time.sleep(2)

driver.quit()
