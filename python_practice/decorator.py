#!/usr/bin/python
# coding:utf-8

import time


def exe_time(fun):
    def wra(*args, **kwargs):
        t0 = time.time()
        back = fun(*args, **kwargs)
        print time.time() - t0
        return back

    return wra


@exe_time
def foo():
    time.sleep(2)

# decorator is a two-level function
#
# 装饰器就是外部函数
# 传进来一个参数（这个参数可以是一个函数）
# 内部函数里面调用这个参数（函数）然后在外层返回这个内部函数的函数名。


def dec(fun):
    def new(*args, **kwargs):
        print 'decorator starts'
        # execute a function
        # fun() or return fun(*args, **kwargs)
        # res=fun(*args, **kwargs);return res # timing
        fun()
        print 'decorator ends'

    # return inner function
    return new


@dec
def test1():
    print '2'


if __name__ == '__main__':
    test1()
