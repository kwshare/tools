#!/usr/bin/python
# coding:utf-8

# tools - cyjl.py
# 2017/12/29 9:31
# 

# from __future__ import unicode_literals
__author__ = 'Benny <benny@bennythink.com>'
from pypinyin import lazy_pinyin
import json


def get_next(pinyin):
    with open('simple.json', 'r') as f:
        data = json.load(f)
    result = data.get(pinyin)
    if result is None:
        return '哎呀，认输了'
    else:
        return result


if __name__ == '__main__':
    while True:
        user_input = raw_input('~~~~~说成语啦\n>').decode('utf-8')
        print get_next(lazy_pinyin(user_input[-1])[0])
