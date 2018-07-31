#!/usr/bin/python
#coding=utf-8

# 上传文件问题

from selenium import webdriver
import time, os

driver = webdriver.Chrome()
filePath = os.path.abspath('uploadFile.html')
driver.get(filePath)

driver.find_element_by_name('file').send_keys('E:\\b.txt')
time.sleep(2)

driver.quit()
