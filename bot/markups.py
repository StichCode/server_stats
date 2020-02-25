from telebot import types


def start_mk():
    mk = types.InlineKeyboardMarkup()
    btn_info = types.InlineKeyboardButton('RAM and CPU', callback_data="/ram_cpu")
    btn_memory = types.InlineKeyboardButton('Memory', callback_data="/memory")
    btn_connections = types.InlineKeyboardButton("Who Connect to server?", "/who_connect")
    mk.row(btn_info, btn_memory, btn_connections)
    return mk
