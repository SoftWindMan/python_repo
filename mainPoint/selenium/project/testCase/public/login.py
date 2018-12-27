#!/usr/bin/python
#coding=utf-8

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

def login(self):
	driver = self.driver

	driver.add_cookie({'name':'.CNBlogsCookie', 'value':'78D3A4BF71FA50E1ABE92DA913864590D20AF60DB9F008952459E179920695C075FC1E79DEF4286A3FFF1CC8E490C5B842B9F848EE5C18634E7CCA82A2D3C95A5D006738CB522EE4AAEED7ECBEE8836C8EEE8C13956A92FA962DE010978D9F2E31C7EACE'})
	driver.add_cookie({'name':'.Cnblogs.AspNetCore.Cookies', 'value':'CfDJ8FHXRRtkJWRFtU30nh_M9mBYKLv7BdWTrgv4qs7xSU2_uZs61IarBz218niChjk_wwUxtmSTBoFejmRl6REXFy3sm44F5eQiTBBCEPwX5Xj627ZUZIJBE1Hq8lZ-VqMqzmuEFyblfj2zxo1RpEG2ZIzuGjHEjIFf3cDpibzsdtE-YXTMYMEnH4v3aMcSl9yuABnYuYR3JKv9H-WMpslvIyMT_VyHpKx-CgLu7MUUhlfXRtoCGybYvuymtZuu1rxy-Qqwdf71o5NAoBgjOqQtZbjKe4aD4neni8LqbCGFmJI0'})

	driver.refresh()
	time.sleep(1)