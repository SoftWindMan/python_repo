#coding=utf-8

import traceback

try:
	1/0
except Exception as e:
	print(e.message)

try:
	1/0
except:
	traceback.print_exc()