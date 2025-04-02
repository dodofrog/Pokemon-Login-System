#inspiration https://github.com/SidPadmanabhan/Secure-Login-System
import sqlite3

sqliteConnection = sqlite3.connect('blueprint.db')
cursor = sqliteConnection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT,
                   password TEXT)''')

cursor.executex