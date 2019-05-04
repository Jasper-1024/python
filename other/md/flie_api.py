#!/usr/bin/python3

import os
import re


# 返回本目录下 .md 文件
def get_dir_md():
    arr = [
        x for x in os.listdir('.')
        if os.path.isfile(x) and os.path.splitext(x)[1] == '.md'
    ]
    return arr


# 文件名含有中文?
def is_fname_zh(filename):
    # 比较每一个字符的编码是否在 unicode 分配的中日韩文编码区
    return any('\u4e00' <= char <= '\u9fff' for char in filename)


# 返回url中图片名
def get_urlname(url):
    return re.search(r'.*\w\/(.*)$', url).group(1)


# 返回md文件 list [图片名称,图片链接]
def get_urlist(flie):
    with open(flie, 'r') as f:
        tmp = re.findall(r'.*!\[(.*?)]\((.*?)\).*', f.read())
        urlist = []
        name = set()
        for t in tmp:
            u = list(t)
            # 如果图片名不全(没有后缀..当时写的不规范),
            if not re.match(r'.*[.].*', u[0]):
                # 图片名为空
                if u[0] == '':
                    # 取url的图片名
                    u[0] = re.search(r'.*\w\/(.*)$', u[1]).group(1)
                # 没有后缀添加后缀(大部分为png)
                else:
                    u[0] += '.png'
            # 如果图片名重名
            if u[0] in name:
                # 取url的文件名
                u[0] = re.search(r'.*\w\/(.*)$', u[1]).group(1)
                print('rename %s' % (u[0]))
            name.add(u[0])
            urlist.append(u)
    return urlist


# 替换md文件中链接
def re_md_url(flie, urlist):
    with open(flie, 'r') as f:
        tmp = f.read()
    for ulist in urlist:
        tmp = tmp.replace(ulist[1], ulist[2])
    with open(flie, 'w') as f:
        f.write(tmp)
