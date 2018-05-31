#!/usr/bin/python
# coding:utf-8

# tools - blog_post.py
# 2018/1/16 9:47
# 

__author__ = 'Benny <benny@bennythink.com>'

import plotly
import plotly.graph_objs as go
import pymysql
import time
from datetime import datetime


def draw(x, y, fn):
    data = [go.Bar(
        x=x,
        y=y
    )]
    layout = go.Layout(
        title='%s - Blog Post Report from %s to %s' % (fn, x[0], x[-1]),
    )

    fig = go.Figure(data=data, layout=layout)
    # not include js
    plotly.offline.plot(fig, data, include_plotlyjs=False, filename='%s.html' % fn)
    # add js here.
    with open('%s.html' % fn, 'r+')as f:
        f.seek(36)
        content = f.read()
        f.seek(36)
        f.write('<script src="https://cdn.bootcss.com/plotly.js/1.38.0/plotly-basic.min.js"></script>' + content)


def wp_analysis():
    con = pymysql.connect(user='root', password='root', host='127.0.0.1', database='wordpress')
    cur = con.cursor()
    cmd = "SELECT post_date FROM wp_posts WHERE post_type='post' AND post_status='publish'"
    cur.execute(cmd)
    data = cur.fetchall()
    return data


def ty_analysis():
    con = pymysql.connect(user='root', password='root', host='127.0.0.1', database='hi')
    cur = con.cursor()
    cmd = "SELECT created FROM bk_contents WHERE type = 'post' AND status = 'publish' ORDER BY created"
    cur.execute(cmd)
    data = cur.fetchall()
    return data


def wordpress():
    x_line = []
    y_line = []
    for i in wp_analysis():
        x_line.append(datetime.strftime(i[0], "%Y-%m"))

    for i in x_line:
        y_line.append(x_line.count(i))

    draw(x_line, y_line, 'WordPress')


def typecho():
    x_line = []
    y_line = []
    for s in ty_analysis():
        x_line.append(time.strftime('%Y-%m', time.localtime(s[0])))

    for i in x_line:
        y_line.append(x_line.count(i))
    draw(x_line, y_line, 'Typecho')


if __name__ == '__main__':
    wordpress()
    typecho()
