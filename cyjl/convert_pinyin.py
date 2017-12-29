#!/usr/bin/python
# coding:utf-8

# tools - convert_pinyin.py
# 2017/12/29 9:38
# 
__author__ = 'Benny <benny@bennythink.com>'

import pyodbc
import json
from pypinyin import lazy_pinyin
import sys

conn_str = (
    'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    'DBQ=C:\\Users\\yanl8\\Documents\\tools\\cyjl\\cnzzz.mdb;'
)
con = pyodbc.connect(conn_str)
cur = con.cursor()
cur.execute('select ChengYu from YesoulChenYu ')
data = cur.fetchall()
cy = {}
for item in data:
	# should consider strict mode
    first_letter = lazy_pinyin(item[0][0])
    cy[first_letter[0]] = item[0]

with open('simple.json', 'w') as f:
    f.write(json.dumps(cy, ensure_ascii=False).encode('utf-8'))
