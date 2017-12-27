#!/usr/bin/python
# coding:utf-8

# tools - convert.py
# 2017/12/22 9:50
# 

__author__ = 'Benny <benny@bennythink.com>'



from pydub import AudioSegment
song = AudioSegment.from_ogg('test.ogg')
song.export('1.wav','wav','pcm','16k')