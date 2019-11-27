import os

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from bot.get_info import get_ram, memory_usage


TOKEN = os.environ.get("TOKEN")

bot = telebot.TeleBot(TOKEN)


# / memory -> dict / ram -> dict / cpy -> get_pid -> dict
memory = memory_usage()["Memory"]


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hi, what you want to known?\n"
                                      "I can show you info about RAM | MEMORY | CPY", reply_markup=keyboard_main)


@bot.message_handler(commands=["ram", "memory", "cpu"])
def send_info(message):
    if message.text == "/ram":
        bot.send_message(message.chat.id, "Not Works now")
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


clear_markup = ReplyKeyboardRemove(selective=False)


memory_btn = InlineKeyboardButton(text="/memory", callback_data="/memory")
ram_btn = InlineKeyboardButton(text="/ram", callback_data="/ram")
cpy_btn = InlineKeyboardButton(text="/cpy", callback_data="/cpy")

custom_keyboard = [[memory_btn, ram_btn, cpy_btn]]
keyboard_main = InlineKeyboardMarkup(custom_keyboard)

bot.polling(none_stop=False, interval=0.5, timeout=0)
