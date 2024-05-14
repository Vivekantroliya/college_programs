# 3.Write a client/server program to demonstrate
# the communication on two different computer.

#Client.py

import socket
HOST = "172.21.17.114" #IP Address
PORT = 12345

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

message = s.recv(1024).decode()
print(f"Received From Server : {message}")

data = "Hello! Server"
s.send(data.encode())
s.close()
