#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8
import functools
import math
import os

print 'I\'m \"OK\"!'

a = 123  # a是整数
print a
a = 'ABC'  # a变为字符串

print a

a = 100
if a >= 0:  # 注意冒号
    print a
else:
    print -a
# int转成string，函数int(string)
# string转成int，函数str(number)
print len(u'ABC')
print 'Hi, %s, you have $%d.' % ('Michael', 1000000)
print 'Age: %s. Gender: %s' % (25, True)

classmates = ['Michael', 'Bob', 'Tracy']
classmates.append('Adam')
classmates.insert(1, 'Jack')
classmates.pop()
classmates.pop(1)
classmates[1] = 123  # 类型可以不同
# 相等的
print classmates
print classmates[len(classmates) - 1] == classmates[-1]
print classmates[len(classmates) - 2] == classmates[-2]

# tuple和list非常类似，但是tuple一旦初始化就不能修改，没有append()，insert()这样的方法
# 可以正常地使用classmates[-1]，但不能赋值成另外的元素
t = ('Michael', 'Bob', 'Tracy')
t = (1,);  # 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1, 2)
print t

# 如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
# 下面打印  teenager
age = 20
if age >= 6:
    print 'teenager'
elif age >= 18:
    print 'adult'
else:
    print 'kid'

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print sum
sum = 0
for x in range(101):
    sum = sum + x
print sum

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum

# 打印
# name = raw_input('please enter your name: ')
# print 'hello,', name

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d['Michael']
d['Adam'] = 67
print d['Adam']
# 要避免key不存在的错误
print 'Thomas' in d
print d.get('Thomas')
print d.get('Thomas', -1)
d.pop('Bob')
key = [1, 2, 3]
# key的对象就不能变,而list是可变的，就不能作为key
# d[key] = 'a list'
print d
# 要创建一个set，需要提供一个list作为输入集合
s1 = set([1, 2, 3])
# 重复元素在set中自动被过滤
s1 = set([1, 1, 2, 2, 3, 3])
s1.add(4)
s1.remove(4)
s2 = set([2, 3, 4])
# 交集、并集
print s1 & s2, s1 | s2

# 对于可变对象，比如list，对list进行操作，list内部的内容是会变化的
a = ['c', 'b', 'a']
a.sort()
print a
# 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。
# 相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
a = 'abc'
b = a.replace('a', 'A')
print a, b
