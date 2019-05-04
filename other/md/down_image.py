#!/usr/bin/python3

import os
from image_api import down
from flie_api import get_dir_md, get_urlist

if __name__ == "__main__":
    # 获取 .md 文件
    arr = get_dir_md()
    for md in arr:
        # 获取urllist
        urlist = get_urlist(md)
        if urlist:
            # 创建目录
            fdir = os.path.splitext(md)[0]
            try:
                os.mkdir(fdir)
            except FileExistsError as e:
                e
            # 进入子目录
            os.chdir(fdir)
            print('enter %s' % (os.path.abspath('.')))
            for u in urlist:
                down(u[0], u[1])
            print('leave %s' % (os.path.abspath('.')))
            # 返回上级目录
            os.chdir('../')
        else:
            # urlist 为空
            continue
