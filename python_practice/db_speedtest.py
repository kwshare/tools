# coding:utf-8

import mysql.connector
import random
import time
from pymongo import MongoClient

IP_NUM = 10000
column_list = []

con = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='speedtest')

mongo_client = MongoClient(host='127.0.0.1', username='root', password='cisco123',
                           authMechanism='SCRAM-SHA-1')


def generate_data():
    for i in xrange(IP_NUM):
        ids = random.randint(1, 255)
        t = int(time.time())
        ip_part1 = str(random.randint(0, 255))
        ip_part2 = str(random.randint(0, 255))
        ip_part3 = str(random.randint(0, 255))
        ip_part4 = str(random.randint(0, 255))
        ip = '%s.%s.%s.%s' % (ip_part1, ip_part2, ip_part3, ip_part4)
        column_list.append([ids, t, ip])


def mysql_write():
    cur = con.cursor()
    cmd = 'INSERT INTO test VALUES (%s,%s,%s)'
    cur.executemany(cmd, column_list)
    con.commit()


def mongo_write():
    # 列表里是字典

    db = mongo_client['speedtest']
    col = db['test']

    insert_list = []
    for i in xrange(len(column_list)):
        c = {'id': column_list[i][0], 'time': column_list[i][1], 'ip': column_list[i][2]}
        insert_list.append(c)

    col.insert_many(insert_list)


def main():
    generate_data()
    mysql_write()
    mongo_write()


if __name__ == '__main__':
    main()
    for i in xrange(1000):
        column_list = []
        main()
        print '%s loop' % i
