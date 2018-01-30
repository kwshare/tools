#!/usr/bin/python
# coding:utf-8

# re

import re

regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~!@#$%^&*])[\S]{8,16}$')

s = '111csdaC@11'

print regex.findall(s)
