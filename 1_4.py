# coding: utf-8
from collections import namedtuple

# 如何为元组中每个元素命名，提高程序可读性

# ('Jim', 16, 'male', 'jim8721@gmail.com')
# ('Lilei', 17, 'mail', 'leile@qq.com')
# ('Lucy', 16, 'female', 'lucy123@yahoo.com')


student = ('Jim', 16, 'male', 'jim8721@gmail.com')

# 不优雅的方式
# name
print student[0]
# age
print student[1]
# ...

# 实现1：定义类似与其他语言的枚举类型，也就是定义一系列数值常量
# NAME = 0
# AGE = 1
# SEX = 2
# EMAIL = 3
NAME, AGE, SEX, EMAIL = xrange(4)
# name
print student[NAME]
# age
print student[AGE]
# ...

# 实现2：使用标准库中 collections.namedtuple 替代内置 tuple
Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
s = Student('Jim', 16, 'male', 'jim8721@gmail.com')
# name
print s.name
# age
print s.age
# ...
