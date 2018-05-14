#!/usr/bin/python
# coding:utf-8

# Intern-Life - yoitsu.py
# 2018/5/9 15:43
# 

__author__ = 'Benny <benny@bennythink.com>'

import json
import os
from base64 import b64encode

import qrcode
config = json.load(open("config.json"))
qrcode.make("ss://%s@%s:%s#%s" % (b64encode(config['method'] + ':' + config['password']), config['server'],
                                  config['server_port'], 'horo')).save("horo.jpg")
os.system('horo.jpg')

