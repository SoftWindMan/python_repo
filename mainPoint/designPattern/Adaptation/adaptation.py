#!/usr/bin/python
#coding=utf-8

# 适配器模式可用作两个不兼容接口之间的桥梁。 这种类型的设计模式属于结构模式，因为此模式结合了两个独立接口的功能。
# 这种模式涉及一个类，它负责连接独立或不兼容接口的功能。 一个现实的例子是读卡器，它是存储卡和笔记本电脑之间的适配器。 您将存储卡插入读卡器，将读卡器插入笔记本电脑，以便通过笔记本电脑读取存储卡。

class EuropeanSocketInterface:
	def voltage(self): pass
	def live(self): pass
	def neutral(self): pass
	def earth(self): pass
	
# Adaptee
class Socket(EuropeanSocketInterface):
	def voltage(self):
		return 230
		
	def live(self):
		return 1
		
	def neutral(self):
		return -1
		
	def earth(self):
		return 0
		
# Target interface
class USASocketInterface:
	def voltage(self): pass
	def live(self): pass
	def neutral(self): pass
	
# The Adapter
class Adapter(USASocketInterface):
	__socket = None
	
	def __init__(self, socket):
		self.__socket = socket
	
	def voltage(self):
		return 110
		
	def live(self):
		return self.__socket.live()
		
	def neutral(self):
		return self.__socket.neutral()
		
# Client
class ElectricKettle:
	__power = None
	
	def __init__(self, power):
		self.__power = power
		
	def boil(self):
		if self.__power.voltage() > 110:
			print 'Kettle on fire!'
		else:
			if self.__power.live() == 1 and self.__power.neutral() == -1:
				print 'Coffee time!'
			else:
				print 'No power.'
				
def main():
	# Plug in
	socket = Socket()
	adapter = Adapter(socket)
	kettle = ElectricKettle(adapter)
	
	# Make coffee
	kettle.boil()
	
	return 0
	
if __name__ == "__main__":
	main()
		
		
	
		