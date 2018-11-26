# coding: utf-8
# practice - perforamce.py
# 2018/11/26 


import time


def exe_time(fun):
    def wrapper(*args, **kwargs):
        t = time.time()
        res = fun(*args, **kwargs)
        print(f'{fun.__name__}: {time.time() - t}')
        return res

    return wrapper
