#!/usr/bin/python
#coding=utf-8

# 滚动条处理

from selenium import webdriver
import time

url = 'http://www.baidu.com'
driver = webdriver.Chrome()
driver.get(url)

kw = driver.find_element_by_id('kw')
kw.clear()
kw.send_keys('selenium')

driver.find_element_by_id('su').click()
time.sleep(2)

js1 = 'var q = document.documentElement.scrollTop = 10000'
driver.execute_script(js1)
time.sleep(2)

driver.quit()
