#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import hashlib
import itertools
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter
import mysql.connector
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：
# p = (1, 2)
# 但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。
# 定义一个class又小题大做了，这时，namedtuple就派上了用场
from pyexpat import ParserCreate

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print p.x, p.y
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈,而list增删慢
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print q

# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print dd['key1']  # key1存在
print dd['key2']  # key2不存在，返回默认值

d = dict([('a', 1), ('b', 2), ('c', 3)])
print d  # dict的Key是无序的
# {'a': 1, 'c': 3, 'b': 2}
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print od  # OrderedDict的Key是有序的,按插入的顺序取


# OrderedDict([('a', 1), ('b', 2), ('c', 3)])


# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key000
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print 'remove:', last
        if containsKey:
            del self[key]
            print 'set:', (key, value)
        else:
            print 'add:', (key, value)
        OrderedDict.__setitem__(self, key, value)


# 统计字符出现的个数
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print c

# Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
print base64.b64encode('binary\x00string')
# 'YmluYXJ5AHN0cmluZw=='
print base64.b64decode('YmluYXJ5AHN0cmluZw==')
# 'binary string'

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in ')
sha1.update('python hashlib?')
print sha1.hexdigest()

# count()会创建一个无限的迭代器
natuals = itertools.count(1)
# for n in natuals:
#     print n

# 打印10次'A'
ns = itertools.repeat('A', 5)
for n in ns:
    print n

# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()
# 等函数根据条件判断来截取出一个有限的序列：
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
for n in ns:
    print n

for c in itertools.chain('ABC', 'XYZ'):
    print c


# 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'

# sax解析xml
class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint


# 解析html
class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print('data')

    def handle_comment(self, data):
        print('<!-- -->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)


parser = MyHTMLParser()
parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')

# MySQL的SQL占位符是%s；
# 通常在连接MySQL时传入use_unicode=True，让MySQL的DB-API始终返回Unicode。
# 必须是已经存在的数据库？
conn = mysql.connector.connect(user='root', password='Liuyu0529', database='day16', use_unicode=True)
cursor = conn.cursor()


# # 创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# # 插入一行记录，注意MySQL的占位符是%s:
# cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
# cursor.rowcount
# # 提交事务:
# conn.commit()
# cursor.close()
#
# # 运行查询:
# cursor = conn.cursor()
# cursor.execute('select * from user where id = %s', ('1',))
# values = cursor.fetchall()
# print values
# # [(u'1', u'Michael')]
# # 关闭Cursor和Connection :
# cursor.close()
# conn.close()


# ORM:把关系数据库的表结构映射到对象上
class User(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name


[
    User('1', 'Michael'),
    User('2', 'Bob'),
    User('3', 'Adam')
]

# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


class School(Base):
    __tablename__ = 'school'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 初始化数据库连接:
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
# 没有成功
engine = create_engine('mysql+mysqlconnector://root:Liuyu0529@localhost:3306/day16')
# engine = create_engine('mysql+mysqldb://root:Liuyu0529@192.168.202.2/day16')
# engine = create_engine('mysql://root:Liuyu0529@192.168.202.2/day16')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
