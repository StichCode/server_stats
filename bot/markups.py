from telebot import types


def main_markup():
    markup = types.InlineKeyboardMarkup()
    button_ram = types.InlineKeyboardButton('RAM', callback_data="/ram")
    button_cpu = types.InlineKeyboardButton('CPU', callback_data="/cpu")
    button_memory = types.InlineKeyboardButton('Memory', callback_data="/memory")
    button_permission = types.InlineKeyboardButton('Want Permission', callback_data="/want_permissions")
    markup.add(button_cpu, button_ram, button_memory, button_permission)
    return markup
