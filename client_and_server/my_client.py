import socket

HOST = 'localhost'
PORT = 8000

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((HOST,PORT))

while True:
    message = input("Insert the message to send >>: ")
    socket.send(message.encode()) #importante codificar el mensaje desde el cliente,decodificar en el servidor
    print(socket.recv(1024).decode())
    print('The message from the client is sended')
    
