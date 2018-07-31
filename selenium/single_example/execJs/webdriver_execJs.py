#!/usr/bin/python
#coding=utf-8

# 执行js问题

from selenium import webdriver
import os, time

driver = webdriver.Chrome()
filePath = 'file:///' + os.path.abspath('execJs.html')
driver.get(filePath)

jsp = 'var p1 = document.getElementById("p1"); p1.style.color="red";'
driver.execute_script(jsp)
time.sleep(2)

jsbtn = 'var btn1 = document.getElementById("btn1"); btn1.value="#4CAF50";'
btn1 = driver.find_element_by_id('btn1')
driver.execute_script(jsbtn, btn1)
time.sleep(2)

driver.quit()
