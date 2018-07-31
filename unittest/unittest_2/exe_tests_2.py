#!/usr/bin/env python 
#coding=utf-8 

import unittest, xmlrunner

suite = unittest.TestSuite()
	
all_tests = unittest.defaultTestLoader.discover('.', 'test_*.py')
for tests in all_tests:
	suite.addTests(tests)
runner = xmlrunner.XMLTestRunner(output='.')
runner.run(suite)	
	