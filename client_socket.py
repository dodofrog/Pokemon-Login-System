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
        email = input("Enter your email/username: ")
        socket.send(email.encode())

        password = input("Enter your password: ")
        socket.send(password.encode())
        break
    elif check == '2':
        socket.send(check.encode())
        newEmail = input("Enter desired email/username: ")
        socket.send(newEmail.encode())

        newPassword = input("Enter new password: ")
        socket.send(newPassword.encode())
        break
    else:
        check = input("Invalid response, try again: Sign in(1) or Log in(2)")
        


response = socket.recv(1024).decode()
print(response)



socket.close()
print("[C]: Connection is closed")
