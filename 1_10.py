# coding: utf-8
from random import randint
from collections import deque
import pickle

# 如何实现用户的历史记录功能

N = randint(0, 10)
# 通过 collections.deque 实现
history = deque([], 5)


def guess(k):
    if k == N:
        print 'right'
        return True
    if k < N:
        print '%s is less-than N' % k
    else:
        print '%s is greater-than N' % k
    return False

while True:
    line = raw_input("please input a number: ")
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == 'history' or line == 'h?':
        print list(history)

# 把结果 history deque 对象存为文件 ???
# pickle.dump(history, open('history', 'w'))
# pickle.load(open('history'))



