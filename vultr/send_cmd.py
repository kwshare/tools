#!/usr/bin/python
# coding:utf-8

# request

import pycurl
import certifi
import config
import logging

BASE = 'https://api.vultr.com/v1/'

c = pycurl.Curl()
c.setopt(pycurl.CAINFO, certifi.where())


def get(url, api=False, data=False):
    """
    send get request
    :param url: action, i.e. server/restart
    :param api: Authentication require, boolean
    :param data: get params
    :return: None
    """
    if data:
        c.setopt(pycurl.URL, BASE + url + '?' + data)
    else:
        c.setopt(pycurl.URL, BASE + url)
    if api:
        c.setopt(pycurl.HTTPHEADER, ['API-Key:' + config.API_KEY])

    c.perform()
    if c.getinfo(pycurl.HTTP_CODE) != 200:
        print
        logging.error('Request failed')


def post(url, api=False, data=False):
    """
    send post request
    :param url: action, i.e. server/restart
    :param api: Authentication require, boolean
    :param data: post header
    :return: None
    """
    c.setopt(pycurl.URL, BASE + url)
    c.setopt(pycurl.CUSTOMREQUEST, 'POST')

    if api:
        c.setopt(pycurl.HTTPHEADER, ['API-Key:' + config.API_KEY])
    if data:
        c.setopt(pycurl.POSTFIELDS, data)

    c.perform()
    if c.getinfo(pycurl.HTTP_CODE) != 200:
        print
        logging.error('Request failed')
