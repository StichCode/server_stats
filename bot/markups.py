from telebot import types

BACK = types.InlineKeyboardButton('Back', callback_data="/start")


def starting_mk():
    mk = types.ReplyKeyboardMarkup()
    btn_ram = types.KeyboardButton("RAM")
    btn_cpu = types.KeyboardButton("CPU")
    btn_memory = types.KeyboardButton("Memory")
    btn_permission = types.KeyboardButton("Admin")
    btn_note = types.KeyboardButton("Notes")
    mk.row(btn_cpu, btn_ram, btn_memory)
    mk.row(btn_permission, btn_note)
    return mk


def remove():
    return types.ReplyKeyboardRemove()

def __default():
    markup = types.InlineKeyboardMarkup()
    button_ram = types.InlineKeyboardButton('RAM', callback_data="/ram")
    button_cpu = types.InlineKeyboardButton('CPU', callback_data="/cpu")
    button_memory = types.InlineKeyboardButton('Memory', callback_data="/memory")
    button_permission = types.InlineKeyboardButton('Want Permission', callback_data="/want_permissions")
    button_notes = types.InlineKeyboardButton('Notes', callback_data='/notes')
    markup.row(button_cpu, button_ram)
    markup.row(button_memory, button_permission)
    markup.row(button_notes)
    return markup


def notes_markup():
    markup = types.InlineKeyboardMarkup()
    button_all_notes = types.InlineKeyboardButton('All my notes', callback_data="/all_notes")
    button_new_note = types.InlineKeyboardButton('Create new note', callback_data="/create_new_note")
    markup.row(button_all_notes, button_new_note)
    markup.row(BACK)
    return markup


def main_markup():
    markup = __default()
    markup.row(BACK)
    return markup


def start_markup():
    markup = __default()
    return markup


def users_markup(data):
    markup = types.InlineKeyboardMarkup()
    for user in data:
        button_user = types.InlineKeyboardButton(f"username: {user['name']} id: {user['id']}", callback_data=user['id'])
        markup.row(button_user)
    markup.row(BACK)
    return markup
