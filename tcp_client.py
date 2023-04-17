from socket import *

server_address = "127.0.0.1"
server_port = 43210

msg = bytes(input("What do you want to say? "), 'utf-8')

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.connect((server_address, server_port))
obj_socket.send(msg)

print("Received: ", obj_socket.recv(1024))

obj_socket.close()
