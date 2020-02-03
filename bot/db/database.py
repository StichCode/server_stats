import os
import sqlite3


def create_db():
    """ Create database """
    conn = __connection()
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY, username TEXT, "
                   "sign_in BOOLEAN, admin BOOLEAN)")
    cursor.execute("CREATE TABLE IF NOT EXISTS notes (id INT PRIMARY KEY AUTOINCREMENT, "
                   "id_user INT, note TEXT, FOREIGN KEY(id_user) REFERENCES users(id));")
    # потом можно сделать категории и название заметок
    create_new_user(295290188, 'rabbit_666', True, True)
    conn.commit()
    conn.close()


def __connection():
    """ Connection to database """
    path_to_database = "/home/parker/database_status.db"
    if not os.path.exists(path_to_database):
        open(path_to_database, 'w').close()
    return sqlite3.connect(path_to_database, check_same_thread=True)


def get_all_data():
    """ Fetch all data from database"""
    conn = __connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    conn.close()
    return users


def create_new_note(id_user, note):
    conn = __connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO notes (id_user, note) VALUES (?,?);", (id_user, note))
    except sqlite3.IntegrityError:
        return False
    conn.commit()
    conn.close()
    return True


def get_all_notes(id_user):
    conn = __connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes WHERE id_user={}".format(id_user))
    info = cursor.fetchall()
    conn.close()
    return info


def create_new_user(id_user, username, has_permission=False, admin=False):
    """Crate new user """
    conn = __connection()
    flag = False
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (id, username, sign_in, admin) "
                       "VALUES (?, ?, ?, ?)", (id_user, username, has_permission, admin))
    except sqlite3.IntegrityError:
        flag = False
    conn.commit()
    conn.close()
    return flag


def has_user_permission(id_users):
    """ Get user by id """
    conn = __connection()
    cursor = conn.cursor()
    cursor.execute("SELECT sign_in FROM users where id = {}".format(id_users))
    has_permission = cursor.fetchone()
    conn.close()
    if has_permission is None or has_permission[0] == 0:
        return False
    return True


def edit_user_settings(id_user, id_to_change):
    """Gives user login permission"""
    conn = __connection()
    cursor = conn.cursor()
    cursor.execute("SELECT admin FROM users where id = {}".format(id_user))
    if cursor.fetchone()[0] == 1:
        if cursor.execute("SELECT sign_in FROM users").fetchone()[0] == 1:
            return "User can already use the functional of the bot"
        cursor.execute("UPDATE users SET sign_in = {} WHERE id = {}".format(True, id_to_change))
        conn.commit()
        return "The changes are completed, user can use the functional of the bot"
    else:
        return "You don't have permission to do this"


def get_users_to_permissions():
    conn = __connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users where sign_in = 0")
    users = cursor.fetchall()
    conn.close()
    if not users:
        return None
    user_data = []
    for i in range(len(users)):
        user_data.append(dict(name=users[i][1], id=users[i][0]))
    return user_data


def get_admin():
    # Need optimisation for this
    conn = __connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users where admin = 1")
    admin = cursor.fetchone()
    conn.close()
    return admin
