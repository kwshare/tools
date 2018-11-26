# coding: utf-8
# practice - test.py
# 2018/11/26


import pymysql

from perforamce import exe_time

con = pymysql.connect(host='pi.lan', user='root', password='root',
                      db='ten', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
cur = con.cursor()

SIZE = 1000
single = (1, 2, 3, 4)
data = [single for i in range(SIZE)]

sql = 'INSERT INTO simple VALUES (%s,%s,%s,%s)'


@exe_time
def execute(value):
    for v in value:
        cur.execute(sql, v)
    con.commit()


@exe_time
def exetutemany(value):
    cur.executemany(sql, value)
    con.commit()


if __name__ == '__main__':
    #execute(data)
    exetutemany(data)

    con.close()
