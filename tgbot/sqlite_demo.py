#!/usr/bin/python
# coding:utf-8

# tools - sqlite_demo.py
# 2018/2/1 12:05
# 

__author__ = 'Benny <benny@bennythink.com>'

import sqlite3

# 使用内存型数据库，实际应用时应该指定文件路径
con = sqlite3.connect(':memory:')
# 创建游标
cur = con.cursor()
create_table = '''CREATE TABLE IF NOT EXISTS job
(
    date DATETIME,
    done TINYINT
)'''
# 执行查询
cur.execute(create_table)
# 提交
con.commit()
# 关闭连接
con.close()
