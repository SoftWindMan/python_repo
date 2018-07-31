#!/usr/bin/python
#coding=utf-8

# cookie处理

from selenium import webdriver
import time

url = 'https://passport.cnblogs.com/user/signin'
driver = webdriver.Chrome()
driver.get(url)

cookies = driver.get_cookies()
print cookies

#driver.add_cookie({'name':'key-aaaaaaa', 'value':'value-bbbb'})
#driver.delete_cookie("CookieName")
#driver.delete_all_cookies()

driver.quit()
