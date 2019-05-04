#!/usr/bin/python3

import os
import time
from image_api import upload
from flie_api import get_dir_md, get_urlist, is_fname_zh, get_urlname, re_md_url

if __name__ == "__main__":
    # 获取.md文件
    arr = get_dir_md()
    for file in arr:
        # 获取urlist
        urlist = get_urlist(file)
        if urlist:
            # 进入子目录
            fdir = os.path.splitext(file)[0]
            os.chdir(fdir)
            print('enter %s' % (os.path.abspath('.')))
            # 上传图片
            for u in urlist:
                # u[0]图片名含有中文,临时重命名
                if is_fname_zh(u[0]):
                    tmp = get_urlname(u[1])
                    os.rename(u[0], tmp)
                else:
                    tmp = u[0]
                # 上传图片
                u.append(upload(tmp))
                os.rename(tmp, u[0])
                # 延时
                time.sleep(20)
            # 返回上级目录
            print('leave %s' % (os.path.abspath('.')))
            os.chdir('../')
            # 替换链接
            re_md_url(file, urlist)
            # 延时
            time.sleep(60)
        else:
            # urlist 为空
            continue
