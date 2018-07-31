#!/usr/bin/env python 
#coding=utf-8

# 打开网页，然后调整浏览器窗口

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
time.sleep(5)

driver.maximize_window()
#driver.set_window_size(480, 800)
time.sleep(2)

driver.quit()


 
