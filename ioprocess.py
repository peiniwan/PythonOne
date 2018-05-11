#!/usr/bin/env python
# -*- coding: utf-8 -*-

# os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中
# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件
import codecs
import json
import os
import random
import threading
import time

try:
    f = open('D:\heihei.txt', 'r')
    print f.read()
    # 如果文件很小，read()一次性读取最方便；
    # 如果不能确定文件大小，反复调用read(size)比较保险；
    # 如果是配置文件，调用readlines()最方便
    for line in f.readlines():
        print(line.strip())  # 把末尾的'\n'删掉
finally:
    if f:
        f.close()

# 上面太繁琐引入了with语句来自动帮我们调用close()方法
with open('D:\heihei.txt', 'r') as f:
    print f.read()

# 直接读出unicode
# with codecs.open('D:/gbk.txt', 'r', 'gbk') as f:
#     f.read() # u'\u6d4b\u8bd5'


print os.name  # 操作系统名字
print os.environ
print os.getenv('PATH')

# 查看当前目录的绝对路径:
print os.path.abspath('.')
# # 在某个目录下创建一个新目录，
# # 首先把新目录的完整路径表示出来:
# os.path.join(os.path.abspath('.'), 'testdir')
# # 然后创建一个目录:
# os.mkdir(os.path.abspath('.') + '/testdir')
# # 删掉一个目录:
# os.rmdir(os.path.abspath('.') + '/testdir')

# 分离路径和名字
print os.path.split('/Users/michael/testdir/file.txt')
# 可以轻松拿到扩展名
print os.path.splitext('/path/to/file.txt')

# 对文件重命名（需要有这个文件）
# os.rename('test.txt', 'test.py')
# 删除文件
# os.remove('test.py')

# 列出当前目录下的所有目录
print [x for x in os.listdir('.') if os.path.isdir(x)]
# 列出所有的.py文件
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

try:
    import cPickle as pickle
except ImportError:
    import pickle

# 序列化
d = dict(name='Bob', age=20, score=88)
# 方法1：pickle.dumps()方法把任意对象序列化成一个str，然后，就可以把这个str写入文件
s = pickle.dumps(d)
# 反序列化
d = pickle.loads(s)
print d

# 方法2：pickle.dump()直接把对象序列化后写入一个file-like Object：
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
# 反序列化
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print d

# 字典转化成json,也有俩种方法
d = dict(name='Bob', age=20, score=88)
s = json.dumps(d)
print json.loads(s)


# 对象序列号
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


# Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON
print(json.dumps(s, default=student2dict))
# 把任意class的实例变为dict
s = json.dumps(s, default=lambda obj: obj.__dict__)
print(s)


# 反序列化
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


print(json.loads(s, object_hook=dict2student))

# 进程和线程
# mac里这样创建
# print 'Process (%s) start...' % os.getpid()
# pid = os.fork()  # 创建一个进程
# if pid == 0:
#     print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
# else:
#     print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)

from multiprocessing import Process, Pool, Queue


# windows下，子进程要执行的代码
def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())


# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程
if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'


def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))


if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'


# 进程间通信
# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()



