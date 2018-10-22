#!/usr/bin/env bash
echo "----------Backup log on `date`----------">>/home/wwwlogs/backup.log

# create tar
echo "* `date` Creating tar...">>/home/wwwlogs/backup.log
mysqldump -u root -p wordpress --password=pass \
--ignore-table=wordpress.wp_slim_stats_archive --ignore-table=wordpress.wp_slim_stats\
> /home/wwwroot/www.bennythink.com/db_backup/`date +%Y%m%d`.sql
tar -jcpf /home/wwwbackup/`date +%Y%m%d`.tar.bz2 /home/wwwroot/www.bennythink.com/ \
--exclude=/home/wwwroot/www.bennythink.com/phpmyadmin >/dev/null 2>&1

# dd if=/dev/zero of=/home/wwwbackup/test bs=1M count=32

# qiniu
echo "* `date` Uploading to qiniu...">>/home/wwwlogs/backup.log
# blame me(?_?)
rm -r /root/.qshell/qupload/
/opt/bin/qshell qupload2 --src-dir=/home/wwwbackup/ -bucket=backup 
echo "* `date` Upload complete.">>/home/wwwlogs/backup.log

# qcloud
echo "* `date` Uploading to Tencent...">>/home/wwwlogs/backup.log
/usr/local/bin/coscmd upload /home/wwwbackup/*  / 
echo "* `date` Upload complete.">>/home/wwwlogs/backup.log

# Google Drive
echo "* `date` Uploading to Google Drive...">>/home/wwwlogs/backup.log
/opt/bin/gdrive upload /home/wwwbackup/`date +%Y%m%d`.tar.bz2 
echo "* `date` Upload complete.">>/home/wwwlogs/backup.log

# delete files
echo "* `date` Deleting files...">>/home/wwwlogs/backup.log
rm -rf /home/wwwbackup/*
rm -rf /home/wwwroot/www.bennythink.com/db_backup/*

echo "----------Backup complete on `date`----------">>/home/wwwlogs/backup.log
echo >>/home/wwwlogs/backup.log
