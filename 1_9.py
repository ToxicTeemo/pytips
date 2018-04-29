# coding: utf-8
from collections import OrderedDict
from time import time
from random import randint

# 如何让字典保持有序

# python dict 默认无序
d = {}
d['Jim'] = (1, 35)
d['Leo'] = (2, 37)
d['Bob'] = (3, 40)
for k in d:
    print k

# 通过 collections.OrderedDict 保持有序
d = OrderedDict()
d['Jim'] = (1, 35)
d['Leo'] = (2, 37)
d['Bob'] = (3, 40)
for k in d:
    print k

# 应用示例
d = OrderedDict()
players = list('ABCDEFGH')
start = time()

for i in xrange(8):
    raw_input()
    p = players.pop(randint(0, 7-i))
    end = time()
    print i + 1, p, end - start,
    d[p] = (i + 1, end - start)
print
print '-' * 20

for k in d:
    print k, d[k]


