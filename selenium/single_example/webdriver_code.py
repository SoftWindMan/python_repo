#!/usr/bin/python
#coding=utf-8

'''
cookie处理的几种方法：
	1、去掉验证码
	2、设置万能验证码
	3、识别验证码技术
	4、cookie绕过
'''

from selenium import webdriver
import time

url = 'https://home.cnblogs.com/'
driver = webdriver.Chrome()
driver.get(url)

driver.add_cookie({'name':'.CNBlogsCookie', 'value':'78D3A4BF71FA50E1ABE92DA913864590D20AF60DB9F008952459E179920695C075FC1E79DEF4286A3FFF1CC8E490C5B842B9F848EE5C18634E7CCA82A2D3C95A5D006738CB522EE4AAEED7ECBEE8836C8EEE8C13956A92FA962DE010978D9F2E31C7EACE'})
driver.add_cookie({'name':'.Cnblogs.AspNetCore.Cookies', 'value':'CfDJ8FHXRRtkJWRFtU30nh_M9mBYKLv7BdWTrgv4qs7xSU2_uZs61IarBz218niChjk_wwUxtmSTBoFejmRl6REXFy3sm44F5eQiTBBCEPwX5Xj627ZUZIJBE1Hq8lZ-VqMqzmuEFyblfj2zxo1RpEG2ZIzuGjHEjIFf3cDpibzsdtE-YXTMYMEnH4v3aMcSl9yuABnYuYR3JKv9H-WMpslvIyMT_VyHpKx-CgLu7MUUhlfXRtoCGybYvuymtZuu1rxy-Qqwdf71o5NAoBgjOqQtZbjKe4aD4neni8LqbCGFmJI0'})
#driver.add_cookie({'name':'UM_distinctid', 'value':'163d4d76fba100-09243e1359212a-5b163f13-15f900-163d4d76fbbca1'})
#driver.add_cookie({'name':'__gads', 'value':'ID=a5104f289441987f:T=1527671778:S=ALNI_MZFefHv1x8qKIhx0PJkJIybmuWSkw'})
#driver.add_cookie({'name':'_ga', 'value':'GA1.2.1593585101.1527647896'})
#driver.add_cookie({'name':'_gat', 'value':'1'})
#driver.add_cookie({'name':'_gid', 'value':'GA1.2.850952285.1528256303'})

driver.refresh()
time.sleep(2)

driver.find_element_by_id('feed_me').click()
time.sleep(2)

driver.quit()
