# 1.Write a program in python which demonstrates
# the client-server connection with in system.

#Server.py

import socket

server_socket = socket.socket()
HOST = socket.gethostname()
PORT = 12345
server_socket.bind((HOST,PORT))
server_socket.listen(5)
while True:
    connection, address = server_socket.accept()
    print("Got Connection From",address)
    connection.send(b"Thank You For Connecting")
    connection.close()
