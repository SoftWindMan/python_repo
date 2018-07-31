#!/usr/bin/python
#coding=utf-8

print 'hello world',
print 'Tom'

# list | tuple | dictionary
print 'list | tuple | dictionary -----------------------------'
list1 = ['a', 'b', 'c']
tup = (1, 2, 3)
dict = {'a': 1, 'b': 2, 'c':3}
for key in dict:
	print 'key:', key, ', value:', dict[key]
	
for value in dict.values():
	print '打印value值'
	break

for key in dict.keys():
	print '打印key值'
	break

# 判断语句 if...elif...else
print 'if...elif...else ------------------------------------'
num = 5
if num==3:
	print 'boss'
elif num==2:
	print 'user'
else:
	print 'roadman'
	
# 循环语句 while | while...else | for...in | for...in...else
print 'while | while...else | for...in | for...in...else -------------------------'
count = 0
while(count<3):
	print 'The count is：', count
	count = count + 1

while count<=6:
	print count, 'is less than 7'
	count = count + 1
else:
	print count, ' is not less than 7'
	
fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
	print '当前水果：', fruit
for index in range(len(fruits)):
	print '之后水果：', fruits[index]
	
# 函数
print '函数 --------------------------------'
def ChangeInt(a):
	a = 10

def changeme(mylist):
	mylist.append([1, 2, 3])
	print '函数内取值：', mylist
	return
	
def sum_1(arg1, arg2):
	total = arg1 + arg2
	print '函数内：', total
	return total
	
sum_2 = lambda arg1, arg2: arg1 + arg2

b = 2
ChangeInt(b)
print b

mylist = [10, 20, 30]
changeme(mylist)
print '函数外取值：', mylist

print sum_1(20, 12)
print sum_2(10, 20)

# 面向对象
print '面向对象 ----------------------------------'
class Employee:
	empCount = 0
	
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1
		
	def displayCount(self):
		print 'Total Employee %d' % Employee.empCount
		
	def displayEmployee(self):
		print 'Name: ', self.name, ', Salary: ', self.salary
		
#	def __del__(self):
#		class_name = self.__class__.__name__
#		print class_name, '销毁'
		
emp1 = Employee('Zara', 2000)
emp2 = Employee('Manni', 5008)
emp1.displayEmployee()
emp2.displayEmployee()
print 'Total Employee %d' % Employee.empCount

class Parent:
	__private_attr = 0   # 私有变量
	_protected_attr = 0  # 保护变量
	publicCount = 0      # 公开变量
	
	def __init__(self):
		print '调用父类构造方法'
		
	def parentMethod(self):
		print '调用父类方法'
		
	def setAttr(self, attr):
		Parent.parentAttr = attr
		
	def getAttr(self):
		print '父类属性：', Parent.parentAttr
		
	def myMethod(self):
		print '调用父类方法'
		
	def  __private_method(self):
		print '调用父类私有方法'
		
class Child(Parent):
	def __init__(self):
		print '调用子类构造方法'
		
	def childMethod(self):
		print '调用子类方法'
		
	def myMethod(self):
		print '调用子类方法'
		
c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
c.myMethod()

		
	

	

	