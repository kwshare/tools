#!/usr/bin/python
# coding:utf-8

# 4 in one snapshot

import paramiko
import threading


def ssh(host=None, pwd=None, cmd=None):
    connector = paramiko.SSHClient()
    connector.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    connector.connect(hostname=host, username='root', password=pwd)
    stdin, stdout, err = connector.exec_command(cmd)
    print ' -- ', host, ' -- \n', stdout.read()
    connector.close()


t = threading.Thread(target=ssh,
                     args=('shemissed.me', '641b44902', 'java -jar /home/qcloud.jar'))
t.start()
t = threading.Thread(target=ssh,
                     args=('mingyueli.com', '39a1c72', 'java -jar /home/encore.jar'))
t.start()
t = threading.Thread(target=ssh,
                     args=('mingyue.tech', 'b7bc0e0', 'java -jar /home/big.jar'))
t.start()
t = threading.Thread(target=ssh,
                     args=('shemissed.me', '641b44902', 'python /home/one_key.py'))
t.start()
