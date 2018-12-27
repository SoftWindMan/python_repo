#coding=utf-8
from collections import namedtuple, deque, OrderedDict, Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

q = deque(['a', 'b', 'c'])
q.append('d')
q.appendleft('e')
print(q)

d = dict([('a', 1), ('b', 2), ('c', 3)])
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(d, od)

c = Counter()
for ch in 'programming':
    c[ch] += 1
print(c)