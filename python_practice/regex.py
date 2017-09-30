#!/usr/bin/python
# coding:utf-8

# re

import re


p = re.compile(r'\d+')
print p.findall('one1two2three3four4')

pattern = re.compile(r'world')

# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
# 这个例子中使用match()无法成功匹配
match = pattern.search('hello world!')

print match.group()