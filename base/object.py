#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 面向过程
import logging
import types

std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 81}


def print_score(std):
    print('%s: %s' % (std['name'], std['score']))


# 面向对象
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.score = score

    # self指向创建的实例本身，可以不传
    # 实现数据的封装
    def print_score(self):
        print('%s: %s' % (self.__name, self.score))

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
print lisa.get_name(), lisa.score


class Animal(object):
    def run(self):
        print 'Animal is running...'


class Dog(Animal):
    def run(self):
        print 'Dog is running...'


class Cat(Animal):
    def run(self):
        print 'Cat is running...'


# 多态
def run_twice(animal):
    if (isinstance(animal, Animal)):
        animal.run()
    else:
        print "类型错误"


print run_twice(Cat())
print run_twice(Student('Bart Simpson', 59));

# 对于class的继承关系来说，使用type()就很不方便。
# 我们要判断class的类型，可以使用isinstance()函数。
print type('abc') == types.StringType
print type(u'abc') == types.UnicodeType
print type([]) == types.ListType
print type(str) == types.TypeType

print  dir('ABC')


class Student(object):
    pass


s = Student()
s.name = 'Michael'  # 动态给实例绑定一个属性
print s.name


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s, Student)  # 给实例绑定一个方法
s.set_age(25)  # 调用实例方法
print s.age  # 测试结果
s2 = Student()  # 创建新的实例


# print s2.set_age(25)  # 尝试调用方法,不能


def set_score(self, score):
    self.score = score


# 为了给所有实例都绑定方法，可以给class绑定方法
Student.set_score = MethodType(set_score, None, Student)


# 定义一个特殊的__slots__变量，来限制该class能添加的属性，但对子类不起作用
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'


# s.score = 99  # 不能绑定属性'score'

# 该属性不是直接暴露的，而是通过getter和setter方法来实现
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.score = 60  # OK，实际转化为s.set_score(60)
s.score  # OK，实际转化为s.get_score()
# s.score = 9999
print s.score  # 实际转化为s.get_score()


# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2014 - self._birth


# 可以多继承
# class Dog(Mammal, RunnableMixin, CarnivorousMixin):
#     pass


# 定制类
# __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name=%s)' % self.name

    __repr__ = __str__


s = Student('Michael')
print s
print Student('Michael')


# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


f = Fib()


# print f(0), f(100)

# 只有在没有找到属性的情况下，才调用__getattr__，已有的属性，不会在__getattr__中查找。
class Student(object):

    def __getattr__(self, attr):
        if attr == 'age':
            # return 25
            return lambda: 25  # 可以retrun函数，调用方式不一样了
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


s = Student()
print s.age()


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path


print Chain().status.user.timeline.list


# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用(像方法一样)
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('Michael')
print s()


# 怎么判断一个变量是对象还是函数呢？
# print callable(Student())
# print callable([1, 2, 3])

def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


# logging模块可以非常容易地记录错误信息
def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)
        print 'Error!'
    finally:
        print 'finally...'


# 只要main()捕获到了，就可以处理
print main()


# assert的意思是，表达式n != 0应该是True，否则，后面的代码就会出错。
# 如果断言失败，assert语句本身就会抛出AssertionError：
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


def main():
    foo('0')


# 和assert比，logging不会抛出错误，而且可以输出到文件
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print 10 / n
