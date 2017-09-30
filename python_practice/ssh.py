#!/usr/bin/python
# coding:utf-8

import paramiko


def traditional():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(hostname='192.168.56.101', username='root', password='96')

    stdin, stdout, stderr = ssh.exec_command('ls')
    print stdout.read()
    ssh.close()


def transport():
    # 复用：paramiko.SFTPClient.from_transport(ssh_client.get_transport())
    trans = paramiko.Transport(('192.168.56.101', 22))
    trans.connect(username='root', password='926')
    ssh = paramiko.SSHClient()
    ssh._transport = trans
    stdin, stdout, stderr = ssh.exec_command('df -h')
    print stdout.read()
    ssh.close()


def key1():
    ssh_client = paramiko.SSHClient()
    ssh_client.connect(hostname='192.168.56.101', username='root', password='946', key_filename='')
    ssh_client.close()


def key2():
    key = paramiko.RSAKey.from_private_key_file('id_rsa')
    ssh_client = paramiko.SSHClient()
    ssh_client.connect(hostname='192.168.56.101', username='root', password='26', pkey=key)
    ssh_client.close()


def sftp():
    trans = paramiko.Transport(('192.168.56.101', 22))
    trans.connect(username='root', password='26')
    ftp = paramiko.SFTPClient.from_transport(trans)
    # upload
    ftp.put('regex.py', '/root/regex.py')
    # download
    ftp.get('/root/regex.py', 'regex.py')
    ftp.close()


if __name__ == '__main__':
    sftp()
