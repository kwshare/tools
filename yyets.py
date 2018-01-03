#!/usr/bin/python
# coding:utf-8

# ExpressBot - yyets.py
# 2018/1/3 11:01
# YYeTs API
# Python 2 only

__author__ = 'Benny <benny@bennythink.com>'

import requests


def show_resource(resource_id):
    """

    :param resource_id:
    :return: ed2k, magnet, baidu
    """
    url = 'http://pc.zmzapi.com/index.php?g=api/pv2&m=index&a=resource&accesskey=519f9cab85c8059d17544947k361a827&id='
    r = requests.get(url + resource_id)
    return r.json()


def search_resource(name):
    """

    :param name: name
    :return: the whole json
    """
    url = 'http://pc.zmzapi.com/index.php?g=api/pv2&m=index&a=search&accesskey=519f9cab85c8059d17544947k361a827&limit=200&k='
    r = requests.get(url + name)
    return r.json()


def breaker(user_msg):
    """
    :param user_msg: user message
    :return: episode name
    """
    return user_msg[6:].lstrip(' ').rstrip(' ')


def process(resource_name):
    """

    :param resource_name: pure episode name
    :return:
    """
    # TODO: access key problem
    name = breaker(resource_name)
    search_result = search_resource(name)

    # get the real resource id
    choice = 0
    s = search_result.get('data')
    if s is None:
        return '没有对应的资源'
    if len(s) > 1:
        print('choose name')
        for key in range(len(s)):
            print('%d. %s %s' % (key, s[key].get('channel'), s[key].get('title')))
        choice = raw_input('你的选择\n>')

    try:
        choice = int(choice)
    except ValueError as e:
        return e
    if choice == '' or choice > len(s):
        return '输入错误'

    resource_id = s[choice].get('id')
    download_link = show_resource(resource_id)
    if download_link.get('status') != 1:
        return '资源关闭，AccessKey的原因？'

    s = download_link.get('data').get('list')
    # try seasons
    season_length = int(s[0].get('season'))

    if season_length == 101:
        print('单剧')
        dl = s[0]
    else:
        choice = raw_input('choice season\n')
        try:
            choice = int(choice)
        except ValueError:
            return '输入错误'

        if choice > season_length or choice == '':
            return '输入错误'
        dl = s[season_length - choice]

    # choose episode
    # 0 - all
    # 3 - episode 3
    # 1,5,6,7 episode 1567
    episode_length = int(dl.get('episodes')[0].get('episode'))
    #    print episode_length
    choice = raw_input('choose episode\n')

    all_address = ''
    if ',' in choice:
        for item in choice.split(','):
            all_address = all_address + get_link(dl.get('episodes')[episode_length - int(item)])
    else:
        try:
            choice = int(choice)
        except ValueError:
            return '输入错误'

        if choice > episode_length or choice == '':
            return '输入错误'
        elif choice == 0:
            for i in range(episode_length):
                c = i + 1
                all_address = all_address + get_link(dl.get('episodes')[episode_length - c])
        else:
            all_address = all_address + get_link(dl.get('episodes')[episode_length - int(choice)])

    return all_address


def get_link(dl_link):
    # HR-HDTV or MP4 or APP
    dl_hr_mp4 = dl_link.get('files').get('HR-HDTV') or dl_link.get('files').get('MP4')
    dl_app = dl_link.get('files').get('APP')
    add = ''
    for key in dl_app:
        if key.get('way') == '104':
            add = add + u'B站：' + key.get('address') + '\n'
        elif key.get('way') == '103':
            add = add + u'A站：' + key.get('address') + '\n'
        elif key.get('way') == '115':
            add = add + u'微云：' + key.get('address') + '\n'

    for key in dl_hr_mp4:
        if key.get('way') == '1':
            add = add + u'电驴ed2k：' + key.get('address') + '\n'
        elif key.get('way') == '2':
            add = add + u'磁力链：' + key.get('address') + '\n'
    return add


if __name__ == '__main__':
    print(process('/yyets 神盾局'))
