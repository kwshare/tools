# coding:utf-8

from multiprocessing import Process
import os


def run_process(name):
    print 'run child %s %s' % (name, os.getpid())


if __name__ == '__main__':
    print 'run parent %s' % os.getpid()

    p = Process(target=run_process, args=('son',))  # tuple
    p.start()
    p.join()  # run child immediately
    print 'end'
