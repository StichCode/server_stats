import sqlite3


def create_db():
    """ Create database """
    conn = __connection()
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY, username TEXT, "
                   "sign_in BOOLEAN, admin BOOLEAN)")
    create_new_user(295290188, 'rabbit_666', True, True)
    conn.commit()
    conn.close()


def __connection():
    """ Connection to database """
    return sqlite3.connect("database_status.db", check_same_thread=True)


def get_all_data():
    """ Fetch all data from database"""
    conn = __connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users


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


def get_user(id_users):
    """ Get user by id """
    conn = __connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users where id = {}".format(id_users))
    user = cursor.fetchone()
    conn.close()
    return user


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
    return users
