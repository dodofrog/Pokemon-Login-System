import socket

try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[C]: Client socket created")
except socket.error as err:
    print(f"Socket open error: {err}")
    exit()

serverBinding = ("localhost", 6000)
socket.connect(serverBinding)

check = input("Create Account(1) or Log in(2): ")
while True:
    if check == '1':
        socket.send(check.encode())  
        userPoke = input("Do you want a Pokémon username? (1: yes, 2: no): ")
        socket.send(userPoke.encode())

        if userPoke == '2': 
            email = input("Enter your desired email/username: ")
            socket.send(email.encode())
        else:
            email = "placeHolder"
            socket.send(email.encode()) 
            print("A Pokémon user will be generated for you!")

        password = input("Enter new password: ")
        socket.send(password.encode())
        break
    elif check == '2':
        socket.send(check.encode())
        placeholder = "placeholder"
        socket.send(placeholder.encode())
        newEmail = input("Enter your email/username: ")
        socket.send(newEmail.encode())
        newPassword = input("Enter password: ")
        socket.send(newPassword.encode())
        break
    else:
        check = input("Invalid response, try again: Sign in(1) or Log in(2)")
        


response = socket.recv(1024).decode()
print(response)



socket.close()
print("[C]: Connection is closed")
