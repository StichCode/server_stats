import sqlite3


conn = sqlite3.connect("database_status.db", check_same_thread=True)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users (ID INT, NAME TEXT)''')
conn.commit()
conn.close()


