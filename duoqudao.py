#!/usr/bin/env python
# -*- coding: utf-8 -*-


import zipfile
import shutil
import os

# 创建空文件，用来存放渠道号
empty_file = 'temp'
f = open('temp', 'w')
f.close()

# 当前目录中的初始apk文件
apk_file = 'iqb.apk'
# 创建存放渠道包的目录
release_dir = 'release/'
if not os.path.exists(release_dir):
    os.mkdir(release_dir)

# 生成新apk的文件名
temp_array = os.path.splitext(apk_file)
new_apk_file_name = release_dir + temp_array[0] + "_{channel}" + temp_array[1]

# 当前目录中的渠道列表
f = open('channel.txt')
channel_list = f.readlines()
f.close()

# 遍历渠道列表
for channel in channel_list:
    # 删除换行符
    channel = channel.strip()
    # 生成新apk文件名
    new_apk = new_apk_file_name.format(channel=channel)
    # 拷贝出新apk
    shutil.copy(apk_file, new_apk)
    # 打开新apk文件
    f = zipfile.ZipFile(new_apk, 'a', zipfile.ZIP_DEFLATED)
    # 生成渠道文件名
    channel_file = "META-INF/channel_{channel}".format(channel=channel)
    # 写入渠道空文件
    f.write(empty_file, channel_file)
    # 关闭文件
    f.close()

# 最后删除空文件
os.remove(empty_file)
