#!/usr/bin/python
#coding=utf-8

# 模板模式使用抽象操作在基类中定义基本算法，其中子类覆盖具体行为。模板模式将算法的轮廓保留在单独的方法中。该方法被称为模板方法。

class MakeMeal:
	def prepare(self): pass
	def cook(self): pass
	def eat(self): pass
	
	def go(self):
		self.prepare()
		self.cook()
		self.eat()
		
class MakePizza(MakeMeal):
	def prepare(self):
		print 'Prepare Pizza'
		
	def cook(self):
		print 'Cook Pizza'
		
	def eat(self):
		print 'Eat Pizza'
		
class MakeTea(MakeMeal):
	def prepare(self):
		print 'Prepare Tea'
		
	def cook(self):
		print 'Cook Tea'
		
	def eat(self):
		print 'Eat Tea'
		
makePizza = MakePizza()
makePizza.go()

print 25 * '+'

makeTea = MakeTea()
makeTea.go()
