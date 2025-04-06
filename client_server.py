import sqlite3
import socket 
import random
import requests 

try: 
    ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("[C]: Client socket created")
except socket.error as err: 
    print('socket open error: {} \n'.format(err))
    exit()

serverBinding = ("localhost", 6000)
ss.bind(serverBinding)
ss.listen()
print("[S]: Server is listening on port 6000")

def verify(email, password): 
    try: 
        conn = sqlite3.connect('secureDatabase.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users  WHERE username = ?",(email,))
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
        conn = sqlite3.connect('secureDatabase.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (email, password))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"[S]: Database error: {e}")
        return False

   
def createPokemonAccount(password):
    try:    
        #pokemon code starts here
        url = f"https://pokeapi.co/api/v2/pokemon/?limit=151" ## changing this to 151 for gen 1 pokemon 
        response = requests.get(url)
        if response.status_code == 200:

            poke_list = response.json()["results"]
            chosen = random.choice(poke_list)
            name = chosen["name"]
            poke_url = chosen["url"]

            ## totalPoke = response.json()["count"]
            ## random_id = random.randint(1,totalPoke)
            ## url = f"https://pokeapi.co/api/v2/pokemon/{random_id}"
            ## response = requests.get(url)
            response = requests.get(poke_url)
            if response.status_code == 200: 
                data = response.json()
                username = data["name"]
                print(f"\nNew Pokemon Username: {username.capitalize()}")
                
                conn = sqlite3.connect("secureDatabase.db")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (username,password) VALUES (?,?)",(username,password))
                conn.commit()
                conn.close() 
                return True
            else: 
                print("Error fetching Pokémon data")
                return False
        else: 
            print("Error fetching total Pokémon count.")
        return True
    except Exception as e:
        print(f"[S]: Database error: {e}")
        return False    
            
def start_connection(client_socket):
    try:
        check = client_socket.recv(1024).decode().strip()
        userPoke = client_socket.recv(1024).decode().strip()
        email = client_socket.recv(1024).decode().strip()
        password = client_socket.recv(1024).decode().strip()
        if check == "2":
            print(f"[S] Recieved email: {email}")
            print(f"[S]: Recieved password: {password}")

            if verify(email, password):
                client_socket.send("Login Successful".encode())
            else:
                client_socket.send("Invalid Login".encode())
        else: 
            if(userPoke == '1'):
                print(f"[S]: Recieved NEW password: {password}")
                if createPokemonAccount(password):
                    client_socket.send("Account Creation Successful".encode())
                else:
                    client_socket.send("Account Creation Unsuccessful".encode())
            else:
                print(f"[S] Recieved NEW email: {email}")
                print(f"[S]: Recieved NEW password: {password}")
                
                if createAccount(email, password):
                    client_socket.send("Account Creation Successful".encode())
                else:
                    client_socket.send("Account Creation Unsuccessful".encode())
            
    finally:
        client_socket.close()
        print("[S]: Connection closed")


client_socket, client_address = ss.accept()
print(f"[S]: Connection established with {client_address}")
start_connection(client_socket)
ss.close()
print("[S]: Server socket closed")