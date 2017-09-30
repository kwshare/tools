#!/usr/bin/python
# coding:utf-8

# delete the oldest snapshot
# and create a new one

import pycurl
import certifi
import logging
import StringIO
import json
import sys

API_KEY = 'Your key'
SERVER_ID = 'Your server ID'
BASE = 'https://api.vultr.com/v1/'
result = StringIO.StringIO()

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
    c.setopt(pycurl.WRITEFUNCTION, result.write)
    if data:
        c.setopt(pycurl.URL, BASE + url + '?' + data)
    else:
        c.setopt(pycurl.URL, BASE + url)
    if api:
        c.setopt(pycurl.HTTPHEADER, ['API-Key:' + API_KEY])
    c.perform()
    if c.getinfo(pycurl.HTTP_CODE) != 200:
        print
        logging.error('Request failed')
        sys.exit(result.getvalue())


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
    c.setopt(pycurl.WRITEFUNCTION, result.write)

    if api:
        c.setopt(pycurl.HTTPHEADER, ['API-Key:' + API_KEY])
    if data:
        c.setopt(pycurl.POSTFIELDS, data)

    c.perform()
    if c.getinfo(pycurl.HTTP_CODE) != 200:
        print
        logging.error('Request failed')
        sys.exit(result.getvalue())


def destroy(snap_id):
    post('snapshot/destroy', True, 'SNAPSHOTID=' + snap_id)


def create(server_id):
    post('snapshot/create', True, 'SUBID=' + server_id)


if __name__ == '__main__':
    get('snapshot/list', True)
    snapshot_id = json.loads(result.getvalue())
    snapshot_id = snapshot_id.get(snapshot_id.keys()[-1]).get('SNAPSHOTID')
    destroy(snapshot_id)
    print 'destroyed... '
    create(SERVER_ID)
    print 'created... ', result.getvalue()
