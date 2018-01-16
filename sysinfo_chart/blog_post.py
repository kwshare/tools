#!/usr/bin/python
# coding:utf-8

# tools - blog_post.py
# 2018/1/16 9:47
# 

__author__ = 'Benny <benny@bennythink.com>'

import plotly
import plotly.graph_objs as go
import mysql.connector
import time
from datetime import datetime


def draw(x, y):
    data = [go.Bar(
        x=x,
        y=y
    )]
    layout = go.Layout(
        title='Blog Post Report from %s to %s' % (x[0], x[-1]),
    )

    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, data, filename='blog_post.html')


def analysis():
    con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='wp')
    cur = con.cursor()
    cmd = "SELECT post_date FROM wp_posts WHERE post_type='post' AND post_status='publish'"
    cur.execute(cmd)
    data = cur.fetchall()
    return data


if __name__ == '__main__':
    x_line = []
    y_line = []
    for i in analysis():
        x_line.append(datetime.strftime(i[0], "%Y-%m"))

    for i in x_line:
        y_line.append(x_line.count(i))

    draw(x_line, y_line)
