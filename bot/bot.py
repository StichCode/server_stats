import os

import telebot

from bot.db.database import create_db, has_user_permission, create_new_user, get_users_to_permissions, get_admin
from bot.get_info import memory_usage, prepare_data, get_cpy_percent

TOKEN = os.environ.get("TOKEN")

bot = telebot.TeleBot(TOKEN)

# / memory -> dict / ram -> dict / cpy -> get_pid -> dict
emoji_snow = u"\u2744"

welcome_message = "Hi, what you want to known?\n" \
                  "I can show you info about:\n" \
                  f"RAM      {emoji_snow}\n" \
                  f"MEMORY   {emoji_snow}\n" \
                  f"CPU      {emoji_snow}"


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, welcome_message)


@bot.message_handler(content_types=["text"])
def send_info(message):
    perm = has_user_permission(message.from_user.id)
    if perm:
        if message.text == "/ram":
            bot.send_message(message.chat.id, prepare_data())
        elif message.text == "/memory":
            bot.send_message(message.chat.id, memory_usage())
        elif message.text == "/cpu":
            bot.send_message(message.chat.id, get_cpy_percent())
        elif message.text == "/want_permissions":
            bot.send_message(message.chat.id, get_users_to_permissions())
    else:
        bot.send_message(message.chat.id, "You don't have permission to use bot")
        create_new_user(message.from_user.id, message.from_user.username)
        bot.send_message(get_admin()[0], f"This user tried to request information\n"
                                         f" {message.from_user.username}({message.from_user.id})")


create_db()
bot.polling(none_stop=False, interval=0.5, timeout=0)
