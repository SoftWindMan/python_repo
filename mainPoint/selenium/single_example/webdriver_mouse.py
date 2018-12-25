#!/usr/bin/env python 
#coding=utf-8

'''
鼠标事件
context_click()
double_click()
drag_and_drop()
move_to_element()
click_and_hold()
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

baiduUrl = 'http://www.baidu.com'

driver = webdriver.Chrome()

driver.get(baiduUrl)
time.sleep(3)

settingBtn = driver.find_element_by_xpath('//*[@id="u1"]/a[8]')
print settingBtn
ActionChains(driver).move_to_element(settingBtn).perform()
time.sleep(2)

driver.quit()
