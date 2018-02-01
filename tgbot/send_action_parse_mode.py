#!/usr/bin/python
# coding:utf-8

# tools - manipulate_msg.py
# 2018/2/1 10:43
# 

__author__ = 'Benny <benny@bennythink.com>'


import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def edit_message(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, '这个是_斜体_哦', parse_mode='Markdown')

    bot.send_chat_action(message.chat.id, 'record_video')
    bot.send_message(message.chat.id, "`print('hello world')`", parse_mode='Markdown')


if __name__ == '__main__':
    bot.polling()
