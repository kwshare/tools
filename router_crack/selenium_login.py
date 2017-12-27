#!/usr/bin/python
# coding:utf-8

# tools - selenium_login.py
# 2017/12/27 9:20
# 

__author__ = 'Benny <benny@bennythink.com>'

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://192.168.1.1')
driver.find_element_by_xpath('//*[@id="lgPwd"]').send_keys('123456')
driver.find_element_by_xpath('//*[@id="loginSub"]').click()
