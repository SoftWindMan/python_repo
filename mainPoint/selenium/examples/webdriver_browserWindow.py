#!/usr/bin/python
#coding=utf-8

# 浏览器多窗口问题

from selenium import webdriver
import time

url = 'http://www.baidu.com'
driver = webdriver.Chrome()
driver.get(url)

loginBtns = driver.find_elements_by_name('tj_login')
for loginBtn in loginBtns:
	if loginBtn.is_displayed():
		loginBtn.click()
time.sleep(2)

nowWindow = driver.current_window_handle

driver.find_element_by_class_name('tang-content').find_element_by_link_text('立即注册').click()

handleWindows = driver.window_handles
for handleWindow in handleWindows:
	if handleWindow != nowWindow:
		driver.switch_to_window(handleWindow)
		driver.find_element_by_id('TANGRAM__PSP_3__submit').click()
		time.sleep(2)
		driver.close()
time.sleep(2)

driver.quit()
