#!/bin/bash
echo ***********`date`  backup is staring************ >>/home/wwwlogs/backup.log
#Benny
mysqldump -u root -p wordpress --password=Y311 > /home/wwwroot/www.bennythink.com/db_backup/`date +%Y%m%d`.sql
tar -jcpf /home/wwwbackup/`date +%Y%m%d`_benny.tar.bz2 /home/wwwroot/www.bennythink.com/ --exclude=/home/wwwroot/www.bennythink.com/phpmyadmin >/dev/null 2>&1
#love
mysqldump -u root -p hi --password=Y311 > /home/wwwroot/www.tougetu.com/db_backup/`date +%Y%m%d`.sql
tar -jcpf /home/wwwbackup/`date +%Y%m%d`_moon.tar.bz2 /home/wwwroot/www.tougetu.com/ >/dev/null 2>&1

#using qshell
rm -r /root/.qshell
qshell qupload /home/qiniu/backup.json >>/home/wwwlogs/backup.log
echo 'qiniu upload succeed'>>/home/wwwlogs/backup.log
#using cos
cd /home/cos && bash start_cos_sync.sh >>/home/wwwlogs/backup.log
echo 'cos upload succeed'>>/home/wwwlogs/backup.log
#using Google Drive
grive -up /home/wwwbackup >>/home/wwwlogs/backup.log
#delete files
rm /home/wwwroot/www.tougetu.com/db_backup/*
rm /home/wwwroot/www.bennythink.com/db_backup/*
rm /home/wwwbackup/*

echo End of backup at `date` >>/home/wwwlogs/backup.log
echo '*****************************************' >>/home/wwwlogs/backup.log

