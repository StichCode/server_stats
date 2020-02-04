from telebot import types

BACK = types.InlineKeyboardButton('Back', callback_data="/back")


def start_mk():
    mk = types.InlineKeyboardMarkup()
    btn_info = types.InlineKeyboardButton('RAM and CPU', callback_data="/ram_cpu")
    btn_memory = types.InlineKeyboardButton('Memory', callback_data="/memory")
    btn_permission = types.InlineKeyboardButton('Settings', callback_data="/settings")
    btn_notes = types.InlineKeyboardButton('Notes', callback_data='/notes')
    btn_connections = types.InlineKeyboardButton("Who Connect to server?", "/who_connect")
    mk.row(btn_info, btn_notes)
    mk.row(btn_memory, btn_permission)
    mk.row(btn_connections)
    return mk


def settings_mk():
    mk = types.InlineKeyboardMarkup()
    btn_show_users = types.InlineKeyboardButton('Show new users', '/show')
    # В будущем добавить больше настроек
    mk.row(btn_show_users, BACK)
    return mk


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
