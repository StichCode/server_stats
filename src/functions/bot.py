import time

import telebot
from loguru import logger

from src.functions.get_info import memory_usage, ram_cpu, check_connections
from src.functions.markups import start_mk
from config import config


bot = telebot.TeleBot(token=config.token)


welcome_message = "Hi, what you want to known?\n" \
                  "I can show you info about:\n"


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, welcome_message, reply_markup=start_mk())
    logger.info(f"User {message.chat.id}, start messaging")

    @bot.callback_query_handler(func=lambda call: True)
    def ram(call):
        if call.data == "/memory":
            logger.info(f"User {message.chat.id}, requested information about memory usage")
            bot.send_message(message.chat.id, memory_usage(), reply_markup=start_mk())
            # bot.edit_message_text(memory_usage(), message.chat.id, bot_message.message_id, reply_markup=start_mk())

        elif call.data == "/ram_cpu":
            logger.info(f"User {message.chat.id}, requested information about ram and cpu")
            bot.send_message(message.chat.id, ram_cpu(), reply_markup=start_mk())
            # bot.edit_message_text(ram_cpu(), message.chat.id, bot_message.message_id, reply_markup=start_mk())

        elif call.data == "/who_connect":
            logger.info(f"User {message.chat.id}, requested information about connected people")
            bot.send_message(message.chat.id, check_connections(), reply_markup=start_mk())

        elif call.data == "/temp":
            logger.info(f"User {message.chat.id}, requested information about temp")
            bot.send_message(message.chat.id, "Not available now", reply_markup=start_mk())


def start_bot():
    while True:
        try:
            bot.polling(none_stop=True, interval=1, timeout=0)
        except Exception:
            time.sleep(10)