#coding=utf-8

class Students(object):
	"""docstring for Students"""
	def __init__(self, *args):
		self.names = args

	def __len__(self):
		return len(self.names)

class Book(object):
	def __setattr__(self, name, value):
		if name == 'value':
			object.__setattr__(self, name, value - 100)
		else:
			object.__setattr__(self, name, value)
		
	def __getattr__(self, name):
		try:
			return object.__getattribute__(name)
		except:
			return name + ' is not found!'

	def __str__(self):
		return self.name + ' cost : ' + str(self.value)

stu = Students('Bob', 'Alice', 'Tim')
print(len(stu))

bk = Book()
bk.name = 'Python'
bk.value = 100
print(bk.name)
print(bk.value)
print(bk)
print(bk.Type)