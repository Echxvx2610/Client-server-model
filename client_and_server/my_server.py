#nota importante
#la primera vez que intente crear un socket me arrojaba el sig problema( module 'socket' has no attribute 'socket')
#tuve que renombrar mi script actual como mysocket y ya que arranco lo renombre a my_server

import socket

#HOST = '172.27.182.132'
HOST = 'localhost' #definimos la ip del host,usando ipconfig en cmd o definiendo localhost
PORT = 8000 #seleccionamos el puerto en donde se comunicara el server,si no funciona puede estar ocupado,podemos cambiar de puerto por ejm. 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #utilizaremos un socket strema con el protocolo TCP
server.bind((HOST,PORT))

server.listen(5) #definimos el maximo de peticiones que puede aceptar el server

while True:
  communication_socket, address = server.accept()
  print(f"Connect to {address}")
  message = communication_socket.recv(1024).decode() #1024 buffer size
  print(f'Message from client is:{message}')
  communication_socket.send('Got your message!,Thank you!'.encode())#.encode('utf-8')
  communication_socket.close()
  print(f'Connection with {address} ended!')
