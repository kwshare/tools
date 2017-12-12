#!/usr/bin/python
# coding:utf-8

# python_practice - phantom.py
# 2017/11/18 10:25
# 

__author__ = 'Benny <benny@bennythink.com>'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.PhantomJS()

for i in range(5):
    driver.get('https://www.bennythink.com')
    driver.page_source()
    #driver.find_element_by_xpath('//*[@id="Addlike"]').click()
    driver.find_element_by_xpath('//*[@id="menu-item-1005"]/a').click()
    # this doesn't work..?
    #driver.delete_all_cookies()
    #driver.page_source()
driver.quit()

