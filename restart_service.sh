#!/bin/bash
#当发现mysql挂了之后， 重新启动mysql 
#需要配合cron
pidof mysqld >/dev/null
if [ $? -eq 0 ]
then
echo "It is running."
else
echo "At `date` MySQL Server was stopped">> /home/wwwlogs/service_log
/etc/init.d/mysql restart
fi

pidof nginx >/dev/null
if [ $? -eq 0 ]
then
echo "It is running."
else
echo "At `date` Nginx Server was stopped">> /home/wwwlogs/service_log
/etc/init.d/nginx restart
fi
