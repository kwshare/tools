#!/usr/bin/python
# coding:utf-8

# tools - nova.py
# 2018/5/31 21:08
# 

__author__ = 'Benny <benny@bennythink.com>'

import plotly
import plotly.graph_objs as go
import json


def draw(x, y, fn):
    # go.Bar, go.Scatter
    data = [go.Scatter(
        x=x,
        y=y
    )]
    layout = go.Layout(title='Status Report')

    fig = go.Figure(data=data, layout=layout)
    # <script src="https://cdn.bootcss.com/plotly.js/1.38.0/plotly-basic.js"></script>
    plotly.offline.plot(fig, data, include_plotlyjs=False, filename='%s.html' % fn)


def parse():
    j = json.load(open('status.json'))
    ":type:dict"

    x = []
    y = []
    for date in j:
        x.append(date)
        y.append(j.get(date, {}).get('count', 0))
    return x, y


if __name__ == '__main__':
    x, y = parse()
    draw(x, y, 'What')
