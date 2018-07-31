#!/usr/bin/python
#coding=utf-8

import unittest
from mathfunc import *

class TestMathFunc(unittest.TestCase):
#	def setUp(self):
#		print 'do something before test.Prepare environment.'
#		
#	def tearDown(self):
#		print 'do something after test.Clear up.'
	
	@classmethod
	def setUpClass(cls):
		print 'do something before test.Prepare environment.'
		
	@classmethod
	def tearDownClass(cls):
		print 'do something after test.Clear up.'
	
	def test_add(self):
		self.assertEqual(3, add(1, 2))
		
	def test_minus(self):
		self.assertEqual(1, minus(3, 2))
	
	@unittest.skip("I don't want to run this case.")
	def test_multi(self):
		self.assertEqual(6, multi(3, 2))
		
	def test_divide(self):
		self.assertEqual(1, divide(6, 3))
		self.assertEqual(2.5, divide(5, 2))
	
	@staticmethod
	def suites():
		tests = ['test_add', 'test_minus']
		return unittest.TestSuite(map(TestMathFunc, tests))

if __name__ == '__main__':
    #unittest.main()
	#unittest.main(verbosity=2)
	#unittest.main(verbosity=2)
	unittest.TextTestRunner(verbosity=2).run(TestMathFunc.suite())
		
	
