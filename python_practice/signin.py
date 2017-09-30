#!/usr/bin/python
# coding:utf-8

# sign in
import mysql.connector
import time


def sign(face_name=None):
    if face_name:
        con = mysql.connector.connect(user='root', password='root',
                                      host='127.0.0.1',
                                      database='sign')
        cur = con.cursor()
        sign_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        cur.execute('INSERT INTO sign VALUES (%s,%s,%s)', ('null', face_name, sign_time))
        con.commit()
        con.close()
    else:
        print 'Error occurred...'


if __name__ == '__main__':
    sign()
