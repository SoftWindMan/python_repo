#!/usr/bin/python
#coding=utf-8

# 使用 Python 小技巧

from collections import Counter

# 变量交换
a = 5
b = 10
a, b = b, a
print a, b

# list转字符串
print '# list转字符串 --------------------------'

fruitArr = ['apple', 'banana', 'pear']
print ' - '.join(fruitArr)

specialArr = ['hello', 1, 3.7]
print ' - '.join(map(str, specialArr))

# list中元素出现次数
print '# list中元素出现次数 --------------------------'

numArr = [1, 1, 1, 3, 5, 6, 6, 6, 6, 6]
print max(set(numArr), key = numArr.count)

cnt = Counter(numArr)
print(cnt.most_common(3))

# 字符串是否anagram（词所用字母及其个数）
print '# 字符串是否anagram --------------------------'

strA = 'abc'
strB = 'cba'
print Counter(strA) == Counter(strB)

# 字符串倒转
print '# 字符串倒转 --------------------------'

strC = 'abcdefghijk'
print strC[::-1]

for char in reversed(strC):
	print char
	
numA = 123456789
print(int(str(numA)[::-1]))

# list倒转
print '# list倒转 --------------------------'

print fruitArr[::-1]

for f in reversed(fruitArr):
	print(f)
	
# 判断key是否在字典中
print '# 判断key是否在字典中 --------------------------'

aDict = {'a':3, 'b':2, 'c':1}
print(aDict.get('d'))

# 字典排序
print '# 字典排序 --------------------------'

print sorted(aDict.items(), key=lambda x:x[0])

# 合并字典
print '# 合并字典 --------------------------'

bDict = {'d':4, 'e':5}
aDict.update(bDict)
print(aDict)

# list去重
print '# list去重 --------------------------'

print list(set(numArr))











