#!/usr/bin/python
# coding:utf-8

# delete the oldest snapshot
# and create a new one

import json
import requests

API_KEY = 'XMAJNQ'
BLOG_SUBID = '7145202'
SS_SUBID = '13152978'
BASE = 'https://api.vultr.com/v1/'


def _list(url):
    return requests.get(BASE + url, headers={'API-Key': API_KEY}).text


def destroy(url, snap_id):
    return requests.post(BASE + url, headers={'API-Key': API_KEY}, data={'SNAPSHOTID': snap_id}).text


def create(url, server_id, desc):
    return requests.post(BASE + url, headers={'API-Key': API_KEY}, data={'SUBID': server_id, 'description': desc}).text


def parse_snap(content, _type):
    return [key for key in content if content[key]['description'] == _type][0]


def process(name):
    snap_list = _list('snapshot/list')
    sub_id = BLOG_SUBID if name == 'blog' else SS_SUBID

    to_be_delete = parse_snap(json.loads(snap_list), name)
    print(destroy('snapshot/destroy', to_be_delete))
    print(create('snapshot/create', sub_id, name))


if __name__ == '__main__':
    process('blog')
    process('shadowsocks')
