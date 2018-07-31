#!/usr/bin/env python 
#coding=utf-8

# 浏览器的前进和后退

from selenium import webdriver
import time

firstUrl = 'http://www.baidu.com'
secondUrl = 'http://news.baidu.com'

driver = webdriver.Chrome()

driver.get(firstUrl)
time.sleep(3)

driver.get(secondUrl)
time.sleep(3)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.quit()
