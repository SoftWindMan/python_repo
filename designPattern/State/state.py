#!/usr/bin/python
#coding=utf-8

# 它为状态机提供了一个模块，它使用从指定的状态机类派生而来的子类来实现。 这些方法独立于状态，并使用装饰器声明转换。

class ComputerState(object):
	name = 'state'
	allowed = []
	
	def switch(self, state):
		
		""" Switch to new state """
		if state.name in self.allowed:
			print 'Current:', self, ' => switched to new state', state.name
			self.__class__ = state
		else:
			print 'Current:', self, ' => switching to', state.name, 'not possible'
			
	def __str__(self):
		return self.name
		
class Off(ComputerState):
	name = 'off'
	allowed = ['on']
	
class On(ComputerState):
	
	""" State of being powered on and working """
	name = 'on'
	allowed = ['off', 'suspend', 'hibernate']
	
class Suspend(ComputerState):
	
	""" State of being in suspended mode after switched on """
	name = 'suspend'
	allowed = ['on']
	
class Hibernate(ComputerState):
	
	""" State of being in hibernation after powered on """
	name = 'hibernate'
	allowed = ['on']
	
class Computer(object):
	
	""" A class representing a computer """
	def __init__(self, model = 'HP'):
		self.model = model
		
		# State of the computer - default is off
		self.state = Off()
		
	def change(self, state):
		
		""" Change state """
		self.state.switch(state)
		
if __name__ == "__main__":
	comp = Computer()
	comp.change(On)
	comp.change(Off)
	comp.change(On)
	comp.change(Suspend)
	comp.change(Hibernate)
	comp.change(On)
	comp.change(Off)
			
		
		