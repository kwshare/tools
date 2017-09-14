#!/usr/bin/python
# coding:utf-8

# Collect system information: CPU, RAM
# and map it into a chart.
# This code sucks.

import psutil
import time
import chart


def show_stat():
    CPU = 'CPU: ' + str(psutil.cpu_percent(1, False)) + '%'
    mem = 'RAM:' + str(psutil.virtual_memory().used / 1024 / 1024) + ' MiB ' + \
          str(psutil.virtual_memory().percent) + '%',

    network = 'Download:' + str(psutil.net_io_counters(False, True).bytes_recv / 1024 / 1024) + \
              ' MiB, Upload:' + str(psutil.net_io_counters(False, True).bytes_sent / 1024 / 1024) + ' Mib'
    disk_read = 'Disk Read:' + str(psutil.disk_io_counters(False, True).read_count / 1024) + \
                'Kib/s Disk write:' + str(psutil.disk_io_counters(False, True).write_count / 1024) + ' KiB/s'
    sysinfo = [CPU, mem, network, disk_read]
    return sysinfo


sys_x = []
sys_y = [[], []]
x = []
y1 = y2 = []


def sys_stat():
    CPU = psutil.cpu_percent(1, False)
    mem = psutil.virtual_memory().percent

    t = time.strftime('%H:%M:%S', time.localtime())
    #
    y1.append(CPU)
    y2.append(mem)
    x.append(t)
    sys_x.append(x)
    sys_y[0].append(CPU)
    sys_y[1].append(mem)


    return sys_x, sys_y


def main():
    count = 0
    while True:
        test = sys_stat()
        time.sleep(2)
        count = count + 1
        if count == 60:
            break
    x, y = test

    chart.draw_chart(x, y)


if __name__ == '__main__':
    main()
