# coding: utf-8
# scripts - yui.py
# 2019/4/28 19:31

__author__ = 'Benny <benny.think@gmail.com>'

import os
import requests

s = requests.session()


def download(url_id, folder):
    url = 'https://ii.hywly.com/a/1/%s/{name}.jpg' % url_id
    folder = folder.replace('/', ' ')
    if not os.path.exists(folder):
        os.mkdir(folder)
    print(f'Downloading {url_id}:{folder}...')

    index = 0
    while True:
        dl = url.format(name=index)
        r = s.get(dl)
        print(f'Saving {dl}')
        index += 1
        if r.status_code == 200:
            path = os.path.join(folder, f'{index}.jpg')
            f = open(path, 'wb')
            f.write(r.content)
            f.close()
        else:
            break


if __name__ == '__main__':
    albums = {8930: "[Bomb.TV] 2006年07月刊 Yui Aragaki 新垣結衣/新垣结衣 写真集",
              15992: "新垣结衣 山本彩 筱田麻里子 榮倉奈々 AKB48 优香 仲村みう 黒澤ゆりか [Weekly Playboy] 2011年No.44 写真杂志",
              25436: "新垣结衣《Fashion Photo Magazine 2012》写真集", 25437: "新垣结衣《Gacky Book [ガッキーブック]》写真集",
              25438: "新垣结衣 [ビジョメガネ] 写真集",
              25439: "新垣结衣 《恋爱部屋》 恋するマドリ 写真集", 25440: "新垣结衣 月刊 Special 图片合辑", 25441: "新垣结衣《水漾青春 ちゅら☆ちゅら》写真集"}

    for _id, _f in albums.items():
        download(_id, _f)
    # https://www.meituri.com/search/%E6%96%B0%E5%9E%A3%E7%BB%93%E8%A1%A3
    # let imgs = document.getElementsByClassName('img')[0]
    # for (i=0;i < 8;i++){
    #     g[imgs.children[i].firstElementChild.href.split('/')[4]]=imgs.children[i].lastElementChild.innerText
    # }
