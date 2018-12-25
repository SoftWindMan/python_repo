#!/usr/bin/python
#coding=utf-8

# 在观察者设计模式这种模式中，对象被表示为等待事件触发的观察者。 一旦发生指定的事件，观察者就会关注该主体。 当事件发生时，主体告诉观察者它已经发生。

import threading, time, pdb

class Downloader(threading.Thread):
	def run(self):
		print 'downloading'
		for i in range(1, 5):
			self.i = i
			time.sleep(2)
			print 'unfunf'
			return 'hello world'
			
class Worker(threading.Thread):
	def run(self):
		for i in range(1, 5):
			print 'worker running: %i (%i)' % (i, t.i)
			time.sleep(1)
			t.join()
		print 'done'
			
t = Downloader()
t.start()

time.sleep(1)

t1 = Worker()
t1.start()

t2 = Worker()
t2.start()

t3 = Worker()
t3.start()

