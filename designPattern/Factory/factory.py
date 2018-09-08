#!/usr/bin/python
#coding=utf-8

# 当用户调用一个方法时，传入一个字符串，并通过工厂方法实现创建一个新对象，并将此对象作为返回值。 工厂方法中使用的对象类型由通过方法传递的字符串确定。

class Button(object):
	html = ''
	
	def get_html(self):
		return self.html
		
class Image(Button):
	html = "<img></img>"
	
class Input(Button):
	html = "<input></input>"
	
class Flash(Button):
	html = "<obj></obj>"
	
class ButtonFactory(object):
	def create_button(self, typ):
		targetclass = typ.capitalize()
		return globals()[targetclass]()
		
button_obj = ButtonFactory()
button = ['image', 'input', 'flash']
for b in button:
	print button_obj.create_button(b).get_html()
