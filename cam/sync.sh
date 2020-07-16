#!/bin/bash

# sync and clean old data

export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games

proxychains4 -q rsync -avz --delete /video/ user@host:/video/

cmd="find /video -mindepth 1 -mtime +30 -delete"

${cmd}
proxychains4 -q ssh user@host ${cmd}
