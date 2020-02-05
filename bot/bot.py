import time

import telebot
from telebot import apihelper

from bot.db.database import create_db, has_user_permission, create_new_user, get_users_to_permissions, get_admin, \
    get_all_notes
from bot.get_info import memory_usage, check_connections, ram_cpu
from bot.markups import start_mk, users_mk, notes_mk
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


@bot.message_handler(commands=['start'])
def start_message(message):
    bot_message = bot.send_message(message.chat.id, welcome_message, reply_markup=start_mk())
    print(bot.send_message(message.chat.id, str(bot_message), reply_markup=start_mk()))

    @bot.callback_query_handler(func=lambda call: True)
    def ram(call):
        if call.data == "/memory":
            bot.send_message(message.chat.id, memory_usage(), reply_markup=start_mk())
            # bot.edit_message_text(memory_usage(), message.chat.id, bot_message.message_id, reply_markup=start_mk())

        elif call.data == "/ram_cpu":
            bot.send_message(message.chat.id, ram_cpu(), reply_markup=start_mk())
            # bot.edit_message_text(ram_cpu(), message.chat.id, bot_message.message_id, reply_markup=start_mk())

        # elif call.data == "/who_connect":
        #     bot.edit_message_text(check_connections(), message.chat.id, bot_message.message_id, reply_markup=start_mk())
        #
        # elif call.data == "/notes":
        #     bot.edit_message_text("What you want to do?", message.chat.id, bot_message.message_id, reply_markup=notes_mk())
        #
        # elif call.data == "/all_notes":
        #     bot.edit_message_text(get_all_notes(message.chat.id), message.chat.id, bot_message.message_id)
        #
        # elif call.data == "/back":
        #     bot.edit_message_text(welcome_message, message.chat.id, bot_message.message_id, reply_markup=start_mk())
        #
        # elif call.data == "/create_new_note":
        #     bot.edit_message_text("Not work.", message.chat.id, bot_message.message_id, reply_markup=start_mk())

            # bot.send_message(user, "Enter note, what you want to save")
            # if create_new_note(user, call.data):
            #     bot.send_message(user, "All has been saved")
        #
        # if call.data == "/settings":
        #     users = get_users_to_permissions()
        #     if users is not None:
        #         bot.edit_message_text("___This users want permissions____", message.chat.id, bot_message.message_id,
        #                               reply_markup=users_mk(users))
        #     else:
        #         bot.edit_message_text("No users what want to have permission", message.chat.id, bot_message.message_id,
        #                               reply_markup=start_mk())
        # elif str(call.data).isdigit():
        #     changed = edit_user_settings(message.chat.id, int(call.data))
        #     bot.send_message(message.chat.id, changed, reply_markup=main_markup())


def start():
    create_db()
    # bot.send_message(get_admin()[0], "I'm online, he-he")
    while True:
        try:
            bot.polling(none_stop=True, interval=1, timeout=0)
        except Exception:
            time.sleep(10)


