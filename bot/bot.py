import os

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from bot.get_info import get_ram, memory_usage


TOKEN = os.environ.get("TOKEN")

bot = telebot.TeleBot(TOKEN)


# / memory -> dict / ram -> dict / cpy -> get_pid -> dict
memory = memory_usage()["Memory"]
emoji = u"U+2744"


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
        bot.send_message(message.chat.id, text_ram)
    elif message.text == "/memory":
        bot.send_message(message.chat.id, "___________MEMORY______________\n"
                                          f"Total   : {round(memory['total'],3)} GiB\n"
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


text_ram = "____________RAM____________"
for line in get_ram():
    text_ram += "\n"
    text_ram += f"Pid        : {line['pid']}\n"
    text_ram += f"Name       : {line['name']}\n"
    text_ram += f"Cmd Lines  : {str(line['cmd line'])}\n"
    text_ram += f"Time works : {line['time works']}\n"
    text_ram += "___________________________"


bot.polling(none_stop=True, interval=5, timeout=0)
