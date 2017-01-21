#!/bin/bash
#旧：1.log	新：2.log
#判断文件是否存在
if [ -e "1.log" ]
then
	echo '1.log exists'
else
	curl https://www.mingyueli.com >1.log
fi

#获取新内容
curl http://www.mingyueli.com >2.log
diff 1.log 2.log
if [ $? -eq 0 ]
then
	echo "At `date` Everything stays the same"
else
	echo "At `date` It updated">> /root/yue.log
	curl -d "diff=`diff 1.log 2.log |base64`" https://shemissed.me/mail.php
	curl https://www.mingyueli.com >1.log
	curl https://www.mingyueli.com >2.log
	
fi
