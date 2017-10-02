#!/usr/bin/python
# coding:utf-8

# 4 in one snapshot

import paramiko


def ssh(host=None, pwd=None, cmd=None):
    connector = paramiko.SSHClient()
    connector.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    connector.connect(hostname=host, username='root', password=pwd)
    stdin, stdout, err = connector.exec_command(cmd)
    print ' -- ', host, ' -- \n', stdout.read()
    connector.close()


ssh('1.com', '476f44902', 'java -jar /home/qcloud.jar')
ssh('2.com', '9991ec5a1c72', 'java -jar /home/encore.jar')
ssh('3.com', 'b7bc6f53100e0', 'java -jar /home/big.jar')
ssh('4.com', '6416f902', 'python /home/one_key.py')
