#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools
import math
import os

# 函数
# 比较函数
print cmp(1, 2)
# 数据类型转换
print int('123')
print int(12.34)
str(1.23)
unicode(100)
bool(1)
bool('')


# 定义函数，如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。
# return None可以简写为return，函数执行完毕没有return语句时，自动return None。
# 只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance实现
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


a = my_abs  # 变量a指向abs函数
print a(-1)  # 所以也可以通过a调用abs函数


# 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句
# pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
# 缺少了pass，代码运行就会有语法错误。
def nop():
    pass


# 可以返回多个值,实际是返回tuple，这样写起来方便
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print x, y
r = move(100, 100, 60, math.pi / 6)
print r


# 默认参数,必选参数在前，默认参数在后
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print power(5), power(5, 3)


def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city


print  enroll('Sarah', 'F')
print enroll('Bob', 'M', 7)
# 当不按顺序提供部分默认参数时，需要把参数名写上
print enroll('Adam', 'M', city='Tianjin')


def add_end(L=[]):
    L.append('END')
    return L


print add_end()
print add_end()  # ['END', 'END']，不对


# 默认参数必须指向不变对象！,修改上面的例子,否则运行会有逻辑错误！
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 可变参数，在参数前面加了一个*号
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print calc(1, 2)
print calc()

# 如果已经有一个list或者tuple，要调用一个可变参数怎么办？
nums = [1, 2, 3]
print calc(nums[0], nums[1], nums[2])
print calc(*nums)


# 关键字参数,可以扩展函数的功能
# 比如，在person函数里，我们保证能接收到name和age这两个参数，
# 但是，如果调用者愿意提供更多的参数，我们也能收到
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw


person('Michael', 30)
# name: Michael age: 30 other: {}
person('Bob', 35, city='Beijing')
# name: Bob age: 35 other: {'city': 'Beijing'}
person('Adam', 45, gender='M', job='Engineer')
# name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=kw['city'], job=kw['job'])
person('Jack', 24, **kw)


# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用
# 注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw


print func(1, 2)
# a = 1 b = 2 c = 0 args = () kw = {}
print func(1, 2, c=3)
# a = 1 b = 2 c = 3 args = () kw = {}
print func(1, 2, 3, 'a', 'b')
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
print func(1, 2, 3, 'a', 'b', x=99)
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}

# 要注意定义可变参数和关键字参数的语法：
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
args = (1, 2, 3, 4)  # tuple
kw = {'x': 99}  # dict
print func(*args, **kw)


# a = 1 b = 2 c = 3 args = (4,) kw = {'x': 99}

# 递归
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


# 尾递归
def fact(n):
    return fact_iter(n, 1)


# 切片
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
r = []
n = 3
for i in range(n):
    r.append(L[i])

# 迭代
print r
# 切片（Slice）操作符,取前3个元素，用一行代码就可以完成
print L[0:3]
# 如果第一个索引是0，还可以省略
print L[:3]
# 取倒数第一个元素
print L[-2:-1]
# 取后俩个元素
print L[-2:]
# 原样复制一个list：
print L[:]
# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
print (0, 1, 2, 3, 4, 5)[:3]
print 'ABCDEFG'[:3]

# 只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代
# 遍历key
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key
# 遍历value
for value in d.itervalues():
    print value
# 遍历key,value
for k, v in d.iteritems():
    print k, '=', v

for ch in 'ABC':
    print ch

from collections import Iterable

print isinstance([1, 2, 3], Iterable)  # list是否可迭代
print isinstance('abc', Iterable)  # str是否可迭代
print isinstance(123, Iterable)  # 整数是否可迭代，false
print isinstance(x, str)  # 判断一个变量是不是字符串

# 这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print i, value

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x, y

# 列表生成式
print range(1, 11)
L = []
# [1x1, 2x2, 3x3, ..., 10x10]
for x in range(1, 11):
    L.append(x * x)
print [x * x for x in range(1, 11)]
# 筛选出仅偶数的平方
print [x * x for x in range(1, 11) if x % 2 == 0]
# 两层循环，可以生成全排列
print [m + n for m in 'ABC' for n in 'XYZ']
# 列出当前目录下的所有文件和目录名
print [d for d in os.listdir('.')]  # os.listdir可以列出文件和目录
L = ['Hello', 'World', 'IBM', 'Apple']
# 一个list中所有的字符串变成小写
print [s.lower() for s in L]

# 生成器:如果列表元素可以按照某种算法推算出来，这样就不必创建完整的list，从而节省大量的空间
# 和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator
L = [x * x for x in range(10)]
g = (x * x for x in range(10))
print g.next()
for n in g:
    print n


# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5


# 在执行过程中，遇到yield就中断，下次又继续执行
# 基本上从来不会用next()来调用它，而是直接使用for循环来迭代
o = odd()
print o.next()
print o.next()
print o.next()


# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
# 函数的名字也是变量
def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))


def f(x):
    return x * x


# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print list(r)
# for也能实现，太麻烦
L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)
print list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


# reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def add(x, y):
    return x + y


print reduce(add, [1, 3, 5, 7, 9]) \
    # 求和运算可以直接用Python内建函数sum()，没必要动用reduce。


# print sum([1, 3, 5, 7, 9])


def fn(x, y):
    return x * 10 + y


print reduce(fn, [1, 3, 5, 7, 9])


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print reduce(fn, map(char2num, '13579'))

# 简化
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


# 用lambda函数进一步简化
def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print str2int('13579')


# filter()函数用于过滤序列
# 根据返回值是True还是False决定保留还是丢弃该元素
def is_odd(n):
    return n % 2 == 1


print list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))


def not_empty(s):
    return s and s.strip()


print list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))

print sorted([36, 5, -12, 9, -21])
print sorted([36, 5, -12, 9, -21], key=abs)
print sorted(['bob', 'about', 'Zoo', 'Credit'])
# 排序应该忽略大小写，按照字母序排序
print sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


# 闭包，函数作为返回值
# 返回的函数并没有立刻执行，而是直到调用了f()才执行。
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print f1() == f2()  # true,比较的值
print f1 == f2  # false,引用不同，所以f1()和f2()的调用结果互不影响。


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
# 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
f1, f2, f3 = count()


def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()  # 1，4，9

# 匿名函数
# 冒号前面的x表示函数参数
print list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


# 匿名函数lambda x: x * x,实际上就是
def f(x):
    return x * x


# 可以把匿名函数赋值给一个变量，再利用变量来调用该函数
# 也可以把匿名函数作为返回值返回
f = lambda x: x * x
print f(4)


# 假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2015-3-25')


print now()

# 偏函数：当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
int2 = functools.partial(int, base=2)


# 不需要我们自己定义
def int3(x, base=2):
    return int(x, base)


print int2('1000000')
print int3('1000000')

# 作者
__author__ = 'Michael Liao'


def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用
# 公开greeting()函数，而把内部逻辑用private函数隐藏起来
def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
