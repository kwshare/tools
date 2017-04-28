#!/usr/bin/python
# coding:utf-8

import os
import requests
from bs4 import BeautifulSoup
import re
import yagmail


def geturl(url):
    """
    function:get url of each post in the first page, 7 now.
    return: just an url, type list
    """
    customheader = {'User-Agent': 'Mozilla/5.0 Sogou web spider'}
    response = requests.get(url, headers=customheader)
    soup1 = BeautifulSoup(response.text, 'html.parser')
    titleAndUrl = soup1.find_all("article")
    url_list = []
    for x in range(7):
        # titleList.append( titleAndUrl[x].h3.text)
        url_list.append(titleAndUrl[x].h3.a.get('href'))
    return url_list, response.text


def download(url):
    customheader = {'User-Agent': 'Mozilla/5.0 Sogou web spider'}
    for x in range(7):
        response = requests.get(url[x], headers=customheader)
        fileName = re.search(r'[0-9]{4}/.*.html', url[x]).group().replace('/', '-')
        soup2 = BeautifulSoup(response.text, 'html.parser')
        f = open('blog/' + fileName, 'w')
        content = ''
        for string in soup2.find('div', class_='article-content clearfix').stripped_strings:
            content = content + string + '\n'
        f.write(content.encode('utf-8'))
        # old way, in one line
        # f.write(soup2.select('div')[23].text.encode('utf-8'))
    f.close()
    return os.system('''cd blog && git add .&&git commit -m "`date`"''')


def sendmail(html):
    yag = yagmail.SMTP \
        (user='no-reply@example.com', password='pass', host='smtp.exmail.qq.com', port='25')
    yag.send(to="someone@qq.com", subject="博客已更新", contents=['主页预览：\n', html.encode('utf-8')])


def main():
    print 'running program'
    url, html = geturl('https://www.mingyueli.com')
    status = download(url)

    if status == 0:
        print '更新了'
        sendmail(html)
    else:
        print '保持原样'


# main
if __name__ == '__main__':
    main()
