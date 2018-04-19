# coding: utf-8
from random import randint

# 如何根据字典中值的大小，对字典中的项排序

# 实现1：字典 --> 元组，value 在第一个元素，先比较 --> sorted 排序元组
data = {x: randint(60, 100) for x in 'xyzabc'}
print sorted(zip(data.itervalues(), data.iterkeys()))


# 实现2: 用 data.items() 方法
print sorted(data.items(), key=lambda x: x[1])

