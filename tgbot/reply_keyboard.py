#!/usr/bin/python
# coding:utf-8

# tools - main.py
# 2018/2/1 9:23
# 

__author__ = 'Benny <benny@bennythink.com>'

import telebot
from config import TOKEN
from telebot import types

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    # also there are ReplyKeyboardRemove and ForceReply
    # types.ReplyKeyboardRemove()
    # types.ForceReply()
    markup = types.ReplyKeyboardMarkup(row_width=3)
    btn1 = types.KeyboardButton('a')
    btn2 = types.KeyboardButton('b')

    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "ReplyKeyboard: ", reply_markup=markup)


@bot.message_handler(commands=['help'])
def send_help(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, 'hello', reply_markup=markup)


if __name__ == '__main__':
    bot.polling()
