from socket import *

server_address = "127.0.0.1"
server_port = 43210

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((server_address, server_port))
# Max 2 clients
obj_socket.listen(2)

print("Waiting client ... ")

while True:
    con, client = obj_socket.accept()
    print("Conected with: ", client)
    while True:
        msg_received = str(con.recv(1024))
        print("Received: ", msg_received)
        con.send(b'200 - Ok')
        break
    con.close()
