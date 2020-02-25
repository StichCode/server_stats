import copy
import time

import telebot
from telebot import apihelper

from bot.get_info import memory_usage, check_connections, ram_cpu
from bot.markups import start_mk
from config import Config

apihelper.proxy = {'https': f'socks5://{Config.USERNAME_SOCKS}:{Config.PASSWORD_SOCKS}'
                            f'@{Config.ADDRESS_SOCKS}:{Config.PORT_SOCKS}'}

bot = telebot.TeleBot(Config.TOKEN)
# / memory -> dict / ram -> dict / cpy -> get_pid -> dict
emoji_snow = u"\u2744"

welcome_message = "Hi, what you want to known?\n" \
                  "I can show you info about:\n"


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, welcome_message, reply_markup=start_mk())
    if message.chat.id not in Config.ADMINISTRATORS:
        bot.send_message(message.chat.id, "Fuck you!")

    @bot.callback_query_handler(func=lambda call: True)
    def ram(call):
        if call.data == "/memory":
            bot.send_message(message.chat.id, memory_usage(), reply_markup=start_mk())
            # bot.edit_message_text(memory_usage(), message.chat.id, bot_message.message_id, reply_markup=start_mk())

        elif call.data == "/ram_cpu":
            bot.send_message(message.chat.id, ram_cpu(), reply_markup=start_mk())
            # bot.edit_message_text(ram_cpu(), message.chat.id, bot_message.message_id, reply_markup=start_mk())

        elif call.data == "/who_connect":
            bot.send_message(message.chat.id, check_connections(), reply_markup=start_mk())


def start():
    while True:
        try:
            bot.polling(none_stop=True, interval=1, timeout=0)
        except Exception:
            time.sleep(10)
