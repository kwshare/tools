#!/bin/bash
#用于备份数据库、备份网站文件并上传至七牛
#需要其他工具的配合
#建议配合cron
echo ***********`date`  backup is staring************ >>/home/wwwlogs/backup.log

mysqldump -u root -p wordpress --password=yourpass > /home/wwwroot/www.bennythink.com/phpmyadmin/upload/`date +%Y%m%d`.sql
tar -jcpf /home/wwwbackup/`date +%Y%m%d`.tar.bz2 /home/wwwroot/ >/dev/null 2>&1
#using qshell
rm -r /home/.qshell
qshell qupload /home/qiniu/backup.json >>/home/wwwlogs/backup.log
echo 'qiniu upload succeed'>>/home/wwwlogs/backup.log
#using cos
cd /home/cos && bash start_cos_sync.sh >>/home/wwwlogs/backup.log
echo 'cos upload succeed'>>/home/wwwlogs/backup.log
#using Google Drive
grive -up /home/wwwbackup >>/home/wwwlogs/backup.log
echo 'Google Drive upload succeed'>>/home/wwwlogs/backup.log
#delete files
rm /home/wwwroot/www.bennythink.com/phpmyadmin/upload/*
rm /home/wwwbackup/*

echo End of backup at `date` >>/home/wwwlogs/backup.log
echo '*****************************************' >>/home/wwwlogs/backup.log

