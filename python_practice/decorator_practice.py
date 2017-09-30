#!/usr/bin/python
# coding:utf-8

# decorator practice
# timing
# logging
# 装饰器就是外部函数
# 传进来一个参数（这个参数可以是一个函数）
# 内部函数里面调用这个参数（函数）然后在外层返回这个内部函数的函数名。

import time


def print_log(fun):
    def wrapper(*args, **kwargs):
        print 'log starts', args, kwargs
        fun(*args, **kwargs)
        print 'log ends'

    return wrapper


def exe_time(fun):
    def wrapper(*args, **kwargs):
        t = time.time()
        res = fun(*args, **kwargs)
        print time.time() - t
        return res

    return wrapper


@print_log
def log_test():
    print 'function of log'


@exe_time
def timing_test():
    print 'function of timing'
    for x in xrange(101000007):
        pass


if __name__ == '__main__':
    log_test()
    # timing_test()
