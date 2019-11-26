import telebot
from telebot import types

from bot.get_info import get_ram, memory_usage

token = "TOKEN"
bot = telebot.TeleBot(token)


# / memory -> dict / ram -> dict / cpy -> get_pid -> dict


@bot.message_handler(command=['start', 'help'])
def start_message(message):
    bot.send_message(message, "Hi, what you want to known?", reply_markup=keyboard_main)


@bot.message_handler(command=["ram", "memory"])
def send_info(message):
    if message.text == "/ram":
        bot.send_message(message.chat.id, get_ram())
    elif message.text == "/memory":
        bot.send_message(message.chat.id, memory_usage())


keyboard_main = telebot.types.InlineKeyboardMarkup()
memory_btn = types.InlineKeyboardButton("/memory")
ram_btn = types.InlineKeyboardButton("/ram")
cpy_btn = types.InlineKeyboardButton("/cpy")
keyboard_main.row(memory_btn, ram_btn, cpy_btn)


bot.polling(none_stop=False, interval=5, timeout=0)
