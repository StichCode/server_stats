import telebot
from telebot import types

from bot.get_info import get_ram, memory_usage

token = "TOKEN"
bot = telebot.TeleBot(token)


# / memory -> dict / ram -> dict / cpy -> get_pid -> dict


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hi, what you want to known?", reply_markup=keyboard_main)


@bot.message_handler(commands=["ram","memory","cpu"])
def send_info(message):
    if message.text == "/ram":
        bot.send_message(message.chat.id, "ram after fix", reply_markup=clear_markup)
    elif message.text == "/memory":
        bot.send_message(message.chat.id, "memory after fix", reply_markup=clear_markup)
    #else:
        #bot.send_message(message.chat.id, "You can saw only: ram or memory info", reply_markup=keyboard_main)


clear_markup = types.ReplyKeyboardRemove(selective=False)


keyboard_main = telebot.types.ReplyKeyboardMarkup()
memory_btn = types.KeyboardButton("/memory")
ram_btn = types.KeyboardButton("/ram")
cpy_btn = types.KeyboardButton("/cpy")
keyboard_main.add(memory_btn, ram_btn, cpy_btn)


bot.polling(none_stop=False, interval=0.5, timeout=0)
