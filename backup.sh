#!/bin/bash
#用于备份数据库、备份网站文件并上传至七牛
#需要qshell的配合
#建议配合cron
mysqldump -u root -p wordpress --password=yourpass > /home/wwwroot/www.bennythink.com/phpmyadmin/upload/`date +%Y%m%d`.sql
tar -jcpf /home/wwwbackup/`date +%Y%m%d`.tar.bz2 /home/wwwroot/ >/dev/null 2>&1
#using qshell
rm -r /root/.qshell
qshell qupload /home/qiniu/backup.json >>/home/wwwlogs/backup.log
echo 'upload succeed'>>/home/wwwlogs/backup.log
#or this
#/home/qiniu/qrsync /home/qiniu/backup2.json

rm /home/wwwroot/www.bennythink.com/phpmyadmin/upload/*
rm /home/wwwbackup/*

echo end of backup at `date` >>/home/wwwlogs/backup.log
echo -------------------------- >>/home/wwwlogs/backup.log

