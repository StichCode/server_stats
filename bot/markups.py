from telebot import types

BACK = types.InlineKeyboardButton('Back', callback_data="/back")


def start_mk():
    markup = types.InlineKeyboardMarkup()
    button_ram = types.InlineKeyboardButton('RAM', callback_data="/ram")
    button_cpu = types.InlineKeyboardButton('CPU', callback_data="/cpu")
    button_memory = types.InlineKeyboardButton('Memory', callback_data="/memory")
    button_permission = types.InlineKeyboardButton('Settings', callback_data="/settings")
    button_notes = types.InlineKeyboardButton('Notes', callback_data='/notes')
    markup.row(button_cpu, button_ram)
    markup.row(button_memory, button_permission)
    markup.row(button_notes)
    return markup


def settings_mk():
    mk = types.InlineKeyboardMarkup()
    btn_show_users = types.InlineKeyboardButton('Show new users', '/show')
    # В будущем добавить больше настроек
    mk.row(btn_show_users)
    return


def notes_mk():
    markup = types.InlineKeyboardMarkup()
    button_all_notes = types.InlineKeyboardButton('All my notes', callback_data="/all_notes")
    button_new_note = types.InlineKeyboardButton('Create new note', callback_data="/create_new_note")
    markup.row(button_all_notes, button_new_note)
    markup.row(BACK)
    return markup


def users_mk(data):
    markup = types.InlineKeyboardMarkup()
    for user in data:
        button_user = types.InlineKeyboardButton(f"username: {user['name']} id: {user['id']}", callback_data=user['id'])
        markup.row(button_user)
    markup.row(BACK)
    return markup
