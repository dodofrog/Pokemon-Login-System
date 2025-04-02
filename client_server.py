import sqlite3
import threading
import socket 
import requests
import random

try: 
    ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("[C]: Client socket created")
except socket.error as err: 
    print('socket open error: {} \n'.format(err))
    exit()

ss.connect("localhost", 5000)
ss.listen()
print("[S]: Server is listening on port 5000")

def verify(email, password): 
    try: 
        conn = sqlite3.connect('blueprint.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users  WHERE email = ?",(email))
        user = cursor.fetchone()
        conn.close()
        if user and user[0] == password: 
            return True
        return False; 
    except Exception as e:
       print(f"[S]: Database error: {e}")
       return False

def createAccount(email, password):
    try: 
        conn = sqlite3.connect('blueprint.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (email, password))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"[S]: Database error: {e}")
        return false


# pokemon code starts here
url = f"https://pokeapi.co/api/v2/pokemon/?limit=1"
response = requests.get(url)

 
if response.status_code == 200:
    totalPoke = response.json()["count"]
    randomPoke = random.randint(1,totalPoke)

    url = f"https://pokeapi.co/api/v2/pokemon/{randomPoke}"
    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()  
        name = data["name"]

        print(f"\nName: {name.capitalize()}")
else:
        
    print("Error fetching Pokemon data")
else: 
    print("Error fetching total Pokemon count.")

   
 


def start_connection(client_socket):
    try:
        check = client_socket.recv(1024).decode().strip()
        email = client_socket.recv(1024).decode().strip()
        password = client_socket.recv(1024).decode().strip()
        if check == "1":
            print(f"[S] Recieved email: {email}")
            print(f"[S]: Recieved password: {password}")

            if verify(email, password):
                client_socket.send("Login Successful".encode())
            else:
                client_socket.send("Invalid Login".encode())
            print(f"[S]: Recieved new password: {password}")
            createAccount(email, password)
    finally:
        client_socket.close()
        print("[S]: Connection closed")

try:             
    while True: 
        client_socket,client_address == ss.accept()
        print(f"[S]: Connection established with {client_address}")
        client_thread = threading.Thread(target=start_connection,args=(client_socket,))
        client_thread.start()

finally: 
    ss.close()
    print("[S]: Server socket closed")



        
