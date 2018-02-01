#!/usr/bin/python
# coding:utf-8

# tools - requests_json.py
# 2018/2/1 12:19
# 

__author__ = 'Benny <benny@bennythink.com>'

import json
import requests
import telebot

from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def edit_message(message):
    if len(message.text.split(' ')) != 2:
        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_message(message.chat.id, '参数错误')
    else:
        location = get_location(message.text.split(' ')[1])
        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_message(message.chat.id, u"你查询的IP地址：`%s`\n%s" % (message.text.split(' ')[1], location),
                         parse_mode='Markdown')


def get_location(ip):
    r = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=' + ip).text
    res = json.loads(r)
    if res.get('code') == 0:
        return res.get('data').get('region') + res.get('data').get('country') + res.get(
            'data').get('isp')
    else:
        return '请求失败'


if __name__ == '__main__':
    bot.polling()
