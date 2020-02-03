import time

import telebot
from telebot import apihelper

from bot.db.database import create_db, has_user_permission, create_new_user, get_users_to_permissions, get_admin, \
    edit_user_settings, get_all_notes, create_new_note
from bot.get_info import memory_usage, prepare_data, get_cpy_percent
from bot.markups import main_markup, users_markup, start_markup, notes_markup, starting_mk, remove
from config import Config


apihelper.proxy = {'https': f'socks5://{Config.USERNAME_SOCKS}:{Config.PASSWORD_SOCKS}'
                            f'@{Config.ADDRESS_SOCKS}:{Config.PORT_SOCKS}'}

bot = telebot.TeleBot(Config.TOKEN)

# / memory -> dict / ram -> dict / cpy -> get_pid -> dict
emoji_snow = u"\u2744"

welcome_message = "Hi, what you want to known?\n" \
                  "I can show you info about:\n"


def like_id(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


# user = 0


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    if has_user_permission(message.chat.id):
        bot.send_message(message.chat.id, welcome_message, reply_markup=main_markup())
    else:
        bot.send_message(message.chat.id, "You don't have permission to use bot")
        create_new_user(message.from_user.id, message.from_user.username)
        bot.send_message(get_admin()[0], f"This user tried to request information\n"
                                         f" {message.from_user.username}({message.from_user.id})")

    @bot.callback_query_handler(func=lambda call: True)
    def ram(call):
        if call.data == "/memory":
            bot.send_message(message.chat.id, memory_usage())

        if call.data == "/ram":
            bot.send_message(message.chat.id, prepare_data())
#
        if call.data == "/memory":
            bot.send_message(message.chat.id, memory_usage())

        if call.data == "/cpu":
            bot.send_message(message.chat.id, "Now we will prepare information output for you.\nPlease wait.\nThanks.")
            cpu = get_cpy_percent()
            bot.send_message(message.chat.id, cpu)

        if call.data == "/notes":
            bot.send_message(message.chat.id, "What you want to do?")

        if call.data == "all_notes":
            info = get_all_notes(message.chat.id)
            bot.send_message(message.chat.id, info)
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     if call.data == "create_new_note":
#         bot.send_message(user, "Enter note, what you want to save")
#         if create_new_note(user, call.data):
#             bot.send_message(user, "All has been saved")
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     if call.data == "/want_permissions":
#         users = get_users_to_permissions()
#         if users is not None:
#             bot.send_message(user, "___This users want permissions____", reply_markup=users_markup(users))
#         else:
#             bot.send_message(user, "No users what want to have permission", reply_markup=markup)
#     elif str(call.data).isdigit():
#         changed = edit_user_settings(user, int(call.data))
#         bot.send_message(user, changed, reply_markup=markup)





def start():
    bot.send_message(get_admin()[0], "I'm online, he-he")
    while True:
        try:
            bot.polling(none_stop=True, interval=0.5, timeout=0)
        except Exception:
            time.sleep(10)


create_db()
start()
