一些我经常用的弱智脚本
====
没啥技术水平，只是把一些常用的脚本分享出来。
目前共有这么几个脚本
##1. backup.sh
备份网站文件并上传到七牛云
需要七牛官方qshell工具的支持，参考`upload.json`和[七牛官方文档](https://support.qiniu.com/question/198313) 
建议配合cron，`upload.json`可能需要一些更改
已经增加Google Drive、腾讯云COS支持，请查看对应的官方文档
##2. compress_log.sh
压缩日志文件，至于是啥日志文件，你说了算。
##3. relay.sh
中转文件至七牛云的一个小脚本，非常简单，需要配合qshell，并且推荐+x丢到`/bin`
##4. restart_service.sh
监测某个进程是否存在、如果不存在则将其重启<br>
目前主要用于监测MySQL，建议配合cron
##5. PHPMailer
主要用于发送邮件，已经配置好了，只需要编辑`mail.php`的配置，之后curl即可发送邮件。
##6. yue.sh
使用curl用来监测某个网站是否更新，更新则发送邮件（目前是使用上面的PHPMailer），建议配合cron
有的时候会有误报，原因可能是每次都是动态生成的吧。
##7. watchvpn.sh
本来是用来监测系统负载，高负载（大于1）则重启VPN服务器……后来发现是我太蠢了嗯。
##8. onekey-snapshot
可以给腾讯云创建一键快照的小工具，会先删除上一个快照（如果有的话），然后再创建新的。可以配合yue.sh，这样每当网站变化就可以自动快照了。需要修改源代码中`secretID`、`secretKey`、`Region`、`diskID`这四个参数然后自行编译再使用。**服务器至少要有jre、只可以对有一台服务器的用户进行快照操作**