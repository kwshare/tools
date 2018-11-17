#!/usr/bin/python
# coding: utf-8

# untitled - ok.py
# 2018/7/8 12:52


__author__ = "Benny <benny@bennythink.com>"

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.HIGH)


