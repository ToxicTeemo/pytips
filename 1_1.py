# coding: utf-8
from random import randint

# 如何在列表中根据条件筛选数据

# xrange(10) 返回 0~9 的数字的迭代器
# randint(-10, 10) 返回 [-10, 10] 之间的随机数
data = [randint(-10, 10) for _ in xrange(10)]
print data

# 实现1： filter 与 lambda
print filter(lambda x: x > 0, data)

# 实现2: 列表表达式
print [x for x in data if x > 0]

# 实现3: 遍历列表判断
newdata = []
for i in data:
    if i > 0:
        newdata.append(i)
print newdata

