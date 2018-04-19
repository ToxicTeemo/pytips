# coding: utf-8
from random import randint

# 如何在集合中根据条件筛选数据

data = [randint(-10, 10) for _ in xrange(10)]
print data

setdata = set(data)
print setdata

# 实现1：集合表达式
print {x for x in setdata if x % 3 == 0}

# 实现2：遍历集合判断
newsetdata = set()
for x in setdata:
    if x % 3 == 0:
        newsetdata.add(x)
print newsetdata