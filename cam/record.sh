#!/bin/bash
export PATH=/root/.autojump/bin:/root/.autojump/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games

now=$(date +"%Y-%m-%d_%H-%M")
RTSP="rtsp://192.168.7.234:554/user=admin&password=DontTouchMe&channel=Channel&stream=Stream.sdp?real_stream"
ffmpeg  -rtsp_transport tcp  -i $RTSP -vcodec  copy -r 1 -t 890  -y /video/${now}.mp4
