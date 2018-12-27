#!/usr/bin/env python 
#coding=utf-8

'''
------ 网页元素常见定位方法
find_element_by_id()
find_element_by_tag_name()
find_element_by_class_name()
find_element_by_name()
find_element_by_link_text()
find_element_by_partial_link_text()
find_element_by_xpath()
find_element_by_css_selector()

find_element_by_id().size
find_element_by_id().text
find_element_by_id().get_attribute('type')
find_element_by_id().is_displayed()
'''

from selenium import webdriver
import time

loginUrl = 'https://passport.cnblogs.com/user/signin'

driver = webdriver.Chrome()

driver.get(loginUrl)
time.sleep(2)

driver.find_element_by_id('input1').clear()
driver.find_element_by_id('input1').send_keys('SoftWindMan')

driver.find_element_by_id('input2').clear()
driver.find_element_by_id('input2').send_keys('Shizheng95@')

driver.find_element_by_id('signin').click()
time.sleep(2)

driver.quit()
