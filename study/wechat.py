# -*- coding: utf-8 -*-

# pip install itchat
import os
import re
from math import sqrt
from PIL import Image

import itchat


class Wechat(object):
    def __init__(self):
        self.basepath = "d:\itchat\\"

    def downFrients(self):
        itchat.auto_login()
        x = 0
        y = 0
        z = 0
        for friend in itchat.get_friends(update=True)[0:]:
            # 可以用此句print查看好友的微信名、备注名、性别、省份、个性签名（1：男 2：女 0：性别不详）
            # print(friend['NickName'], friend['RemarkName'], friend['Sex'], friend['Province'], friend['Signature'])

            if friend['Sex'] == 1:
                x = x + 1
            elif friend['Sex'] == 2:
                y = y + 1
            else:
                z = z + 1

            img = itchat.get_head_img(userName=friend["UserName"])
            rstr = "[\/\\\:\*\?\"\<\>\|]"
            new_NickName = re.sub(rstr, "_", friend['NickName'])
            if os.path.isdir(self.basepath):
                pass
            else:
                os.makedirs(self.basepath)
            path = self.basepath + new_NickName + "(" + friend['RemarkName'] + ").jpg"
            try:
                with open(path, 'wb') as f:
                    f.write(img)
            except Exception as e:
                print(repr(e))
        itchat.run()
        print '男生%s个，女生%s个，未知的%s个' % (x, y, z)

    def save(self):
        # path是存放好友头像图的文件夹的路径
        pathList = []
        for item in os.listdir(self.basepath):
            imgPath = os.path.join(self.basepath, item)
            pathList.append(imgPath)
        total = len(pathList)  # total是好友头像图片总数
        line = int(sqrt(total))  # line是拼接图片的行数（即每一行包含的图片数量）
        NewImage = Image.new('RGB', (128 * line, 128 * line))
        x = y = 0
        for item in pathList:
            try:
                img = Image.open(item)
                img = img.resize((128, 128), Image.ANTIALIAS)
                NewImage.paste(img, (x * 128, y * 128))
                x += 1
            except IOError:
                print("第%d行,%d列文件读取失败！IOError:%s" % (y, x, item))
                x -= 1
            if x == line:
                x = 0
                y += 1
            if (x + line * y) == line * line:
                break
        NewImage.save(self.basepath + "final.jpg")


wechat = Wechat();
# wechat.downFrients()
wechat.save()
