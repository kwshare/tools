# coding: utf-8
# douban-dl - remains.py
# 2019/1/27

__author__ = 'Yan Liu <yanl8@cisco.com>'

import os
import requests

REFER = 'https://movie.douban.com/celebrity/1018562/photo/'
BASE = 'https://img1.doubanio.com/view/photo/raw/public/%s'
headers = {
    "Referer": REFER,
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36"
}
r = requests.session()

files = os.listdir('bad')
for filename in files:
    print('downloading %s' % filename)
    response = r.get(BASE % filename, headers=headers)
    with open(os.path.join('ok', filename), 'wb') as f:
        print('Writing %s' % filename)
        f.write(response.content)
