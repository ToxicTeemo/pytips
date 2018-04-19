# coding: utf-8
import re
from collections import Counter

# 对某英文文章的单词，进行词频统计，找到出现次数最高的 10 个单词，它们出现次数是多少？

# 实现1：用 re.split('\W+', txt) 来分割单词
with open("coding-style.txt") as f:
    txt = f.read()
    # 对非字母的文字进行分割
    c = Counter(re.split('\W+', txt))
    print c
    print c.most_common(10)
