import os

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.get_info import memory_usage, prepare_data

TOKEN = os.environ.get("TOKEN")

bot = telebot.TeleBot(TOKEN)

# / memory -> dict / ram -> dict / cpy -> get_pid -> dict
memory = memory_usage()["Memory"]
emoji = u"\u2744"


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hi, what you want to known?\n"
                                      "I can show you info about:\n"
                                      f"RAM    {emoji}\n"
                                      f"MEMORY {emoji}\n"
                                      f"CPU    {emoji}", reply_markup=reply_markup)


@bot.message_handler(commands=["ram", "memory", "cpu"])
def send_info(message):
    if message.text == "/ram":
        bot.send_message(message.chat.id, prepare_data())
    elif message.text == "/memory":
        print(message)
        bot.send_message(message.chat.id, "___________MEMORY______________\n"
                                          f"Total   : {round(memory['total'], 3)} GiB\n"
                                          f"Used    : {round(memory['used'], 3)} GiB\n"
                                          f"Free    : {round(memory['free'], 3)} GiB\n"
                                          f"Percent : {round(memory['%'], 3)} %\n")
    elif message.text == "/cpu":
        bot.send_message(message.chat.id, "IT's not worked")
    else:
        bot.send_message(message.chat.id, "You can saw only: ram or memory info")


@bot.message_handler(content_types=["text"])
def send_info(message):
    if message.text == "/check":
        pass
    else:
        bot.send_message(message.chat.id, "I can show you only:\n"
                                          f"RAM    {emoji}\n"
                                          f"MEMORY {emoji}\n"
                                          f"CPU    {emoji}")


memory_btn = InlineKeyboardButton(text="/memory", callback_data="memory")
ram_btn = InlineKeyboardButton(text="/ram", callback_data="ram")
cpy_btn = InlineKeyboardButton(text="/cpy", callback_data="cpy")

custom_keyboard = [[memory_btn, ram_btn, cpy_btn]]
reply_markup = InlineKeyboardMarkup(custom_keyboard)


bot.polling(none_stop=False, interval=0.5, timeout=0)
