import os

import telebot
from telebot import types

from bot.get_info import get_ram, memory_usage


TOKEN = os.environ.get("TOKEN")

bot = telebot.TeleBot(TOKEN)


# / memory -> dict / ram -> dict / cpy -> get_pid -> dict
memory = memory_usage()["Memory"]
print(memory)
# memory["total"]
# memory["used"]
# memory['free']
# memory['%']


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hi, what you want to known?", reply_markup=keyboard_main)


@bot.message_handler(commands=["ram", "memory", "cpu"])
def send_info(message):
    if message.text == "/ram":
        bot.send_message(message.chat.id, "Not Works", reply_markup=clear_markup)
    elif message.text == "/memory":
        bot.send_message(message.chat.id, "___________MEMORY______________"
                                          f"Total   : f{memory['total']}\n"
                                          f"Used    : f{memory['used']}\n"
                                          f"Free    : f{memory['free']}\n"
                                          f"Percent : f{memory['%']}\n", reply_markup=clear_markup)
    elif message.text == "/cpu":
        bot.send_message(message.chat.id, "IT's not worked")
    else:
        bot.send_message(message.chat.id, "You can saw only: ram or memory info", reply_markup=keyboard_main)


clear_markup = types.ReplyKeyboardRemove(selective=False)
keyboard_main = telebot.types.InlineKeyboardMarkup()
memory_btn = types.InlineKeyboardButton("/memory")
ram_btn = types.InlineKeyboardButton("/ram")
cpy_btn = types.InlineKeyboardButton("/cpy")
keyboard_main.add(memory_btn, ram_btn, cpy_btn)


bot.polling(none_stop=False, interval=0.5, timeout=0)
