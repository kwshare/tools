#!/usr/bin/python
# coding:utf-8

# python_practice - phantom.py
# 2017/11/18 10:25
# 

__author__ = 'Benny <benny@bennythink.com>'

from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('https://www.bennythink.com/ubuntumate-raspberry2.html')
driver.find_element_by_xpath('//*[@id="Addlike"]').click()
# this doesn't work..?
driver.delete_all_cookies()
driver.quit()

