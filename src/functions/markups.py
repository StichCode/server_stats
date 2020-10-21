from telebot import types


def start_mk():
    mk = types.InlineKeyboardMarkup()
    btn_info = types.InlineKeyboardButton('RAM and CPU', callback_data="/ram_cpu")
    btn_memory = types.InlineKeyboardButton('Memory', callback_data="/memory")
    btn_connections = types.InlineKeyboardButton("Who Connect to server?", callback_data="/who_connect")
    btn_temperature = types.InlineKeyboardButton("Temperature", callback_data="/temp")
    mk.row(btn_info, btn_memory, btn_temperature)
    mk.row(btn_connections)
    return mk