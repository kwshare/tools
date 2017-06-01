#!/usr/bin/python
# coding:utf-8

import os
import psutil
import time

# FIX: escape character \
taskList = [item for item in os.listdir('./') if 'jpg' in item]
processCount = psutil.cpu_count(logical=True)
parallelJobs = min(len(taskList), processCount)
# print parallelJobs

while True:
    currentJobs = len([pro.name() for pro in psutil.process_iter() if 'guetzli' in pro.name()])
    if len(taskList) == 0:
        break
    elif currentJobs < parallelJobs:
        os.system('guetzli ' + taskList[0] + ' ' + taskList[0] + '&')
        print 'add **' + taskList[0] + '** to job list'
        taskList.pop(0)
    time.sleep(1)
print 'Mission accomplished...please just wait for guetzli process to finish its job...'
