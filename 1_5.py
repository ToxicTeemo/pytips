# coding: utf-8
from random import randint
from collections import Counter

# 如何统计序列中元素的出现频度, 找到出现次数最高的 3 个元素，它们出现的次数是多少


# 实现1：用 dict.fromkeys 初始化一个序列化值为 key 的字典，value 为 0
data = [randint(0, 20) for _ in xrange(30)]
c = dict.fromkeys(data, 0)
for x in data:
    c[x] += 1
# 如何实现找到出现次数最高的 n 个元素？？？ --> 先排序，再取出前三个元素
sorted_c = sorted(c.items(), key=lambda x: x[1], reverse=True)
print sorted_c[:3]


# 实现2: 用 collections.Counter 库
c2 = Counter(data)
print c2.most_common(3)
