#!/usr/bin/python
# coding:utf-8

import os
import psutil
import time
import subprocess


def get_file():
    file_list = []
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if ('jpg' in name) or ('jpeg' in name) or ('png' in name):
                file_list.append(os.path.join(root, name))

    return file_list


def op(task_list):
    parallel_jobs = min(len(task_list), psutil.cpu_count(logical=True))
    # file path in task_list:
    while True:
        current_jobs = len([pro.name() for pro in psutil.process_iter() if 'guetzli' in pro.name()])
        if not task_list:
            break
        elif current_jobs < parallel_jobs:
            cmd = 'guetzli "%s" "%s"' % (task_list[0], task_list[0])
            if os.name == 'posix':
                os.system(cmd + '&')
            else:
                subprocess.Popen(cmd)
            print '** guetzli is processing %s **' % task_list[0]
            task_list.pop(0)
        else:
            time.sleep(2)


def final_check():
    while True:
        current_jobs = len([pro.name() for pro in psutil.process_iter() if 'guetzli' in pro.name()])
        if current_jobs == 0:
            print '** Job completed. **'
            break
        else:
            print '** Please wait for final processing... **'
        time.sleep(5)


if __name__ == '__main__':
    start = time.time()
    op(get_file())
    final_check()
    print '------------------------------------------'
    print ' Total Elapsed: %s seconds' % str(round(time.time() - start, 2))
    print '------------------------------------------'
