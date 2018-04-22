# coding: utf-8
from random import randint, sample

# 如何快速找到多个字典中的公共键

s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}

# 实现1: 遍历字典键
res = []
for k in s1:
    if k in s2 and k in s3:
        res.append(k)
print res

# 实现2：利用集合（set）的交集操作
print s1.viewkeys() & s2.viewkeys() & s3.viewkeys()

# 实现3: N 个字典的实现
# 利用字典的 viewkeys() 方法，得到一个字典 keys 的集合
# 使用 map 函数，得到所有字典的 keys 的集合
# 使用 reduce 函数，取所有字典的 keys 的集合的交集
print reduce(lambda a, b: a & b, map(dict.viewkeys, [s1, s2, s3]))


