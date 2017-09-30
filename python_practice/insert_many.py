#!/usr/bin/python
# coding:utf-8

import mysql.connector
import random
import time
from pymongo import MongoClient

con = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='speedtest')

cur = con.cursor()
a=[]
for i in range(20):
    id = random.randint(1, 255)
    t = int(time.time())
    ip_part1 = str(random.randint(0, 255))
    ip_part2 = str(random.randint(0, 255))
    ip_part3 = str(random.randint(0, 255))
    ip_part4 = str(random.randint(0, 255))
    ip = ip_part1 + '.' + ip_part2 + '.' + ip_part3 + '.' + ip_part4
    a.append([id,t,ip])
cmd = 'insert into test VALUES (%s,%s,%s)'
cur.executemany(cmd, a)
con.commit()
con.close