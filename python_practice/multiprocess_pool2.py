# coding:utf-8

from multiprocessing import Process, Queue
import time, random


def write(q):
    for i in range(5):
        q.put(i)
        time.sleep(random.random())


def read(q):
    while True:
        print 'get %s' % q.get(True)


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=write, args=(q,))
    p2 = Process(target=read, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.terminate()
