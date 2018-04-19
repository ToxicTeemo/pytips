# coding: utf-8
from random import randint

# 如何在字典中根据条件筛选数据

# x 为学号，value 为分数
data = {x: randint(60,100) for x in xrange(1, 21)}
print data

# 实现1：字典表达式
print {k: v for k, v in data.iteritems() if v > 90}

# 实现2：遍历字典判断
newdata = {}
for k, v in data.iteritems():
    if v > 90:
        newdata[k] = v
print newdata
