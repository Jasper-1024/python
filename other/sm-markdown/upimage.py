#!/usr/bin/python3
import requests
import json
from glob import glob

import time
import os

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

params = {'format': 'json', 'ssl': True}
prefix = 'https://sm.ms/api'

image_name = "tmp.jpg"


# 上传图片
def api_upload(image):
    '''upload an image file'''
    files = {'smfile': open(image, 'rb')}
    resp = requests.post(
        '{}/upload'.format(prefix), files=files, params=params)
    return resp.text


# 上传图片
def upload(filename):
    images = glob(filename)
    if not images:
        print('%s not image' % (filename))
    for image in images:
        # upload an image
        resp = json.loads(api_upload(image))
        # 返回上传图片的url
        if resp['code'] == 'error':
            # 打印错误信息
            print('uploda error msg:%s' % (resp['msg'].lower()))
            return None
        else:
            # print('%s upload success' % (filename))
            return resp['data']['url']


# 剪贴板获取图片
def get_image_Clipboard(clipboard):
    image = clipboard.wait_for_image()
    if image:
        image.savev(image_name, "jpeg", ["quality"], ["100"])
        return True
    else:
        return False


# url复制到剪贴板
def set_url_Clipboard(url, clipboard):
    clipboard.clear()
    if isinstance(url, str):
        clipboard.set_text(url, -1)
        clipboard.store()
    else:
        print('url type error')


# 删除临时文件
def del_flie(fliename):
    os.remove(fliename)


if __name__ == "__main__":
    clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
    # clipboard = Gtk.Clipboard.get(Gdk.SELECTION_PRIMARY)
    # set_url_Clipboard("123456", clipboard)
    while True:
        if get_image_Clipboard(clipboard):
            url = upload(image_name)
            set_url_Clipboard(url, clipboard)
            del_flie(image_name)

        time.sleep(0.8)
