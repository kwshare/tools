#!/usr/bin/python
# coding:utf-8
# MySQL Connector

import mysql.connector
import MySQLdb

con = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='test')

user_input = 22

cur = con.cursor()
cur.execute('select * from table1 WHERE ID=%s', (user_input,))
print cur.fetchone()

cur.execute('select * from table1 WHERE ID=%s AND TYPE =%s',
            (2,'ARP'))
print cur.fetchone()

# print MySQLdb.paramstyle
# print mysql.connector.paramstyle
