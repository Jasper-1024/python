#!/usr/bin/python3

import os
import requests
import json
from glob import glob
from urllib import request

params = {'format': 'json', 'ssl': True}
prefix = 'https://sm.ms/api'


# 上传图片
def api_upload(image):
    '''upload an image file'''
    files = {'smfile': open(image, 'rb')}
    print()
    resp = requests.post(
        '{}/upload'.format(prefix), files=files, params=params)
    return resp.text


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
            print('%s upload success' % (filename))
            return resp['data']['url']


# 下载图片
def down(file, url):
    if not os.path.exists(file):
        print('down %s' % (file))
        # 本地http代理
        proxy = request.ProxyHandler({'http': '127.0.0.1:1081'})
        opener = request.build_opener(proxy)
        request.install_opener(opener)
        request.urlretrieve(url, file)
    else:
        # 文件已存在
        print('%s is exist' % (file))