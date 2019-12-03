from telebot import types

BACK = types.InlineKeyboardButton('Back', callback_data="/start")


def main_markup():
    markup = types.InlineKeyboardMarkup()
    button_ram = types.InlineKeyboardButton('RAM', callback_data="/ram")
    button_cpu = types.InlineKeyboardButton('CPU', callback_data="/cpu")
    button_memory = types.InlineKeyboardButton('Memory', callback_data="/memory")
    button_permission = types.InlineKeyboardButton('Want Permission', callback_data="/want_permissions")
    markup.row(button_cpu, button_ram)
    markup.row(button_memory, button_permission)
    markup.row(BACK)
    return markup


def users_markup(data):
    markup = types.InlineKeyboardMarkup()
    for user in data:
        button_user = types.InlineKeyboardButton(f"username: {user['name']} id: {user['id']}", callback_data=user['id'])
        markup.row(button_user)
    markup.row(BACK)
    return markup
