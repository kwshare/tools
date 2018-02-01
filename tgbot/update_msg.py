#!/usr/bin/python
# coding:utf-8

# tools - manipulate_msg.py
# 2018/2/1 10:43
# 

__author__ = 'Benny <benny@bennythink.com>'

import time

import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def edit_message(message):
    msg_id = bot.send_message(message.chat.id, '这里是原始消息').message_id
    time.sleep(2)
    # Below is wrong!!!
    # bot.edit_message_text('更新了耶', message.chat.id, message.message_id)
    bot.edit_message_text('更新了耶', message.chat.id, msg_id)
    # another hack
    # bot.edit_message_text('更新了耶', message.chat.id, message.message_id + 1)


@bot.message_handler(commands=['help'])
def delete_message(message):
    msg_id = bot.send_message(message.chat.id, '这里是要被删除的消息').message_id
    time.sleep(2)
    bot.delete_message(message.chat.id, msg_id)


if __name__ == '__main__':
    bot.polling()
