#!/bin/bash

#生成SSH欢迎信息，仅适用于Ubuntu
#如果遇到path问题，取消下面一行的注释
#export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
#因为要写入/etc，所以检查root
if [ $(id -u) != "0" ]; then
    echo "Error: You must be root to run this script."
    exit 1
fi

echo '请输入可以生成标准输出都命令，比如cowsay hi'
read command
$command>temp.sh

#转义、echo
sed 's/\\/\\\\/g' temp.sh>welcome.sh
sed 's/"/\\"/g' welcome.sh>temp.sh
sed '/./{s/^/echo "&/;s/$/&"/}' temp.sh > welcome.sh

#拷贝到/etc
cp welcome.sh /etc/update-motd.d/welcome.sh
#mv /etc/update-motd.d/10-help-text /etc/update-motd.d/10-help-text.bak
echo "#!/bin/sh">/etc/update-motd.d/10-help-text
echo "sh /etc/update-motd.d/welcome.sh">>/etc/update-motd.d/10-help-text

#测试效果
sudo run-parts /etc/update-motd.d
rm temp.sh welcome.sh

