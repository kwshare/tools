#!/usr/bin/python
# coding:utf-8

import time


# --exeTime
def exeTime(func):
    def newFunc(*args, **kwargs):
        t0 = time.time()
        print "@%s, {%s} start" % (time.strftime("%X", time.localtime()), func.__name__)
        back = func(*args, **kwargs)
        print "@%s, {%s} end" % (time.strftime("%X", time.localtime()), func.__name__)
        print "@%.3fs taken for {%s}" % (time.time() - t0, func.__name__)
        return back

    return newFunc


@exeTime
def foo():
    time.sleep(2)


if __name__ == "__main__":
    foo()
