#!/usr/bin/python
# coding:utf-8

# python_practice - tiny_craw.py
# 2017/11/7 11:26
# unfinished project

__author__ = 'Benny <benny@bennythink.com>'

import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://interactivepython.org/runestone/static/pythonds/'


def get_each():
    """
    get each a lable's url and title
    :return: [()] tuple inside of list
    """
    html = requests.get(BASE_URL + 'index.html')
    soup = BeautifulSoup(html.text, "html5lib")
    url_title = [(BASE_URL + i['href'], i.text) for i in soup.find_all('a', class_='reference internal')]
    return url_title


def parse_each(t):
    """
    parse each [()],get its title and content
    :param t: [()] generate by get_each()
    :return: None
    """
    for i in t:
        html = requests.get(i[0])
        soup = BeautifulSoup(html.text, "html5lib")
        # use bs4 to retreive `p` lable, maybe you need some more modifications here.
        p = soup.find_all('p')[0].text
        write_file(i[1], p)


def write_file(fn, text):
    """
    write content to file
    :param fn: filename
    :param text: content to be written
    :return: None
    """
    # windows filename restrictions.
    fn = fn.replace('?', '')
    with open('result/' + fn + '.txt', 'w')as f:
        # Python 3 may not need `encode` method
        f.write(text.encode('utf-8'))


if __name__ == '__main__':
    res = get_each()
    parse_each(res)
