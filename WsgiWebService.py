#!/usr/bin/env python
# -*- coding: utf-8 -*-

# environ：一个包含所有HTTP请求信息的dict对象；
# start_response：一个发送HTTP响应的函数。
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # return '<h1>Hello, web!</h1>'
    return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')


# server.py
# Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现
# 启动成功后，打开浏览器，输入http://localhost:8000/，就可以看到结果了
from wsgiref.simple_server import make_server

# 导入我们自己编写的application函数:
# from web import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:

httpd = make_server('', 8000, application)
print "Serving HTTP on port 8000..."
# 开始监听HTTP请求:
httpd.serve_forever()
