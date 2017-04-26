#!/usr/bin/python
# coding:utf-8

import requests
from bs4 import BeautifulSoup
import re
import os


def geturl(url):
    """
    function:get url of each post in the first page, 7 now.
    return: dict or list
    Q: just an url or with tile?
    """
    customheader={'User-Agent':'Mozilla/5.0'}
    response = requests.get(url,headers=customheader)
    soup1 = BeautifulSoup(response.text, 'html.parser')
    titleAndUrl=soup1.find_all("article")
    urlList=[]
    for x in range(7):
        #titleList.append( titleAndUrl[x].h3.text)
        urlList.append(titleAndUrl[x].h3.a.get('href'))
    return urlList


def download(url):
    customheader = {'User-Agent': 'Mozilla/5.0'}
    for x in range(7):
        response = requests.get(url[x], headers=customheader)
        fileName=re.search(r'[0-9]{4}/.*.html',url[x]).group().replace('/','-')
        soup2 = BeautifulSoup(response.text, 'html.parser')
        f=open('blog/'+fileName,'w')
        f.write(soup2.select('div')[23].text.encode('utf-8'))
    f.close()
    os.system('''cd blog && git add .&&git commit -m "`date`"''')


def sendmail():
    pass


def check():
    pass


# main
if __name__=='__main__':
    print 'running program'
    url=geturl('https://www.mingyueli.com')
    download(url)

