#!/bin/bash
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games

today=$(date +"%Y-%m-%d")
RTSP="rtsp://127.0.0.1:554/user=user&password=password&channel=Channel&stream=Stream.sdp?real_stream"

ffmpeg  -rtsp_transport tcp  -i $RTSP -vcodec  copy -r 1 -t 43200  -y /video/${today}.mp4
