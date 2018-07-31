#!/usr/bin/python
#coding=utf-8

# alert、comfirm和prompt定位问题

from selenium import webdriver
import time

url = 'http://www.baidu.com'
driver = webdriver.Chrome()
driver.get(url)

driver.find_element_by_xpath('//*[@id="u1"]/a[8]').click()
time.sleep(1)

driver.find_element_by_class_name('setpref').click()
time.sleep(2)

driver.find_element_by_id('general').find_element_by_class_name('prefpanelgo').click()

alert = driver.switch_to_alert()
print alert.text.encode('utf-8')
alert.accept()
time.sleep(2)

# 有的话就可以执行下面的语句
#alert.dismiss()
#alert.send_keys('内容')

driver.quit()
