#coding:utf-8

import requests
from bs4 import BeautifulSoup
import pdfkit
import os

pseudoAgent={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.18.2) AppleWebKit/537.24.12 (KHTML, like Gecko) Chrome/57.0.2937.20 Safari/537.24.12 OPR/46.0.2112.154'}
response = requests.get('https://www.shemissed.me/',headers=pseudoAgent)
#response.encoding='uft-8'
soup = BeautifulSoup(response.text,'html.parser')
dic={}
for link in soup.find_all('article'):
    dic[link.header.h2.a.get('title')]=link.header.h2.a.get('href')
i=0
for title,url in dic.items():
    print title,url
    i=i+1
    s=str(i)+'.pdf'
    pdfkit.from_url(url,s)
    os.rename(s,title+'.pdf')
    print '重命名完成'

