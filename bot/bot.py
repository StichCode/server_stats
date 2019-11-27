import os

import telebot
from telebot import types

from bot.get_info import get_ram, memory_usage


TOKEN = os.environ.get("TOKEN")

bot = telebot.TeleBot(TOKEN)


# / memory -> dict / ram -> dict / cpy -> get_pid -> dict
memory = memory_usage()["Memory"]


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hi, what you want to known?", reply_markup=keyboard_main)


@bot.message_handler(commands=["ram", "memory", "cpu"])
def send_info(message):
    if message.text == "/ram":
        bot.send_message(message.chat.id, "Not Works now")
    elif message.text == "/memory":
        bot.send_message(message.chat.id, "___________MEMORY______________"
                                          f"Total   : f{memory['total']}\n"
                                          f"Used    : f{memory['used']}\n"
                                          f"Free    : f{memory['free']}\n"
                                          f"Percent : f{memory['%']}\n")
    elif message.text == "/cpu":
        bot.send_message(message.chat.id, "IT's not worked")
    else:
        bot.send_message(message.chat.id, "You can saw only: ram or memory info")


clear_markup = types.ReplyKeyboardRemove(selective=False)


memory_btn = types.InlineKeyboardButton("/memory", callback_data="/memory")
ram_btn = types.InlineKeyboardButton("/ram", callback_data="/ram")
cpy_btn = types.InlineKeyboardButton("/cpy", callback_data="/cpy")

custom_keyboard = [[memory_btn, ram_btn, cpy_btn]]
keyboard_main = telebot.types.ReplyKeyboardMarkup(custom_keyboard)

bot.polling(none_stop=False, interval=0.5, timeout=0)
