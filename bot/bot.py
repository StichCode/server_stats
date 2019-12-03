import os
import time

import telebot
from telebot import types

from bot.db.database import create_db, has_user_permission, create_new_user, get_users_to_permissions, get_admin
from bot.get_info import memory_usage, prepare_data, get_cpy_percent
from bot.markups import main_markup

TOKEN = os.environ.get("TOKEN")

bot = telebot.TeleBot(TOKEN)

# / memory -> dict / ram -> dict / cpy -> get_pid -> dict
emoji_snow = u"\u2744"

welcome_message = "Hi, what you want to known?\n" \
                  "I can show you info about:\n" \
                  f"RAM      {emoji_snow}\n" \
                  f"MEMORY   {emoji_snow}\n" \
                  f"CPU      {emoji_snow}"

# user = 0


@bot.message_handler(commands=['start'])
def start_message(message):
    # global user
    user = message.chat.id
    if has_user_permission(message.chat.id):
        markup = main_markup()
        bot.send_message(message.chat.id, welcome_message, reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "You don't have permission to use bot")
        create_new_user(message.from_user.id, message.from_user.username)
        bot.send_message(get_admin()[0], f"This user tried to request information\n"
                                         f" {message.from_user.username}({message.from_user.id})")

    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        # markup = main_markup()
        if call.data == "/ram":
            bot.send_message(user, prepare_data(), reply_markup=markup)
        elif call.data == "/memory":
            bot.send_message(user, memory_usage(), reply_markup=markup)
        elif call.data == "/cpu":
            bot.send_message(user, get_cpy_percent(), reply_markup=markup)
        elif call.data == "/want_permissions":
            bot.send_message(user, get_users_to_permissions(), reply_markup=markup)


def start():
    while True:
        try:
            bot.polling(none_stop=True, interval=0.5, timeout=0)
        except Exception:
            time.sleep(10)


create_db()
start()
