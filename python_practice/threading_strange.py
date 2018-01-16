#!/usr/bin/python
# coding:utf-8

# tools - threading_strange.py
# 2018/1/7 19:36
# database.json
# link, title, error_count, subscriber
# /rss xxx.com/feed
# /unrss xxx.com/feed
# /quickunrss msg
# /export

__author__ = 'Benny <benny@bennythink.com>'

import threading
import time
import random


def fun():
    print 'running %s' % threading.current_thread()
    time.sleep(random.random())


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=fun)
        t.start()

    # while threading.activeCount() > 1:
    #     pass
    print 'main ends here'

