#!/usr/bin/python
#coding=utf-8

# 代理设计模式包含一个新对象，称为“代理”，代替被称为“真实主体”的现有对象。 由真实主体创建的代理对象必须位于相同的接口上，以便不让客户端知道使用代理来代替真实对象。 客户端向代理生成的请求将通过真实主体传递。

class Image:
	def __init__(self, filename):
		self._filename = filename
		
	def load_image_from_disk(self):
		print "loading " + self._filename
		
	def display_image(self):
		print "display " + self._filename
		
class Proxy:
	def __init__(self, subject):
		self._subject = subject
		self._proxystate = None
		
class ProxyImage(Proxy):
	def display_image(self):
		if self._proxystate == None:
			self._subject.load_image_from_disk()
			self._proxystate = 1
		self._subject.display_image()
		
proxy_image1 = ProxyImage(Image('HisRes_10Mb_Photo1'))
proxy_image2 = ProxyImage(Image('HisRes_10Mb_Photo2'))

proxy_image1.display_image() # loading necessary
#proxy_image1.display_image() # loading unnecessary
proxy_image2.display_image() # loading necessary
#proxy_image2.display_image() # loading unnecessary
#proxy_image1.display_image() # loading unnecessary
		
