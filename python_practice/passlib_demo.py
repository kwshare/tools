#!/usr/bin/python
# coding:utf-8

# python_practice - test.py
# 2017/11/20 15:38
# 

__author__ = 'Benny <benny@bennythink.com>'

from passlib.hash import pbkdf2_sha256


hash = pbkdf2_sha256.hash("password")

print pbkdf2_sha256.verify("password", hash)
