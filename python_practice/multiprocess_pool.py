# coding:utf-8

from multiprocessing import Pool
import random, time, os


def long_time(name):
    start = time.time()
    print 'run child %s, %s' % (name, os.getpid()), '--', start
    time.sleep(random.random() * 3)
    end = time.time()
    print 'child %s costs %.2f seconds' % (name, end - start)


if __name__ == '__main__':
    print 'run parent %s' % os.getpid()
    p = Pool()
    for i in range(5):
        p.apply_async(long_time, (i,))
    print 'waiting for sub process'
    p.close()
    p.join()
    print 'all done.'
