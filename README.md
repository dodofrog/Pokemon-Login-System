# Pokemon Login System
## Project Overview
This project is a rudimentary login system that allows users to create accounts and log into them using **Python** and **SQLite** within a **client-server model**. The Pokemon API allows users to make their username a random Gen-1 Pokemon.

## Directions
### 1. Create the Database
- Run `python3 client_database.py` in the terminal in order to create the database (if not already created)
### 2. Start the Server
- Run `python3 client_server.py` in the terminal in order to start the server and start listening for client connections.
### 3. Run the Socket
- Run `python3 client_socket.py` in the terminal in order to allow the client(you) to communicate with the server and perform actions

## Files
- ***Database:*** Uses SQLite to store client usernames/passwords.
- ***Server:*** Bridges client and database, creates accounts, communicates with the Pokemon API, and verifies users.
- ***Socket:*** Directly communicates with the client, allowing users to log in/create an account.

## Dependencies
- Python 3
- SQLite

## Credits
- Akshit Garg
- Ishani Rajeshirke 
- Divena Deshmukh
- Casey Fritz
- Sean Gelacio
