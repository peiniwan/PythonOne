#!/usr/bin/env python
# -*- coding: utf-8 -*-

# host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
# 加上decode_responses=True，写入的键值对中的value为str类型，不加这个参数写入的则为字节类型
import time

import redis

# r = redis.Redis(host='localhost', port=6379, decode_responses=True)
# r.set('name', 'xiaoyu')
# print(r['name'])
# print(r.get('name'))  # 取出键name对应的值
# print(type(r.get('name')))


# redis-py使用connection pool来管理对一个redis server的所有连接，
# 避免每次建立、释放连接的开销。默认，每个Redis实例都会维护一个自己的连接池。
# 可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个Redis实例共享一个连接池
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
r.set('gender', 'male')
print(r.get('gender'))

# redis基本命令 String
# 在Redis中设置值，默认，不存在则创建，存在则修改
# 参数：
# ex，过期时间（秒）
# px，过期时间（毫秒）
# nx，如果设置为True，则只有name不存在时，当前set操作才执行（新建）
# xx，如果设置为True，则只有name存在时，当前set操作才执行 （修改）
# ex，过期时间（秒） 这里过期时间是3秒，3秒后p，键food的值就变成None
r.set('food', 'mutton', ex=3, xx=True)
print(r.get('food'))
print(r.setnx('fruit1', 'banana'))  # fruit1不存在，输出为True

# r.setex("fruit2", "orange", 5)
# time.sleep(5)
# print(r.get('fruit2'))  # 5秒后，取值就从orange变成None

# 批量设置值
r.mget({'k1': 'v1', 'k2': 'v2'})
r.mset(k1="v1", k2="v2") # 这里k1 和k2 不能带引号 一次设置对个键值对
# 批量获取
print(r.mget("k1", "k2"))   # 一次取出多个键对应的值
print(r.mget("k1"))
print(r.mget(['k1', 'k2']))
print(r.mget("fruit", "fruit1", "fruit2", "k1", "k2"))  # 将目前redis缓存中的键对应的值批量取出来

# 设置新值并获取原来的值
print(r.getset("fruit1", "barbecue"))

# 获取子序列（根据字节获取，非字符）
r.set("cn_name", "君惜大大") # 汉字
print(r.getrange("cn_name", 0, 2))   # 取索引号是0-2 前3位的字节 君 切片操作 （一个汉字3个字节 1个字母一个字节 每个字节8bit）
print(r.getrange("cn_name", 0, -1))  # 取所有的字节 君惜大大 切片操作
r.set("en_name","junxi") # 字母
print(r.getrange("en_name", 0, 2))  # 取索引号是0-2 前3位的字节 jun 切片操作 （一个汉字3个字节 1个字母一个字节 每个字节8bit）
print(r.getrange("en_name", 0, -1)) # 取所有的字节 junxi 切片操作

# 修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加）
r.setrange("en_name", 1, "ccc")
print(r.get("en_name"))    # jccci 原始值是junxi 从索引号是1开始替换成ccc 变成 jccci

# 获取name对应的值的二进制表示中的某位的值 （0或1）
print(r.getbit("foo1", 0)) # 0 foo1 对应的二进制 4个字节 32位 第0位是0还是1

# 返回name对应值的字节长度（一个汉字3个字节）
print(r.strlen("foo"))  # 4 'goo1'的长度是4

# 自增 name对应的值，当name不存在时，则创建name＝amount，否则，则自增。
r.set("foo", 123)
print(r.mget("foo", "foo1", "foo2", "k1", "k2"))
r.incr("foo", amount=1)
print(r.mget("foo", "foo1", "foo2", "k1", "k2"))
# 应用场景 – 页面点击数
# 当redis服务器启动时，可以从关系数据库读入点击数的初始值（12306这个页面被访问了34634次）
r.set("visit:12306:totals", 34634)
print(r.get("visit:12306:totals"))
# 每当有一个页面点击，则使用INCR增加点击数即可。
r.incr("visit:12306:totals")
r.incr("visit:12306:totals")
# 页面载入的时候则可直接获取这个值
print(r.get("visit:12306:totals"))
# 自减 name对应的值，当name不存在时，则创建name＝amount，否则，则自减。
r.decr("foo4", amount=3) # 递减3
r.decr("foo1", amount=1) # 递减1
print(r.mget("foo1", "foo4"))

# 在redis name对应的值后面追加内容
r.append("name", "haha")    # 在name对应的值junxi后面追加字符串haha
print(r.mget("name"))