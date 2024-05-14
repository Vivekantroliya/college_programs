# 1.Write a program in python which demonstrates
# the client-server connection with in system.

#Client.py

import socket

client_socket = socket.socket()
HOST = socket.gethostname()
PORT = 12345
client_socket.connect((HOST,PORT))
recv = client_socket.recv(1024).decode('utf8')
print(recv)
client_socket.close()
