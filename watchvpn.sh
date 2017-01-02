#!/bin/bash
#15m average load
aload=0
aload=`uptime | awk '{print $10}'`
echo 15m load is $aload

if [ `expr 1 \> $aload` -eq 0 ]
then
	#do something here..
	echo `date` high load,restarting now >> /home/vpnload.log
	/root/vpnserver/vpnserver start >> /home/vpnload.log
else
	echo `date` 15m average load is $aload, keep it up
fi
