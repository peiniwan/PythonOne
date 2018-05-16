#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

# 基础
# \d可以匹配一个数字，\w可以匹配一个字母或数字
# .可以匹配任意字符，所以：'py.'可以匹配'pyc'、'pyo'、'py!'等等。
# ，用*表示任意个字符（包括0个），用+表示至少一个字符(没有空格)，要空格的话是\s+
# 用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符：

# \d{3}\s+\d{3,8}。
# \d{3}表示匹配3个数字，例如'010'；
# \s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，' '等；
# \d{3,8}表示3-8个数字，例如'1234567'。
# 要匹配'010-12345'这样的号码呢？由于'-'是特殊字符，在正则表达式中，要用'\'转义，所以正则是\d{3}\-\d{3,8}。

# 进阶
# 要做更精确地匹配，可以用[]表示范围
# [0-9a-zA-Z\_]可以匹配一个数字或字母或者下划线；
# [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
# [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
# [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。

# A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。
# ^表示行的开头，^\d表示必须以数字开头。
# $表示行的结束，\d$表示必须以数字结束。
# py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了。

# match：匹配string 开头，成功返回Match object, 失败返回None，只匹配一个。
# search：在string中进行搜索，成功返回Match object, 失败返回None, 只匹配一个。
# findall：在string中查找所有 匹配成功的组, 即用括号括起来的部分。返回list对象，每个list item是由每个匹配的所有组组成的list。
# finditer：在string中查找所有 匹配成功的字符串, 返回iterator，每个item是一个Match object。

# 将正则表达式编译成 Pattern 对象，注意 hello 前面的 r 的意思是 “原生字符串”


content = '333STR1666STR299'
regex = r'([A-Z]+(\d))'
# 最外边的括号去掉，即regex = r'[A-Z]+(\d)'，组的个数就会减少一个
# content的开头不符合正则，所以结果为None。
print(re.match(regex, content))
# None

# 只会找一个匹配，match[0]是regex所代表的整个字符串，match[1]是第一个()中的内容，match[2]是第二对()中的内容。
match = re.search(regex, content)
print('\nre.search() return value: ' + str(type(match)))
print(match.group(0), match.group(1), match.group(2))
# re.search() return value: <type '_sre.SRE_Match'>
# ('STR1', 'STR1', '1')

result1 = re.findall(regex, content)
print('\nre.findall() return value: ' + str(type(result1)))
for m in result1:
    print(m[0], m[1])
# re.findall() return value: <type 'list'>
# ('STR1', '1')
# ('STR2', '2')


result2 = re.finditer(regex, content)
print('\nre.finditer() return value: ' + str(type(result2)))
for m in result2:
    print(m.group(0), m.group(1), m.group(2))  #字符串
# re.finditer() return value: <type 'callable-iterator'>
# ('STR1', 'STR1', '1')
# ('STR2', 'STR2', '2')

# 切分字符串
print re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
# _sre.SRE_Match object at 0x1026e18b8>
print re.match(r'^\d{3}\-\d{3,8}$', '010 12345')

print re.split(r'\s+', 'a b   c')
print re.split(r'[\s\,]+', 'a,b, c  d')
# 空格或，或；+至少一个空格
print re.split(r'[\s\,\;]+', 'a b;; c  d')


# 分组
# 用()表示的就是要提取的分组（Group）
# group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print m.group(0)
print m.group(1)
print m.group(2)

t = '19:05:30'
m = re.match(
    r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',
    t)
print m.groups()

# 识别日期：'^(0[1-9]|1[0-2]|[0-9])-(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[0-9])$'
# 对于'2-30'，'4-31'这样的非法日期，用正则还是识别不了，或者说写出来非常困难，这时就需要程序配合识别了。

# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。举例如下，匹配出数字后面的0：
print re.match(r'^(\d+)(0*)$', '102300').groups()
# ('102300', '')
# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
print re.match(r'^(\d+?)(0*)$', '102300').groups()
# ('1023', '00')

# 预编译该正则表达式
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
print re_telephone.match('010-12345').groups()
# ('010', '12345')
print re_telephone.match('010-8086').groups()
# ('010', '8086')

# someone@gmail.com
# <Tom Paris> tom@voyager.org

# 正则表达式中，“.”的作用是匹配除“\n”以外的任何字符，也就是说，
# 它是在一行中进行匹配。这里的“行”是以“\n”进行区分的。a字符串有每行的末尾有一个“\n”，不过它不可见。
# 如果不使用re.S参数，则只在每一行内进行匹配，如果一行没有，就换下一行重新开始，不会跨行。而使用re.S参数以后，
# 正则表达式会将这个字符串作为一个整体，将“\n”当做一个普通的字符加入到这个字符串中，在整体中进行匹配。
a = '''asdfhellopass:
    123
    worldaf
    '''
b = re.findall('hello(.*?)world', a)
c = re.findall('hello(.*?)world', a, re.S)
print 'b is ', b
print 'c is ', c
# b is  []
# c is  ['pass:\n\t123\n\t']

text = ''
file = open('sina.html')
for line in file:
    text = text + line

file.close()

# {}表示位数，[][]表示第一位第二位
# ()是或者，几个（）就是几个元素的数组，没有会是""，所以过滤了下
# 1）.*? 是一个固定的搭配，.和*代表可以匹配任意无限多个字符，加上？表示使用非贪婪模式进行匹配
# 也就是我们会尽可能短地做匹配，以后我们还会大量用到 .*? 的搭配。
# 2）(.*?)代表一个分组，在这个正则表达式中我们匹配了五个分组，在后面的遍历item中，
# item[0]就代表第一个(.*?)所指代的内容，item[1]就代表第二个(.*?)所指代的内容，以此类推。
pattern = re.compile(
    '<div class="author clearfix">.*?<a.*?<h2>(.*?)</h2>.*?<div class="articleGender manIcon">(.*?)</div>.*?<div class="content">.*?<span>(.*?)</span>.*?<span class="stats-vote"><i class="number">(.*?)</i>',
    re.S)
items = re.findall(pattern, text)
for item in items:
    print item

# final_result = set()
# for pair in result:
#     if pair[0] not in final_result:
#         final_result.add(pair[0])
#         if pair[1] not in final_result:
#             final_result.add(pair[1])
#
# final_result.remove('')
# print(final_result)
print items
