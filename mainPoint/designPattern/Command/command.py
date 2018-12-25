#!/usr/bin/python
#coding=utf-8

# 客户端创建一个包含要执行的命令列表的命令对象。 创建的命令对象实现了特定的接口。

def demo(a, b, c):
	print 'a:', a
	print 'b:', b
	print 'c:', c
	
class Command:
	def __init__(self, cmd, *args):
		self._cmd = cmd
		self._args = args
		
	def __call__(self, *args):
		return apply(self._cmd, self._args + args)
		
cmd = Command(dir, __builtins__)
print cmd()

cmd = Command(demo, 1, 2)
cmd(3)

