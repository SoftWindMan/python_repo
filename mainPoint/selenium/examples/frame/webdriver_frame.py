#!/usr/bin/env python
#coding=utf-8

# frame定位问题

from selenium import webdriver
import os, time

driver = webdriver.Chrome()
filePath = 'file:///' +os.path.abspath('frame.html')
driver.get(filePath)
#time.sleep(5)

driver.switch_to_frame("f_1")
driver.find_element_by_id('btn').click()
time.sleep(2)
 
driver.quit()
 
