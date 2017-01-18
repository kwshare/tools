#!/bin/bash
#压缩、删除web服务器日志
#建议配合cron
tar -jcvf /home/logs.bz2 /home/wwwlogs
rm /home/wwwlogs/*
service nginx restart
echo "At time: `date` : All logs were compressed and deleted. ">> /home/wwwlogs/compress.log
