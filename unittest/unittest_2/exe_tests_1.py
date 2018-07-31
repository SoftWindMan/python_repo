#!/usr/bin/env python 
#coding=utf-8 

import unittest, HTMLTestRunner, time

nowTime = time.strftime("%Y-%m-%d %H_%M_%S")
filePath = nowTime + '_result.html'
f = open(filePath, 'wb')

suite = unittest.TestSuite()
	
all_tests = unittest.defaultTestLoader.discover('.', 'test_*.py')
for tests in all_tests:
	suite.addTests(tests)
runner = HTMLTestRunner.HTMLTestRunner(stream = f, title = '测试结果', description='结果')
runner.run(suite)	
	