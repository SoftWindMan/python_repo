#!/usr/bin/python
#coding=utf-8

# 享元(flyweight)设计模式属于结构设计模式类别。 它提供了一种减少对象数的方法。 它包含各种有助于改进应用程序结构的功能。享元对象最重要的特性是不可变的。 这意味着一旦构建就不能修改它们。 该模式使用HashMap来存储引用对象。

class ComplexGenetics(object):
	def __init__(self):
		pass
		
	def genes(self, gene_code):
		return 'ComplexPatter[%s]TooHugeinSize' % (gene_code)
		
class Families(object):
	family = {}
	
	def __new__(cls, name, family_id):
		try:
			id = cls.family[family_id]
		except KeyError:
			id = object.__new__(cls)
			cls.family[family_id] = id
		return id
		
	def set_genetic_info(self, genetic_info):
		cg = ComplexGenetics()
		self.genetic_info = cg.genes(genetic_info)
		
	def get_genetic_info(self):
		return self.genetic_info
		
def test():
	data = (('a', 1, 'ATAG'), ('a', 2, 'AAGT'), ('b', 1, 'ATAG'))
	family_objects = []
	
	for i in data:
		obj = Families(i[0], i[1])
		obj.set_genetic_info(i[2])
		family_objects.append(obj)
		
	for i in family_objects:
		print 'id = ' + str(id(i))
		print i.get_genetic_info()
		
	print "similar id's says that they are same objects"
	
if __name__ == "__main__":
	test()