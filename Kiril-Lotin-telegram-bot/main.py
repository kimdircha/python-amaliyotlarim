# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 21:30:25 2021

@author: User
"""
from transliterate import to_latin, to_cyrillic
import telebot

bot = telebot.TeleBot('1731055837:AAHdxb9i0vgjEplzbwg_zxBP6M2IUM59hHk', parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """Assalomu aleykum. Xush kelibsiz!

Bot bilan tanishish uchun /help buyrug'idan foydalaning.

Dasturchi: @Suhayl_Qodirov""")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Menga kirill alifbosida yozilgan matn jo'natsangiz \
uni lotinga, lotin alifbosida yozilgan matn jo'natsangiz \
kirillga o'girib beraman.\n\nMatn kiriting:")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.polling()