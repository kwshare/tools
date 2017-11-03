#!/usr/bin/python
# coding:utf-8

# Intern-Life - mysql2es_demo.py
# 2017/10/27 12:35
# 

__author__ = 'Benny <benny@bennythink.com>'

import mysql.connector
from elasticsearch import Elasticsearch
from elasticsearch import helpers

SIZE = 100
es = Elasticsearch()


def bulk_read_write(db, tb):
    """
    read multiple lines from MySQL and insert it into ES
    :param db: database name, which will turn into index name in ES
    :param tb: table name, determine dict.
    :return: None
    """
    con = mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database=db)
    cur = con.cursor()
    # SQL Injection. but however the format %s param doesn't work. How so???
    cur.execute('SHOW  COLUMNS from %s' % tb)
    col_data = cur.fetchall()
    col_field = [i[0] for i in col_data]

    cur.execute('SELECT * FROM %s' % tb)
    while True:
        data = cur.fetchmany(SIZE)
        if data:
            bulk_dic = []
            for i in range(len(data)):
                es_dic = dict(zip(col_field, data[i]))
                es_dic.update(_index=tb, _type='hey')
                bulk_dic.append(es_dic)
            helpers.bulk(es, bulk_dic)
        else:
            break
    con.close()


if __name__ == '__main__':
    bulk_read_write('wordpress', 'wp_comments')
    # es.indices.delete('wordpress')
