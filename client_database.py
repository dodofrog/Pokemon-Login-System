import sqlite3

sqliteConnection = sqlite3.connect('secureDatabase.db')
cursor = sqliteConnection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT NOT NULL UNIQUE,
                   password TEXT NOT NULL)''')

#Add 7 different usernames and passwords into USERS table
cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", ("johnny2000","rhythm"))
cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", ("bigturtle89","stamina"))
cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", ("elasticbanana32","boomerang"))
cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", ("terrythegymnast","ironcross"))
cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", ("banjoonthemoon","marias"))
cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", ("buzzcut","firefirefire"))
cursor.execute("INSERT INTO users (username, password) VALUES (?,?)", ("chickennugget","mcdonalds"))
sqliteConnection.commit()

#Retrieve all usernames and passwords from USERS table
cursor.execute("SELECT username, password FROM users")
lines = cursor.fetchall()

#Print out all usernames and password
for line in lines:
    print(f"Username: {line[0]}, Password: {line[1]}")
sqliteConnection.close()
