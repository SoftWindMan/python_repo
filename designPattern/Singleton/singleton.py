#!/usr/bin/python
#coding=utf-8

# 单例模式将类的实例化限制为一个对象

class Singleton(object):
	__instance = None
	
	@staticmethod
	def getInstance():
		if Singleton.__instance == None:
			Singleton()
		return Singleton.__instance
	
	def __init__(self):
		if Singleton.__instance != None:
			raise Exception('This class is a singleton!')
		else:
			Singleton.__instance = self
				
s = Singleton()
print s

s = Singleton.getInstance()
print s

s= Singleton.getInstance()
print s