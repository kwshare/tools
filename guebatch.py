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
    total = len(task_list)
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
            progress_bar(round((total - len(task_list)) * 1.0 / total * 100, 2))
        else:
            time.sleep(2)


def progress_bar(percentage):
    complete = '■'
    uncomplete = '□'
    count = int(percentage / 5)
    print complete * count + uncomplete * (20 - count) + '   %s %%' % percentage


def final_check():
    # Fuzzy...
    total = len([pro.name() for pro in psutil.process_iter() if 'guetzli' in pro.name()]) + 1
    count = total - 1

    while True:
        current_jobs = len([pro.name() for pro in psutil.process_iter() if 'guetzli' in pro.name()])
        if current_jobs == 0:
            print '-- Job completed. --'
            break
        else:
            if current_jobs != total:
                print '-- Please wait for final processing... --'
                progress_bar(round((count - current_jobs) * 1.0 / count * 100, 2))
                total = total - 1
        time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    op(get_file())
    final_check()
    print '------------------------------------------'
    print ' Total Elapsed: %s seconds' % str(round(time.time() - start, 2))
    print '------------------------------------------'
