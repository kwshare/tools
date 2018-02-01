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
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Google', url='https://www.google.com/ncr')
    btn2 = types.InlineKeyboardButton('Action', callback_data='Act Now')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "InlineKeyboard: ", reply_markup=markup)


@bot.message_handler(commands=['help'])
def edit_reply_markup(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Apple', url='https://www.apple.com')
    btn2 = types.InlineKeyboardButton('Microsoft', url='https://www.microsoft.com')
    markup.add(btn1, btn2)
    # use hack
    bot.edit_message_reply_markup(message.chat.id, message.message_id - 1, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_handle(call):
    # bot.answer_callback_query(call.id, '哎哟', show_alert=True)
    bot.answer_callback_query(call.id, '哎哟')
    bot.send_message(call.message.chat.id, 'You clicked %s' % call.data)


if __name__ == '__main__':
    bot.polling()
