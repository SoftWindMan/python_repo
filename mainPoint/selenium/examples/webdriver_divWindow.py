#!/usr/bin/python
#coding=utf-8

# div型对话框定位问题

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

driver.find_element_by_class_name('tang-content').find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()

username = driver.find_element_by_id("TANGRAM__PSP_10__userName")
username.clear()
username.send_keys('username')

password = driver.find_element_by_id("TANGRAM__PSP_10__password")
password.clear()
password.send_keys('password')

driver.find_element_by_id("TANGRAM__PSP_10__submit")
time.sleep(2)

driver.quit()
